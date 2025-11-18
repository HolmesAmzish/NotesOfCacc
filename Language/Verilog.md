## 数值表示

Verilog HDL有四种基本值来表示硬件电路中的电平逻辑：

- 0：逻辑 0 或 "假"
- 1：逻辑 1 或 "真"
- x 或 X：未知
- z 或 Z：高阻

**x** 意味着信号数值的不确定，即在实际电路里，信号可能为 1，也可能为 0。

**z** 意味着信号处于高阻状态，常见于信号（input, reg）没有驱动时的逻辑结果。例如一个 pad 的 input 呈现高阻状态时，其逻辑值和上下拉的状态有关系。上拉则逻辑值为 1，下拉则为 0 。

### 整数数值表示方法

数字声明时，合法的基数格式有 4 中，包括：十进制('d 或 'D)，十六进制('h 或 'H)，二进制（'b 或 'B），八进制（'o 或 'O）。数值可指明位宽，也可不指明位宽。

**指明位宽：**

``` verilog
4'b1011     *// 4bit 数值*
32'h3022_c0de  *// 32bit 的数值*
```
其中，下划线 **_** 是为了增强代码的可读性。

**不指明位宽:**

一般直接写数字时，默认为十进制表示，例如下面的 3 种写法是等效的：

```verilog
counter = 'd100 ; *//一般会根据编译器自动分频位宽，常见的为32bit*
counter = 100 ;
counter = 32'h64 ;
```
**负数表示**

通常在表示位宽的数字前面加一个减号来表示负数。例如：

```
-6'd15  
-15
```

### 字符串表示方法

字符串是由双引号包起来的字符队列。字符串不能多行书写，即字符串中不能包含回车符。Verilog 将字符串当做一系列的单字节 ASCII 字符队列。例如，为存储字符串 "www.runoob.com", 需要 14*8bit 的存储单元。例如：

```verilog
reg [0: 14*8-1] str ;
initial begin
  str = "www.runoob.com";
end
```



## Verilog 数据类型

### 线网（wire）

wire 类型表示硬件单元之间的物理连线，由其连接的器件输出端连续驱动。如果没有驱动元件连接到 wire 型变量，缺省值一般为 "Z"。举例如下：

```verilog
wire   interrupt ;
wire   flag1, flag2 ;
wire   gnd = 1'b0 ;  
```

### 寄存器（reg）

寄存器（reg）用来表示存储单元，它会保持数据原有的值，直到被改写。声明举例如下：

```verilog
reg    clk_temp;
reg    flag1, flag2 ;
```

例如在 always 块中，寄存器可能被综合成边沿触发器，在组合逻辑中可能被综合成 wire 型变量。寄存器不需要驱动源，也不一定需要时钟信号。在仿真时，寄存器的值可在任意时刻通过赋值操作进行改写。例如：

```verilog
reg rstn ;
initial begin
    rstn = 1'b0 ;
    #100 ;
    rstn = 1'b1 ;
end
```



使用Verilog HDL描述如下所示四旋翼多路选择器mux4to1。其中输入a,b,c,d,s1,s0和输出y的对应关系如下：

| s1   | s0   | y    |
| ---- | ---- | ---- |
| 0    | 0    | a    |
| 0    | 1    | b    |
| 1    | 0    | c    |
| 1    | 1    | d    |

```verilog
module mux4to1 (
    input a,          // 输入a
    input b,          // 输入b
    input c,          // 输入c
    input d,          // 输入d
    input s1,         // 选择信号s1
    input s0,         // 选择信号s0
    output reg y      // 输出y
);

always @(*) begin
    case ({s1, s0})
        2'b00: y = a;  // 当s1=0, s0=0时，输出a
        2'b01: y = b;  // 当s1=0, s0=1时，输出b
        2'b10: y = c;  // 当s1=1, s0=0时，输出c
        2'b11: y = d;  // 当s1=1, s0=1时，输出d
        default: y = 1'b0; // 默认值
    endcase
end

endmodule
```



使用Verilog HDL描述一个16 bits宽的9选1多路选择器Mux, sel=0选择a进行输出，sel=1选择b输出，......，sel=9选择i进行输出，其他的sel取值，输出的所有位都置为1。请补充完整如下的设计代码。

```verilog
module top_module(
    input [15:0] a, b, c, d, e, f, g, h, i,
    input [3:0] sel,
    output reg [15:0] out
);
    
always @(*) begin
    case (sel)
        4'd0: out = a;
       	4'd1: out = b;
  		4'd2: out = c;
       	4'd3: out = d;
       	4'd4: out = e;
       	4'd5: out = f;
       	4'd6: out = g;
       	4'd7: out = h;
    	4'd8: out = i;
        default: out = 16'hFFFF
    endcase
end
           
endmodule
```



创建一 Verilog 模块，将 16bit 输入信号 in 分成两个 8bit 的信号 out_hi、out_lo，然后输出。输入格式: 输入信号 in, 位宽 16bit，类型为 wire。输出格式: 输出信号 out_hi，位宽 8bit，为输入信号的高 8 位。 输出信号 out_lo，位宽 8bit，为输入信号的低 8 位。

