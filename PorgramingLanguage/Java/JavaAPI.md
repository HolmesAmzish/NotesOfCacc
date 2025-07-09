### java.net.InetAddress

- static InetAddress getByName(String host)
- static InetAddress[] getAllByName(String host)
- static InetAddress getLocalHost()
- byte[] getAddress()
- String getHostAddress()
- String getHostName()

### java.net.Socket

- Socket()
- void connect(SocketAddress address)
- void connect(SockAddress address, int timeoutInMilliseconds)
- void setSoTimeout(int timeoutInMilliseconds)
- boolean isConnected()
- boolean isClosed()