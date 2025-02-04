#Max Holdaway Simple Morse Code Translator

#Making the lists for the letters and morse code.
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "?"]
morse_characters_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".-.-.-", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", "-.-.--", "..--.."]

#Converting english words to morse words
def english_word_to_morse(word):
    morse_word = []
    for character in word:
        if character in alphabet_list:
            character_index = alphabet_list.index(character)
            morse_character = morse_characters_list[character_index]
            morse_word.append(morse_character)
    return " ".join(morse_word)

    
#Converting english phrases to morse code
def english_to_morse(user_input):
    morse_word_list = []
    user_input = user_input.lower()
    list_of_english_words = user_input.split()
    for word in list_of_english_words:
        morse_word_list.append((english_word_to_morse(word)))
    return " / ".join(morse_word_list)

#Converting morse characters to english characters
def morse_character_to_english(character):
    english_character = []
    if character in morse_characters_list:
        morse_index = morse_characters_list.index(character)
        print(morse_index)
        english_character = alphabet_list[morse_index]
        print(english_character)
        return " ".join(english_character)
    elif character == "/":
        english_character = " "
        return english_character
    else:
        print("One or more characters in your sentence were not morse code characters.")
        return ""

    
#Converting morse phrases into english phrases
def morse_to_english(user_input):
    english_character_list = []
    english_word_list = []
    list_of_morse_characters = user_input.split()
    for character in list_of_morse_characters:
        english_character_list.append(morse_character_to_english(character))
    print(english_character_list)
    for character in english_character_list:
        english_word_list = ''.join(english_character_list)
    print(english_word_list)
    return english_word_list

#Main function handles UI
def main():
    while True:
        user_main_input = input("Do you want to translate english to morse code, morse code to english, or exit?(1 for english to morse, 2 for morse to english, and 3 for exiting): ")
        if user_main_input.isnumeric():
            user_main_input = int(user_main_input)
            if user_main_input == 1:
                english_sentence_to_translate = input("Please give the sentence (or multiple sentences) you want to translate (this program only accounts for periods any other characters that are not letters will cause an error): ")
                print(f"Here is your phrase in morse code: {english_to_morse(english_sentence_to_translate)}")
            if user_main_input == 2:
                morse_sentence_to_translate = input("Please give the sentence (or multiple sentences) you want to translate (no space in between dots and dashes in a letter, one space in between letters, and (space / space) in between words): ")
                print(f"Here is your phrase in english: {morse_to_english(morse_sentence_to_translate)}")
            if user_main_input == 3:
                print("Hope this translator was useful!")
                break
        else:
            print("You have not typed a number please try again.")

main()