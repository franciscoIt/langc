from dotenv import load_dotenv
load_dotenv()
from importlib.metadata import version

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI


def __init__(self):
    load_dotenv()


    
def exercise_first_chain():
    """
    Creates a chain that:
    1. Takes a product name and a target audience
    2. Generates a marketing tagline
    3. Returns just the tagline as a string
    """
    prompt = ChatPromptTemplate.from_template(
        """You are a tagline generator.
You will receive a product and a target audience, and you generate a tagline suited to that audience.

Product: {product}
Audience: {audience}

Respond with ONLY the tagline text — no quotes, no labels, no extra formatting."""
    )


    model=ChatAnthropic(model="claude-sonnet-4-5-20250929")
    parser= StrOutputParser() 

    chain = prompt | model | StrOutputParser()
    return chain

def main(): 
    chain = exercise_first_chain()
    tagline = chain.invoke({"product": "AI course", "audience": "developers"})
    print(tagline)



if __name__ == "__main__":
    main() 




