### 编程训练报告

------

#### 1. 环境准备

##### 1.1 安装VS.NET开发环境

首先，确保您的计算机上安装了Visual Studio .NET。可以从[Visual Studio官方网站](https://visualstudio.microsoft.com/)下载并安装最新版本。安装时选择C#开发环境和Windows桌面开发工作负载。

------

#### 2. 在阿里物联网云上创建设备

##### 2.1 注册并登录阿里云

访问[阿里云官方网站](https://www.aliyun.com/)，如果没有账号，请先注册一个阿里云账号，然后登录。

##### 2.2 创建物联网平台实例

1. 在阿里云控制台中，找到“物联网平台”并进入。
2. 创建一个物联网平台实例，选择实例规格和地域，完成实例的创建。

##### 2.3 创建产品和设备

1. 在物联网平台实例中，创建一个新产品，例如“DeviceA_Product”和“DeviceB_Product”。
2. 在每个产品下，分别创建设备“DeviceA”和“DeviceB”。

------

#### 3. 开发C#窗体应用

##### 3.1 创建Visual Studio项目

1. 打开Visual Studio，选择“创建新项目”。
2. 选择“Windows 窗体应用 (.NET Framework)”模板，分别创建两个项目：`FormA`和`FormB`。
3. 在每个项目中，添加必要的控件（如TextBox和Button）来发送和接收消息。

##### 3.2 安装阿里云SDK

在NuGet包管理器中，安装阿里云IoT SDK。打开“工具”菜单，选择“NuGet 包管理器”->“管理解决方案的NuGet包”，搜索并安装`AlibabaCloud.SDK.Iot`。

##### 3.3 连接阿里云物联网平台

在项目中，编写代码连接阿里云物联网平台，使用设备的DeviceName和DeviceSecret进行身份验证。

示例代码：

```csharp
using System;
using System.Windows.Forms;
using AlibabaCloud.SDK.Iot20180120;
using AlibabaCloud.SDK.Iot20180120.Models;
using AlibabaCloud.OpenApiClient;
using AlibabaCloud.OpenApiClient.Models;
using AlibabaCloud.SDK.Iot20180120.Client.Models;

namespace FormA
{
    public partial class FormA : Form
    {
        private IClient client;
        private const string productKey = "YourProductKey";
        private const string deviceName = "DeviceA";
        private const string deviceSecret = "YourDeviceSecret";

        public FormA()
        {
            InitializeComponent();
            InitializeAliyunClient();
        }

        private void InitializeAliyunClient()
        {
            var config = new Config
            {
                AccessKeyId = "YourAccessKeyId",
                AccessKeySecret = "YourAccessKeySecret",
                Endpoint = "iot.cn-shanghai.aliyuncs.com"
            };
            client = new Client(config);
            ConnectDevice();
        }

        private void ConnectDevice()
        {
            var loginRequest = new PubRequest
            {
                ProductKey = productKey,
                DeviceName = deviceName,
                DeviceSecret = deviceSecret
            };

            try
            {
                var response = client.Pub(loginRequest);
                if (response.IsSuccess())
                {
                    Console.WriteLine("Device connected successfully.");
                    ReceiveMessage();
                }
                else
                {
                    Console.WriteLine("Failed to connect device: " + response.ErrorMessage);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception in connecting device: " + ex.Message);
            }
        }

        private void SendMessage(string message)
        {
            var pubRequest = new PubRequest
            {
                ProductKey = productKey,
                DeviceName = deviceName,
                TopicFullName = $"/{productKey}/{deviceName}/user/update",
                MessageContent = Convert.ToBase64String(System.Text.Encoding.UTF8.GetBytes(message)),
                Qos = 0
            };

            try
            {
                var response = client.Pub(pubRequest);
                if (response.IsSuccess())
                {
                    Console.WriteLine("Message sent successfully.");
                }
                else
                {
                    Console.WriteLine("Failed to send message: " + response.ErrorMessage);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception in sending message: " + ex.Message);
            }
        }

        private void ReceiveMessage()
        {
            var subRequest = new SubRequest
            {
                ProductKey = productKey,
                DeviceName = deviceName,
                TopicFullName = $"/{productKey}/{deviceName}/user/update"
            };

            try
            {
                client.OnMessageReceived += (sender, e) =>
                {
                    var payload = e.Payload;
                    var message = System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(payload));
                    Invoke((MethodInvoker)delegate
                    {
                        textBoxReceivedMessages.Text += message + Environment.NewLine;
                    });
                };

                var response = client.Sub(subRequest);
                if (response.IsSuccess())
                {
                    Console.WriteLine("Subscribed to topic successfully.");
                }
                else
                {
                    Console.WriteLine("Failed to subscribe to topic: " + response.ErrorMessage);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception in receiving message: " + ex.Message);
            }
        }

        private void buttonSend_Click(object sender, EventArgs e)
        {
            var message = textBoxSendMessage.Text;
            SendMessage(message);
        }
    }
}

```

##### 3.4 发送和接收消息

在两个窗体项目中，分别实现发送和接收消息的功能。通过阿里云物联网平台的Topic进行数据通信。

------

#### 4. 云上配置规则引擎

##### 4.1 配置规则引擎

1. 在阿里云物联网平台实例中，找到“规则引擎”并进入。
2. 创建一个新规则，设置数据源为“设备上报数据”，选择设备A和设备B。
3. 配置数据处理逻辑，将设备A的消息转发到设备B的Topic，反之亦然。

示例规则：

- 数据源：设备A的Topic
- 数据目的地：设备B的Topic

反之亦然。

------

#### 5. 总结

通过本次编程训练，我们学会了如何使用VS.NET开发C#窗体应用，连接阿里云物联网平台，并通过规则引擎实现设备之间的数据通信。这一过程不仅加强了我们对物联网技术的理解，也提升了我们的编程技能和解决实际问题的能力。