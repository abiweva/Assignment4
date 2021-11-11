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

By running the regarding code, we will get the relevant link to the homepage with authorization. And after signing in we will have access to the bars which will provide the appropriate number of paragraphs by each typed coin name.

![image_2021-11-11_12-44-26](https://user-images.githubusercontent.com/93276431/141275318-761207b7-7b96-4226-8a13-51dec56560af.png)
![image_2021-11-11_12-46-21](https://user-images.githubusercontent.com/93276431/141275308-d684e33c-5ff4-4d24-bc72-f690a8b9c8e3.png)
![image_2021-11-11_12-44-45](https://user-images.githubusercontent.com/93276431/141275338-f20de9d0-8737-4ddb-8c71-aa5336e4930f.png)
![image_2021-11-11_12-44-59 (1)](https://user-images.githubusercontent.com/93276431/141275343-d847a2e7-267e-4dc1-a405-b46c78e1e478.png)

![image_2021-11-11_12-44-59 (1)](https://user-images.githubusercontent.com/93276431/141275223-8fdf8a12-17e9-4ed8-a0cc-6ffd7294c9b5.png)![image_2021-11-11_12-45-16](https://user-images.githubusercontent.com/93276431/141275326-6647932b-b809-45b6-a299-a37ec5b0becf.png)
![image_2021-11-11_12-44-59](https://user-images.githubusercontent.com/93276431/141275349-2d997730-48a4-410f-80b9-dcb29bfa0590.png)


![image_2021-11-11_12-45-45](https://user-images.githubusercontent.com/93276431/141275293-0861a650-4009-49d3-b2bc-856bffe477a4.png)


## API Documentation

https://pypi.org/project/requests/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
