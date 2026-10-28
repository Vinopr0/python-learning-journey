sentence = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

words = [word.lower() for word in sentence.split()]

word_recurrence = {word: words.count(word) for word in words}

print(f"Total words: {len(words)}")

print(f"Unique words: {len(set(words))}")

print(f"Longest Word: {max(words, key=len)}")

print(word_recurrence)

print([word for word in words if len(word) > 5])

