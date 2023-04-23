from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True
import random,sys,decimal
from math import ceil

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    elif request.method == "POST":
        global plaintext
        global algo
        global key
        plaintext = request.form.get("plaintext")
        algo = request.form.get("algo")
        key = request.form.get("key")
        print(algo)
        cipher = choose_algo(plaintext,algo,key)
        return render_template('try.html', cipher = cipher)

def choose_algo(plaintext,algo,key):
    print(algo)
    if algo== "DES":
        pass
        # x = DES(plaintext,key)
        # cipher = x.encrypt()
    elif algo == "Vigenere":
        x = Vigenere()
        cipher = x.encipherment(plaintext,key)
    elif algo == "PF":
        x = PF()
        cipher = x.Encrypt(plaintext,key)
    elif algo == "RSA":
        x = RSA()
        cipher = x.Encryption_RSA(plaintext)

    return cipher

class Vigenere:
    # def __init__(self,plaintext,key) -> None:
    #     self.pt = plaintext
    #     self.key = key
    
    def generate_key(self,pt,key):
        pt_len = len(pt)
        repeat_time = ceil(len(pt)/len(key))
        key*=repeat_time
        key = key[:pt_len]
        return key
    
    def encipherment(self,pt,key):
        pt=pt.replace(" ","")
        key=key.replace(" ","")
        key = self.generate_key(pt,key)
        ct = ''
        if pt.isupper():
            key=key.upper()
            for i in range(len(pt)):
                x = ord(pt[i])-65
                y = ord(key[i])-65
                res = (x+y)%26
                ct+= chr(res+65)
            return ct
        else:
            pt = pt.lower()
            for i in range(len(pt)):
                x = ord(pt[i])-97
                y = ord(key[i])-97
                res =(x+y)%26
                ct+= chr(res+97)
            return ct
        
class PF:
    def toLowerCase(self,text):
        return text.lower()

# Function to remove all spaces in a string

    def removeSpaces(self,text):
        return text.replace(" ","")

    # Function to group 2 elements of a string as a list element

    def Diagraph(self,text):
        Diagraph = []

        while len(text):
            Diagraph.append(text[0:2])
            text = text[2:]
        return Diagraph

    # Function to fill a letter in a string element
    # If 2 letters in the same string matches

    def FillerLetter(self,text):
        i=0
        while(i!=len(text)-1):
            if text[i]==text[i+1]:
                text=text[:i+1] +'x' + text[i+1:]
            i+=2
        if len(text)%2 !=0:
            text+= 'x'
        return text



    # Function to generate the 5x5 key square matrix

    def generateKeyTable(self,word, list1):
        key_letters = []
        d={}
        for i in word:
            if i not in d:
                d[i]=0
                key_letters.append(i)

        compElements = []
        d={}
        for i in key_letters:
            if i not in d:
                d[i]=0
                compElements.append(i)
        for i in list1:
            if i not in d:
                d[i]=0
                compElements.append(i)

        matrix = []
        while len(compElements):
            matrix.append(compElements[:5])
            compElements = compElements[5:]

        return matrix

    def search(self,mat, element):
        for i in range(5):
            for j in range(5):
                if(mat[i][j] == element):
                    return i, j


    def encrypt_RowRule(self,matr, e1r, e1c, e2r, e2c):
        char1 = matr[e1r][(e1c+1)%5]

        char2 = matr[e2r][(e2c+1)%5]

        return char1, char2


    def encrypt_ColumnRule(self,matr, e1r, e1c, e2r, e2c):

        char1 = matr[(e1r+1)%5][e1c]

        char2 = matr[(e2r+1)%5][e2c]

        return char1, char2


    def encrypt_RectangleRule(self,matr, e1r, e1c, e2r, e2c):

        char1 = matr[e1r][e2c]

        char2 = matr[e2r][e1c]

        return char1, char2


    def encryptByPlayfairCipher(self,Matrix, plainList):
        CipherText = ""
        for i in range(0, len(plainList)):
            c1 = 0
            c2 = 0
            ele1_x, ele1_y = self.search(Matrix, plainList[i][0])
            ele2_x, ele2_y = self.search(Matrix, plainList[i][1])

            if ele1_x == ele2_x:
                c1, c2 = self.encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
                # Get 2 letter cipherText
            elif ele1_y == ele2_y:
                c1, c2 = self.encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = self.encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

            cipher = c1 + c2
            CipherText+=cipher
        return CipherText

    def Encrypt(self,plaintext,key):
    # text_Plain = 'instruments'
        text_Plain = self.removeSpaces(self.toLowerCase(plaintext))
        PlainTextList = self.Diagraph(self.FillerLetter(text_Plain))
        # if len(PlainTextList[-1]) != 2:
        #     PlainTextList[-1] = PlainTextList[-1]+'z'

        # key = "Monarchy"
        # print("Key text:", key)
        key = self.toLowerCase(key)
        Matrix = self.generateKeyTable(key, list1)

        # print("Plain Text:", text_Plain)
        # print("Matrix:", Matrix)

        CipherText = self.encryptByPlayfairCipher(Matrix, PlainTextList)

        return CipherText


         
    # @app.route("/check",methods=['GET'])
    # def check():
    #     return render_template("index.html")

