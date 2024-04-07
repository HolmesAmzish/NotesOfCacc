# Serial

`Serial`是Arduino中用于串行通信的库，它允许Arduino板通过其内置的UART（通用异步收发传输器）与计算机或其他设备进行数据交换。

| 函数                  | 作用                                             |
| ------------------- | ---------------------------------------------- |
| available()         | 返回当前可用的带读取字节数                                  |
| availableForWrite() | 返回可以立即写入到串口缓冲区的可用空间大小                          |
| begin()             | 初始化串口通信并设置波特率，例如Serial.begin(9600)会将波特率设置为9600 |
| end()               | 关闭串口通信                                         |
| find()              | 在串口缓冲区中搜索指定的字符串，并返回找到的第一个字符的位置索引               |
| findUntil()         | 同样在缓冲区搜索字符串，但直到遇到特定终止符才停止搜索                    |
| flush()             | 清空发送缓冲区                                        |
| parseFloat()        |                                                |
| parseInt()          |                                                |
| peek()              |                                                |
| print()             | 将一个或多克参数作为ASCII文本或者数值格式发送出去                    |
| println()           | 发送且换行                                          |
| read()              | 从串口接受换成去读取下一个字节并返回该字节的值                        |
| readBytes()         |                                                |
| readString()        |                                                |
| readStringUntil()   |                                                |
| setTimeout()        | 设置超时时间                                         |
| write()             | 将一个或多个字节以二进制形式写入串口，可以用于发送ASCII文本整数或者二进制数据      |
| serialEvent()       |                                                |