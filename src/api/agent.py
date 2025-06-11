import logging
from agents import Agent, function_tool
from prompts.base_agent import PROMPT_SYSTEME_ZLV_AGENT
from prompts.common import TABLES_SCHEMA_COMMON_PROMPT
from prompts.establishment import TABLES_SCHEMA_ESTABLISHMENT_PROMPT
from prompts.joins_prompt import TABLES_SCHEMA_JOINS_PROMPT
from prompts.production_prompt import TABLES_SCHEMA_PRODUCTION_PROMPT
from prompts.sql_agent_prompt import PROMPT_SYSTEM_AGENT_SQL
from pydantic import BaseModel
import pandas as pd
from typing import Literal, Optional

logger = logging.getLogger("openai.agents") # or openai.agents.tracing for the Tracing logger

class Query(BaseModel):
    query: str

class GeographicalQuery(BaseModel):
    level: Literal["city", "department", "region"]
    metric: str  # The metric to aggregate (e.g., "count(*)", "sum(revenue)", etc.)
    table: str   # The main table to query from
    filters: Optional[str] = None  # Optional WHERE clause filters
    join_clauses: Optional[str] = None  # Optional JOIN clauses if needed

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
        logger.error("Aucune requête SQL fournie.")
        return "Aucune requête SQL fournie."
    try:
        logger.info(f"Connexion à la base de données MotherDuck")
        con = duckdb.connect(database="md:dwh?motherduck_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJhcGhhZWwuY291cml2YXVkQGJldGEuZ291di5mciIsInNlc3Npb24iOiJyYXBoYWVsLmNvdXJpdmF1ZC5iZXRhLmdvdXYuZnIiLCJwYXQiOiI4Xzg2N0ZxeFBVTzJBbU94UlNtNGlMNDBjMXctZUQyZHpiR3dfRVl4ekFJIiwidXNlcklkIjoiN2RiYjUyNjctNTc0Zi00Yjc2LTk5MjctNWQyYmQ4ZjZjMjUxIiwiaXNzIjoibWRfcGF0IiwicmVhZE9ubHkiOmZhbHNlLCJ0b2tlblR5cGUiOiJyZWFkX3dyaXRlIiwiaWF0IjoxNzQ5NjU0MTUyLCJleHAiOjE3NTA1MTgxNTJ9.AiIs1gSEVjLc8wanlbCsKWBqHVmsCB5BpmDCkVa1te0", read_only=True)
        logger.info(f"Exécution de la requête SQL: {query.query}")
        result = con.execute(query.query).fetchdf()
        logger.info(f"Résultat de la requête SQL: {result}")
        output = result.to_dict(orient="records")
        logger.info(f"Résultat de la requête SQL: {output}")
        return str(output)
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution de la requête SQL: {str(e)}")
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

        Tu as maintenant deux outils principaux:
        1. motherduck_tool: Pour les requêtes SQL générales
        2. geographical_analysis_tool: Pour les analyses géographiques par ville, département ou région

        Pour les analyses géographiques, utilise geographical_analysis_tool qui peut:
        - Analyser par niveau: 'city', 'department', ou 'region'
        - Retourner les codes géographiques appropriés
        - Agréger les données selon le niveau choisi
        - Inclure des métriques personnalisées

        Créé une requête appropriée pour répondre à la question de l'utilisateur. 
        Ensuite utilise l'outil adapté pour exécuter la requête et récupérer les données.
        Renvoies les informations de la requête et des données récupérées.
        """,
        model="gpt-4.1",
        tools=[tool_motherduck],
    )
    return agent
