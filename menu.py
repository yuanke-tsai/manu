#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:43:37 2021

@author: yuanke.tsai
"""

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
    
    #solution 3
    products.append([name, price])
print(products)