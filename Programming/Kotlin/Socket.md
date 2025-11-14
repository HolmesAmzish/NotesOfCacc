```kotlin
// TcpServer.kt
import java.net.*
import java.io.*
import kotlin.concurrent.thread

private const val PORT = 5678

fun main() {
    ServerSocket(PORT).use { server ->
        println("TCP Server 正在监听端口 $PORT")
        while (true) {
            val client = server.accept()          // 阻塞等待连接
            println("新客户端连接: ${client.inetAddress}")
            // 每个客户端一个线程（或协程）处理
            thread { handleClient(client) }
        }
    }
}

private fun handleClient(socket: Socket) {
    socket.use { sock ->
        val reader = sock.getInputStream().bufferedReader()
        val writer = sock.getOutputStream().bufferedWriter()

        try {
            var line: String?
            while (reader.readLine().also { line = it } != null) {
                println("收到 [${sock.inetAddress}]: $line")
                writer.write("Server 收到: $line\n")
                writer.flush()
            }
        } catch (e: IOException) {
            println("客户端 ${sock.inetAddress} 异常或断开")
        } finally {
            println("客户端 ${sock.inetAddress} 断开")
        }
    }
}
```

```kotlin

```
