#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:09:05 2021

@author: yuanke.tsai
"""
#老師的版本
products = []
while True:
    name = input('請輸入購買的商品（q/離開）：')
    if name == 'q':
        break
    price = input('請輸入商品價個：')
    products.append([name, price])
    
for product in products:
    print(product[0], product[1])
    
with open('menu_w.txt', 'w') as file:
    for product in products:
        file.write(product[0] + product[1] + '\n')