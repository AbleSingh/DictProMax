import requests

def meaningGet(wordFound):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(wordFound)
    response = requests.get(url)

    if response.status_code == 200:
        defin = response.json()[0]
        # print(type(defin))
        # for i in defin:
        #     print(i)
        #     print("")
        # print(type(defin['meanings']))
        defin2 = (defin['meanings'])[0]
        # for i in defin2:
        #     print(i)
        #     print("")

        defin3 = ((defin2['definitions'])[0])
        # print(defin3)
        # print(type(defin3))

        defin4 = defin3['definition']
        print(defin4)
    else:
        print("Meaning Not found")
