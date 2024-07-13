def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        character_dict = count_characters(text)
        character_dict.sort(reverse=True,key=sort_on)
        print_report(character_dict,text)
def count_words(text):
    words = text.split()
    return len(words)
    

def count_characters(text):
    character_dict = {}
    for word in text:
        lower_case_word = word.lower()
        for character in lower_case_word:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
    return [{"word": k,"count":v} for k,v in character_dict.items()] 

def sort_on(dict):
    return dict["count"] 

def print_report(dict,text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print()
    for character_count in dict:
        if character_count["word"].isalpha():
            print(f"The '{character_count["word"]}' character was found {character_count["count"]} times")
    print("--- End report ---")







if __name__ == "__main__":
    main()
