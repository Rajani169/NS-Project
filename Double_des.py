import random
from utils import *
from Boxes import *
from DES_Algorithm import DES


def _64bits_random_key_generate():
    key = "1"
    for _ in range(1, 64):
        key += str(random.randint(0, 1))
    return key


KEY1 = _64bits_random_key_generate()
KEY1 = permutation(KEY1, key_per, 56)

left1 = KEY1[:28]
right1 = KEY1[28:]

rounded_keys1 = []  # rounded keys list

for i in range(16):
    left1 = shift_left(left1, shift_table[i])
    right1 = shift_left(right1, shift_table[i])

    combined_key = left1 + right1

    rounded_key = permutation(combined_key, key_comp, 48)

    rounded_keys1.append(rounded_key)

reversed_rounded_keys1 = rounded_keys1[::-1]

des_encrypt1 = DES(rounded_keys1)
des_decrypt1 = DES(reversed_rounded_keys1)


KEY2 = _64bits_random_key_generate()
KEY2 = permutation(KEY2, key_per, 56)
left2 = KEY2[:28]
right2 = KEY2[28:]

rounded_keys2 = []  # rounded keys list

for i in range(16):
    left1 = shift_left(left1, shift_table[i])
    right1 = shift_left(right1, shift_table[i])

    combined_key = left1 + right1

    rounded_key = permutation(combined_key, key_comp, 48)

    rounded_keys2.append(rounded_key)

reversed_rounded_keys2 = rounded_keys2[::-1]

des_encrypt2 = DES(rounded_keys2)
des_decrypt2 = DES(reversed_rounded_keys2)


def main():
    
    lines = []
    with open("input.txt", "r") as file:
        for i in range(10):
            line = file.readline()
            lines.append(line)
        
    file=open("output.txt", "w")
    filedecrypt=open("decrypt.txt", "w")

    for i in range(10):
        text=lines[i]
        print(text)
        binary_text = get_binary_message(text)
        cipher = des_encrypt1.text_encrypt(binary_text)
        #with open("output.txt", "a") as file:
            
            #file.write(f"Encrypted message after round 1  = {cipher}")
            

            # print("Encrypted message after round 1 ", cipher)
        cipher = des_encrypt2.text_encrypt(cipher)
        with open("output.txt", "a") as file:
            
            file.write(f"Encrypted message = {cipher}" + "\n")
            
            # print("Encrypted message after round 2 ", cipher)

        decrypted_cipher = des_decrypt2.text_encrypt(cipher)
        #with open("output.txt", "a") as file:
            
            #file.write(f"Decrypted message in binary after round 1  = {decrypted_cipher}")
            
                #print("Decrypted message in binary after round 1 ", decrypted_cipher)
        decrypted_cipher = des_decrypt1.text_encrypt(decrypted_cipher)
        #with open("output.txt", "a") as file:
            
            #file.write(f"Decrypted message in binary after round 2  = {decrypted_cipher}")
            
                #print("Decrypted message in binary after round 2 ", decrypted_cipher)
        with open("decrypt.txt", "a") as filedecrypt:
            
            filedecrypt.write(f"Decrypted message  = {get_ascii_message(decrypted_cipher)}"+ "\n")
        #print(get_ascii_message(decrypted_cipher))
            


if __name__ == "__main__":
    main()
