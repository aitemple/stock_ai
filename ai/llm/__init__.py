from langchain_openai import AzureChatOpenAI
from openai import OpenAI
import os
azure_llm = AzureChatOpenAI(
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOY_NAME_GPT3"),
    model_name=os.getenv("AZURE_OPENAI_DEPLOY_NAME_GPT3"),
    openai_api_version=os.getenv("AZURE_OPENAI_VERSION"),
    openai_api_key=os.environ["AZURE_OPENAI_KEY"],
    temperature=0
)
kiki_llm = OpenAI(
    base_url=os.getenv("KIKI_OPENAI_BASE_URL"),
    api_key=os.getenv("KIMI_API_KEY")
)
deep_llm = OpenAI(
    base_url=os.getenv("DEEPSEEK_OPENAI_BASE_URL"),
    api_key=os.getenv("DEEPSEEK_API_KEY")
)
