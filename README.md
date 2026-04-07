# Daily Limit Plugin

Limit the number of conversations per user per day for LangBot.

## Features

- **Per-user daily limit**: Set a maximum number of conversations each user can have per day
- **Customizable message**: Configure the message shown when a user exceeds their daily limit
- **Silent mode**: Optionally discard messages silently without any reply when the limit is reached
- **Timezone-aware reset**: Configure the timezone and hour for daily counter reset
- **Automatic cleanup**: Old usage data is automatically cleaned up to prevent storage bloat

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `daily_limit` | integer | `50` | Maximum conversations per user per day. Set to `0` to disable. |
| `limit_message` | string | `您今天的对话次数已达上限，请明天再来吧~` | Message shown when limit is exceeded. |
| `reset_timezone_offset` | integer | `8` | UTC offset in hours for daily reset. E.g. `8` for UTC+8 (China), `9` for UTC+9 (Japan). |
| `reset_hour` | integer | `0` | Hour of the day (in configured timezone) when the counter resets. |
| `silent_mode` | boolean | `false` | When enabled, excess messages are silently dropped. |

## How It Works

The plugin listens to both private and group normal message events. For each incoming message, it checks the sender's daily usage count against the configured limit. If the limit is reached:

- **Silent mode off**: Replies with the configured limit message and blocks further processing.
- **Silent mode on**: Silently blocks further processing without any reply.

Usage counts reset at the configured hour in the configured timezone (default: midnight UTC+8).
