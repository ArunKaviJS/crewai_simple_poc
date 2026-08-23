import json

from llm.azure_llm import AzureLLM

from .prompts import (
    DATA_AGENT_SYSTEM_PROMPT
)

from .tools import (
    list_datasets,
    inspect_dataset,
    analyze_dataset,
)


DATA_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "list_datasets",
            "description": (
                "List all CSV datasets available."
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
            "name": "inspect_dataset",
            "description": (
                "Inspect a CSV dataset including "
                "columns, data types, row count "
                "and sample records."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": (
                            "CSV filename."
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
            "name": "analyze_dataset",
            "description": (
                "Perform statistical analysis "
                "on a CSV dataset."
            ),
            "parameters": {
                "type": "object",
                "properties": {

                    "filename": {
                        "type": "string",
                        "description": (
                            "CSV filename."
                        )
                    },

                    "analysis": {
                        "type": "string",
                        "description": (
                            "Description of the "
                            "analysis required."
                        )
                    }

                },
                "required": [
                    "filename",
                    "analysis"
                ]
            }
        }
    }
]


def execute_tool(
    tool_name,
    arguments
):

    if tool_name == "list_datasets":

        return list_datasets()

    if tool_name == "inspect_dataset":

        return inspect_dataset(
            arguments["filename"]
        )

    if tool_name == "analyze_dataset":

        return analyze_dataset(
            arguments["filename"],
            arguments["analysis"]
        )

    return {
        "error": f"Unknown tool: {tool_name}"
    }


def run_data_agent(user_task):

    print("\n")
    print("=" * 60)
    print("📊 DATA AGENT")
    print("=" * 60)

    llm = AzureLLM()

    messages = [

        {
            "role": "system",
            "content": DATA_AGENT_SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": user_task
        }

    ]

    while True:

        response = llm.chat(
            messages=messages,
            tools=DATA_TOOLS
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
                f"\n📌 Data Agent selected: "
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