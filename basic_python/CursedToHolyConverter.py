cursed_words = {
    "damn": "God bless you",
    "hell": "Heaven above",
    "crap": "gracious me",
    "stupid": "misguided",
    "idiot": "beloved soul",
    "wtf": "Oh my goodness",
    "omg": "Oh my Lord",
    "freak": "unique child of light",
    "shut up": "let’s speak kindly",
    "kill": "forgive and uplift"
}

sentence = input("Enter a sentence: ")

for bad_word, holy_word in cursed_words.items():
    if bad_word in sentence.lower():
        sentence = sentence.replace(bad_word, holy_word)
        sentence = sentence.replace(bad_word.capitalize(), holy_word.capitalize())

print("Holy version:", sentence)
