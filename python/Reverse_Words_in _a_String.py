def reverseWords(s: str) -> str:
    return ' '.join(word[::-1] for word in s.split())

print(reverseWords("Let's take LeetCode contest"))
