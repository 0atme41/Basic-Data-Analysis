import math
import collections
import itertools

words = sorted({line.strip().lower() for line in open("words.txt", "r")})

# finding anagrams
def signature(word):
    return "".join(sorted(word))

words_by_sig = collections.defaultdict(set)

for word in words:
    words_by_sig[signature(word)].add(word)

# created a dictionary of signature-anagrams pairs
anagrams_by_sig = {sig: wordset for sig, wordset in words_by_sig.items() if len(wordset) > 1}

# finding palindromes from the anagrams
pairs = []

for wordset in anagrams_by_sig.values():
    for word1 in wordset:
        for word2 in wordset:
            # consider only sorted pairs to avoid duplicate matches
            if word1 >= word2 and word1[::-1] == word2:
                pairs.append((word1, word2))

print(pairs)