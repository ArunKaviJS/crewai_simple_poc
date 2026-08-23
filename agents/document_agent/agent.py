import json

from llm.azure_llm import AzureLLM

from .prompts import (
    DOCUMENT_AGENT_SYSTEM_PROMPT
)

from .tools import (
    list_documents,
    read_document,
    search_document,
)


DOCUMENT_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "list_documents",
            "description": (
                "List all available text documents."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "read_document",
            "description": (
                "Read the contents of a text document."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": (
                            "Name of the document to read."
                        )
                    }
                },
                "required": ["filename"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "search_document",
            "description": (
                "Search all documents for a keyword."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": (
                            "Keyword to search for."
                        )
                    }
                },
                "required": ["keyword"]
            }
        }
    }
]


def execute_tool(
    tool_name,
    arguments
):

    if tool_name == "list_documents":

        return list_documents()

    if tool_name == "read_document":

        return read_document(
            arguments["filename"]
        )

    if tool_name == "search_document":

        return search_document(
            arguments["keyword"]
        )

    return {
        "error": f"Unknown tool: {tool_name}"
    }


def run_document_agent(user_task):

    print("\n")
    print("=" * 60)
    print("📄 DOCUMENT AGENT")
    print("=" * 60)

    llm = AzureLLM()

    messages = [

        {
            "role": "system",
            "content": DOCUMENT_AGENT_SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": user_task
        }

    ]

    while True:

        response = llm.chat(
            messages=messages,
            tools=DOCUMENT_TOOLS
        )

        message = response.choices[0].message

        if not message.tool_calls:

            return message.content

        messages.append(message)

        for tool_call in message.tool_calls:

            tool_name = (
                tool_call.function.name
            )

            arguments = json.loads(
                tool_call.function.arguments
            )

            print(
                f"\n📌 Document Agent selected: "
                f"{tool_name}"
            )

            print(
                f"Arguments: {arguments}"
            )

            result = execute_tool(
                tool_name,
                arguments
            )

            print(
                f"📦 Tool result: {result}"
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                }
            )