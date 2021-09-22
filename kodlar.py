#!/usr/bin/env python
# coding: utf-8

# In[336]:


from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import time
import requests
import random
import pandas as pd
import csv
import string


bozkurt = []
driver_patch = "D:\chromedriver.exe"
browser = webdriver.Chrome(driver_patch)
browser.get('https://www.hepsiburada.com/bilgisayarlar-c-3000500?siralama=yorumsayisi')
PcPureHtml = browser.find_elements_by_css_selector('[data-test-id="product-card-container"]>a')
PcUrl = []
for i in PcPureHtml:
    PcUrl.append(i.get_attribute('href') + '-yorumlari?sayfa=2&ozellik')
for i in PcUrl:
    browser.get(i)
    comment_pc = browser.find_elements_by_css_selector("div.hermes-ReviewCard-module-2dVP9>span ")
    product_name=browser.find_elements_by_css_selector(".hermes-ProductRate-module-NoJXU>span ")   
    point=browser.find_elements_by_css_selector(".hermes-ReviewCard-module-19LDC")
    for i in product_name:
        for j in comment_pc:
            for a in point:
                bozkurt.append(i.text + "--" + j.text+ "--" +a.text+"@")    
    with open('Deneme9.txt', 'w',encoding = "UTF-8") as f:
        for item in bozkurt:
                f.write("%s\n" % item)

#Telefon
Phone= []
browser.get('https://www.hepsiburada.com/cep-telefonlari-c-371965?siralama=yorumsayisi')
PhonePureHtml = browser.find_elements_by_css_selector('[data-test-id="product-card-container"]>a')
PhoneUrl = []
for i in PhonePureHtml:
    PhoneUrl.append(i.get_attribute('href') + '-yorumlari?sayfa=2&ozellik')
for i in PhoneUrl:
    browser.get(i)
    comment_phone = browser.find_elements_by_css_selector("div.hermes-ReviewCard-module-2dVP9>span ")
    product_phone=browser.find_elements_by_css_selector(".hermes-ProductRate-module-NoJXU>span ")   
    point_phone=browser.find_elements_by_css_selector(".hermes-ReviewCard-module-19LDC")
    for i in product_phone:
        for j in comment_phone:
            for a in  point_phone:
                Phone.append(i.text + "--" + j.text+ "--" +a.text+"@")    
    with open('Deneme9.txt', 'a',encoding = "UTF-8") as f:
        for item in Phone:
                f.write("%s\n" % item)

#Dolap
cooler= []
browser.get('https://www.hepsiburada.com/buzdolaplari-c-22154?siralama=yorumsayisi')
coolerPureHtml = browser.find_elements_by_css_selector('[data-test-id="product-card-container"]>a')
coolerUrl= []
for i in COOLHtml:
    coolerUrl.append(i.get_attribute('href') + '-yorumlari?sayfa=2&ozellik')
for i in coolerUrl:
    browser.get(i)
    product_cooler=browser.find_elements_by_css_selector(".hermes-ProductRate-module-NoJXU>span ")  
    comment_cooler = browser.find_elements_by_css_selector("div.hermes-ReviewCard-module-2dVP9>span ") 
    point_cooler=browser.find_elements_by_css_selector(".hermes-ReviewCard-module-19LDC")
    for i in product_cooler:
        for j in comment_cooler:
            for a in point_cooler:
                 cooler.append(i.text + "--" + j.text + "---" +a.text+"@")    
    with open('Deneme9.csv', 'a',encoding = "UTF-8") as f:
        for item in cooler:
                f.write("%s\n" % item)

        
        
            
              
   
                  
                





