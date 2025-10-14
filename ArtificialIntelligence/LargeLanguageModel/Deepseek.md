Deepseek 官方提供 OpenAI 规范的接口调用。官方接口文档：https://api-docs.deepseek.com/zh-cn/

## 接口文档

DeepSeek API 使用与 OpenAI 兼容的 API 格式，通过修改配置，您可以使用 OpenAI SDK 来访问 DeepSeek API，或使用与 OpenAI API 兼容的软件。

| PARAM      | VALUE                                                          |
| ---------- | -------------------------------------------------------------- |
| base_url * | `https://api.deepseek.com`                                     |
| api_key    | apply for an [API key](https://platform.deepseek.com/api_keys) |

\* 出于与 OpenAI 兼容考虑，您也可以将 `base_url` 设置为 `https://api.deepseek.com/v1` 来使用，但注意，此处 `v1` 与模型版本无关。

\* **`deepseek-chat` 模型指向 DeepSeek-V3-0324，** 通过指定 `model='deepseek-chat'` 调用。

\* **`deepseek-reasoner` 模型指向 DeepSeek-R1-0528，** 通过指定 `model='deepseek-reasoner'` 调用。

### 调用对话 API

在创建 API key 之后，你可以使用以下样例脚本的来访问 DeepSeek API。样例为非流式输出，您可以将 stream 设置为 true 来使用流式输出。

请求格式

```bash
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <API Key>" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {
        "role": "user",
        "content": "请用中文回答：什么是人工智能？"
      }
    ],
    "stream": false
  }'
```

响应格式

```json
{
  "id": "10dad2df-031e-4810-91fe-a87a33284dfe",
  "object": "chat.completion",
  "created": 1745284123,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "人工智能（Artificial Intelligence，简称 AI）是指由人类创造的计算机系统或机器所展现出的智能，能够模拟、延伸或扩展人类的认知能力（如学习、推理、决策、感知等）。其核心目标是让机器执行通常需要人类智能才能完成的任务，甚至在某些领域超越人类的表现。\n\n### 人工智能的关键特点：\n1. **学习能力**  \n   - 通过算法从数据中识别模式并自我改进（如机器学习、深度学习）。\n2. **推理与决策**  \n   - 处理复杂信息并给出逻辑判断（如自动驾驶、医疗诊断）。\n3. **感知与交互**  \n   - 理解图像、语音、文字等（如人脸识别、语音助手）。\n4. **适应性**  \n   - 根据环境变化调整行为（如推荐系统、游戏AI）。\n\n### 主要类型：\n- **弱人工智能（Narrow AI）**  \n  专精于特定任务（如AlphaGo、ChatGPT）。\n- **强人工智能（General AI）**  \n  理论上具备人类水平的通用智能（尚未实现）。\n- **超级智能（Super AI）**  \n  超越人类所有能力的假想形态。\n\n### 应用场景：\n- **日常生活**：智能助手（Siri）、推荐算法（抖音、淘宝）。\n- **行业应用**：金融风控、工业机器人、AI辅助医疗。\n- **前沿领域**：自动驾驶、量子计算辅助AI、脑机接口。\n\n### 争议与挑战：\n- **伦理问题**：隐私、算法偏见、失业风险。\n- **技术瓶颈**：数据依赖、可解释性不足、能耗高。\n\n人工智能正在重塑社会，但其发展需平衡技术创新与人类价值观的约束。"
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 11,
    "completion_tokens": 347,
    "total_tokens": 358,
    "prompt_tokens_details": {
      "cached_tokens": 0
    },
    "prompt_cache_hit_tokens": 0,
    "prompt_cache_miss_tokens": 11
  },
  "system_fingerprint": "fp_3d5141a69a_prod0225"
}
```

流式响应

```json
data: {
    "id":"089ee93b-51e7-4375-a7c9-ccfc4e87aa75",
    "object":"chat.completion.chunk",
    "created":1745284369,
    "model":"deepseek-chat",
    "system_fingerprint":"fp_3d5141a69a_prod0225",
    "choices":[
        {
            "index":0,
            "delta":{
                "role":"assistant",
                "content":""
            },
            "logprobs":null,
            "finish_reason":null
        }
    ]
}

data: {
    "id":"089ee93b-51e7-4375-a7c9-ccfc4e87aa75",
    "object":"chat.completion.chunk",
    "created":1745284369,
    "model":"deepseek-chat",
    "system_fingerprint":"fp_3d5141a69a_prod0225",
    "choices":[
        {
            "index":0,
            "delta":{
                "content":"人工智能"
            },
            "logprobs":null,
            "finish_reason":null
        }
    ]
}

data: {
    "id":"089ee93b-51e7-4375-a7c9-ccfc4e87aa75",
    "object":"chat.completion.chunk",
    "created":1745284369,
    "model":"deepseek-chat",
    "system_fingerprint":"fp_3d5141a69a_prod0225",
    "choices":[
        {
            "index":0,
            "delta":{
                "content":"（"
            },
            "logprobs":null,
            "finish_reason":null
        }
    ]
}

data: {"id":"089ee93b-51e7-4375-a7c9-ccfc4e87aa75","object":"chat.completion.chunk","created":1745284369,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":"Artificial"},"logprobs":null,"finish_reason":null}]}

data: {"id":"089ee93b-51e7-4375-a7c9-ccfc4e87aa75","object":"chat.completion.chunk","created":1745284369,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" Intelligence"},"logprobs":null,"finish_reason":null}]}

data: {"id":"089ee93b-51e7-4375-a7c9-ccfc4e87aa75","object":"chat.completion.chunk","created":1745284369,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":"，"},"logprobs":null,"finish_reason":null}]}

data: {"id":"089ee93b-51e7-4375-a7c9-ccfc4e87aa75","object":"chat.completion.chunk","created":1745284369,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":"简称"},"logprobs":null,"finish_reason":null}]}

data: {"id":"089ee93b-51e7-4375-a7c9-ccfc4e87aa75","object":"chat.completion.chunk","created":1745284369,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" AI"},"logprobs":null,"finish_reason":null}]}

......

data: {
    "id":"089ee93b-51e7-4375-a7c9-ccfc4e87aa75",
    "object":"chat.completion.chunk",
    "created":1745284369,
    "model":"deepseek-chat",
    "system_fingerprint":"fp_3d5141a69a_prod0225",
    "choices":[
        {
            "index":0,
            "delta":{
                "content":""
            },
            "logprobs":null,
            "finish_reason":"stop"
        }
    ],
    "usage":{
        "prompt_tokens":11,
        "completion_tokens":382,
        "total_tokens":393,
        "prompt_tokens_details":{
            "cached_tokens":0
        },
        "prompt_cache_hit_tokens":0,
        "prompt_cache_miss_tokens":11
    }
}

data: [DONE]
```
