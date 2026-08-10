from dotenv import load_dotenv
load_dotenv()

from langchain_core import __version__ as core_version

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI


def main():
    # Automatically uses the (GEMINI_API_KEY) environment variable
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0.2,
    )

    response = llm.invoke("Explain quantum computing in one short paragraph.")

    print(response.content)


if __name__ == "__main__":
    main()