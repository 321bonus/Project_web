from flask import Flask , render_template
from sqlalchemy.ext.declarative import declarative_base 
from bs4 import BeautifulSoup

import requests
import psycopg2


app  = Flask(__name__)





### DATA for scrpaing   ####
##################################################################################
url = "https://finance.yahoo.com/currencies?.tsrc=fin-srch"
req = requests.get(url)
req.encoding = "utf-8"
soup = BeautifulSoup(req.text, "html.parser")
##################################################################################




#Top page
@app.route('/')
def index():
    return render_template('Home.html')


#Home page
@app.route('/Home')
def Home():
    return render_template('Home.html')



@app.route('/Table')
def Table():

    connection= psycopg2.connect(user ='webadmin',
                                password ='MDDnfo15110',
                                host = 'node38352-bunnapon.proen.app.ruk-com.cloud', 
                                port = '5432',
                                database ='work')

    Cursor = connection.cursor()
    Cursor2 = connection.cursor()
    Cursor3 = connection.cursor()

    select_data = "SELECT last_price, change, change_per FROM euro"
    select_data_2 = "SELECT last_price, change, change_per FROM thai"
    select_data_3 = "SELECT last_price, change, change_per FROM yen"
        
    Cursor.execute(select_data)
    Cursor2.execute(select_data_2)
    Cursor3.execute(select_data_3)

    all_cur = Cursor.fetchall()
    all_cur2 = Cursor2.fetchall()
    all_cur3 = Cursor3.fetchall()
    all_cur.reverse()
    all_cur2.reverse()
    all_cur3.reverse()



    result_euro = []
    result_japan =[]
    result_thai=[]

    for i in  all_cur[0]:
        result_euro.append(i) 

    for j in  all_cur2[0]:
        result_thai.append(j) 

    for k in  all_cur3[0]:
        result_japan.append(k) 



    return render_template('Table.html',result_euro=result_euro, result_japan=result_japan, result_thai=result_thai)






#Graph Euro price
@app.route('/Graph_eu')
def Graph_eu():

    connection= psycopg2.connect(user ='webadmin',
                                password ='MDDnfo15110',
                                host = 'node38352-bunnapon.proen.app.ruk-com.cloud', 
                                port = '5432',
                                database ='work')

    Cursor = connection.cursor()
    Cursor2 = connection.cursor()
    Cursor3 = connection.cursor()

    select_data = "SELECT last_price, change, change_per FROM euro"
    select_data_2 = "SELECT last_price, change, change_per FROM thai"
    select_data_3 = "SELECT last_price, change, change_per FROM yen"

    Cursor.execute(select_data)
    Cursor2.execute(select_data_2)
    Cursor3.execute(select_data_3)

    all_cur = Cursor.fetchall()
    
    result_euro = []
    all_money_hole = []
    for i in all_cur:
        all_money_hole.append(i[0])

    all_money_hole.reverse()
    all_money = [all_money_hole[2],all_money_hole[1],all_money_hole[0]]
    
    #Loop of result
    all_cur.reverse()
    for i in  all_cur[0]:
        result_euro.append(i) 
    
    


    return render_template('Graph_eu.html', all_money = all_money,result_euro=result_euro)


#Garph Thai
@app.route('/Graph_th')
def Graph_th():

    connection= psycopg2.connect(user ='webadmin',
                                password ='MDDnfo15110',
                                host = 'node38352-bunnapon.proen.app.ruk-com.cloud', 
                                port = '5432',
                                database ='work')

    Cursor = connection.cursor()
    Cursor2 = connection.cursor()
    Cursor3 = connection.cursor()

    select_data = "SELECT last_price, change, change_per FROM euro"
    select_data_2 = "SELECT last_price, change, change_per FROM thai"
    select_data_3 = "SELECT last_price, change, change_per FROM yen"

    Cursor.execute(select_data)
    Cursor2.execute(select_data_2)
    Cursor3.execute(select_data_3)

    all_cur = Cursor2.fetchall()
    
    result_thai = []
    all_money_hole = []
    for i in all_cur:
        all_money_hole.append(i[0])

    all_money_hole.reverse()
    all_money = [all_money_hole[2],all_money_hole[1],all_money_hole[0]]
    
    #Loop of result
    all_cur.reverse()
    for i in  all_cur[0]:
        result_thai.append(i) 
    
    


    return render_template('Graph_th.html', all_money = all_money,result_thai=result_thai)

#Grahp japan
@app.route('/Graph_jp')
def Graph_jp():

    connection= psycopg2.connect(user ='webadmin',
                                password ='MDDnfo15110',
                                host = 'node38352-bunnapon.proen.app.ruk-com.cloud', 
                                port = '5432',
                                database ='work')

    Cursor = connection.cursor()
    Cursor2 = connection.cursor()
    Cursor3 = connection.cursor()

    select_data = "SELECT last_price, change, change_per FROM euro"
    select_data_2 = "SELECT last_price, change, change_per FROM thai"
    select_data_3 = "SELECT last_price, change, change_per FROM yen"

    Cursor.execute(select_data)
    Cursor2.execute(select_data_2)
    Cursor3.execute(select_data_3)

    all_cur = Cursor3.fetchall()
    
    result_japan = []
    all_money_hole = []
    for i in all_cur:
        all_money_hole.append(i[0])

    all_money_hole.reverse()
    all_money = [all_money_hole[2],all_money_hole[1],all_money_hole[0]]
    
    #Loop of result
    all_cur.reverse()
    for i in  all_cur[0]:
        result_japan.append(i) 
    
    


    return render_template('Graph_jp.html', all_money = all_money,result_japan=result_japan)

#Present page
@app.route('/Present')
def Present():
    return render_template('Present.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port =80 ,debug = True)