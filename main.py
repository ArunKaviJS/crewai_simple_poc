# main.py

import os
import json

from dotenv import load_dotenv
from openai import AzureOpenAI

from tool_definitions import tools

from tools.file_tools import (
    list_files,
    search_file
)

from tools.weather_tools import (
    get_weather
)

from tools.calculator_tools import (
    calculate
)


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# AZURE OPENAI CLIENT
# ============================================================

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")


# ============================================================
# TOOL EXECUTOR
# ============================================================

def execute_tool(tool_name, arguments):

    print("\n--------------------------------")
    print("EXECUTING TOOL")
    print("--------------------------------")

    print("Tool:", tool_name)
    print("Arguments:", arguments)

    # --------------------------------
    # FILE TOOLS
    # --------------------------------

    if tool_name == "list_files":

        return list_files()


    elif tool_name == "search_file":

        return search_file(
            arguments["filename"]
        )


    # --------------------------------
    # WEATHER TOOL
    # --------------------------------

    elif tool_name == "get_weather":

        return get_weather(
            arguments["city"]
        )


    # --------------------------------
    # CALCULATOR
    # --------------------------------

    elif tool_name == "calculate":

        return calculate(
            arguments["expression"]
        )


    else:

        return {
            "error": f"Unknown tool: {tool_name}"
        }


# ============================================================
# USER INPUT
# ============================================================

user_question = input(
    "\n👤 User: "
)


# ============================================================
# INITIAL MESSAGE
# ============================================================

messages = [

    {
        "role": "system",
        "content": """
You are a helpful AI assistant.

You have access to several tools.

Use tools when they are necessary to answer the user's question.

You can call multiple tools if necessary.
"""
    },

    {
        "role": "user",
        "content": user_question
    }

]


# ============================================================
# AGENT LOOP
# ============================================================

while True:

    print("\n🤖 Calling Azure OpenAI...")

    response = client.chat.completions.create(

        model=deployment,

        messages=messages,

        tools=tools,

        tool_choice="auto"
    )


    message = response.choices[0].message


    # ========================================================
    # NO TOOL REQUIRED
    # ========================================================

    if not message.tool_calls:

        print("\n================================")
        print("🤖 FINAL ANSWER")
        print("================================")

        print(message.content)

        break


    # ========================================================
    # TOOL CALLS FOUND
    # ========================================================

    print("\n================================")
    print("🤖 LLM REQUESTED TOOL(S)")
    print("================================")


    # Add assistant message containing tool calls
    messages.append(message)


    # ========================================================
    # EXECUTE EVERY TOOL REQUESTED
    # ========================================================

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )


        print("\n📌 Tool requested by LLM:")
        print("   Name:", tool_name)
        print("   Arguments:", arguments)


        # Execute actual Python function

        result = execute_tool(
            tool_name,
            arguments
        )


        print("\n📦 Tool returned:")
        print(result)


        # ====================================================
        # SEND TOOL RESULT BACK TO LLM
        # ====================================================

        messages.append(

            {
                "role": "tool",

                "tool_call_id": tool_call.id,

                "content": json.dumps(result)
            }

        )