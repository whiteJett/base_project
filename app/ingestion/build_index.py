from app.ingestion.loader import load_docs,split_docs
from app.deps import get_embeddings,get_vs

def main():
    docs=split_docs(load_docs("/home/zero/PycharmProjects/PythonProject1/date/docs"))
    vs=get_vs()
    vs.add_documents(docs)
    print(f"Indexed{len(docs)} chunks into Chroma.")

if __name__ == "__main__":
    main()