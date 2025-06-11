
from agents import Agent, function_tool
from prompts.base_agent import PROMPT_SYSTEME_ZLV_AGENT
from prompts.common import TABLES_SCHEMA_COMMON_PROMPT
from prompts.establishment import TABLES_SCHEMA_ESTABLISHMENT_PROMPT
from prompts.joins_prompt import TABLES_SCHEMA_JOINS_PROMPT
from prompts.production_prompt import TABLES_SCHEMA_PRODUCTION_PROMPT
from prompts.sql_agent_prompt import PROMPT_SYSTEM_AGENT_SQL
from pydantic import BaseModel

class Query(BaseModel):
    query: str

@function_tool(name_override="motherduck_tool")
async def tool_motherduck(query: Query) -> str:
    """
    Exécute une requête SQL sur MotherDuck et retourne les résultats.

    Args:
        query: Un objet contenant la requête SQL à exécuter.

    Returns:
        Les résultats de la requête SQL sous forme de liste de dictionnaires, ou un message d'erreur.
    """
    import duckdb

    if not query or not query.query:
        return "Aucune requête SQL fournie."
    try:
        con = duckdb.connect(database="md:dwh?motherduck_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJhcGhhZWwuY291cml2YXVkQGJldGEuZ291di5mciIsInNlc3Npb24iOiJyYXBoYWVsLmNvdXJpdmF1ZC5iZXRhLmdvdXYuZnIiLCJwYXQiOiJINU1ucmFyVFRCNGlob0J0aTFxWUlqNVMxRWJTdVo3M2w1QllET0Q3cEF3IiwidXNlcklkIjoiN2RiYjUyNjctNTc0Zi00Yjc2LTk5MjctNWQyYmQ4ZjZjMjUxIiwiaXNzIjoibWRfcGF0IiwicmVhZE9ubHkiOmZhbHNlLCJ0b2tlblR5cGUiOiJyZWFkX3dyaXRlIiwiaWF0IjoxNzQ5NjUxNzE3LCJleHAiOjE3NTA1MTU3MTd9.bpR8-82I3S7p1ELI4nV0trvs2XOcisOIma3-DJo4H5U'", read_only=True)
        result = con.execute(query.query).fetchdf()
        output = result.to_dict(orient="records")
        return str(output)
    except Exception as e:
        return f"Erreur lors de l'exécution de la requête SQL: {str(e)}"

async def build_zlv_agent() -> Agent:
    agent = Agent(
        name="ZLV Assistant",
        instructions=f"""{PROMPT_SYSTEME_ZLV_AGENT}
        <{PROMPT_SYSTEM_AGENT_SQL}>
        <{TABLES_SCHEMA_COMMON_PROMPT}>
        <{TABLES_SCHEMA_ESTABLISHMENT_PROMPT}>
        <{TABLES_SCHEMA_JOINS_PROMPT}>
        <{TABLES_SCHEMA_PRODUCTION_PROMPT}>

        Use tools to answer the user question.

        Créé une requête SQL pour répondre à la question de l'utilisateur. 
        Ensuite utilise la tool motherduck pour exécuter la requête SQL et récupérer les données.
        Renvoies les informations de la requête SQL et des données récupérées.
        """,
        model="gpt-4.1",
        tools=[tool_motherduck],
    )
    return agent
