# 基础输入输出

## 引脚硬件

### 数字引脚

Arduino Uno开发板上有14个数字引脚，标记为D0至D13。这些引脚既可以作为数字输入，也可以作为数字输出使用：

- **数字输入**：通过`pinMode(pin, INPUT)`函数配置为输入模式，然后使用`digitalRead(pin)`函数读取引脚上的电平状态（HIGH或LOW）。
- **数字输出**：配置为输出模式时，可以通过`pinMode(pin, OUTPUT)`设置，并使用`digitalWrite(pin, HIGH)`或`digitalWrite(pin, LOW)`函数将引脚设定为高电平或低电平，用于控制如LED灯、继电器或其他数字设备的开关。

> [!NOTE]
>
> 另外，部分数字引脚还支持**PWM（脉宽调制）**输出，这允许它们模拟不同的电压级别，从而调整例如LED亮度或电机速度。在Arduino Uno上，以下数字引脚支持PWM输出：3，5，6，9，10，11
>
> 对于PWM功能，使用的是`analogWrite(pin, value)`函数，其中`value`是一个介于0（全关）和255（全开）之间的值，表示占空比。
>
> 同时，引脚2和3还支持**中断**



### 模拟引脚

Arduino Uno还拥有6个模拟引脚，通常标记为A0至A5：

- **模拟输入**：模拟引脚主要用于读取连续变化的电压信号，例如来自传感器的数据。通过`analogRead(pin)`函数读取模数转换器（ADC）的结果，返回一个介于0（0V）到1023（5V，对于Uno这样的5V系统）之间的整数值，对应输入电压的相对比例。
- *有限的数字功能：虽然主要用作模拟输入，模拟引脚也可被配置为数字输入或数字输出，但由于其内部结构，这样做并不常见，且会牺牲掉其模拟功能。*



## 引脚函数

### 数字I/O

1. `digitalRead()` 该函数用于读取Arduino开发板上指定数字引脚的电平状态。它返回一个整数值，如果是高电平（逻辑1）则返回`HIGH`，如果是低电平则为`LOW`。
2. `digitalWrite()` 设置数字引脚的输出电平，当给定参数为`HIGH`时为高电平，反之为低电平。
3. `pinMode()` 用于配置指定引脚的工作模式，定义是输入，输出还是内部上拉电阻的输入。

   ```c
   void pinMode(uint8_t pin, uint8_t mode);
   ```

   其中工作模式包括

   - `INPUT`：设置引脚为输入模式
   - `OUTPUT`：设置引脚为输出模式
   - `INPUT_PULLUP`：设置引脚为输入模式，并启用内部上拉电阻



### 模拟I/O

1. `analogRead()` ：该函数从指定的模拟引脚（如A0到A5等）读取模拟电压值，并将其转换成一个介于0（0V）和1023（最大参考电压，通常是5V）之间的整数。这样可以读取连续变化的电压信号，如来自传感器的数据。
2. `analogReadResolution()` ：这个函数允许你改变模数转换器（ADC）读取模拟输入时的位数（即分辨率），从而影响`analogRead()`返回的精度。不是所有Arduino板都支持自定义模拟读取分辨率。
3. `analogReference()` ：此函数用于设置模拟输入的基准电压，以便在进行模数转换时确定电压范围。例如，可以选择内部固定电压（DEFAULT）、内部带隙参考（INTERNAL）、外部参考电压（EXTERNAL）或者其他特定的内部参考电压（如INTERNAL1V1，在某些板子上可用）。
4. `analogWrite()` ：尽管名字中包含“模拟”，但`analogWrite()`实际上实现的是PWM（脉宽调制）功能，它将一个介于0和255之间的数字值转化为占空比可变的方波信号输出到具有PWM功能的数字引脚上，以此来模拟不同的电压等级。
5. `analogWriteResolution()` ：与`analogReadResolution()`类似，此函数作用于PWM输出，允许调整PWM波形的细分程度，即PWM输出的精度。通过提高分辨率，可以得到更细腻的模拟电压控制级别，但并非所有Arduino板都能自定义PWM的分辨率。



数字引脚3，5，6，9，10，11具有PWM功能

```c
#define LED_PIN 10
void setup() {
    pinMode(LED_PIN, OUTPUT);
}
void loop() {
    for (int value = 0; value < 255; value++) {
        analogWrite(LED_PIN, value);
    }
    // 逐渐变亮
}
```



# 时间

这些函数在Arduino编程中用于处理时间相关的任务和延时。每个函数有不同的用途，下面对它们逐一进行解释：

1. **`delay()` 函数**
   ```c++
   void delay(unsigned long milliseconds);
   ```
   此函数用于暂停程序执行指定的毫秒数（milliseconds）。例如，如果你调用 `delay(1000)`，程序将在该行之后停止执行任何其他代码达1秒钟。这个函数对于实现定时器功能、控制LED闪烁或其他需要等待特定时间段的操作非常有用。

2. **`delayMicroseconds()` 函数**
   ```c++
   void delayMicroseconds(unsigned int microseconds);
   ```
   这个函数与`delay()`类似，但提供了微秒级的延迟精度。它暂停程序执行指定的微秒数。请注意，其精度受限于硬件和系统的计时能力，尤其是在较旧或较低性能的微控制器上。

3. **`micros()` 函数**
   ```c++
   unsigned long micros();
   ```
   这是一个返回自板子启动以来经过的微秒数的函数。每次调用此函数都会得到一个不断递增的值，这对于精确计时或测量短时间间隔很有帮助。

4. **`millis()` 函数**
   ```c++
   unsigned long millis();
   ```
   类似于`micros()`，不过这个函数返回的是自板子启动以来经过的毫秒数。它同样可用于实现更长时间间隔的计时器逻辑。

示例用法：

```c++
unsigned long startTime = millis(); // 记录开始时间

// 执行一些操作...

while (millis() - startTime < 5000) { // 等待5秒
  // 在这里做一些循环内的事情...
}

delayMicroseconds(100); // 延迟100微秒

digitalWrite(pin, HIGH); // 立即设置引脚状态
delay(1000); // 然后延迟1秒
```

在实际项目中，通常会结合使用这些函数来创建复杂的定时任务和周期性动作。







直流电机控制

直流电机在接入

湿度传感器

```c
#icnlude <dht11.h>
// 包含用于操作DHT11温湿度传感器的库文件
#define DHT11_PIN 4
dht11 DHT;
// 声明一个名为DHT的对象，类型为的dht11
void setup() {
    Serial.begin(9600);
}
void loop() {
    int chk;
    chk = DHT.read(DHT11_PIN);
    if(chk == DHTLIB_OK) {
        // DHTLIB_OK为的dht11类中read方法一个返回值
        Serial.print(DHT.humidity, 1);
        // 打印湿度值并保留一位小数
        Serial.print(",\t");
        Serial.println(DHT.temperature, 1);
        // 打印温度值并打印一位小数并换行
    }
    delay(1000);
}
```

