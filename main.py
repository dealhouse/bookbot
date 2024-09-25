with open("./books/frankenstein.txt", "r") as f:
    words = f.read()
    word_list = words.split()
    lower = words.lower()
    characters = list(lower)
    character_list = {}
    for character in characters:
        if character.isalpha() and character not in character_list:
            character_list[character] = 1
        elif character.isalpha() and character in character_list: 
            character_list[character] += 1
    sorted_character_list = sorted(character_list.items(), key=lambda item:item[1], 
                                reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(word_list)} words found in the document")
    print("")
    for character in sorted_character_list:
        print(f"The '{character[0]}' character was found {character[1]} times")
    print("--- End report ---")
    

