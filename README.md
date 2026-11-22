# AIBuy MCP 客户端工具包

GitHub 会根据仓库内容生成 ZIP 下载包：[下载接入工具包](https://github.com/LaoSun0720/aibuy-mcp-client/archive/refs/heads/main.zip)。

MCP 服务地址：`https://mcp.aibuy.top/v1`

## 连接 Codex

```bash
codex mcp add aibuy --url https://mcp.aibuy.top/v1
codex mcp login aibuy --oauth-client-registration dcr
```

浏览器打开授权页后，登录 AIBuy 并选择需要的权限。授权完成后，浏览器会返回 Codex。其他客户端请使用同一个服务地址，并按其官方 MCP/OAuth 配置方式连接。

## 文件

- [快速接入说明](MCP_CLIENT_GUIDE.md)
- [卸载、撤销授权和本机清理说明](MCP_UNINSTALL.md)
- [Cursor 配置示例](aibuy-mcp-cursor.json)
- [本机加密操作日志工具](aibuy_mcp_local_audit.py)

## 安全与隐私

工具包只包含连接配置、使用说明和本机日志工具，不包含网站密码、Cookie、访问令牌、刷新令牌、服务器密钥或数据库。业务数据只会在你完成授权后按所选权限处理。

本机日志使用设备上生成的密钥加密；服务器会保留必要的操作记录。不要把密钥或令牌粘贴给 AI。

连接状态只在需要时检查，不会自动覆盖或安装文件。
