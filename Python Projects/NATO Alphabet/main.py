import pandas

nato_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic = {row.letter: row.code for (index, row) in nato_dict.iterrows()}

print(nato_phonetic)
def restart_phonetic():
    word = input("Enter a word: ").upper()
    try:
        results = [nato_phonetic[letter] for letter in word]
    except KeyError:
        print("Sorry,only letters from alphabet.")
        restart_phonetic()
    else:
        print(results)


restart_phonetic()
