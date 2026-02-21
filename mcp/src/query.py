from weaviate.agents.query import QueryAgent

from src.utils import get_weaviate_sync_client

def ask(query: str) -> str:
    weaviate_sync_client = get_weaviate_sync_client()
    try:
        query_agent = QueryAgent(
            client=weaviate_sync_client,
            collections=["IRPAPERS"],
        )
        response = query_agent.ask(query)
        return response.final_answer
    finally:
        weaviate_sync_client.close()

if __name__ == "__main__":
    print("Here")
    response = ask("What is IRPAPERS?")
    print(response)