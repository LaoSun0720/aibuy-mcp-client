# AIBuy MCP 客户端卸载说明

本说明用于移除你自己设备上的 AIBuy MCP 连接、撤销账号授权，并按需清理本机加密日志。请只删除名称为 `aibuy` 的连接；不要清空其他 MCP 配置。卸载客户端连接不会删除 AIBuy 主站账号或服务器审计记录。

## 1. 从 AI 客户端移除连接

### Codex CLI

先确认列表中有 `aibuy`，然后执行：

```bash
codex mcp list
codex mcp remove aibuy
```

如果客户端没有 `remove` 命令，请在客户端设置中只删除名为 `aibuy` 的 MCP 条目。不要删除其他 MCP 服务。

### Claude Code

```bash
claude mcp remove aibuy
```

如果命令不可用，请按 Claude Code 官方说明打开 MCP 配置，并只删除 `aibuy` 对象。

### 其他客户端

在该客户端的 MCP 设置中移除名称为 `aibuy` 的服务器。它使用的服务地址是：

```text
https://mcp.aibuy.top/v1
```

如果需要编辑 JSON 配置，只删除下面这个对象，不要覆盖整个配置文件：

```json
{
  "mcpServers": {
    "aibuy": {
      "url": "https://mcp.aibuy.top/v1"
    }
  }
}
```

删除客户端配置后，该客户端将不再发起新的连接；这一步不会撤销已经授予的账号权限。

## 2. 撤销 AIBuy 账号授权

1. 在浏览器打开 [AIBuy 已授权连接](https://mcp.aibuy.top/oauth/connections)。
2. 登录你授权时使用的 AIBuy 账号。
3. 找到对应的 AI 客户端连接并撤销。
4. 确认该连接已从授权列表移除。

撤销后，服务器端会使该连接的令牌失效并清除相关加密网站会话。不要把账号密码、Cookie、访问令牌、刷新令牌或服务器密钥交给 AI。

## 3. 清理本机加密操作日志（可选）

随附工具的本机密钥和加密日志保存在 `~/.config/aibuy-mcp/`。先确认该目录只含有你希望删除的 AIBuy MCP 本机数据，再执行：

```bash
rm -rf ~/.config/aibuy-mcp
```

这会永久删除本机密钥和加密日志；密钥删除后，已删除的本机日志无法恢复。此操作只影响当前设备，不会删除服务器保留的审计记录。

如果你只想删掉部分本机日志而保留其余记录，请使用工具的保留数量选项：

```bash
python3 aibuy_mcp_local_audit.py prune --keep 500
```

## 4. 检查卸载结果

- AI 客户端的 MCP 列表中不再有 `aibuy`。
- AIBuy 的已授权连接页面中已撤销对应连接。
- 如选择清理本机日志，`~/.config/aibuy-mcp/` 已不存在。

如需彻底删除服务器端审计数据或停用服务，请由 AIBuy 管理员通过内部运维流程处理；普通用户无需执行服务器命令。卸载客户端连接时不要停止、重启或删除任何服务器服务。
