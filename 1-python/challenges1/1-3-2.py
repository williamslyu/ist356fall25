def cleanup(text):
    for ch in "?,.!":
        text = text.replace(ch, "")
    return text.strip().lower()



examples = [
    " Hello, World! ",
    "Python? Great. ",
    "   CLEANUP test!!!   "
]

for ex in examples:
    print(f"Original: '{ex}' -> Cleaned: '{cleanup(ex)}'")
