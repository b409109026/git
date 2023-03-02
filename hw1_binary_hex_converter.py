#!/usr/bin/env python
# coding: utf-8

# In[29]:


#設計一個輸入為10進位，輸出為2進位與16進位數字的程式
dec=float(input('請輸入一個10進位的數:'))
if dec>256 or dec<0:
    print('請重新輸入')
else:   
    #分離整數小數
    d1=int(dec)
    d2=dec-d1

    #10進位整數部分轉2進位
    d1=int(dec)
    b1=''
    b2=''
    while d1>0:
        b1=str(d1%2)+b1
        d1//=2

    #10進位小數部分轉2進位
    while d2<1 and d2>0:
        d2*=2
        if d2>=1:
            b2+='1'
        else:
            b2+='0'

    #10進位整數部分轉16進位
    d1=int(dec)
    d2=dec-d1
    h1=''
    h2=''
    h='0123456789ABCDEF'
    while d1>0:
        h1=h[d1%16]+h1
        d1//=16

    #10進位小數部分轉16進位     
    while d2<1 and d2>0:
            d2*=16
            digit=int(d2)
            h2+=h[digit]
    if d2==0:
        print('轉換為2進位:',b1)
        print('轉換為16進位:',h1)
    else:
        print('轉換為2進位:',b1+'.'+b2)
        print('轉換為16進位:',h1+'.'+h2)


# In[ ]:





# In[ ]:




