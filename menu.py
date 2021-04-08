#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:43:37 2021

@author: yuanke.tsai
"""
#新增讀取檔案、跳過欄位讀取(L66)


#檔案讀取
products = []
with open('menu_write.csv', 'r', encoding = 'utf-8') as file:
    for line in file:
        if '商品,價格' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print('先前購買物品清單：', '\n', products)

#使用者輸入
while True:
    name = input('請輸入購買的商品（q/離開）：')
    if name == 'q':
        break
    price = input('請輸入商品價個：')
    products.append([name, price]) #此時清單products = '舊資料 + 新輸入'

#顯示過去已購買物品    
i = 0
r = 1
while True:
    if i < len(products):
        print('No.', r, '，產品：', products[i][0], '，',products[i][1], '元')
        i += 1
        r += 1
    else:
        break

#新清單 producs 做寫入
with open('menu_write.csv', 'w', encoding = 'utf-8') as file:
    file.write('商品,價格' + '\n')
    for product in products:
        file.write(product[0] + ',' + product[1] + '\n')
    
    