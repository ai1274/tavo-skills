# Tavo MCP Plugin Compatibility Table (1.3.2)

Historical table: unchanged through the 2026-11-07 1.9.0 capture. The 2026-11-14 1.10.0 resource adds `contributes.settings.schema.when` and `contributes.settings.schema.list`, both since 1.10.0; see `references/37-tavo-1100-mcp-evidence.md` for that version and [1.11.0 evidence](38-tavo-1110-mcp-evidence.md) for the later compatibility declarations. The original dates, hash and table below are retained.

整理日期：`2026-09-11`（Asia/Shanghai）  
证据级别：`mcp-runtime`  
来源：`tavo://docs/plugins/compatibility`  
字符数：`2351`  
SHA-256：`4f802fab4142c743e913f06a49fb2fc20eaca1b339cbe6b50f790776d10606b7`  
机器可读原文：`assets/evidence/1.3.2/20260911-plugins-compatibility.json`

本文件是 1.3.2 现场只读 `resources/read` 的可读整理。它不是官网 14 页中文主题页，也不证明安装、UI、持久化或 live 行为。连接文案标注 `1.3.1`；`initialize` 返回 `1.3.2`。

## 规则

- 将 `minAppVersion` 设为插件**实际使用**且 `affectsMinimum=true` 的能力中最高的 `since`。不要默认写成当前 Tavo 版本。
- 若所用能力不在本表，报告缺少兼容元数据，不要猜版本。
- `minAppVersion` 安装拦截自 `0.93.0` 起对 `specVersion: 2` 生效。字段 `manifest.minAppVersion` 本身的 `affectsMinimum` 为 `false`，不会单独抬高最低版本。

## 能力表

| id | since | affectsMinimum | manifestDetectable | 摘要 |
| --- | --- | --- | --- | --- |
| `manifest.specVersion.2` | 0.91.0 | true | true | Plugin manifest specification version 2. |
| `manifest.minAppVersion` | 0.93.0 | false | true | Installation enforcement for specVersion 2. This metadata does not raise the plugin minimum by itself. |
| `contributes.inputActions` | 0.91.0 | true | true | Native actions in the chat input menu. |
| `contributes.settings` | 0.91.0 | true | true | Declarative plugin settings and `tavo.plugin.config`. Alias: `tavo.plugin.config`. |
| `contributes.sidebar` | 0.91.0 | true | true | Native actions in the chat sidebar. |
| `contributes.htmlFragments` | 0.91.0 | true | true | Plugin HTML fragments mounted in Advanced Rendering. |
| `tavo.generate` | 0.91.0 | true | false | One-off text generation from plugin runtime code. |
| `tavo.message.variant` | 1.3.0 | true | false | Create and manage alternative candidates for a message. |
| `contributes.lastMessageActions` | 1.3.0 | true | true | Actions beside the absolute-last stable chat message. |

对本仓库活动插件 `tavo-memory-steward-tpg-v2/`：必须使用 `specVersion: 2`、根 `entry.js` 和声明的 `localization`。平台仍兼容缺省/`1` 与 `scripts.actions` 别名，但项目禁止用它们做新开发。当前 Memory Steward 贡献面为 `inputActions`、`sidebar`、`htmlFragments`；未使用 `lastMessageActions` 或 `tavo.message.variant`，因此不能仅因 1.3.2 主机而把 `minAppVersion` 抬到 `1.3.0`。

## 原文

见 `assets/evidence/1.3.2/20260911-plugins-compatibility.json`。该文件与本次读取的 UTF-8 正文字节一致。
