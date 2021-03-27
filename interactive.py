import json
from difflib import get_close_matches

data = json.load(open("data.json"))




def clear():
    for x in range(100):
        print("")

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesnt exist. Please try again!"
        else:
            return "We didnt understand your entry."
    else:
        return "The word u enter does not exist, please try again!"


word = ""
clear()
while word.lower() != "q":  
    word = input("\n(Press Q to QUIT)\nEnter word: ")
    clear()    
    output = translate(word)
    if type(output) == list:   
        for item in output:
            print(item)
    else:
        print(output)
    