#MCP SERVICE DEMO

This is a basic app to run an mcp server with a client in a dockerized container.

## Local Setup

1. Copy the .env file to create an .env.local.
2. Populate Azure_Open_API_Key in .env.local.
3. run `docker build -t mcp-service .`
4. run `./docker-start.ps1`