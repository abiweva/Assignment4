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
import requests
from bs4 import BeautifulSoup
import ArticleFinder
from ArticleFinder import Finder
f1 = Finder()
soup = BeautifulSoup(req.content, 'html.parser')
```

## Examples

By using the findArticle method, the f1 "Finder()" object and entering a cryptocurrency's name we are searching any cryptomarket articles in Alexandria catalogue.

C:\Users\Админ\Desktop\Новая папка>python parserForPythonAss.py
https://www.google.com/url?q=https://coinmarketcap.com/alexandria&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAkQAg&usg=AOvVaw2DdkE5WjwFmiVWGHj_7c_2
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/categories/crypto-basics&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQ0gJ6BAgJEAQ&usg=AOvVaw12WqfGaotrJfq0gdyCiMMh
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/glossary&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQ0gJ6BAgJEAU&usg=AOvVaw1FiF3yIn-YrHAqO-kiU3F6
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/bitcoin-price-analysis-the-upcoming-bull-run-will-be-wilder-than-the-previous-one&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQ0gJ6BAgJEAY&usg=AOvVaw2AnuN0flRZ56cS3AqN3jA7
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/categories/how-to-guides&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQ0gJ6BAgJEAc&usg=AOvVaw17_-9CcPYJIES3jodEkKG5
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/about&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAgQAg&usg=AOvVaw3Oo4iWr9ed24qGDUs3kPB0
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/glossary&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAYQAg&usg=AOvVaw352xv2RMAub9Kx-kK0ziQs
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/categories/crypto-basics&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAcQAg&usg=AOvVaw0gv0SnZc0Qjd73UatvXDLi
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/how-to-live-on-bitcoin&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAoQAg&usg=AOvVaw3Jpow2Uh7tOMBKvTa03MWS
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/glossary/cryptocurrency&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAMQAg&usg=AOvVaw2DBNTLigCSXcnUlPmiilt5
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/coinmarketcap-daily-oct-5-bitcoin-to-50k&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAAQAg&usg=AOvVaw0WF-56vpsE5WUsX9cPSAsW
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/bitcoin-hits-50-000-for-first-time-in-a-month&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAQQAg&usg=AOvVaw2f_5C-QTQPSYFXTj9u8CPL
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/bitcoin-price-prediction&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAEQAg&usg=AOvVaw15JIKgz50TdCPFPvReHLXY
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/bitcoin-to-cross-55k-in-a-week&sa=U&ved=2ahUKEwi8mb7Dq8DzAhWmpYsKHQ2aDkEQFnoECAIQAg&usg=AOvVaw3J2Mxhu0HTt82Agv-uSI5V

TOTAL AMOUNT OF sites: 14



## API Documentation

https://pypi.org/project/requests/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
