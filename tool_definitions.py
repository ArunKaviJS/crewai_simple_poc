# tool_definitions.py


tools = [

    # -----------------------------
    # FILE TOOLS
    # -----------------------------

    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List all files available in the system.",
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
            "name": "search_file",
            "description": "Search for a file using its filename.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The filename or part of the filename to search for."
                    }
                },
                "required": ["filename"]
            }
        }
    },

    # -----------------------------
    # WEATHER TOOL
    # -----------------------------

    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather information for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city."
                    }
                },
                "required": ["city"]
            }
        }
    },

    # -----------------------------
    # CALCULATOR TOOL
    # -----------------------------

    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression such as 10 + 20 or 100 / 5."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]