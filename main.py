from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(openai_api_key="")
llm.invoke("how can langsmith help with testing?")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm 

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

chain.invoke({"input": "how can langsmith help with testing?"})




