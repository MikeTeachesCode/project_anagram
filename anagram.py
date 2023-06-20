class Anagram:

    from english_words import words as words_string
    _res = {}
    _res2 = {}
    _real_words = []
    _anagram_list = []
    _non_anagram_list = []
    _words = words_string.split(" ")
    
    def __init__(self):
        pass
    
    @classmethod
    def enterWords(cls):
        sentence = input("Enter some words").lower()
        if sentence == "" or sentence == " ":
            print("Cannot be an empty string!")
        else:

            for word in sentence.split(" "):
                if word in cls._words: # ENGLISH_WORDS.PY
                    cls._real_words.append(word)
        for word in cls._real_words:

            cls._res[tuple(sorted(word))] = []

        for key in cls._res:
            for real_word in cls._real_words:

                if tuple(sorted(real_word)) == key:
                    cls._res[key].append(real_word)

        for w in list(cls._res.values()):
            if len(w) >= 2:
                cls._anagram_list.append(w)
            else:
                cls._non_anagram_list.append(w)
        print("Finished")
        
    @classmethod
    def clearResults(cls):
        cls._res.clear()
        cls._anagram_list.clear()
        cls._non_anagram_list.clear()
        cls._real_words.clear()
        print("Cleared all results")
        
    @classmethod
    def showResults(cls):
        print("ANAGRAM LIST")
        for a in cls._anagram_list:
            print(a)
        print("\nNON-ANAGRAM LIST")
        for na in cls._non_anagram_list:
            print(na)
            
    @classmethod
    def oneWord(cls):
        one_word = input("Anagrams for a single word: ").lower()
        
        if one_word in cls._words:

            word = tuple(sorted(one_word))
            cls._res2[word] = []

            for w in cls._words: # ENGLISH_WORDS.PY
                if tuple(sorted(w)) == word:
                    cls._res2[word].append(w)
        print(cls._res2)
        
    @classmethod
    def clearOneWord(cls):
        cls._res2.clear()
        print("Cleared res2")
