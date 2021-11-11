# Assignment #4

## TITLE

Task will be to scrap all the related information about different cryptocurrencies 


## Requirements!

``` bash 
1)Web page should provide input text field and receive coin name
2)Once coin name is provided and pressed CHECK button, web page should display list of paragraphs
3)Store parsed news and blogs from Assignment 2 into the database
4)Web server should provide at least 1 route
5)Receive as input coin name
/coin


```


## Usage

``` bash 
from datetime import datetime, timedelta
from re import U, template
from flask import Flask, request, render_template
from flask.helpers import make_response
import jwt
from sqlalchemy.orm import session
import tableforass4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text
from sqlalchemy import create_engine


app = tableforass4.app
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
```

## Examples

By running the code and then opening the relevant link taht will us the page with authorization and further bars demonstrating the articles paragraphs.

![image_2021-11-11_12-44-26](https://user-images.githubusercontent.com/74869146/141271893-bd69ed18-58f3-45d2-8bbd-57465b3663c3.png)

![image_2021-11-11_12-44-45](https://user-images.githubusercontent.com/74869146/141271921-c33f41f2-b7f4-423d-b362-32d1d081eeb2.png)

![image_2021-11-11_12-44-59](https://user-images.githubusercontent.com/74869146/141271934-13cb7055-442e-4ad1-b6b5-4bbee9e43717.png)

![image_2021-11-11_12-45-16](https://user-images.githubusercontent.com/74869146/141271947-8a423885-9602-49fc-ac0e-a8fcf444d7ce.png)

![image_2021-11-11_12-45-45](https://user-images.githubusercontent.com/74869146/141271965-93b09251-7d99-45b2-bbd6-eaa941ca60bd.png)

![image_2021-11-11_12-46-21](https://user-images.githubusercontent.com/74869146/141271976-400ed0ad-984c-40ae-84d4-ffc138dfe5c0.png)


## API Documentation

https://pypi.org/project/requests/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
