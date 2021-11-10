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


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")
    

@app.route("/mainpage", methods=['POST'])
def main():
    username = request.form.get("ussername")
    password = request.form.get("passwordd")
    userid = 1
    tableforass4.Usser.tablefunc(userid)
    if username == tableforass4.loginn and password == tableforass4.passwordd:
        return render_template("main.html")
    return "Could not verify"

@app.route("/formpage")
def formpage():
    return render_template("findbyform.html")

@app.route('/formanswer', methods=['POST'])
def formanswer():

    coinname = request.form.get("coinname")
    newscount = request.form.get("newscount")

    #delete_this = tableforass4.News.query.filter_by(idcoin=1).first()
    #tableforass4.db.session.delete(delete_this)
    #tableforass4.db.session.commit()

    #url of the page we want to scrape
    url = 'https://coinmarketcap.com/currencies/' + coinname + '/news/'
  
    # initiating the webdriver. Parameter includes the path of the webdriver.
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Downloads\chromedriver.exe', options = options) 
    driver.get(url) 
    loadmorebutton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/div/main/button')
    for i in range(3):
        loadmorebutton.click() 
        time.sleep(8) 

  
    html = driver.page_source
  
    # this renders the JS code and stores all
    # of the information in static HTML code.
  
    # Now, we could simply apply bs4 to html variable
    soup = BeautifulSoup(html, "html.parser")
    all_divs = soup.find('div', {'class' : 'wav26n-1 gWmJSZ'})
    job_profiles = all_divs.find_all('a')

    listofnews = []
    # printing top ten job profiles
    count = 0
    for job_profile in job_profiles :
        listofnews.append(job_profile.text)
        count = count + 1
        if(count == newscount) :
            break

    driver.close() # closing the webdriver

    new_info = tableforass4.News(1, 'bitcoin', 'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello6', 'hello7', 'hello8', 'hello9', 'hello10', 'hello11', 'hello12', 'hello13', 'hello14', 'hello15', 'hello16', 'hello17', 'hello18','hello19','hello20')
    tableforass4.db.session.add(new_info)
    tableforass4.db.session.commit() 

    countfortable = 1
    listindex = 0
    for i in listofnews:
        with tableforass4.engine.connect() as connection:
            result = connection.execute(text('update News set news' + str(countfortable) + ' = $$' + listofnews[listindex] + '$$ where News.coin_name = '+ "'" + str(coinname) + "'"))
        connection.close()
        if(countfortable == newscount):
            break
        countfortable = countfortable + 1
        listindex = listindex + 1

    return render_template("formanswer.html", len = len(listofnews), listofnews = listofnews, amount = int(newscount))

@app.route('/tabledisplay')
def tabledisplay():
    pass

@app.route('/scraper')
def scraper():
    #url of the page we want to scrape
    url = 'https://coinmarketcap.com/currencies/bitcoin/news/'
  
    # initiating the webdriver. Parameter includes the path of the webdriver.
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Downloads\chromedriver.exe', options = options) 
    driver.get(url) 
    loadmorebutton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/div/main/button')
    for i in range(4):
        loadmorebutton.click() 
        time.sleep(5) 

  
    html = driver.page_source
  
    # this renders the JS code and stores all
    # of the information in static HTML code.
  
    # Now, we could simply apply bs4 to html variable
    soup = BeautifulSoup(html, "html.parser")
    all_divs = soup.find('div', {'class' : 'wav26n-1 gWmJSZ'})
    job_profiles = all_divs.find_all('a')

    hello = ""
    # printing top ten job profiles
    count = 0
    for job_profile in job_profiles :
        hello + str(job_profile) + "\n--------------------------------------------------\n"
        count = count + 1
        if(count == 20) :
            break

    driver.close() # closing the webdriver

    return hello



if __name__ == '__main__':
    app.run(debug=True)