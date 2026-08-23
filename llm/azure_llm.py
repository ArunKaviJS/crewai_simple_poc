from openai import AzureOpenAI

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    TEMPERATURE,
    MAX_TOKENS,
)


class AzureLLM:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=AZURE_OPENAI_API_KEY,
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_version=AZURE_OPENAI_API_VERSION,
        )

        self.deployment = AZURE_OPENAI_DEPLOYMENT

    def chat(
        self,
        messages,
        tools=None,
        tool_choice="auto",
    ):

        kwargs = {
            "model": self.deployment,
            "messages": messages,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
        }

        if tools:
            kwargs["tools"] = tools
            kwargs["tool_choice"] = tool_choice

        response = self.client.chat.completions.create(
            **kwargs
        )

        return response