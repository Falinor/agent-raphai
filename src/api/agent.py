

from agents import Agent
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from agents.mcp import MCPServerStdio
from prompts.base_agent import PROMPT_SYSTEME_ZLV_AGENT
from prompts.common import TABLES_SCHEMA_COMMON_PROMPT
from prompts.establishment import TABLES_SCHEMA_ESTABLISHMENT_PROMPT
from prompts.joins_prompt import TABLES_SCHEMA_JOINS_PROMPT
from prompts.production_prompt import TABLES_SCHEMA_PRODUCTION_PROMPT
from prompts.sql_agent_prompt import PROMPT_SYSTEM_AGENT_SQL


async def build_zlv_sql_agent() -> Agent:
    # Get the predefined queries prompt section

    async with MCPServerStdio(
        params={
            "command": "uvx",
            "args": [
                "mcp-server-motherduck",
                "--db-path",
                "md:",
                "--motherduck-token",
                "<YOUR_MOTHERDUCK_TOKEN_HERE>"
            ],
        }
    ) as server:
        tools = await server.list_tools()
        
    agent = Agent(
        name="SQL Assistant",
        instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
        <{PROMPT_SYSTEM_AGENT_SQL}>
        <{TABLES_SCHEMA_COMMON_PROMPT}>
        <{TABLES_SCHEMA_ESTABLISHMENT_PROMPT}>
        <{TABLES_SCHEMA_JOINS_PROMPT}>
        <{TABLES_SCHEMA_PRODUCTION_PROMPT}>

        Use tools to answer the user question.

        First, determine if you can use a predefined query to answer the question:
        1. Use the list_predefined_queries tool to see available queries.
        2. Use the get_predefined_query tool to retrieve a specific query if it matches the user's needs.
        3. You can modify the predefined query if needed to better match the user's question.

        If no predefined query matches the user's needs, write a custom SQL query.

        Next steps:
        1. Perform the SQL query to get the data. If it's not needed just answer the user question directly.
        2. Then, if needed you can use the tools to create visualisations of the data:
           - Table visualisations
           - Scatter chart visualisations
           - Bar chart visualisations
           - Pie chart visualisations
           - Line chart visualisations
        """,
        tools=[],
        mcp_servers=[tools],
        
        model="gpt-4.1",
        input_guardrails=[],
        tool_use_behavior="run_llm_again",
    )
    return agent



def build_zlv_agent() -> Agent:
    agent = Agent(
        name="ZLV Assistant",
        instructions=PROMPT_SYSTEME_ZLV_AGENT,
        model="gpt-4.1",
        handoffs=[build_zlv_sql_agent()],
        handoff_description="Use SQL Agent to answer the user question if needed",
    )
    return agent
