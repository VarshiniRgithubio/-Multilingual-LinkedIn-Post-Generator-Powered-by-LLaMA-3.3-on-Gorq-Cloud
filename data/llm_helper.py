# go to env file and set as that enviroment variable
from dotenv import load_dotenv
from langchain_groq import ChatGroq


import os


load_dotenv()
# run the model it will not working driectly it is going into the groq and fetching the data from there
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")


if __name__=='__main__':
    reponse = llm.invoke('what is the two main ingrident in biryani')
    print(reponse.content)