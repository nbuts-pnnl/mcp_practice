import asyncio
import os

from langchain_openai import AzureChatOpenAI
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent


async def agent_get():

    async with streamablehttp_client("http://localhost:8080/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            try:
                print("Initializing session...")
                await session.initialize()

                # Get tools
                print("Loading MCP tools...")
                tools = await load_mcp_tools(session)

                # Create and run the agent
                print("Creating agent...")
                azure_deployment_name='gpt-4o'
                azure_openai_api_version='2024-05-01-preview'
                azure_openai_api_key=os.getenv("AZURE_OPENAI_API_KEY")
                azure_openai_endpoint='https://policyai-openai-westus.openai.azure.com/'

                llm = AzureChatOpenAI(
                    azure_endpoint=azure_openai_endpoint,
                    api_key=azure_openai_api_key,
                    api_version=azure_openai_api_version,
                    deployment_name=azure_deployment_name,
                    temperature=0.7,
                )


                agent = create_react_agent(llm, tools)
                print("Invoking agent...")
                agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
                response = agent_response  # your returned dict
                for msg in response['messages']:
                    if msg.__class__.__name__ == "AIMessage" and msg.content:
                        print(msg.content)  # This is the natural language response
            except Exception as e:
                print("Error occurred while invoking agent:", e)

if __name__ =="__main__":
    asyncio.run(agent_get())