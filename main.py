import requests
import lxml
from bs4 import BeautifulSoup

from tkinter import *
true_url=''

window=Tk()
window.title('amazon price tracker')
window.config(padx=20,pady=20)
window.geometry('500x300')
window.config(background='blue',bg='lightblue')

def fun(*args):
    email=phoneno_input.get()
    url2=url_input.get()
    target_price2=target_price_input.get()
    print(email,target_price2)

def get_url(*args):
    url2=url_input.get()
    return url2

label=Label(window, text='Enter The Required Details', font=("Courier 10 bold"))
label.grid(row=0,column=0)
#label.pack()

urltext=Label(window,text='ENTER URL: ')
urltext.grid(row=1,column=0,padx=20,pady=20)
url_input=Entry()
url_input.grid(row=1,column=1,padx=20,pady=20)

target_price=Label(window,text='ENTER TARGET PRICE: ')
target_price.grid(row=3,column=0,padx=20,pady=20)
target_price_input=Entry()
target_price_input.grid(row=3,column=1,padx=20,pady=20)

phoneno=Label(window,text='ENTER YOUR PHONE NO.: ')
phoneno.grid(row=4,column=0,padx=20,pady=20)
phoneno_input=Entry()
phoneno_input.grid(row=4,column=1,padx=20,pady=20)

checkbutton=Button(window,text='SUBMIT',command=fun)
checkbutton.grid(row=5,column=2)

exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.grid(row=6,column=2)
window.mainloop()

url = 'https://www.amazon.in/Apple-iPhone-14-128GB-Blue/dp/B0BDK62PDX/ref=sr_1_1_sspa?keywords=iphone%2B14&qid=1682010914&sprefix=iphon%2Caps%2C978&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()
if ',' in price:
    price_without_currency = price.split(",")
    ogprice=''.join(price_without_currency)
    m=len(ogprice)
    ogprice=ogprice[:m-1]
    ogprice2=ogprice
    ogprice2=int(ogprice2)
    #price_as_float = float(price_without_currency)
    print(ogprice2)
    title = soup.find(id="productTitle").get_text().strip()
    print(title)
#price_without_currency = price.split(",")
#ogprice=''.join(price_without_currency)
else:
    m=len(price)
    ogprice2=price[:m-1]
    ogprice2=int(ogprice2)
    print(ogprice2)
'''print(price)
ogprice=ogprice[:m]
ogprice2=ogprice
ogprice2=int(ogprice2)
#price_as_float = float(price_without_currency)
print(ogprice2)
title = soup.find(id="productTitle").get_text().strip()
print(title)'''