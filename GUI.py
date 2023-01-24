from tkinter import *
import tkinter
import psycopg2
import requests
from PIL import Image, ImageTk


def find_customers_from():
    query = """SELECT     id,bericht
               FROM       feedback
               WHERE      beoordeling IS TRUE 
               ORDER BY datum_beoordeeld DESC 
               LIMIT 5"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        records = cursor.fetchall()
    return records

connection_string = "host='localhost' dbname='test1' user='postgres' password='karoen2001'"
conn = psycopg2.connect(connection_string)

customers = find_customers_from()
lst =[]
for record in customers:
    lst.append(record[1])
cursor = conn.cursor()

column_names = []
data_rows = []

with conn as connection:
    with connection.cursor() as cursor:
      cursor.execute("select ov_bike, elevator, toilet, park_and_ride from station_service where station_city ='Utrecht'")
      column_names = [desc[0] for desc in cursor.description]
      for row in cursor:
        for i in row:
          data_rows.append(i)

tuples = [(key, value) for i, (key, value) in enumerate(zip(column_names, data_rows))]
res = dict(tuples)

conn.commit()
conn.close()


url = "https://api.openweathermap.org/data/2.5/weather?q=Utrecht&units=metric&appid=7751f43e6e24b3097fa9579eb6e0795e"

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
a = ('Temperature : {} degree celcius'.format(temp))

wind_speed = data['wind']['speed']
b = ('Wind Speed : {} m/s'.format(wind_speed))

latitude = data['coord']['lat']
c = ('Latitude : {}'.format(latitude))

longitude = data['coord']['lon']
d = ('Longitude : {}'.format(longitude))

description = data['weather'][0]['description']
e = ('Description : {}'.format(description))


win = Tk()
win.title("Stationshalscherm")
win.geometry("1100x550")
win.config(bg="#E0E066")

naam = Label(win,text ='Utrecht Centraal', font = ('Helvetica', 30, 'bold'),fg="Navyblue",bg="#E0E066")
naam.grid(row=0,column=0,sticky=E)


w = Label(win, text ='Berichten van de dag:', font = ('Helvetica', 20, 'bold'),fg="Navyblue",bg="#E0E066")
w.grid(row=1,column=0,sticky=W,padx=10,pady=10)

label = Label(win, text=lst[0], font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label.grid(row=2,column=0,sticky=W,padx=10)

label1 = Label(win, text=lst[1], font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label1.grid(row=3,column=0,sticky=W,padx=10)

label2 = Label(win, text=lst[2], font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label2.grid(row=4,column=0,sticky=W,padx=10)

label3 = Label(win, text=lst[3], font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label3.grid(row=5,column=0,sticky=W,padx=10)

label4 = Label(win, text=lst[4], font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label4.grid(row=6,column=0,sticky=W,padx=10)

label5 = Label(win, text="\n"+ "\nActuele weergegevens", font = ('Helvetica', 20, 'bold'),fg="Navyblue",bg="#E0E066")
label5.grid(row=8,column=0,sticky=W,padx=10)

label6 = Label(win, text=a, font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label6.grid(row=9,column=0,sticky=W,padx=10)

label7 = Label(win, text=b, font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label7.grid(row=10,column=0,sticky=W,padx=10)

label8 = Label(win, text=c, font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label8.grid(row=11,column=0,sticky=W,padx=10)

label9 = Label(win, text=d, font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label9.grid(row=12,column=0,sticky=W,padx=10)

label10 = Label(win, text=e, font = ('Helvetica', 16, 'bold'),bg="#E0E066")
label10.grid(row=13,column=0,sticky=W,padx=10)

label11 = Label(win, text="\n"+"\nDe beschikbare faciliteiten", font=('Helvetica', 20, 'bold'),fg="Navyblue",bg="#E0E066")
label11.grid(row=8,column=1,sticky=W)


image1 = Image.open("img_ovfiets.png")
test = ImageTk.PhotoImage(image1)
label12 = tkinter.Label(image=test)
label12.image = test
label12.place(x=750,y=370)

image2 = Image.open("img_toilet.png")
test1 = ImageTk.PhotoImage(image2)
label12 = tkinter.Label(image=test1)
label12.image = test1
label12.place(x=930,y=370)

image3 = Image.open("my-removebg-preview.png")
test2 = ImageTk.PhotoImage(image3)
label13 = tkinter.Label(image=test2,bg="#E0E066")
label13.image = test2
label13.place(x=800,y=-30)

win.mainloop()