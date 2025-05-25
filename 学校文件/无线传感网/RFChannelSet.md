---
title: 无线传感网 第五次实验 无线信道的设置
date: 2025-05-17
---

# 无线传感网 第五次实验报告

## 一、实验目的

1. 学习 CC2430 无线发射信道设置的方法; 
2. 了解 IEEE802.15.4 协议。

## 二、实验内容

修改程序以完成一下功能：

1. 发送端增加输入对方地址和要修改的无线信道号；发送后修改自己的无线信道并显示确认；
2. 接受端加入显示对方地址、对方要求修改的信道号；接收后修改自己的无线信道并显示确认；

## 三、实验程序

原程序 `SetRFChannelM.nc`

```c
/*************************************************
*	FUNCTION NAME : SetRFChannelM.nc
*	FUNCTION DESCRIPTION : 发射信道设备
*	FUCNTION DATE :2010/10/19
*	FUNCTION AUTHOR: EMDOOR
**/

#define DBG_LEV 1000

module SetRFChannelM
{
	uses {
		interface Boot;
		interface StdControl as UartStdControl;
		interface UartStream;		
		interface AMSend;
		interface Receive;
		interface Packet;
		interface AMPacket;
		interface CC2420Config;
		interface SplitControl as RFControl;
		interface Leds;
	}
}

implementation
{	
	enum
	{
		MAX_CHANNEL = 26,
		MIN_CHANNEL = 11,
		MAX_CHANNEL_LEN = 2,
		INPUT_CHOICE = 0,
		INPUT_CHANNEL = 1,
	};

	message_t msg;
	uint16_t count = 0;	
	char m_channel_str[MAX_CHANNEL_LEN] = {0};
	uint8_t m_channel_index = 0;
	uint8_t m_input_type = 0;
	bool choice = FALSE;

	task void sendData();

	/*显示菜单*/
	task void showMenu()
	{
		if(m_input_type == INPUT_CHANNEL)
		{/*等待输入频道值*/
			ADBG(DBG_LEV, "\r\n* Input new channel(valid range:11~26):\r\n");
			m_channel_index = 0;
		}
		else
		{/*选择是否改变频道*/
			ADBG(DBG_LEV, "\r\n#########################################################\r\n* MY nodeId = 0x%x, GROUP = 0x%x,  Current Channel = %d, set channel ?(Y/N)\r\n",
				ADBG_N(call AMPacket.address()),
				ADBG_N(TOS_IEEE_PANID),
				ADBG_N(call CC2420Config.getChannel())
			);

			m_input_type = INPUT_CHOICE;
			choice = FALSE;
		}
	}

	uint8_t getChannel()
	{
		uint16_t channel = 0;
		uint16_t i = 0;
		
		if(m_channel_index > MAX_CHANNEL_LEN)
		{
			m_channel_index = MAX_CHANNEL_LEN -1;
		}

		for ( i=0; i < m_channel_index; ++i)
		{
			uint8_t digital = m_channel_str[i];
			
			if(digital >= '0' && digital <= '9')
			{
				digital = digital - '0';
			}

			channel = channel*10 +digital;
		}

		return channel;
	}
		

	task void setChannel()
	{
		uint8_t channel;
		channel = getChannel();
		if(channel >= 11  && channel <= 26)
		{			
			call CC2420Config.setChannel(channel);
			if(call AMPacket.address() !=1)
			{
				post sendData();
			}
			else
			{
				post showMenu();
				m_input_type = INPUT_CHOICE;
			}
			ADBG(DBG_LEV, "\r\n**Set Channel OK!\r\n");
		}
		else
		{
			ADBG(DBG_LEV, "\r\nInvalid Channel input\r\n");
			post showMenu();
		}
	}

	task void sendData()
	{
		uint8_t i;
		uint8_t* payload = call Packet.getPayload(&msg, NULL);
		uint16_t address = call AMPacket.address();
		uint16_t dest_address = 1;

		count++;

		payload[0] = count;
		payload[1] = count >> 8;

		ADBG( DBG_LEV, "\r\n\r\n* Sending ... from [%d], to [%d], len=[%d]\r\n",
			ADBG_N(address),
			ADBG_N(dest_address),
			ADBG_N(sizeof(count))
		);

		call AMSend.send(dest_address, &msg, sizeof(count));

		call Leds.BlueLedToggle();
	}

	/*发送完处理*/
	event void AMSend.sendDone(message_t* msg, error_t success)
	{
		ADBG(DBG_LEV, "* Sent%s!\r\n", (success == SUCCESS) ? "OK" : "FAIL");		

		m_input_type = INPUT_CHOICE;

		post showMenu();
	}



	/*从串口接收数*/
	async event void UartStream.receivedByte(uint8_t c)
	{
		if(c != '\r')
		{
			if(m_input_type == INPUT_CHOICE)
			{/*输入选择*/
				ADBG(DBG_LEV, "%c", c);
				
				if(c == 'Y' || c == 'y')
				{
					choice = TRUE;
					return;
				}
				else if(c == 'N' || c== 'n')
				{
					post sendData();
					return;
				}
				else
				{
					ADBG(DBG_LEV, "\r\n invalid input!!\r\n");					
					post showMenu();
					return;
				}
			}
			else
			{/*输入频道值*/
				if(m_channel_index < MAX_CHANNEL_LEN)
				{
					m_channel_str[m_channel_index++] = c;
					ADBG(DBG_LEV, "%c", c);
				}

				if(m_channel_index < MAX_CHANNEL_LEN)
				{
					return;
				}
			}
		}

		if(m_input_type == INPUT_CHANNEL)
		{
			post setChannel();
		}
		else 
		{
			if(choice ==TRUE) {
				m_input_type = INPUT_CHANNEL;
				post showMenu();	
			}
			return;
		}
		
	}
		
	/*节点启动*/
	event void Boot.booted()
	{	
		/*开启射频*/
		call RFControl.start();

		/*开启串口通信*/
		call UartStdControl.start();

		call Leds.YellowLedOff();
		call Leds.BlueLedOff();

		ADBG(DBG_LEV, "\r\n#####################################################\r\n");
		ADBG(DBG_LEV, "   [SETRFCHANNEL DEMO] My Address = 0x%x, Group = 0x%x\r\n", ADBG_N(call AMPacket.address()), ADBG_N(TOS_IEEE_PANID));
		ADBG(DBG_LEV, "#####################################################\r\n");

		m_input_type = INPUT_CHOICE;
		post showMenu();
	}

	/** 实现接口RFControl 接口中的事件*/
	event void RFControl.startDone(error_t result)
	{
	}

	event void RFControl.stopDone(error_t result)
	{
	}

	/** 实现接口UartStream 接口中的事件*/
	async event void UartStream.sendDone(uint8_t* buf, uint16_t len, error_t error)
	{		
	}

	async event void UartStream.receiveDone(uint8_t* buf, uint16_t len, error_t error)
	{
	}

	event void CC2420Config.syncDone(error_t err)
	{
	}

	/*射频接收数据*/
	event message_t* Receive.receive(message_t* msg, void* payload, uint8_t len)
	{
		uint8_t i;
		ADBG(DBG_LEV, "\r\n*Receive, len = [%d]\r\n", ADBG_N(len));
		
		call Leds.YellowLedToggle();

		m_input_type = INPUT_CHOICE;

		post showMenu();
	}
}
```



## 四、结论

