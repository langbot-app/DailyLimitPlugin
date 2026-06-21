# Daily Limit Plugin

> ⚠️ **This repository is archived and no longer maintained.**
>
> DailyLimitPlugin has been migrated to the new LangBot plugin SDK and now lives in the
> **[langbot-plugin-demo](https://github.com/langbot-app/langbot-plugin-demo/tree/main/DailyLimitPlugin)** repository,
> where it has been upgraded to be production-ready with a management Page (view/configure/reset
> per-session limits). Please use that version.
>
> 此仓库已归档，不再维护。DailyLimitPlugin 已迁移至新版插件 SDK，现位于
> **[langbot-plugin-demo](https://github.com/langbot-app/langbot-plugin-demo/tree/main/DailyLimitPlugin)** 仓库，
> 并升级为带可视化管理页面的生产可用版本，请使用该版本。

---

Limit the number of conversations per user per day for LangBot.

## Features

- **Per-user daily limit**: Set a maximum number of conversations each user can have per day
- **Customizable message**: Configure the message shown when a user exceeds their daily limit
- **Silent mode**: Optionally discard messages silently without any reply when the limit is reached
- **Timezone-aware reset**: Configure the timezone and hour for daily counter reset
- **Automatic cleanup**: Old usage data is automatically cleaned up to prevent storage bloat
