# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# # #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas

nato_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic = {row.letter: row.code for (index, row) in nato_dict.iterrows()}

print(nato_dict)
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