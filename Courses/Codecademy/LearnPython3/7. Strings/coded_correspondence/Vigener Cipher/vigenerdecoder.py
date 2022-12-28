alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "


def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ""
    for i in range(0, len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer + 1) % len(keyword)
    translated_message = ""
    for i in range(0, len(coded_message)):
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message


msg = str(input("Please provide encrypted message: "))
kwrd = str(input("Please provide specific keyword to encrypt message: "))

print("Decrypted message is: ", vigenere_decoder(coded_message=msg, keyword=kwrd))
