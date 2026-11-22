# AIBuy MCP 客户端工具包

**当前版本：2026.11.22.1**

GitHub 会根据仓库内容生成 ZIP 下载包：[下载 ZIP](https://github.com/LaoSun0720/aibuy-mcp-client/archive/refs/heads/main.zip)。

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
- [文件校验值](CLIENT_SHA256SUMS)

## 安全与隐私

此仓库只发布客户端配置、说明和本机日志工具，不包含 MCP 服务端源码、服务器密钥、网站账号密码、Cookie、访问令牌、刷新令牌或数据库。业务实现保留在 AIBuy 服务器上。

本机日志使用本机生成的密钥加密；服务端审计记录由服务端保管。不要把密钥或令牌粘贴给 AI。客户端配置和说明无需加密；分发到用户设备的程序无法保证绝对不可逆向，因此核心业务逻辑不随此工具包发布。

客户端每日最多检查一次版本，只提示更新，不会自动覆盖或安装文件。