![img](https://p.ananas.chaoxing.com/star3/origin/bc90dfbc50515759bdbdf37da38c4cc1.png)

```verilog
module top_module( 
    input wire [15:0] in,
    output wire [7:0] out_hi,
    output wire [7:0] out_lo 
);

assign out_hi = in[15:8];
assign out_lo = in[7:0];

endmodule
```



![img](https://p.ananas.chaoxing.com/star3/origin/bab1e59256f4c47dd15aa94b277422de.png)

```verilog
module top_module( 
    input [2:0] a,
    input [2:0] b,
    output [2:0] out_or_bitwise,
    output out_or_logical,
    output [5:0] out_not
);

	assign out_or_bitwise = a | b;
	assign out_or_logical = |a || |b;
	assign out_not = ~{a, b};

endmodule
```



![img](https://p.ananas.chaoxing.com/star3/origin/33f1e7a8e999479689af270a715a4efe.png)

```verilog
module top_module( 
    input [3:0] in,
    output out_and,
    output out_or,
    output out_xor
);

assign out_and = in[3] & in[2] & in[1] & in[0];
assign out_or = in[3] | in[2] | in[1] | in[0];
assign out_xor = in[3] ^ in[2] ^ in[1] ^ in[0];

endmodule
```



```verilog
module top_module ( input clk, input[7:0] d, input [1:0] s, output []7:0] q );
    wire [7:0]  w1,w2,w3;
    my_dff8   inst1(clk,d,w1);
    my_dff8   inst2(clk,w1,w2);
    my_dff8   inst3(clk,w2,w3);
    mux4to1  inst4(d,w1,w2,w3,s,q);
endmodule
```

![verilog.PNG](https://p.ananas.chaoxing.com/star3/origin/bf2109e0d5bdaf0af82dbafef9ceb3b7.PNG)

```verilog
module  circuit1(input A, B, C, output F);
    wire P1,P2,P3,P4,P5;
    assign P1 = ~A;
    assign P2 = B | C;
    assign P3 = ~(B & C);
    assign P4 = ~(P1 & P2);
    assign P5 = ~(A & P3);
    assign F = ~(P4 & P5);
endmodule
```

![wavedrom (1).png](https://p.ananas.chaoxing.com/star3/origin/2d61fff532a00daedc5e561bbbff3cc9.png)

```verilog
module top_module (
	input clk,
    input reset,
    output [3:0] q
);
    always @(posedge clk, posedge reset)
        if (reset)
            q <= 4'd1;
    	else
            if (q == 4'd5)
                q <= 4'd1;
    		else
                q <= q + 1;
endmodule
```

![wavedrom.png](https://p.ananas.chaoxing.com/star3/origin/052e2822b3f4d169eb6bc83c2998b391.png)

```verilog
module top_module (
	input clk,
    input reset,
    output reg [3:0] q
);
    reg [3:0] cnt;
    always @(posedge clk, posedge reset) begin
        if (reset) cnt <= 4'd0;
        else cnt <= cnt + 1;
    end
    assign q = cnt;
endmodule
```

![gate_dff.png](https://p.ananas.chaoxing.com/star3/origin/61f1bdf8a0e557cb07c97c6e745bc08c.png)

```verilog
module top_module (
	input clk,
    input in,
    output out
);
    always @ (posedge clk) begin
        out = in ^ out;
    end
endmodule
```

![img](https://p.ananas.chaoxing.com/star3/origin/b90435de86f97fae63ecbf8ba61f1b67.png)

```verilog
module snailController(

  input clk,      // 时钟输入信号
  input rst,      // 异步复位输入信号，高电平复位
  input code,     // 爬过的纸带上符号，0 或者 1
  output reg smile  // 蜗牛是否微笑
);

  // 状态编码常量 S0~S4
  parameter S0 = 3'b000;
  parameter S1 = 3'b001;
  parameter S2 = 3'b010;
  parameter S3 = 3'b011;
  parameter S4 = 3'b100;

  // 现态、次态变量
  reg [2:0] state, nextstate;

  // (1) 状态寄存器时序逻辑描述
  always @(posedge clk or posedge rst) begin
    if (rst) 
      state <= S0;
    else
      state <= nextstate;
  end

  // (2) 次态生成电路的组合逻辑描述
  always @(*) begin
    case (state)
      S0: nextstate = code ? S1 : S0;
      S1: nextstate = code ? S2 : S0;
      S2: nextstate = code ? S3 : S0;
      S3: nextstate = code ? S4 : S0;
      S4: nextstate = code ? S2 : S0;
      default: nextstate = S0;
    endcase
  end

  // (3) 输出电路的组合逻辑描述
  always @(posedge clk or posedge rst) begin
    if (rst)
      smile <= 0;
    else
      smile <= (state == S4 && !code);
  end

endmodule
```

```verilog
module MotorFire(input clock, input reset, input X, output Z);
    reg [2:0] state, nextstate;
    
    parameter S0 = 2'b00;
    parameter S1 = 2'b01;
    parameter S2 = 2'b10;
    parameter S3 = 2'b11;
    
    always @ (posedge clock, posedge reset)
        if (reset) state <= S0;
   		else state <= nextstate;
    always @ (*)
        case(state)
            S0: nextstate = X ? S1 : S0;
            S1: nextstate = X ? S0 : S2;
            S2: nextstate = X ? S0 : S3;
            S3: nextstate = S0;
        endcase
    assign Z = (state == S3 && X == 1);
endmodule
```

