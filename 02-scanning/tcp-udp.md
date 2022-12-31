**TCP**
--
- Tansmition Control Protocol and is the most commonly used protocol on the internet
- To load a web site, your machine is sending TCP packages to the server address asking to send the webpage to you, then the webserver responds sending a stream of tcp packages.
- It's the same when you clic in a link or post a comment. etc. Your web browser send tcp packages to the web browser and this server send packages back
- However TCP is not a one way communication

**Three Way Hanshake**
--
1. SYN = the client stablished connection with the server = Syncronyzed Sequence Number
2. SYN/ACK = The server responds to the clientś request with signal bit set
3. ACK = The client acknowledge the response of server and both stablished conneciton

**UDP**
--
- User Datagram Protocol
- A datagram is a packet of information
- Work similarly to TCP, but it's UDT is faster because throw out all the errors
- Is used when speed is desirable and error correciton is not neccesary
- Used frequently by online games and live broatcast 
