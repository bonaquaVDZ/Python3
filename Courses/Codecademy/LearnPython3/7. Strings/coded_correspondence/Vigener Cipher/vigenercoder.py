"""It is a snippet of code that will produce from a plain message decrypted message with specific keyword."""
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "


def vigenere_coder(message, keyword):
    """Function that will encrypt a message using Vigener Method of Encryption."""
    letter_pointer = 0
    keyword_final = ""
    for i in range(0, len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer + 1) % len(keyword)
    translated_message = ""
    for i in range(0, len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message


msg = str(input("Please enter a message to encrypt: "))
kwrd = str(input("Please enter a keyword for encryption: "))

print(">> Your encrypted message looks like: ", vigenere_coder(message=msg, keyword=kwrd))
