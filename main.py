from dotenv import load_dotenv
load_dotenv()

from langchain_core import __version__ as core_version

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI


def main():
    test_con()


def test_con():
    # Automatically uses the (GEMINI_API_KEY) environment variable
    llm_gemini = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0.1,
    )
    
    response = llm_gemini.invoke(""Say'setup complete!' in one word"")

    print(response.content)

    llm_anthropic = ChatAnthropic(
        model="claude-sonnet-4-5-20250929",
        temperature=0,
    )
    response_anthropic = llm_anthropic.invoke("Say'setup complete!' in one word")
    print(f"Response anthropic: {response_anthropic}")

if __name__ == "__main__":
    main()