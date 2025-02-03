#Max Holdaway Simple Morse Code Translator

#Making the lists for the letters and morse code.
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "."]
morse_characters_list = [". ---", "--- . . .", "--- . --- .", "--- . .", ".", ". . --- .", "--- --- .", ". . . .", ". .", ". --- --- ---", "--- . ---", ". --- . .", "--- ---", "--- .", "--- --- ---", ". --- --- .", "--- --- . ---", ". --- .", ". . .", "---", ". . ---", ". . . ---", ". --- ---", "--- . . ---", "--- . --- ---", "--- --- . .", ".-.-.-"]

def word_to_morse(word):
    morse_word = []
    for character in word:
        if character in alphabet_list:
            character_index = alphabet_list.index(character)
            morse_character = morse_characters_list[character_index]
            morse_word.append(morse_character)
    return " ".join(morse_word)

    

def english_to_morse(user_input):
    morse_word_list = []
    user_input = user_input.lower()
    list_of_words = user_input.split()
    for word in list_of_words:
        morse_word_list.append((word_to_morse(word)))
    return " / ".join(morse_word_list)

    

def morse_to_english(user_input):
    pass

sentence_1 = "Morse code is annoying."
sentence_2 = "--- . --- . . --- --- .-.-.-"