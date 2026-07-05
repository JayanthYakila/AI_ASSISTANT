from llm.chat import ask_llm

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ask_llm(question)

    print("\nAssistant:")
    print(answer)
    print("-" * 50)