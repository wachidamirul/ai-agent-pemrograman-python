from core.agent import Agent

def main():
    agent = Agent()
    print("Agent siap. Ketik 'exit' atau tekan Ctrl+C untuk keluar.")

    try:
        while True:
            user_input = input("\nUSER > ")

            if user_input.lower() in ["exit", "quit"]:
                print("\nAGENT > Good bye 👋")
                break

            result = agent.run(user_input)
            print("\nAGENT >", result)

    except KeyboardInterrupt:
        print("\n\nAGENT > Good bye 👋")

if __name__ == "__main__":
    main()
