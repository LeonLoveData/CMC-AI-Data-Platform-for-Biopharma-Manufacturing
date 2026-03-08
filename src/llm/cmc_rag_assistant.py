from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


def build_rag():

    loader = TextLoader("docs/cmc_guidelines.txt")

    documents = loader.load()

    embeddings = OpenAIEmbeddings()

    db = FAISS.from_documents(documents, embeddings)

    retriever = db.as_retriever()

    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(),
        retriever=retriever
    )

    return qa


if __name__ == "__main__":

    qa = build_rag()

    question = "What are critical quality attributes?"

    answer = qa.run(question)

    print(answer)
