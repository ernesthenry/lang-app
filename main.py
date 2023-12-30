from langchain.chat_models import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OpenAIEmbeddings


loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
llm = ChatOpenAI(openai_api_key="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")


llm.invoke("how can langsmith help with testing?")
docs = loader.load()
embeddings = OpenAIEmbeddings()