class RSA:
    def extendedGCD(self,a: int, b: int) -> (int, int):
        if b:
            u, v = self.extendedGCD(b, a % b)
            return v, u - v * (a // b)

        return 1, 0

    def calculatePrivateKey(self,e: int, p: int, q: int) -> int:
        u, _ = self.extendedGCD(e, (p - 1) * (q - 1))
        return u
    
    def randomBitsGenerator(self,bit_length: int) -> int:
        return random.getrandbits(bit_length)
    
    def separatePowersOfTwo(self,n: int) -> (int, int):
        r = 0
        d = n

        while d > 0 and d % 2 == 0:
            d = d // 2
            r += 1

        return r, d

    def millerRabinPrimalityTest(self,n: int, k: int) -> bool:
        r, d = self.separatePowersOfTwo(n - 1)

        for i in range(k):
            a = self.randomBitsGenerator(n.bit_length())
            while a not in range(2, n - 2 + 1):
                a = self.randomBitsGenerator(n.bit_length())
            print(a)
            print(d)
            print(n)
            # a = decimal.Decimal(a)
            # d = decimal.Decimal(d)
            # x = a**d
            # print(x)
            # x%=n
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            prime_found = False
            for j in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    prime_found = True
                    break

            if not prime_found:
                return False

        return True

    def primeGenerator(self,bit_length: int) -> int:
        range_lower_limit = pow(2, bit_length - 1)
        range_upper_limit = pow(2, bit_length) - 1

        while True:
            sampled_prime = self.randomBitsGenerator(bit_length)
            while sampled_prime not in range(int(range_lower_limit), int(range_upper_limit) + 1) or (sampled_prime % 2 == 0):
                sampled_prime = self.randomBitsGenerator(bit_length)

            k = 64
            if self.millerRabinPrimalityTest(sampled_prime, k):
                return sampled_prime 
    
    def encrypt(self,plaintext: bytes, e: int, n: int) -> int:
        pt_converted = int.from_bytes(plaintext, "big")
        return pow(pt_converted, e, n)


    def decrypt(self,ciphertext: int, d: int, n: int) -> bytes:
        pt_converted = pow(ciphertext, d, n)
        return pt_converted.to_bytes((pt_converted.bit_length() + 7) // 8, "big")

    def Encryption_RSA(self,plaintext):
        key_size = 1024
        prime_number_bit_length = key_size // 2
        print(plaintext)
        pt_in_bytes = bytes(plaintext, 'utf-8')
        print(pt_in_bytes)
        p = self.primeGenerator(prime_number_bit_length)
        q = self.primeGenerator(prime_number_bit_length)

        n = p * q
        # standard value of 'e' assumed
        e = 65537
        d = self.calculatePrivateKey(e, p, q)
        public_key = (e,n)
        pt_in_bytes = bytes(plaintext, 'utf-8')
        print(pt_in_bytes)
        ciphertext = self.encrypt(pt_in_bytes, e, n)
        
        return ciphertext



    if __name__=="__main__":
        app.run(debug=True)