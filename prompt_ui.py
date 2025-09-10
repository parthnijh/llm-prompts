from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
import streamlit as st
import os
llm=HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2",
                        huggingfacehub_api_token=os.getenv("HUGGING_FACE_API"),
                        task="text-generation")
model=ChatHuggingFace(llm=llm)
st.header("Research Paper Tool")
paper= st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style=st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length=st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )
template=load_prompt("template.json")

if st.button("Summarize"):
    chain=template | model
 
    result=chain.invoke({
    "paper":paper,
    "style":style,
    "length":length
    })
    st.write(result.content)