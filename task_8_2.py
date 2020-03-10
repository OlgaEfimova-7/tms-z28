def palindrome_definition(word: str):
    """
    :param word: entered word
    :return: the answer is whether the number is a palindrome
    """
    if word == word[::-1]:
        return f'{word} is palindrome'
    else:
        return f'{word} is NOT palindrome'


first_word = 'dad'
second_word = 'cat'
third_word = 'level'
print(palindrome_definition(first_word))
print(palindrome_definition(second_word))
print(palindrome_definition(third_word))
