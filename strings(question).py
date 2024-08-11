######################################################################################################
# Write a function that takes a string and returns it reversed
######################################################################################################
def rev(s: str):
    string = string[::-1]
    return string


s = "python"
print(s)


######################################################################################################
# Write a function that takes a string and returns it in uppercase.
######################################################################################################
def upp(s: str) -> str:

    stri = ""
    for char in s:
        if "a" <= char <= "z":
            stri += chr(ord(char) - 32)
        else:
            stri += char
    return stri


my_string = "aB677^&*hx"

print(upp(my_string))


######################################################################################################
# Write a function that removes all vowels (a, e, i, o, u) from a given string.
######################################################################################################
def remove(s: str) -> str:
    v = ["a", "e", "i", "o", "u", "A", "I", "E", "O", "U"]
    result = " "
    for letter in s:
        if letter not in v:
            result += letter
    return result


zs = "sheshang"
print(remove(zs))


######################################################################################################
# Write a function that counts the number of words in a given string.
# (String may only contain alphabets and spaces)
######################################################################################################
def count_words(s: str) -> int:
    if not s:
        return 0
    word_count = 1
    for char in s:
        if char == " ":
            word_count += 1
    return word_count


my_string = "pytho11n is easy to learn"
print(count_words(my_string))


######################################################################################################
# Write a function that finds and returns the longest word in a given string.
######################################################################################################
def logest_word(s: str):
    long = ""
    curr = ""
    for char in s:
        if char == " ":
            if len(curr) > len(long):
                long = curr
            curr = " "
        else:
            curr += char
            if len(curr) > len(long):
                long = curr
    return long


a = "sheshang harge"
print(logest_word(a))


######################################################################################################
# Write a function that capitalizes the fi rst letter of each word in a given string.
######################################################################################################
def capit(s: str) -> str:
    result = " "
    new_word = True
    for char in s:
        if new_word and "a" <= char <= "z":
            result += chr(ord(char) - 32)
            new_word = False
        else:
            result += char
        if char == " ":
            new_word = True
    return result


m = "Sheshang harge"
print(capit(m))


######################################################################################################
# Write a function that replaces all consonants in a given string with asterisks (*).
######################################################################################################
def removee(s: str) -> str:
    vo = "aeiouAEIOU"
    result = " "
    for char in s:
        if ("a" <= char <= "z" or "A" <= char <= "Z") and char not in vo:
            result += "*"
        else:
            result += char
    return result


abc = "sheshang"
print(removee(abc))


######################################################################################################
# Write a function that removes all non-alphabetic characters from a given string.
######################################################################################################
def remove_non_alphabetic(s: str) -> str:
    result = ""
    for char in s:
        if ("a" <= char <= "z") or ("A" <= char <= "Z") or char == " ":
            result += char
    return result


aas = "saaaadww2d3"
print(remove_non_alphabetic(aas))


######################################################################################################
# Write a function that counts the number of digits in a given string.
######################################################################################################
def count_digits(s: str) -> int:
    digit_count = 0
    for char in s:
        if "0" <= char <= "9":
            digit_count += 1
    return digit_count


my_string = "abcd1239"
print(count_digits(my_string))


######################################################################################################
# Write a function that removes duplicate characters from a given string.
######################################################################################################
def removeduplicat(s: str):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result


my_string = "aaannnvvvwerewq"
print(removeduplicat(my_string))


######################################################################################################
# Write a function that checks if a given string contains only alphanumeric characters.
######################################################################################################
def is_alphanumeric(s: str) -> bool:
    for char in s:
        if not (("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9")):
            return False
    return True


######################################################################################################
# Write a function that replaces all spaces in a given string with hyphens (-).
######################################################################################################
def replace(s: str) -> str:
    result = ""
    for char in s:
        if char == " ":
            result += "-"
        else:
            result += char
    return result


my_string = "python is a very easy coding language to learn"
print(replace(my_string))
