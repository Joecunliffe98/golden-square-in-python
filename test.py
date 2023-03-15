from twilio.rest import Client 
from datetime import datetime
from datetime import timedelta
 
now = datetime.now()

current_time = now.strftime("%H:%M")
account_sid = 'AC0f751cae28a58f91a2e9c2ec66dbf5bf' 
auth_token = '16e504a998e0038893478a401afafca0' 
client = Client(account_sid, auth_token) 
ready_time = now + timedelta(minutes=30)
ready_time_string = str(ready_time.strftime("%H:%M"))
message = client.messages.create(  
                              messaging_service_sid='MG271670ef6e1e83ea553f9463e0b6037c', 
                              body="Thank you! Your order was placed at " + str(current_time) + " and will be ready at " + ready_time_string + ".",      
                              to='+447387194012' 
                          ) 
 
print(message.sid)