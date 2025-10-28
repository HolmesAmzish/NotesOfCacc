# 网络仿真技术 实验一

## 任务步骤

在实验前，由于我想直接创建一个工作目录专门存放网络仿真的作业，需要将 ns3 添加到路径以方便操作

```bash
export PATH="$PATH:$HOME/Workspace/ns-3.46" 
```

```
cacc@paradiso [01:50:23 PM] [~] 
-> % which ns3                                  
/home/cacc/Workspace/ns-3.46/ns3
```

### 任务 1：环境准备与第一次运行

1. 打开终端，进入ns3主目录（如：~/ns3-workspace/ns-allinone-3.44/ns-3.44）。

2. 运行以下命令，编译并运行<u><a href="https://first.cc/">first.cc</a></u>：

```bash
./ns3 run scratch/first
```

3. 观察运行结果，记录输出信息。

在实验中，可能是不同版本结构问题，无法在 scratch 文件夹中无法找到 first.cc 这个文件，因此在文件夹找了一会后发现。

```
cacc@paradiso [04:26:57 AM] [~/Workspace/ns-3.46] 
-> % ls scratch | grep first
cacc@paradiso [04:31:28 AM] [~/Workspace/ns-3.46] 
-> % find . -name 'first.cc'
./examples/tutorial/first.cc
```

随后运行示例

```
cacc@paradiso [04:31:48 AM] [~/Workspace/ns-3.46] 
-> % ./ns3 run examples/tutorial/first.cc
At time +2s client sent 1024 bytes to 10.1.1.2 port 9
At time +2.00369s server received 1024 bytes from 10.1.1.1 port 49153
At time +2.00369s server sent 1024 bytes to 10.1.1.1 port 49153
At time +2.00737s client received 1024 bytes from 10.1.1.2 port 9
```

### 任务 2：阅读与理解first.cc源代码

1. 使用文本编辑器打开scratch/first.cc。

2. 阅读代码，回答以下问题：
   
   - 程序包含了哪些头文件？这些头文件的作用是什么？
   
   - 主函数中做了哪些事情？请按步骤说明。
   
   - 代码中使用了哪些ns3的命名空间？
   
   - 解释NS_LOG_COMPONENT_DEFINE宏的作用。
   
   - 说明LogComponentEnable的作用。
   
   - 打开 ns-3 Documentation在线文档，

*https://www.nsnam.org/docs/release/3.44/doxygen/index.html* ，试查询LogComponentEnableAll函数，并了解其功能。

```
cacc@paradiso [04:36:09 AM] [~/Workspace/ns-3.46] 
-> % cat examples/tutorial/first.cc | grep include 
#include "ns3/applications-module.h"
#include "ns3/core-module.h"
#include "ns3/internet-module.h"
#include "ns3/network-module.h"
#include "ns3/point-to-point-module.h"
```

- **ns3/applications-module.h**：提供应用层协议和行为的类，例如 UdpEchoServerHelper 和 UdpEchoClientHelper，用于模拟应用层流量（如本代码中的 UDP 回显客户端和服务器）。
- **ns3/core-module.h**：包含 ns-3 的核心功能，如模拟时间管理（Time、Seconds）、模拟器控制（Simulator）、日志记录和命令行解析（CommandLine）。
- **ns3/internet-module.h**：提供互联网协议相关的组件，如 TCP/IP 协议栈，支持 IP 寻址和路由（InternetStackHelper、Ipv4AddressHelper）。
- **ns3/network-module.h**：提供基础网络组件，如节点（NodeContainer）、网络设备（NetDeviceContainer）和数据包处理。
- **ns3/point-to-point-module.h**：提供配置点对点连接的类，如 PointToPointHelper，用于建立两个节点之间的直接连接，并设置数据速率和延迟等属性。

通读文件， main 函数按以下步骤设置并运行了网络模拟

1. 解析命令行参数并初始化，在本例中没有用到。

2. 设置时间分辨率和启用日志
   
   ```cpp
   Time::SetResolution(Time::NS);
   LogComponentEnable("UdpEchoClientApplication", LOG_LEVEL_INFO);
   LogComponentEnable("UdpEchoServerApplication", LOG_LEVEL_INFO);
   ```
   
   时间分辨率设置为纳秒，同时为上面两个组件设置等级为 INFO 的日志

