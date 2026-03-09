from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

def build_rag():

    loader = TextLoader("docs/cmc_guidelines.txt")
    documents = loader.load()

    # 本地 embedding，不需要 OpenAI
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    db = FAISS.from_documents(documents, embeddings)
    retriever = db.as_retriever()

    qa = RetrievalQA.from_chain_type(
        llm=ChatGroq(
            model="llama-3.1-8b-instant",
            groq_api_key=os.getenv("GROQ_API_KEY")
        ),
        retriever=retriever
    )

    return qa



if __name__ == "__main__":

    qa = build_rag()

    question = "What are critical quality attributes?"

    answer = qa.run(question)

    print(answer)
