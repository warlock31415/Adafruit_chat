from Adafrui_IO import Client

aio = Client('1bf490ed9e8d4a03ae3fd81c684d4e97')

feed = raw_input('Enter your name: ')
temp_feed = feed + ' entered chat'
aio.send(feed, temp_feed)

message = '\0'

while message!='q':
  message = raw_input ('Message:')
  send_message = '-> ' + message
  aio.send(feed,send_message)
