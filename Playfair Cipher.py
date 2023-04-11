#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Python program to implement Playfair Cipher

# Function to convert the string to lowercase


def toLowerCase(text):
    return text.lower()

# Function to remove all spaces in a string


def removeSpaces(text):
#     newText = ""
#     for i in text:
#         if i == " ":
#             continue
#         else:
#             newText = newText + i
    
    return text.replace(" ","")

# Function to group 2 elements of a string
# as a list element

#code by gfg
# def Diagraph(text):
# 	Diagraph = []
#     i=0
#     while len(text):
#         Diagraph.append(text[0:2])
#         text = text[2:]
# # 	group = 0
# # 	for i in range(2, len(text), 2):
# # 		Diagraph.append(text[group:i])

# # 		group = i
# # 	Diagraph.append(text[group:])
# 	return Diagraph

#code by me
def Diagraph(text):
    Diagraph = []

    while len(text):
        Diagraph.append(text[0:2])
        text = text[2:]
    return Diagraph

# Function to fill a letter in a string element
# If 2 letters in the same string matches

#gfg code
# def FillerLetter(text):
#     k = len(text)
#     if k % 2 == 0:
#         for i in range(0, k, 2):
#             if text[i] == text[i+1]:
#                 new_word = text[0:i+1] + str('x') + text[i+1:]
#                 new_word = FillerLetter(new_word)
#                 break
#             else:
#                 new_word = text
#     else:
#         for i in range(0, k-1, 2):
#             if text[i] == text[i+1]:
#                 new_word = text[0:i+1] + str('x') + text[i+1:]
#                 new_word = FillerLetter(new_word)
#                 break
#             else:
#                 new_word = text
#     return new_word

#my code
def FillerLetter(text):
    i=0
    while(i!=len(text)-1):
        if text[i]==text[i+1]:
            text=text[:i+1] +'x' + text[i+1:]
        i+=2
    if len(text)%2 !=0:
        text+= 'x'
    return text


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to generate the 5x5 key square matrix


def generateKeyTable(word, list1):
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


def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[e1r][(e1c+1)%5]

    char2 = matr[e2r][(e2c+1)%5]

    return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):

    char1 = matr[(e1r+1)%5][e1c]

    char2 = matr[(e2r+1)%5][e2c]

    return char1, char2


def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):

    char1 = matr[e1r][e2c]


    char2 = matr[e2r][e1c]

    return char1, char2


def encryptByPlayfairCipher(Matrix, plainList):
	CipherText = ""
	for i in range(0, len(plainList)):
		c1 = 0
		c2 = 0
		ele1_x, ele1_y = search(Matrix, plainList[i][0])
		ele2_x, ele2_y = search(Matrix, plainList[i][1])

		if ele1_x == ele2_x:
			c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
			# Get 2 letter cipherText
		elif ele1_y == ele2_y:
			c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
		else:
			c1, c2 = encrypt_RectangleRule(
				Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

		cipher = c1 + c2
		CipherText+=cipher
	return CipherText


text_Plain = 'instruments'
text_Plain = removeSpaces(toLowerCase(text_Plain))
PlainTextList = Diagraph(FillerLetter(text_Plain))
# if len(PlainTextList[-1]) != 2:
#     PlainTextList[-1] = PlainTextList[-1]+'z'

key = "Monarchy"
print("Key text:", key)
key = toLowerCase(key)
Matrix = generateKeyTable(key, list1)

print("Plain Text:", text_Plain)
# print("Matrix:", Matrix)

CipherText = encryptByPlayfairCipher(Matrix, PlainTextList)

# CipherText = ""
# for i in CipherList:
# 	CipherText += i
print("CipherText:", CipherText)

# This code is Contributed by Boda_Venkata_Nikith


# In[ ]:





# In[ ]:




