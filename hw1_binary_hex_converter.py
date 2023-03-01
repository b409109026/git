#!/usr/bin/env python
# coding: utf-8

# In[18]:


#設計一個輸入為10進位，輸出為2進位與16進位數字的程式
dec=int(input('請輸入一個10進位的數:'))
d=dec
#10進位轉2進位
bin=''
while dec>0:
    bin=str(dec%2)+bin
    dec=dec//2
    
#10進位轉16進位
hex=''
h='0123456789ABCDEF'
while d>0:
    hex=h[d%16]+hex
    d=d//16
     
print('轉換為2進位:',bin)
print('轉換為16進位:',hex)


# In[ ]:





# In[ ]:





# In[ ]:




