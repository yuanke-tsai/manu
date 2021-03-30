#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:43:37 2021

@author: yuanke.tsai
"""
#新增商品陳列

products = []
while True:
    name = input('請輸入購買的商品（q/離開）：')
    if name == 'q':
        break
    price = input('請輸入商品價個：')
    #solution 1
    #product = []
    #product.append(name)
    #product.append(price)
    
    #solution 2
    #product = [name, price]
    #products.append(product)
    
    #solution 3
    products.append([name, price])
    
i = 0
r = 1
while True:
    if i < len(products):
        print('No.', r, '，產品：', products[i][0], '，',products[i][1], '元')
        i += 1
        r += 1
    else:
        break