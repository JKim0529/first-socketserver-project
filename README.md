![This is an image](http://sergeyzhuk.me/assets/images/posts/reactphp/sockets.jpg)
# Socketserver
## Ping and communicate other clients through server in socketserver
###### This project uses socket-server with python language and it connects with the Arduino. 
Socketserver helps with one client with communicating to the server, and giving tasks.
It can be used with Java and Python for language, and this one is used with python.
The server is linked with Arduino by Firmata, which you can activate by putting Standard Firmata from Firmata in examples within Arduino file
Server can start, and clients can join, message, command, and disconnect.
In this project, the server address must match with the local network address by command "ifconfig" on the terminal.
