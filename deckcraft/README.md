# deckcraft skill

Working notes for driving [DeckCraft](https://github.com/storytold/deckcraft) from an AI agent. Last tested on 0.11.1 (Linux AppImage).

Live editing: start the app with `--control 47824`, then register
`claude mcp add deckcraft -- deckcraft-cli mcp --connect 127.0.0.1:47824`. Headless use needs only `deckcraft-cli`
(extract it from the AppImage). `deckcraft-cli app --port 47824 …` works whenever the port is open.
