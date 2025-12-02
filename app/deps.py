from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
# from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import DashScopeEmbeddings
from app.config import settings
from app.rag.vectorstore import get_vectorstore

# def get_llm():
#     return ChatOpenAI(
#         model=settings.model_name,
#         api_key=settings.openai_api_key,
#         temperature=0.2,
#         streaming=True,
#
#     )

def get_llm():
    return ChatOpenAI(
        model=settings.model_name,
        api_key=settings.openai_api_key,
        temperature=0.2,
        streaming=True,
        base_url=settings.base_url,

    )
# def get_llm():
#     return ChatOllama(
#         model=settings.model_name,
#         temperature=0.2,
#         streaming=True,
#
#     )




def get_embeddings():
    return DashScopeEmbeddings(
        model=settings.qwen_embedding_model,
        dashscope_api_key=settings.dashscope_api_key,

    )


def get_vs():
    return get_vectorstore(get_embeddings())


if __name__ == '__main__':
    print('--------------')
    print(get_llm())
    print('--------------')
    print(get_vs())
    print('--------------')
