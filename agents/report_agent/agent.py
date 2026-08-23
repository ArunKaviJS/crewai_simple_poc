import json

from llm.azure_llm import AzureLLM

from .prompts import (
    REPORT_AGENT_SYSTEM_PROMPT
)

from .tools import (
    save_report
)


REPORT_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "save_report",
            "description": (
                "Save a business report "
                "to a markdown file."
            ),
            "parameters": {
                "type": "object",
                "properties": {

                    "filename": {
                        "type": "string",
                        "description": (
                            "Filename for the report."
                        )
                    },

                    "content": {
                        "type": "string",
                        "description": (
                            "Complete report content."
                        )
                    }

                },
                "required": [
                    "filename",
                    "content"
                ]
            }
        }
    }
]


def execute_tool(
    tool_name,
    arguments
):

    if tool_name == "save_report":

        return save_report(
            arguments["filename"],
            arguments["content"]
        )

    return {
        "error": f"Unknown tool: {tool_name}"
    }


def run_report_agent(user_task):

    print("\n")
    print("=" * 60)
    print("📝 REPORT AGENT")
    print("=" * 60)

    llm = AzureLLM()

    messages = [

        {
            "role": "system",
            "content": REPORT_AGENT_SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": user_task
        }

    ]

    while True:

        response = llm.chat(
            messages=messages,
            tools=REPORT_TOOLS
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
                f"\n📌 Report Agent selected: "
                f"{tool_name}"
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