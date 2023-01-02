import math
import numpy as np
import cx_Oracle
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta


class user : 
    
    def __init__(self, login, pw):
        self.login = login
        self.pw = pw
    
    def checklog(self, password) : 
        if (password == self.pw) :
            return True
        else :
            return False
        
    def change_pw(self, actual, new):
        if (actual == self.pw) :
            self.pw = new
            return 'Password changed'
        else :
            return 'Wrong actual password'


class product : 
    
    def __init__(self, id, nom, current_stock, capacity, avg_daily):
        self.id = id
        self.name = nom
        self.current_stock = current_stock
        self.capacity = capacity
        self.avg_daily = avg_daily

    def get_id(self):
        return self.id
    def get_stock(self):
        return self.current_stock
    def get_name(self):
        return self.name
    def get_capacity(self):
        return self.capacity
    def get_futur_stock(self, days) : 
        return self.current_stock-(self.avg_daily*days)
    
class provider : 
    
    def __init__(self, id_provider, name, tel, mail):
        self.id = id_provider
        self.name = name
        self.tel = tel
        self.mail = mail
    
class order :
    
    def __init__(self, id_order, id_product, id_provider, arrival_date, quantity):
        self.id_order = id_order,
        self.id_product = id_product
        self.id_provider = id_provider
        self.arrival_date = arrival_date
        self.quantity = quantity
    

def query_products(dsn_tns):
 
    conn = cx_Oracle.connect('SYSTEM', 'Jsap*am2c2F.Q', dsn_tns)
    c = conn.cursor()
    c.execute('select * from mv_produit')
    return c

def query_order(dsn_tns):
    
    conn = cx_Oracle.connect('SYSTEM', 'Jsap*am2c2F.Q', dsn_tns)
    c = conn.cursor()
    c.execute('select * from mv_livraison')
    return c

def query_order_futur(days, product, dsn_tns):
    
    conn = cx_Oracle.connect('SYSTEM', 'Jsap*am2c2F.Q', dsn_tns)
    futur_date = date.today() + timedelta(days)
    c = conn.cursor()
    c.execute('select * from mv_livraison where id_produit ='+str(product.get_id())+
              " and date_livraison > sysdate " + 
              r" and date_livraison > TO_DATE('"+str(futur_date)+ r"', 'YYYY/MM/DD')")
    return c

def init_stock(dsn_tns):
    stock = list()
    conn = cx_Oracle.connect('SYSTEM', 'Jsap*am2c2F.Q', dsn_tns)
    c = conn.cursor()
    c.execute('select * from mv_produit')
    for row in c:
        newprod = product(row[0], row[1], row[2], row[3], row[4]) 
        #VERIFIER CA ET QU'IL Y A BIEN AVG DAILY
        stock.append(newprod)
    return stock

def color_stock(capacity, stock):
    
    coef = stock/capacity
    if coef <= 0.10 :
        return "red"
    elif coef < 0.20 :
        return "orange"
    elif coef < 0.30 :
        return "yellow"
    else:
        return "green"

def get_stock_diag():
    
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XEPDB1')
    current_stock = init_stock(dsn_tns)
    stock = dict()
    colors= []
    for i in current_stock :
        stock[i.get_name()] = i.get_stock()
        colors.append(color_stock(i.get_capacity(), i.get_stock()))
    f = plt.figure()
    f.set_figwidth(21)
    f.set_figheight(5)
    plt.grid()
    plt.bar(stock.keys(), stock.values(), color = colors)
    plt.savefig('stock.jpg')
    
def get_stock_tab():
    
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XEPDB1')
    current_stock = init_stock(dsn_tns)
    stock = np.array()
    for i in current_stock :
        newline = [i.get_id(), i.get_name(),i.get_stock()]
        stock.append(newline)
    return stock

def get_futur_stock_diag(current_stock, days):
    
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XEPDB1')
    stock = init_stock(dsn_tns)
    stock = dict()
    colors = []
    for i in current_stock :
        arrivals = 0
        for c in query_order_futur(days, i, dsn_tns):
            arrivals = arrivals + c[3]
        futur = i.get_futur_stock(days) + arrivals
        stock[i.get_name()] = futur
        colors.append(color_stock(i.get_capacity(), i.get_futur_stock(days)))
    f = plt.figure()
    f.set_figwidth(21)
    f.set_figheight(5)
    plt.grid()
    plt.bar(stock.keys(), stock.values(), color = colors)
    plt.savefig('futur_stock.jpg')
    
def get_futur_stock_tab(current_stock, days):
    
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XEPDB1')
    stock = init_stock(dsn_tns)
    stock = np.array()
    
    for i in current_stock :
        arrivals = 0
        for c in query_order_futur(days, i, dsn_tns):
            arrivals = arrivals + c[3]
        futur = i.get_futur_stock(days) + arrivals
        newline = [i.get_id(), i.get_name(),futur]
        stock.append(newline)
    return stock


def create_order( id_order, id_product, id_provider, arrival_date, quantity):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XEPDB1')
    conn = cx_Oracle.connect('SYSTEM', 'Jsap*am2c2F.Q', dsn_tns)
    c = conn.cursor()
    print('insert into mv_livraison values ('+ str(id_order) +r", "+str(id_product)+r", '"+
              str(id_provider)+r"', TO_DATE('"+arrival_date+r"', 'YYYY/MM/DD'), "+ str(quantity)+')')
    c.execute('insert into livraison values ('+ str(id_order) +r", "+str(id_product)+r", '"+
              str(id_provider)+r"', TO_DATE('"+arrival_date+r"', 'YYYY/MM/DD'), "+ str(quantity)+')')
    c.execute('commit')
    return c
