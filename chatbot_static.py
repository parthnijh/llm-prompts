from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import os
load_dotenv()
llm=HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2",
                        huggingfacehub_api_token=os.getenv("HUGGING_FACE_API"),
                        task="text-generation")
model=ChatHuggingFace(llm=llm)
chat_history=[
    SystemMessage(content="You are a helpful assistant")
]
while True:
    user=input("You :")
    chat_history.append(HumanMessage(content=user))
    if(user=="exit"):
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI :",result.content)
print(chat_history)