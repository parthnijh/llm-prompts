from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
chat_temp=ChatPromptTemplate([
    ("system","you are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")
])
chat_history=[]
myfile=open("chat_history.txt","r")
chat_history.extend(myfile.readlines())
myfile.close()
prompt=chat_temp.invoke({"chat_history":chat_history,"query":"wheres my refund"})
print(prompt)