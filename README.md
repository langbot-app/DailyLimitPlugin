# Daily Limit Plugin

Limit the number of conversations per user per day for LangBot.

## Features

- **Per-user daily limit**: Set a maximum number of conversations each user can have per day
- **Customizable message**: Configure the message shown when a user exceeds their daily limit
- **Silent mode**: Optionally discard messages silently without any reply when the limit is reached
- **Automatic cleanup**: Old usage data is automatically cleaned up to prevent storage bloat

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `daily_limit` | integer | `50` | Maximum conversations per user per day. Set to `0` to disable. |
| `limit_message` | string | `您今天的对话次数已达上限，请明天再来吧~` | Message shown when limit is exceeded. |
| `silent_mode` | boolean | `false` | When enabled, excess messages are silently dropped. |

## How It Works

The plugin listens to both private and group normal message events. For each incoming message, it checks the sender's daily usage count against the configured limit. If the limit is reached:

- **Silent mode off**: Replies with the configured limit message and blocks further processing.
- **Silent mode on**: Silently blocks further processing without any reply.

Usage counts reset automatically each day (UTC-based).
