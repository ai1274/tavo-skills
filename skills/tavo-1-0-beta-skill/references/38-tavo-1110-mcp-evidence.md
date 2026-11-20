# Tavo 1.11.0：MCP 只读发现与技术更新

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](../../tavo-skill/references/public-release-sources.md)。

2026-11-18（UTC+08:00），本机 `initialize` 和 `tavo_app_version` / `tavo_app_version_number` 均确认 Tavo `1.11.0` / build `1110`；请求和协商协议都是 `2025-06-18`。此版本仅指本次连接，不据此确认所有发布渠道的最新版本。

## 连接和证据范围

使用用户授权的本机直连 HTTP JSON-RPC：`POST /mcp`、`Authorization: Bearer <token>`、接受 JSON 与 SSE。先 `initialize`，再 `notifications/initialized`；后续沿用协商协议和服务器返回的会话 ID（若有）。应用工具经 `tools/call`，名称写在 `params.name`，不是顶层 RPC 方法。凭据不落盘。

`tools/list`、`resources/list`、`resources/templates/list`、`prompts/list` 均成功且无后续分页：**112 工具 / 21 资源 / 8 资源模板 / 0 prompts**。另读取 19 项公开 capabilities、文档和 schema；没有请求用户数据、当前聊天、`runtime` 或 `status`。公开响应和完整描述符见 [1.11.0 快照（来源说明）](../../tavo-skill/references/public-release-sources.md#本地资料)（519216 bytes，SHA-256 `150f1b157b05f6a2f55d4fc1e6de13e7eba33f86109371aea7fabed25bf13157`）。

## 相对 1.10.0 的声明差异

与 [1.10.0 工具（来源说明）](../../tavo-skill/references/public-release-sources.md#本地资料)和[公开文本（来源说明）](../../tavo-skill/references/public-release-sources.md#本地资料)对照，工具名称没有增删，6 个工具仅 `inputSchema` 有变化：

| 工具 | 声明变化 |
| --- | --- |
| `tavo_theme_create` / `tavo_theme_update` | `theme.customJs` / `patch.customJs` 是高级渲染主题脚本字符串。更新省略保留、传 `""` 清空、`null` 无效；主题归档字段为 `custom_js`。重命名或删除资源不会改写 CSS / JS 中的引用。 |
| `tavo_lorebook_create` / `tavo_lorebook_update` / `tavo_lorebook_import` / `tavo_lorebook_entry_upsert` | 激活类型新增 `vectorized`，但工具与条目 schema 明确声明它**尚不会激活**；不能当作可用的世界书召回，也不等于长记忆向量检索。 |

变化的 7 项公开正文：`tavo://docs/` 下的 `tools`、`tavojs`、`plugins`、`plugins/compatibility`、`tool-calling`，及 `tavo://schemas/` 下的 `lorebook-entry` 和 `chat-theme`。其余 12 项正文一致。摘要省略旧细节不证明能力被删除；写入前应按目标重新发现精确 schema。

## 工程适配

- **设置兼容性**：`tavo://docs/plugins/compatibility` 标注 `header`、`placeholder`、textarea 的 `minLines` / `maxLines`、列表默认记录字段的 `$t` 自 `1.11.0` 起且影响最低版本；用到任一项时 `minAppVersion >= 1.11.0`。已有 `list` / `when` 仍从 `1.10.0` 起；不统一抬高现有插件的最低版本。
- **表单语义**：`header` 的 `when` 只控制标题及其布局，不控制后续字段。`placeholder` 可用字符串或 `$t`；省略时普通字段使用 label，列表内无提示，空字符串显式关闭提示。textarea 默认 2–10 行，列表内 2–6 行；有效行数是正整数且上限不低于下限。列表作为整体保存，保留用户保存的空数组；清除覆盖后恢复当前语言的默认值，读取已解析的字符串字段。详见[插件开发](https://docs.tavoai.dev/cn/guides/plugin-development/)。
- **短记忆**：`tavo.memory.getShortTermLength()` 读取最新全局历史消息条数上限；`0` 表示不限制，不是零条。它既不是 token / 轮数，也不是单次生成实际带入的消息数，未出现在外部 MCP 工具列表。详见 [TavoJS API](https://docs.tavoai.dev/cn/guides/javascript-api/)。
- **主题脚本**：`tavo.theme.on` / `.emit` 属于主题脚本环境，不是普通消息脚本接口；自定义事件限定在当前主题、当前聊天，不用它替代插件业务 hooks。详见[主题开发](https://docs.tavoai.dev/cn/guides/theme-development/)。

[官网技术文档同步清单（来源说明）](../../tavo-skill/references/public-release-sources.md#本地资料)记录 17 篇中文技术章节，本次更新 5 篇，其余 12 篇保留原文件。官网与 MCP 声明不是行为实测；未执行主题脚本、世界书激活、安装、业务写入、持久化或任何模型/向量提供方调用。旧版本向量、表单和主题封面声明见 [1.10.0 归档](37-tavo-1100-mcp-evidence.md)。
