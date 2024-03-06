# your code goes here!
#!/usr/bin/env python3
class Anagram:
    def  __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))

    def match(self, words):
        "Returns a list of words that match the initialized word."
        return [word for word in words if self.sorted_word in ''.join(sorted(word)) == self.sorted_word]