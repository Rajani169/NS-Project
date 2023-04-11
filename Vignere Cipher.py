#!/usr/bin/env python
# coding: utf-8

# from math import *

# In[87]:


pt = "hello world i am swati"
pt="HELLO WORLx I AM SWATI"
key = "abcdefghijklmnop"
# pt = "SWATI"
# key = "abc"


# In[88]:


def generate_key(pt,key):
    pt_len = len(pt)
#     print(pt_len)
    repeat_time = ceil(len(pt)/len(key))
    key*=repeat_time
    key = key[:pt_len]
    return key
    
    


# In[89]:


print(generate_key(key,pt.replace(" ","")))


# In[90]:


def encipherment(pt,key):
    pt=pt.replace(" ","")
    key=key.replace(" ","")
    key = generate_key(pt,key)
    print(pt,key)
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
#             print(x,y,res,ct,i)
        return ct
        
    


# In[91]:


print(encipherment(pt,key))


# In[ ]:




