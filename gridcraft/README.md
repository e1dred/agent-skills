# gridcraft skill

Working notes for driving [GridCraft](https://github.com/storytold/gridcraft) from an AI agent. Last tested on 0.14.2 (Linux AppImage).

Live editing: start the app with `--control 47823` (e.g. in its `.desktop` launcher), then register
`claude mcp add gridcraft -- gridcraft-cli mcp --connect 47823`. Headless use needs only `gridcraft-cli`
(extract it from the AppImage). Without the app running the MCP server reports "failed to connect";
`gridcraft-cli send 47823 …` works as soon as the port is open.
