from twilio.rest import Client
from main import soup,ogprice2,url

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 60000
# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'AC3633824b887f8e16782fae5919ebfa1d'
auth_token = '8e19b400571fb27af03bf688364a201d'
  
if BUY_PRICE>ogprice2 or BUY_PRICE<ogprice2:
    client = Client(account_sid, auth_token)
  
''' Change the value of 'from' with the number 
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
                              from_='+16206788927',
                              body =f'the current price of {title} is : {ogprice2} which is {ogprice2-BUY_PRICE} more than your target',
                              to ='+919399895418'
                          )
  
print(message.sid)