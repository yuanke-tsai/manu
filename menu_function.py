#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:42:37 2021

@author: yuanke.tsai
"""

#menu.py 修改成 function 形式

import os
    
#第一段：檔案讀取，並檢查使否存在可讀取
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print('先前購買物品清單：', '\n', products)
    return products     

#第二段：使用者輸入
def user_input(products):
    while True:
        name = input('請輸入購買的商品（q/離開）：')
        if name == 'q':
            break
        price = input('請輸入商品價個：')
        products.append([name, price]) #此時清單products = '舊資料 + 新輸入'
    return products

#第三段：顯示過去已購買物品
def print_products(products):
    i = 0
    r = 1
    while True:
        if i < len(products):
            print('No.', r, '，產品：', products[i][0], '，',products[i][1], '元')
            i += 1
            r += 1
        else:
            break

#第四段：新清單 producs 做寫入
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write('商品,價格' + '\n')
        for product in products:
            file.write(product[0] + ',' + product[1] + '\n')
    print(products)

 
def main():
    filename = 'menu.csv'
    if os.path.isfile(filename):
        print('檔案存在，執行中', '\n')   
        products = read_file(filename)
    else:
        print('檔案不存在，請進行以下建立檔案')   
    products = user_input(products)
    print_products(products) 
    write_file('menu.csv', products)

main()