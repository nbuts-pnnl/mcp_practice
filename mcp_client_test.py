from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import asyncio
import traceback

client = MultiServerMCPClient(
    {
        "Math": {
            #"command": "python",
            # Replace with absolute path to your math_server.py file
            #"args": ["<absolute_path_to>/mcp_test.py"],
            #"transport": "stdio",
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
        # "weather": {
        #     # Ensure you start your weather server on port 8000
        #     "url": "http://localhost:8000/mcp",
        #     "transport": "streamable_http",
        # }
    }
)

async def agent_get():
    print("starting execution")
    print("getting tools")
    tools = await client.get_tools()
    print("creating agent")
    try:
        agent = create_react_agent(
            "anthropic:claude-3-7-sonnet-latest",
            tools
        )
        print("Invoking math")
        math_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
        )
        # print("invoking weather")
        # weather_response = await agent.ainvoke(
        #     {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
        # )
    except Exception as e:
        print(e)
        traceback.print_exc()
        return
    print("printing responses")
    print(math_response.messages)
    #print(weather_response.messages)

if __name__ =="__main__":
    asyncio.run(agent_get())