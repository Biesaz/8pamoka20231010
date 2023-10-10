# [20:21] Mindaugas Rudzevičius

# write a program witch takes at least 5 minimum words (use only 1 input) separated by comma. 
# From those words , make a dictionary where the key is a letter and value is a number of the 
# frequency the letter did appear in all those words. Letters should be in alphabetical order.

# Everything should be done thorugh github workflow.

# isprinitinti dictionary pvz alibaba a-3. reikia naujos sakos

# minimum_five_words = input("Enter at least 5 minimum words separated by comma: ")
# minimum_five_words_list = (minimum_five_words.split(","))
# create_letter_frequency_dictionar = {}
# if len(minimum_five_words_list) < 5:
#   print("Please enter at least 5 words.")
# letter_frequency_dictionary = create_letter_frequency_dictionary(minimum_five_words_list)
# print(letter_frequency_dictionary)


# # splitinti padaryti i lista kableliu split builin
# # key: value
# # letter: a number of the  frequency the letter did appear in all those words

# def create_letter_frequency_dict(input_text):
#     # Remove spaces and split the input into a list of words
#     words = input_text.replace(" ", "").split(",")

#     # Initialize an empty dictionary to store letter frequencies
#     letter_frequency_dict = {}

#     # Iterate through each word in the list
#     for word in words:
#         # Iterate through each character in the word
#         for char in word:
#             # Check if the character is a letter
#             if char.isalpha():
#                 # Convert the character to lowercase
#                 char = char.lower()
#                 # Update the letter frequency dictionary
#                 if char in letter_frequency_dict:
#                     letter_frequency_dict[char] += 1
#                 else:
#                     letter_frequency_dict[char] = 1

#     # Sort the dictionary by keys (letters)
#     sorted_letter_frequency_dict = dict(sorted(letter_frequency_dict.items()))

#     return sorted_letter_frequency_dict

# # Get input from the user
# input_text = input("Enter at least 5 words separated by commas: ")

# # Call the function to create the letter frequency dictionary
# letter_frequency_dict = create_letter_frequency_dict(input_text)

# # Print the resulting dictionary
# for letter, frequency in letter_frequency_dict.items():
#     print(f"{letter}: {frequency}")
