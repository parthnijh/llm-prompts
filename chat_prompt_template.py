from langchain_core.prompts import ChatPromptTemplate
chat_temp=ChatPromptTemplate([
    ("system","you are a helpful expert of {domain}"),
    ("human","what is {topic}")
])
prompt=chat_temp.invoke({"domain":"cricket","topic":"swing"})
print(prompt)