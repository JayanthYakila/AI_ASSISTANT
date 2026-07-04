from speech.listen import listen

print("=" * 50)
print("Testing Faster Whisper")
print("=" * 50)

text = listen()

print("\nYou said:")
print(text)