3. 创建节点
   
   ```c
   NodeContainer nodes;
   nodes.Create(2);
   ```

4. 配置点对点链路
   
   ```cpp
   PointToPointHelper pointToPoint;
   pointToPoint.SetDeviceAttribute("DataRate", StringValue("5Mbps"));
   pointToPoint.SetChannelAttribute("Delay", StringValue("2ms"));
   NetDeviceContainer devices;
   devices = pointToPoint.Install(nodes);
   ```
   
   使用 PointToPointHelper 创建并配置两个节点之间的点对点链路，设置速率为 5Mbps，信道延迟 2ms。在节点上安装点对点设备，并存储在 NetDeviceContainer 中。

5. 安装互联网协议栈
   
   ```cpp
   InternetStackHelper stack;
   stack.Install(nodes);
   ```
   
   在两个节点上安装互联网协议栈，以启用通信功能

6. 分配 IP 地址

7. 设置 UDP 回显服务器：
   
   ```cpp
   UdpEchoServerHelper echoServer(9);
   ApplicationContainer serverApps = echoServer.Install(nodes.Get(1));
   serverApps.Start(Seconds(1));
   serverApps.Stop(Seconds(10));
   ```
   
   配置 UDP 回显服务器应用，监听端口 9。然后在 1 号（node1）上安装这个应用，并在一秒时开启，十秒后关闭

8. 设置 UDP 回显客户端
   
   ```cpp
   UdpEchoClientHelper echoClient(interfaces.GetAddress(1), 9);
   echoClient.SetAttribute("MaxPackets", UintegerValue(1));
   echoClient.SetAttribute("Interval", TimeValue(Seconds(1)));
   echoClient.SetAttribute("PacketSize", UintegerValue(1024));
   ApplicationContainer clientApps = echoClient.Install(nodes.Get(0));
   clientApps.Start(Seconds(2));
   clientApps.Stop(Seconds(10));
   ```
   
   在节点 n0 上配置 UDP 回显客户端，向服务器的 IP 地址和端口 9 发送数据包，设置客户端属性，发送一个数据包，发送间隔一秒，数据包大小1024字节，安装客户端，模拟时间2秒启动，10秒停止。

9. 最后安装并清理模拟
   
   ```cpp
   Simulator::Run();
   Simulator::Destroy();
   ```

代码中主要使用了 ns3 命令空间，这是 ns-3 模拟器的核心命名空间。主要还包括了 `Time` 和 `Simulator` 属于模拟中时间控制和模拟器中事件调度的控制。

`LogComponentEnable` 的作用为启用两个应用的INFO等级的日志。

根据

### 任务 3：修改 first.cc 增加日志输出

通过添加 `std::cout` 函数在控制台应用中输出日志。

```diff
  Simulator::Run();
  Simulator::Destroy();
+ std::cout << "Simulation ends" << std::endl;
  return 0;
```

```
cacc@paradiso [01:18:27 PM] [~/Workspace/ns-3.46] 
-> % ./ns3 run examples/tutorial/first.cc
[0/2] Re-checking globbed directories...
[2/3] Linking CXX executable /home/cacc/Workspace/ns-3.46/build/examples/tutorial/ns3.46-first-debug
Simulation begins
At time +2s client sent 1024 bytes to 10.1.1.2 port 9
At time +2.00369s server received 1024 bytes from 10.1.1.1 port 49153
At time +2.00369s server sent 1024 bytes to 10.1.1.1 port 49153
At time +2.00737s client received 1024 bytes from 10.1.1.2 port 9
Simulation ends
```

### 任务 4：修改仿真发送间隔与数据包数量

按照要求首先找到相关行，已经写出，只需要按照要求修改数值即可。

```diff
- echoClient.SetAttribute("MaxPackets", UintegerValue(1));
+ echoClient.SetAttribute("MaxPackets", UintegerValue(3));

- echoClient.SetAttribute("Interval", TimeValue(Seconds(1)));
+ echoClient.SetAttribute("Interval", TimeValue(Seconds(2)));
```
