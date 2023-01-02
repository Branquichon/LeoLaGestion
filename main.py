from tkinter import *
from tkinter import messagebox
from functools import partial
import string
from PIL import Image, ImageTk
from tkinter import Canvas
import sqlite3
import sys
import traceback
#from Classes import *


class window():
    
    
    # initial window
    def __init__(self):
        self.f = Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        champ_label = Label(self.f, text="Welcome in Leo LaGESTION").pack()
        bouton1 = Button(self.f,text="User page",command=self.log_page).pack()
        bouton2 = Button(self.f,text="Administrator page",command=self.admin_page).pack()
        self.f.mainloop()


#### USER PART

    def log_page(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Login Menu").pack()
        global login 
        login=StringVar()
        global password 
        password=StringVar()
        t1=Label(self.f,text="Please fill the blank and press login to connect to your account").pack()
        t2=Label(self.f,text="Enter your login").pack()
        log_entry=Entry(self.f,textvariable=login,width=30).pack()
        t3=Label(self.f,text="Enter your password").pack()
        password_entry=Entry(self.f,textvariable=password,width=30,show='*').pack()
        log_button=Button(self.f,text="Login",command=self.logincheck).pack()
        
        baclmenu=Button(self.f,text="Back to the inital menu",command=self.backlog).pack()
        self.f.mainloop()
        
    def user_menu(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="User Menu").pack()
        b1=Button(self.f,text="View the current stock",command=self.current_stock_menu).pack()
        b2=Button(self.f,text="View the future stock",command=self.future_stock).pack()
        b3=Button(self.f,text="Make an order ",command=self.order).pack()
                
        backmenu=Button(self.f,text="Back to the utilisator log page",command=self.log_page).pack()
        self.f.mainloop()
        
    def current_stock_menu(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Current stock Menu").pack()
        
        b1=Button(self.f,text="View the current stock in a tab",command=self.current_stock_tab).pack()
        b2=Button(self.f,text="View the current stock in a chart",command=self.current_stock_chart).pack()
        
        backmenu=Button(self.f,text="Back to the user menu",command=self.user_menu).pack()
        self.f.mainloop()
        
    def current_stock_tab(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Current stock tab").pack()
        tableau = Treeview(self.f, columns=('nomfamille', 'prenom', 'da'))
        tableau.heading('nomfamille', text='Nom de famille')
        tableau.heading('prenom', text='Prénom')
        tableau.heading('da', text='DA')
        tableau['show'] = 'headings' 
        tableau.pack()
        
        backmenu=Button(self.f,text="Back to the current stock menu",command=self.current_stock_menu).pack()
        self.f.mainloop()
        
    def current_stock_chart(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("1500x1000")
        Title=Label(self.f,text="Current stock chart").pack()
        get_stock_diag()
        image = ImageTk.PhotoImage(Image.open("stock.jpg"))
 
        label = Label(self.f)
        label.img = image
        label.config(image=label.img)
        label.pack()
        
        backmenu=Button(self.f,text="Back to the current stock menu",command=self.current_stock_menu).pack()
        self.f.mainloop()
        
    def future_stock(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Vizualisation of future stock").pack()
        b2=Button(self.f,text="View the furure stock in a chart",command=self.future_stock_chart).pack()
        
        
        baclmenu=Button(self.f,text="Back to the inital menu",command=self.user_menu).pack()
        self.f.mainloop()
        
        
    def future_stock_chart(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Vizualisation of future stock").pack()
        t1=Label(self.f,text="Enter the number of day for the prevision").pack()
        global nbday
        nbday=IntVar()
        nbday_entry=Entry(self.f,textvariable=nbday,width=30).pack()
        b2=Button(self.f,text="View the furure stock in a chart",command=self.future_stock_chart2).pack()
        
        
        baclmenu=Button(self.f,text="Back to the inital menu",command=self.user_menu).pack()
        self.f.mainloop()
        
    def future_stock_chart2(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("1500x1000")
        Title=Label(self.f,text="Vizualisation of future stock").pack()
        get_futur_stock_diag(nbday)
        image = ImageTk.PhotoImage(Image.open("futur_stock.jpg"))
 
        label = Label(self.f)
        label.img = image
        label.config(image=label.img)
        label.pack()
        
        baclmenu=Button(self.f,text="Back to the inital menu",command=self.user_menu).pack()
        self.f.mainloop()
    
    
    
    def order(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x400")
        Title=Label(self.f,text="Order Menu").pack()
        global id_order
        global id_product
        global id_provider
        global arrival_date
        global quantity
        
        id_order=StringVar()
        id_product=StringVar()
        id_provider=StringVar()
        arrival_date=StringVar()
        quantity=IntVar()
        
        t1=Label(self.f,text="Enter the id_order").pack()
        id_order_entry=Entry(self.f,textvariable=id_order,width=30).pack()
        t2=Label(self.f,text="Enter the id_product").pack()
        id_product_entry=Entry(self.f,textvariable=id_product,width=30).pack()
        t2=Label(self.f,text="Enter the id_provider").pack()
        id_provider_entry=Entry(self.f,textvariable=id_provider,width=30).pack()
        t2=Label(self.f,text="Enter the arrival_date").pack()
        arrival_date_entry=Entry(self.f,textvariable=arrival_date,width=30).pack()
        t2=Label(self.f,text="Enter the quantity").pack()
        quantity_entry=Entry(self.f,textvariable=quantity,width=30).pack()
        
        
        validation=Button(self.f,text="Make the order",command=self.order2).pack()
        
        baclmenu=Button(self.f,text="Back to the user menu",command=self.user_menu).pack()
        self.f.mainloop()
        
        
    def order2(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Order Menu").pack()
        order_menu=Button(self.f,text="Back to the order menu",command=self.order).pack()
        backmenu=Button(self.f,text="Back to the user menu",command=self.user_menu).pack()
        self.f.mainloop()

### ONLY VIEW PART
    
    def user_menu_view(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="User Menu").pack()
        b1=Button(self.f,text="View the current stock",command=self.current_stock_menu_view).pack()
        b2=Button(self.f,text="View the future stock",command=self.future_stock_view).pack()
        backmenu=Button(self.f,text="Back to the inital menu",command=self.backlog).pack()
        self.f.mainloop()
    
    def current_stock_menu_view(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Current stock Menu").pack()
        b1=Button(self.f,text="View the current stock in a tab",command=self.current_stock_tab_view).pack()
        b2=Button(self.f,text="View the current stock in a chart",command=self.current_stock_chart_view).pack() 
        backmenu=Button(self.f,text="Back to the user menu",command=self.user_menu_view).pack()
        self.f.mainloop()
        
    def current_stock_chart_view(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("1500x1000")
        Title=Label(self.f,text="Current stock chart").pack()
        get_stock_diag()
        image = ImageTk.PhotoImage(Image.open("stock.jpg"))
        label = Label(self.f)
        label.img = image
        label.config(image=label.img)
        label.pack()
        backmenu=Button(self.f,text="Back to the current stock menu",command=self.current_stock_menu_view).pack()
        self.f.mainloop()
        
    def current_stock_tab_view(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Current stock tab").pack()
        tableau = Treeview(fenetre, columns=('nomfamille', 'prenom', 'da'))
        tableau.heading('nomfamille', text='Nom de famille')
        tableau.heading('prenom', text='Prénom')
        tableau.heading('da', text='DA')
        tableau['show'] = 'headings' 
        tableau.pack()
        
        backmenu=Button(self.f,text="Back to the current stock menu",command=self.current_stock_menu_view).pack()
        self.f.mainloop()
        
    def future_stock_view(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Vizualisation of future stock").pack()
        b2=Button(self.f,text="View the furure stock in a chart",command=self.future_stock_chart_view).pack()
        backmenu=Button(self.f,text="Back to the inital menu",command=self.user_menu_view).pack()
        self.f.mainloop()
        
        
    def future_stock_chart_view(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Vizualisation of future stock").pack()
        t1=Label(self.f,text="Enter the number of day for the prevision").pack()
        global nbday
        nbday=IntVar()
        nbday_entry=Entry(self.f,textvariable=nbday,width=30).pack()
        b2=Button(self.f,text="View the furure stock in a chart",command=self.future_stock_chart2_view).pack()
        backmenu=Button(self.f,text="Back to the inital menu",command=self.user_menu_view).pack()
        self.f.mainloop()
        
    def future_stock_chart2_view(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("1500x1000")
        Title=Label(self.f,text="Vizualisation of future stock").pack()
        get_futur_stock_diag(nbday)
        image = ImageTk.PhotoImage(Image.open("futur_stock.jpg"))
        label = Label(self.f)
        label.img = image
        label.config(image=label.img)
        label.pack()
        baclmenu=Button(self.f,text="Back to the inital menu",command=self.user_menu_view).pack()
        self.f.mainloop()
        
        

##### ADMIN PART 

        
    def admin_page(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Administrator Menu").pack()
        global login_ad
        login_ad=StringVar()
        global password_ad
        password_ad=StringVar()
        t1=Label(self.f,text="Please fill the blank and press login to connect to your account").pack()
        t2=Label(self.f,text="Enter your login").pack()
        log_entry=Entry(self.f,textvariable=login_ad,width=30).pack()
        t3=Label(self.f,text="Enter your password").pack()
        password_entry=Entry(self.f,textvariable=password_ad,width=30,show='*').pack()
        log_button=Button(self.f,text="Login",command=self.logincheck_admin).pack()
        baclmenu=Button(self.f,text="Back to the inital menu",command=self.backlog).pack()
        self.f.mainloop()
        
    def admin_menu(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Administrator Menu").pack()
        b1=Button(self.f,text="Add a new product to the data base",command=self.admin_add).pack()
        b2=Button(self.f,text="Remove a  product from the data base",command=self.admin_pop).pack()
        backmenu=Button(self.f,text="Back to the log page ",command=self.admin_page).pack()
        self.f.mainloop()
        
    def admin_add(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="New product Menu").pack()
        backmenu=Button(self.f,text="Back to the administrator menu",command=self.admin_menu).pack()
        self.f.mainloop()
        
    def admin_pop(self):
        self.f.destroy()
        self.f=Tk()
        self.f.title("Stock Tool")
        self.f.geometry("400x300")
        Title=Label(self.f,text="Remove a product  Menu").pack()
        backmenu=Button(self.f,text="Back to the administrator menu",command=self.admin_menu).pack()
        self.f.mainloop()

    def logincheck_admin(self):
        if ((login_ad.get()=="baptiste") & (password_ad.get()=="1234")):
            self.admin_menu()
        self.log_page()



    def logincheck(self):
        if ((login.get()=="antoine") & (password.get()=="1234")):
            self.user_menu()
        elif ((login.get()=="florian") & (password.get()=="5678")):
            self.user_menu_view()
        self.log_page()


    def backlog(self):
         self.f.destroy()
         self.__init__()

        
main=window()