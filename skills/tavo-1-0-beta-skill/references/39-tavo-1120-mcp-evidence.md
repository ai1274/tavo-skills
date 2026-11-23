# Tavo 1.12.0 MCP 公开验证摘要

2026 年 11 月 23 日复查的本机实例为 Tavo `1.12.0`（构建 `1120`）。直连 HTTP JSON-RPC 协商协议 `2025-06-18`。发现 112 个工具、21 个资源、8 个资源模板和 0 个提示模板。工具和资源描述符以及读取的 19 项公开正文均与 2026 年 11 月 20 日的同版本快照一致。实际使用前请重新发现目标实例的版本和 schema。[直连运行手册](11-mcp-runtime.md)

## 相较 1.11.0 的声明变化

- 角色脚本和插件可使用 `tavo.decision.evaluate`。插件须声明 `generate` 权限。实际调用依赖用户在 App 中配置的决策模型。[决策开发指南](https://docs.tavoai.dev/cn/guides/decision-api/)
- 启用高级渲染时，`tavo.plugin.on` 和 `tavo.plugin.emit` 可在同一聊天、同一插件的入口脚本与 `/chat` HTML 片段间传递自定义事件。使用这些能力时须针对目标宿主核实支持版本。[插件开发](https://docs.tavoai.dev/cn/guides/plugin-development/)

兼容性资源在这次发现中未标注上述接口的最低版本。表单字段沿用独立的最低版本门槛。[1.11.0 对照](38-tavo-1110-mcp-evidence.md)

## 插件开发校验

合成 TPG v2 样例通过 `tavo_plugin_validate_manifest` 和 `tavo_plugin_audit`。移除 `author` 后，清单检查返回 `missingRequired`。这组检查覆盖清单与合成源码，宿主安装、启用、实际 WebView 渲染和模型执行待单独验证。[插件开发校验](11-mcp-runtime.md#插件开发校验)

官网技术章节使用独立的复核记录。公开仓库保留此验证摘要。[技术文档与证据](../../tavo-skill/references/public-release-sources.md)
