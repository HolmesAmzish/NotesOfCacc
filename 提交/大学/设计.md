# 硬件设计

硬件需求：Arduino开发版，LED，LCD，按钮矩阵，舵机，红外传感器，工控主板，USB摄像头。

Arduino连接蜂鸣器，LED警示灯，红外传感器，按钮矩阵，LCD屏幕，舵机。

上位机连接USB摄像头和Arduino开发版，为了保证通网，最好使用网线连接wifi（也可以加装无线模块进行无线连接）。

![devices](devices.png)

# Arduino开发板

使用Arduino开发板和I/O拓展板进行设计，主要负责接收上位机的信号和处理，进行对电机的开关控制，以及对密码的判断和处理。同时将相关信息和状态显示到LCD屏幕上。

![arduino](arduino.jpg)

## 上位机

将Linux上位机与Arduino开发版连接，相互传输数据与信号，具体包括一下几点：

1. 在触发电机时，向上位机发送开启的信号，上位机再根据时间和情况进行数据处理和记录。
2. 上位机在人脸识别等事件完成后，输入信号，例如人脸识别失败，或者开门的信号。

## 舵机开关控制

舵机负责控制开关门，如果密码输入匹配成功，那么传输开启信号给电机开门。或者上位机传输开启信号进行开门。

```c
Servo servo;
servo.attach(kServoPin);
bool door_opened = false;

void OpenDoor() {
    servo.write(90);
    door_opened = true;
}

void CloseDoor() {
    servo.write(0);
    door_opened = false;
}
```



## 红外检测

用于检测是否还有人停留在门口，如果有人那么唤醒系统对人脸进行检测和开启LCD屏幕显示。其次是开门后判断人是否已经离开，等到人彻底离开之后关闭门，防止在有人的情况下关门

```c
bool person_present = false;
void loop() {
    if (digitalRead(kSensorPin) == HIGH) {
        person_present = true;
        OpenDoor();
    } else if (digitalRead(kSensorPin) == LOW) {
        delay(3000);
        person_present = false;
        CloseDoor();
    }
}
```



## 警报

![beep](beep.jpeg)

蜂鸣器和警示灯，在人脸识别失败和密码输入失败次数过多时，触发警报。需要手动输入密码解除。

```c
bool alert_active = false;
......

while (alert_active) {
    lcd.println("Too many failed attempts");
    analogWrite(kBuzzerPin, 128);
    digitalWrite(kLedPin, HIGH);
    if (VerifyPassword()) 
        alert_active = false;
}
```



## LCD显示屏

![lcd](lcd.jpg)

接入LCD显示屏显示信息，包括密码输入显示，密码对错显示，人脸识别成功显示。

```c
lcd.setCursor(0, 1);
switch (message_code) {
	case 1: 
        lcd.print("message1")
        break;
    case 2:
        lcd.print("message2");
        break;
        ......
    default:
}
```



## 按钮矩阵

![buttons](buttons.png)

负责手动输入密码

```c
const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
{'1','2','3'},
{'4','5','6'},
{'7','8','9'},
{'#','0','*'}
};
byte rowPins[ROWS] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {8, 7, 6}; //connect to the column pinouts of the keypad
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS );
```



# Linux上位机

![design](design.png)

![4b](4B.jpg)

## Python脚本

### 人脸识别模块

利用OpenCV进行人脸识别

```python
import cv2

def face_recognition(image):
    # 使用OpenCV进行人脸识别
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) > 0:
        return True
    else:
        return False

```



### 数据库模块

对数据库进行写入

```python
import sqlite3

def insert_record(record_type, description):
    conn = sqlite3.connect('lock666.db')
    c = conn.cursor()
    c.execute("INSERT INTO record (type, date, description) VALUES (?, datetime('now'), ?)", (record_type, description))
    conn.commit()
    conn.close()

```



## 数据库设计（lock666）

识别人脸（face）

| ID（id） | 姓名（name) | 文件位置（path）     |
| -------- | ----------- | -------------------- |
| 自动生成 |             | 依据上传文件自动生成 |

出入记录（record）

| ID（id） | 类型（type） | 时间（date） | 描述（description） |
| -------- | ------------ | ------------ | ------------------- |
| 自动生成 | 警告/普通    | 自动生成     |                     |

账户（user）

| ID（id） | 类型（type） | 用户名（username） | 密码（password） |
| -------- | ------------ | ------------------ | ---------------- |
| 自动生成 | 管理员/客人  |                    |                  |



## 服务器控制

最好能在不同系统下都能直接访问这个服务器并进行操作，综合开发难度还是直接构建一个Web服务器并允许设备访问来进行操作。在Linux服务器上开启一个Web服务器，再利用后端脚本进行简单的交互，显示到前端页面上。

**身份认证**

身份认证首先会自动创建一个初始化管理员，其次是在操作中可以由管理员生成临时客人账户并在某一段时间后删除。

**上传人脸上传和修改密码**

登录管理员账户之后进行操作。包括修改人脸数据库和远程修改密码。

**查看出入记录**

通过向数据库查询后，显示所有出入记录。