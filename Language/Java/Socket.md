```java
// TcpServer.java
import java.io.*;
import java.net.*;

public class TCPServer {
    private static final int PORT = 8080;

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("TCP Server 正在监听端口: " + PORT);

            while (true) {
                // 等待客户端连接
                Socket clientSocket = serverSocket.accept();
                System.out.println("新客户端连接: " + clientSocket.getInetAddress());

                // 为每个客户端启动一个线程处理（支持多客户端）
                new Thread(new ClientHandler(clientSocket)).start();
            }
        } catch (IOException e) {
            System.err.println("服务器异常: " + e.getMessage());
        }
    }

    // 处理单个客户端的线程
    private static class ClientHandler implements Runnable {
        private final Socket socket;

        public ClientHandler(Socket socket) {
            this.socket = socket;
        }

        @Override
        public void run() {
            try (
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))
            ) {
                String inputLine;
                while ((inputLine = in.readLine()) != null) {
                    System.out.println("收到 [" + socket.getInetAddress() + "]: " + inputLine);

                    // 回显（可选）
                    out.println("Server 收到: " + inputLine);
                }
            } catch (IOException e) {
                System.out.println("客户端断开: " + socket.getInetAddress());
            } finally {
                try {
                    socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

```java
// TcpClient.java
import java.io.*;
import java.net.*;

public class TCPClient {
    private static final String SERVER_IP = "127.0.0.1";  // 服务器 IP
    private static final int PORT = 8080;

    public static void main(String[] args) {
        try (
            Socket socket = new Socket(SERVER_IP, PORT);
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in))
        ) {
            System.out.println("已连接到服务器: " + SERVER_IP + ":" + PORT);
            System.out.println("输入消息（输入 exit 退出）:");

            String userInput;
            while ((userInput = stdIn.readLine()) != null) {
                if ("exit".equalsIgnoreCase(userInput)) {
                    break;
                }

                // 发送消息
                out.println(userInput);
                System.out.println("发送: " + userInput);

                // 接收服务器回显
                String response = in.readLine();
                System.out.println("服务器回复: " + response);
            }
        } catch (IOException e) {
            System.err.println("客户端异常: " + e.getMessage());
        }
    }
}
```
