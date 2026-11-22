# AIBuy MCP 快速接入

服务地址：`https://mcp.aibuy.top/v1`

## Codex CLI

```bash
codex mcp add aibuy --url https://mcp.aibuy.top/v1
codex mcp login aibuy --oauth-client-registration dcr
```

打开授权链接后，在 AIBuy 登录并逐项选择权限。完成后浏览器会返回 Codex。不要把密码、Cookie、访问令牌或服务器密钥交给 AI。

## Cursor

可参考 `aibuy-mcp-cursor.json`，将 `mcpServers.aibuy.url` 加到客户端的 MCP 配置中。OAuth 登录由支持远程 HTTP MCP 与 OAuth 的客户端发起。

## 其他客户端

添加远程 HTTP MCP 服务并使用上述 URL。客户端需要支持 OAuth 2.1、动态客户端注册和 PKCE。不同客户端配置格式不同，请按照对应客户端的官方配置说明填写。

## 权限和安全

- 授权页按类别列出权限；账号写入、举报、删除评论和撤销连接使用单独的细分权限。
- 只勾选当前任务需要的权限。连接可以在 AIBuy 的已授权连接页面撤销。
- MCP 每日自动检查一次版本；自动检查只提示更新，不会替你安装更新。
- 服务端保留操作审计记录。客户端也可保存本机加密副本，使用随附的 `aibuy_mcp_local_audit.py`。

## 本地加密日志工具

需要 Python 3.10 或更新版本及 `cryptography`：

```bash
python3 -m pip install cryptography
python3 aibuy_mcp_local_audit.py init
python3 aibuy_mcp_local_audit.py list --limit 50
python3 aibuy_mcp_local_audit.py prune --keep 500
```

密钥和日志保存在 `~/.config/aibuy-mcp/`，文件权限限制为当前用户。`prune` 只清理本机副本，不会删除服务器记录。不要删除 `audit.key`，否则无法读取已有日志。
