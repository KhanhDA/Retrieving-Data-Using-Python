from tkinter import *
from tkinter import ttk,messagebox,filedialog
import pandas as pd
import os
import csv
my_app=Tk()
os.getcwd()
my_app.geometry('850x600')
my_app.title('PHẦN MỀM TÍNH HÓA ĐƠN')
wr1=LabelFrame(my_app,text='Nhập dữ liệu')
wr2=LabelFrame(my_app,text='Xuất dữ liệu')
wr1.pack(fill='both',expand='yes',padx=20,pady=2)
wr2.pack(fill='both',expand='yes',padx=20,pady=10)
#Phần nhập dữ liệu
def temp_text(e): #Phần ẩn chữ khi click
    txt3.delete(0,"end")
def temp_text1(e): #Phần ẩn chữ khi click
    txt4.delete(0,"end")
def search():   #Search
    df=pd.read_csv("dulieuthang.csv")
    df=df.dropna()
    a=txt3.get()
    df6=df[(df['Ten hang hoa']==a)]
    df6.to_csv("Search.csv", index=False)
    treeview['column']=list(df6.columns)
    treeview['show']='headings'
    for column in treeview['column']:
        treeview.heading(column,text=column)
    DataFrameRows=df6.to_numpy().tolist()
    for row in DataFrameRows:
        treeview.insert('','end',values=row)
    return None
def Load_Data():    #Xuất file
    df5=pd.read_csv('dulieuthang.csv')
    treeview['column']=list(df5.columns)
    treeview['show']='headings'
    for column in treeview['column']:
        treeview.heading(column,text=column)
    DataFrameRows=df5.to_numpy().tolist()
    for row in DataFrameRows:
        treeview.insert('','end',values=row)
    return None
df=pd.read_csv('Sales_August_2019.csv')
df=df[df["Quantity Ordered"]!="Quantity Ordered"]
df["Quantity Ordered"] = df["Quantity Ordered"].astype(float)
df['Ten hang hoa']=df['Product']
df["Ton Kho"]=df["Quantity Ordered"]
df["Price Each"] = df["Price Each"].astype(float)
df1=df.drop(["Purchase Address","Order Date","Quantity Ordered","Price Each","Product"], axis = 1)
df["Don gia"]=df["Price Each"]
df1=df.groupby(['Ten hang hoa'])["Ton Kho"].sum().reset_index()
def func(x):
        s=1
        return s
df1["So luong"]=df["Order Date"].apply(func)
df1['Don gia']=df['Don gia']
df1.to_csv("dulieuthang.csv", index=False)
def delete():
    txt3.delete(0,"end")
    txt4.delete(0,"end")
def submitform():
    df=pd.read_csv("dulieuthang.csv")
    df=df.dropna()
    a=txt3.get()
    df3=df[(df['Ten hang hoa']==a)]
    def funb(x):
      a=float(txt4.get())
      return a
    df3['So luong']=df3['So luong'].apply(funb)
    df3['Tong USD']=df3['So luong']*df3['Don gia']
    name="Ten Khach Hang:"+txt1.get()
    print(name)
    address="Dia Chi Khach Hang: "+txt2.get()
    print(address)
    c={name:[""],address:[""]}
    yourin4=pd.DataFrame(c)
    print(yourin4)
    df3=df3.join(yourin4)
    df3.to_csv("Hoa Don.csv", index=False)
treeview=ttk.Treeview(wr2)   
treeview.place(relheight=3,relwidth=3) 
lb1=Label(wr1,text='PHẦN MỀM TÍNH HÓA ĐƠN',font=('Arial',25))
lb1.grid(column=1,row=0)
lb2=Label(wr1,text='Tên khách hàng')
lb2.grid(column=0,row=1)
txt1=Entry(wr1,width=100)
txt1.grid(column=1,row=1)
lb3=Label(wr1,text='Địa chỉ/SĐT')
lb3.grid(column=0,row=2)
txt2=Entry(wr1,width=100)
txt2.grid(column=1,row=2)
btnIndon=Button(wr1,text='In Đơn',width=10,height=4,bg='blue',foreground="white",font=('Arial',9),command=submitform)
btnIndon.grid(column=3,row=1,rowspan=3)
txt3=Entry(wr1,width=100,justify=RIGHT,bg='yellow')
txt3.insert(0, 'Nhập sản phẩm cần tìm....')
txt3.bind("<FocusIn>", temp_text)
txt3.grid(column=0,row=3,columnspan=2,sticky="W")
txt4=Entry(wr1,width=100,justify=RIGHT,bg='yellow')
txt4.insert(0, 'Nhập số lượng cần mua....')
txt4.bind("<FocusIn>", temp_text1)
txt4.grid(column=0,row=4,columnspan=2,sticky="W")
btnXoa=Button(wr1,text='Xóa',width=10,bg='orange',command=delete)
btnXoa.grid(column=1,row=3,sticky="E")
#Phần xuất dữ liệu
btnBrowseFile=Button(wr1,text='Xuất File',bg='blue',command=Load_Data)
btnBrowseFile.grid(column=0,row=5)
btnS=Button(wr1,text='Tìm hàng',width=10,bg='orange',command=search)
btnS.grid(column=1,row=5)
my_app.mainloop()
