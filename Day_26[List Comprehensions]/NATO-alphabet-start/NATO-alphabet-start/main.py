import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
word_data_frame = pandas.DataFrame(data)
data_dict = {row.letter : row.code for (index, row) in word_data_frame.iterrows()}
print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def gen_ph():
    inp_word = input("Enter a word : ").upper()
    try:
        data_list = [data_dict[letter] for letter in inp_word]
    except KeyError:
        print("Sorry, only letters in alphabet please")
        gen_ph()

    else:
        print(data_list)
gen_ph()



