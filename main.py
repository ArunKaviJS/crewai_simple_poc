from config.settings import validate_settings

from orchestrator.main_agent import (
    run_main_agent
)


def main():

    validate_settings()

    print("=" * 60)
    print("🤖 ADVANCED MULTI-AGENT SYSTEM")
    print("=" * 60)

    print("\nAvailable agents:")
    print("1. Document Agent")
    print("2. Data Agent")
    print("3. Report Agent")

    print("\nType 'exit' to quit.")

    while True:

        user_question = input(
            "\n👤 User: "
        )

        if user_question.lower() == "exit":
            break

        try:

            answer = run_main_agent(
                user_question
            )

            print("\n")
            print("=" * 60)
            print("🎯 FINAL ANSWER")
            print("=" * 60)

            print(answer)

        except Exception as e:

            print("\n❌ ERROR:")
            print(e)


if __name__ == "__main__":
    main()