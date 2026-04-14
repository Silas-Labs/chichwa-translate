def translate_text(text, source, target):
    #initialize dictionary with prepopulated data
    EN_TO_SW = {
        "hello" : "jambo",
        "tea" : "chai",
        "gari" : "car", 
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

  