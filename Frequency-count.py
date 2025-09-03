"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Count the frequency of each letter in a given sentence.

Args:
   sentence (str): The input string to analyze.

Returns:
        dict[str, int]: A dictionary with letters as keys and their frequencies as values.
"""
def count_letter_frequency(sentence: str) -> dict[str, int]:
    letter_count: dict[str, int] = {}
    for char in sentence:
        if char.isalpha():  # consider only alphabetic characters
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count



# Example usage
sentence = "My name is Khouloud and I am a Developer"
result = count_letter_frequency(sentence)
print(result)
