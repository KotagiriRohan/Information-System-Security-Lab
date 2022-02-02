
val = input("Enter plain text: ")

key = input("Enter Encription Key Value: ")

encrypted = "".join([chr(((ord(char) - 97) + int(key))%26 + 97) for char in val])

decrypted = "".join([chr(((ord(char) - 97) - int(key))%26 + 97) for char in encrypted])

print("\n\t TEXT: ", val, '\n\t ENCRYPTED TEXT: ', encrypted, '\n\t DECRYPTED TEXT: ', decrypted)
