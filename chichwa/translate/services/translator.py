def translate_text(text, source, target):
    #initialize dictionary with prepopulated data
    EN_TO_SW = {
        "hello" : "jambo",
        "tea" : "chai",
        "car" : "gari", 
        "fish" : "samaki",
        "thanks" : "asante",
        "please" : "tafadhali",
        "father" : "baba",
        "mother" : "mama",
        "shark" : "papa",
        "tree" : "mti"
    }

    #initialize empty SW->EN dictionary
    SW_TO_EN={}
    
    #populate SW dictionary from EN
    for k,v in EN_TO_SW.items():
        SW_TO_EN[f"{v}"]=k

    translated_words = []

    to_translate = text.split(" ")

    if source.lower() == "en" and target.lower()== "sw":
        for i in to_translate:
            if i in EN_TO_SW:
                translated_words.append(EN_TO_SW[i.lower()])
            else:
                return "No such word in dictionary"
        return " ".join(translated_words)
    
    if source.lower() == "sw" and target.lower()== "en":
        for i in to_translate:
            if i in SW_TO_EN:
                translated_words.append(SW_TO_EN[i.lower()])
            else:
                return "No such word in dictionary"

        return " ".join(translated_words)
    
    if source.lower() == "sw" and target.lower()== "sw":
        return text
    
    if source.lower() == "en" and target.lower()== "en":
        return text