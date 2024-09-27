meme_dict = {
            "CRINGE": "Что-то очень странное или стыдное",
            "LOL": "Что-то очень смешное"
            }
word = input("Введите непонятное слово (): ")
if word.upper() in meme_dict.keys():
    print(meme_dict[word.upper()])
else:
    print("Sorry we're not found this word")
   
