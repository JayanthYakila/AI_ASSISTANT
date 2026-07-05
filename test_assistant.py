from speech.listen import listen
from llm.chat import ask_llm

print("=" * 60)
print("AI Assistant Test")
print("=" * 60)

while True:

    text = listen()

    if not text:
        continue

    print(f"\nYou: {text}")

    if text.lower() == "exit":
        break

    answer = ask_llm(text)

    print("\nAssistant:")
    print(answer)
    print("-" * 60)