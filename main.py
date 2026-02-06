from core.agent import Agent

def main():
    agent = Agent()

    while True:
        user_input = input("\nUSER > ")
        if user_input.lower() in ["exit", "quit"]:
            break

        result = agent.run(user_input)
        print("\nAGENT >", result)

if __name__ == "__main__":
    main()
