from pydantic_ai import Agent
from backend.data_models import RagResponse, Prompt
import lancedb
from backend.constants import VECTOR_DB_PATH

vector_db = lancedb.connect(VECTOR_DB_PATH)

rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt=(
        "You are an expert in rabbit races and knows how to distinguish between the rabbits",
        "Always answer based on the retrieved knowledge, but you can mix in your expertise to make the answer more coherent",
        "Don't hallucinate, rather say you can't answer it if the user prompts outside of the retrieved knowledge",
        "Make sure to keep the answer clear and concise, getting to the point directly, max 6 sentences",
        "Also describe which file you have used as source",
    ),
    output_type=RagResponse,
)


@rag_agent.tool_plain
def retrieve_top_documents(query: str, top_results=3) -> str:
    """
    Uses vector search to find top_results closest matching documents to use as context to the query
    """
    results = vector_db["articles"].search(query=query).limit(top_results).to_list()

    return f"""
    Filename: {results[0]["filename"]},
    Filepath: {results[0]["filepath"]},
    Content: {results[0]["content"]}
    """