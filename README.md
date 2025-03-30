# Think Server

## セットアップ方法

### MCPサーバーの設定

Claude Desktopでこのサーバーを使用するには、以下の設定を`claude_desktop_config.json`に追加してください：

```json
{
    "mcpServers": {
        "think": {
            "command": "uv",
            "args": [
                "--directory",
                "C:\\Users\\{user}\\mcp_server\\think_server",
                "run",
                "server.py"
            ]
        }
    }
}
```

注意：
- `{user}`は実際のユーザー名に置き換えてください
- パスは実際のサーバーのインストール場所に合わせて調整してください
