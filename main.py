from dotenv import load_dotenv
load_dotenv()
from importlib.metadata import version

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.chat_models import init_chat_model

from langchain_core.messages import HumanMessage,SystemMessage




def main():
    demo_basic_chain()


def test_con():
    # Automatically uses the (GEMINI_API_KEY) environment variable
    llm_gemini = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0.1,
    )
    
    response = llm_gemini.invoke("Say'setup complete!' in one word")

    print(response.content)

    llm_anthropic = ChatAnthropic(
        model="claude-sonnet-4-5-20250929",
        temperature=0,
    )
    response_anthropic = llm_anthropic.invoke("Say'setup complete!' in one word")
    print(f"Response anthropic: {response_anthropic}")

def demo_basic_chain():
    """Demonstrates a basic chain using LEL and Runnables"""
    prompt = ChatPromptTemplate.from_template("You are a helpful assistant. Answer in one sentence:{question}")
    model=ChatAnthropic(model="claude-sonnet-4-5-20250929")
    parser= StrOutputParser()   

    # The pipe operator (|)
    # LangChain overrides Python's __or__ method (that's what | calls) on its core building blocks — Runnable objects. 
    # Every major LangChain component (prompts, models, parsers, retrievers, etc.) inherits from Runnable, so they all support this operator.
    chain = prompt | model | parser

    # execute with input 
    result = chain.invoke({"question":"What is langChain?"})
            
    print(f"response: {result}") 
    return chain 

    
def init_chat():
    """ new universal way to init the model"""
    model = init_chat_model("claude-sonnet-4-5-20250929", temperature=0.7, max_tokens=2000)
    return model
    

if __name__ == "__main__":
    main()