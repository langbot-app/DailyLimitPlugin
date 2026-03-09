from __future__ import annotations

import json
import time
from datetime import datetime, timezone, timedelta

from langbot_plugin.api.definition.components.common.event_listener import EventListener
from langbot_plugin.api.entities import events, context
from langbot_plugin.api.entities.builtin.platform import message as platform_message


class DefaultEventListener(EventListener):

    async def initialize(self):
        await super().initialize()

        @self.handler(events.PersonNormalMessageReceived)
        async def on_person_message(event_context: context.EventContext):
            await self._check_limit(event_context, str(event_context.event.sender_id))

        @self.handler(events.GroupNormalMessageReceived)
        async def on_group_message(event_context: context.EventContext):
            await self._check_limit(event_context, str(event_context.event.sender_id))

    async def _check_limit(self, event_context: context.EventContext, user_id: str):
        config = self.plugin.get_config()
        daily_limit = config.get("daily_limit", 50)

        # 0 means no limit
        if daily_limit <= 0:
            return

        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        storage_key = f"daily_count:{today}:{user_id}"

        # Get current count
        try:
            raw = await self.plugin.get_plugin_storage(storage_key)
            count = int(raw.decode("utf-8")) if raw else 0
        except Exception:
            count = 0

        if count >= daily_limit:
            silent_mode = config.get("silent_mode", False)

            if not silent_mode:
                limit_message = config.get("limit_message", "")
                if not limit_message:
                    limit_message = "您今天的对话次数已达上限，请明天再来吧~"

                await event_context.reply(
                    platform_message.MessageChain([
                        platform_message.Plain(text=limit_message),
                    ])
                )

            event_context.prevent_default()
            return

        # Increment count
        count += 1
        await self.plugin.set_plugin_storage(storage_key, str(count).encode("utf-8"))

        # Cleanup: delete previous day's keys to avoid storage bloat
        yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
        try:
            keys = await self.plugin.get_plugin_storage_keys()
            for key in keys:
                if key.startswith("daily_count:") and not key.startswith(f"daily_count:{today}:") and not key.startswith(f"daily_count:{yesterday}:"):
                    await self.plugin.delete_plugin_storage(key)
        except Exception:
            pass
