# tools/calculator_tools.py


def calculate(expression):
    """
    Calculate a mathematical expression.
    """

    print(f"\n🔧 TOOL CALLED: calculate(expression='{expression}')")

    try:

        # Simple demonstration only.
        # Don't use eval like this with untrusted production input.
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return {
            "expression": expression,
            "result": result
        }

    except Exception as e:

        return {
            "expression": expression,
            "error": str(e)
        }