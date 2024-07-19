def detectCapitalUse(word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()

print(detectCapitalUse("USA"))
print(detectCapitalUse("FlaG"))