def s4_h1():
    """1. Write a Python script to calculate the length of a string"""
    text: str = input("Enter a string: ")
    length = len(text)
    print("The length of the string is: " + str(length))


def s4_h2():
    """2. Write a Python script that takes a string and prints it 3 times"""
    text: str = input("Enter a string: ")
    output = text * 3
    print(output)


def s4_h3():
    """3. Write a Python script that takes two strings, compares them and prints the result of the comparison"""
    text_1: str = input("Enter the first string: ")
    text_2: str = input("Enter the second string: ")
    result = text_1 == text_2
    print("Is " + text_1 + " equal to " + text_2 + "? Result: " + str(result))


def s4_h4():
    """4. Write a Python script that takes a string and prints the longest word of the string and its length"""
    text: str = input("Enter a string: ")
    words = text.split()
    words.sort(key=len, reverse=True)
    longest_word = words[0]
    length = len(longest_word)
    print(longest_word + " - " + str(length))


def s4_h5():
    """5. Write a Python script that replaces the word 'bad' with the word 'good' and removes the word 'not' in a string"""
    text: str = input("Enter a string: ")
    text = text.replace("bad", "good")
    text = text.replace("not", "")
    print(text)
