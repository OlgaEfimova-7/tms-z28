def count_number_of_letters_in_word_as_dict(word):
    """
    :param word: entered word
    :return: dictionary with key - letter, value - amount of this letter in the word
    """
    new_dict = {}
    for key in list(word.lower()):
        if key == ' ':
            continue
        if key in new_dict:
            new_dict[key] += 1
        else:
            new_dict[key] = 1
    return new_dict


def anagram(word1: str, word2: str):
    dict_from_word1 = count_number_of_letters_in_word_as_dict(word1)
    dict_from_word2 = count_number_of_letters_in_word_as_dict(word2)
    if dict_from_word1 == dict_from_word2:
        return 'This is ANAGRAM'
    else:
        return 'This is NOT ANAGRAM'


print(anagram('School master', 'The classroom'))
