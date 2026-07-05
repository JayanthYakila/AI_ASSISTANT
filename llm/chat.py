import ollama


def ask_llm(prompt: str) -> str:
    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant. "
                    "Answer in English. "
                    "Do not reveal your reasoning or internal thinking. "
                    "Reply directly."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]