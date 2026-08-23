import json

from llm.azure_llm import AzureLLM

from .prompts import (
    MAIN_AGENT_SYSTEM_PROMPT
)

from agents.document_agent.agent import (
    run_document_agent
)

from agents.data_agent.agent import (
    run_data_agent
)

from agents.report_agent.agent import (
    run_report_agent
)


ORCHESTRATOR_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "call_document_agent",
            "description": (
                "Delegate document-related work "
                "to the Document Agent."
            ),
            "parameters": {
                "type": "object",
                "properties": {

                    "task": {
                        "type": "string",
                        "description": (
                            "Detailed task for "
                            "the Document Agent."
                        )
                    }

                },
                "required": ["task"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "call_data_agent",
            "description": (
                "Delegate data-analysis work "
                "to the Data Agent."
            ),
            "parameters": {
                "type": "object",
                "properties": {

                    "task": {
                        "type": "string",
                        "description": (
                            "Detailed task for "
                            "the Data Agent."
                        )
                    }

                },
                "required": ["task"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "call_report_agent",
            "description": (
                "Delegate report creation "
                "to the Report Agent."
            ),
            "parameters": {
                "type": "object",
                "properties": {

                    "task": {
                        "type": "string",
                        "description": (
                            "Detailed task for "
                            "the Report Agent."
                        )
                    }

                },
                "required": ["task"]
            }
        }
    }
]


def execute_agent(
    agent_name,
    task
):

    if agent_name == "call_document_agent":

        return run_document_agent(task)

    if agent_name == "call_data_agent":

        return run_data_agent(task)

    if agent_name == "call_report_agent":

        return run_report_agent(task)

    return {
        "error": "Unknown agent"
    }


def run_main_agent(user_question):

    print("\n")
    print("=" * 60)
    print("🧠 MAIN ORCHESTRATOR AGENT")
    print("=" * 60)

    llm = AzureLLM()

    messages = [

        {
            "role": "system",
            "content": MAIN_AGENT_SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": user_question
        }

    ]

    while True:

        response = llm.chat(
            messages=messages,
            tools=ORCHESTRATOR_TOOLS
        )

        message = response.choices[0].message

        # ------------------------------------------
        # No more agents required
        # ------------------------------------------

        if not message.tool_calls:

            return message.content

        # Add orchestrator decision
        messages.append(message)

        # ------------------------------------------
        # Execute selected agents
        # ------------------------------------------

        for tool_call in message.tool_calls:

            agent_name = (
                tool_call.function.name
            )

            arguments = json.loads(
                tool_call.function.arguments
            )

            task = arguments["task"]

            print("\n")
            print("🚀 MAIN AGENT DELEGATED:")
            print(
                f"   Agent: {agent_name}"
            )
            print(
                f"   Task: {task}"
            )

            result = execute_agent(
                agent_name,
                task
            )

            print("\n")
            print("📨 SPECIALIST RESULT:")
            print(result)

            # Send specialist result
            # back to main agent

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )