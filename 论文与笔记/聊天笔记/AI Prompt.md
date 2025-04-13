<!DOCTYPE html>

<html lang="zh-CN">

<head>

  <meta charset="UTF-8">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>智眸精检车辆零部件缺陷检测系统 - AI分析</title>

  <script src="https://cdn.tailwindcss.com"></script>

  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

  <style>

​    .sidebar-button.active {

​      @apply bg-blue-600 text-white;

​    }

​    \#aiResult h1 { font-size: 1.5em; margin-top: 1em; }

​    \#aiResult h2 { font-size: 1.3em; margin-top: 0.8em; }

​    \#aiResult h3 { font-size: 1.1em; margin-top: 0.6em; }

​    \#aiResult ul, #aiResult ol { padding-left: 20px; }

​    \#aiResult pre { 

​      background-color: #f1f1f1; 

​      padding: 10px; 

​      border-radius: 4px; 

​      overflow-x: auto; 

​    }

​    .chart-container {

​      flex: 1;

​      height: 300px;

​      max-width: 30%;

​      display: flex;

​      flex-direction: column;

​      justify-content: flex-start;

​    }

​    .typing-cursor::after {

​      content: "|";

​      animation: blink 1s infinite;

​    }

​    @keyframes blink {

​      0%, 100% { opacity: 1; }

​      50% { opacity: 0; }

​    }

  </style>

</head>

<body class="bg-gray-100 min-h-screen">

  <div class="flex min-h-screen">

​    <aside class="w-40 bg-white shadow-md p-4 flex-shrink-0 relative">

      <div class="mb-6">

​        <h1 class="text-center font-bold text-gray-800">工具栏</h1>

​      </div>

​      <nav class="sticky top-0"></nav>

​      <ul class="space-y-2">

​        <li><a href="index.html" class="block w-full text-left px-4 py-2 hover:bg-blue-50 rounded-md transition-colors flex"><img src="icon/search-for-similar.png" alt="" class="w-6 h-6 mr-2"> 图片检测</a></li>

​        <li><a href="video.html" class="block w-full text-left px-4 py-2 hover:bg-blue-50 rounded-md transition-colors flex"><img src="icon/video.png" alt="" class="w-6 h-6 mr-2"> 视频检测</a></li>

​        <li><a href="data.html" class="block w-full text-left px-4 py-2 hover:bg-blue-50 rounded-md transition-colors flex"><img src="icon/charts-bar.png" alt="" class="w-6 h-6 mr-2"> 数据查询</a></li>

​        <li><a href="data-vis.html" class="block w-full text-left px-4 py-2 hover:bg-blue-50 rounded-md transition-colors flex"><img src="icon/charts-pie.png" alt="" class="w-6 h-6 mr-2"> 可视化</a></li>

​        <li><a href="ai-analysis.html" class="block w-full text-left px-4 py-2 hover:bg-blue-50 rounded-md transition-colors flex"><img src="icon/atm.png" alt="" class="w-6 h-6 mr-2"> AI 分析</a></li>

​        <li><hr class="my-2 border-t-2 border-gray-200 w-28 mx-auto"></li>

​        <li><a href="console.html" class="block w-full text-left px-4 py-2 hover:bg-blue-50 rounded-md transition-colors flex"><img src="icon/calculator.png" alt="" class="w-6 h-6 mr-2"> 控制台</a></li>

​        <li><a href="settings.html" class="block w-full text-left px-4 py-2 hover:bg-blue-50 rounded-md transition-colors flex"><img src="icon/code.png" alt="" class="w-6 h-6 mr-2"> 设置</a></li>

​      </ul>

      <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 text-center w-full p-4">

​        <img src="icon/sdd-logo.png" class="w-16 mx-auto mb-4 opacity-75">

        <p class="text-xs text-gray-500">汽车零部件检测系统 v2.1.0</p>

​      </div>

​    </aside>



    <div class="flex-1 p-4">

​      <h2 class="text-center text-2xl font-semibold mb-5">AI 分析缺陷数据</h2>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

        <div class="lg:col-span-2 bg-white rounded-xl shadow-md p-6">

          <div class="mb-4">

​            <label for="promptInput" class="block text-sm font-medium text-gray-700">输入你的分析请求</label>

​            <textarea class="mt-1 w-full p-3 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"

​                      id="promptInput" rows="4" placeholder="例如：请分析最近一周的缺陷数据趋势..."></textarea>

​          </div>

          <div class="flex space-x-2">

​            <button id="analyzeButton" class="flex-1 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition duration-300"

​                    onclick="analyzeData()">提交给 AI</button>

​            <button id="stopButton" class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700 transition duration-300 hidden"

​                    onclick="stopAnalysis()">停止生成</button>

​          </div>

          <div class="mt-5">

​            <h4 class="text-lg font-medium">分析结果</h4>

            <div id="aiResult" class="p-3 bg-gray-50 border rounded-md h-48 overflow-y-auto">

              <div id="aiContent"></div>

              <div id="typingIndicator" class="typing-cursor hidden"></div>

​            </div>

​          </div>

​          

​          <!-- Status -->

          <div id="status" class="mt-4 text-sm text-gray-500"></div>

​        </div>



​        <!-- Data review -->

        <div class="bg-white rounded-xl shadow-md p-6">

​          <h4 class="text-lg font-medium mb-4">近期数据概览</h4>

          <div class="space-y-4">

            <div class="chart-container">

​              <canvas id="quickLabelChart"></canvas>

​            </div>

            <div class="chart-container">

​              <canvas id="quickTimeChart"></canvas>

​            </div>

​          </div>

​          <button class="mt-4 w-full bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300 transition duration-300"

​                  onclick="fetchQuickData()">刷新概览数据</button>

​        </div>

​      </div>

​    </div>

  </div>



  <script src="../renderer/ai-analysis.js"></script>

</body>

</html>const analyzeButton = document.getElementById('analyzeButton');

const stopButton = document.getElementById('stopButton');

const promptInput = document.getElementById('promptInput');

const aiContent = document.getElementById('aiContent');

const typingIndicator = document.getElementById('typingIndicator');

const statusDiv = document.getElementById('status');

let quickLabelChart, quickTimeChart;

let abortController = null;

let isStreaming = false;



marked.setOptions({

​    breaks: true,

​    gfm: true

});



async function analyzeData() {

​    const prompt = promptInput.value.trim();

​    if (!prompt) {

​        showStatus('请输入分析请求', 'error');

​        return;

​    }



​    aiContent.innerHTML = '';

​    typingIndicator.classList.remove('hidden');

​    showStatus('AI 正在分析中...', 'processing');

​    analyzeButton.disabled = true;

​    stopButton.classList.remove('hidden');

​    isStreaming = true;

​    abortController = new AbortController();



​    try {

​        const context = await getDataContext();



​        const fullPrompt = buildFullPrompt(prompt, context);



​        await callAIStreaming(fullPrompt);



​        showStatus('分析完成！', 'success');

​    } catch (error) {

​        if (error.name !== 'AbortError') {

​            console.error('AI分析错误:', error);

​            showStatus(`错误: ${error.message}`, 'error');

​            aiContent.innerHTML = marked.parse('**分析过程中发生错误，请稍后重试。**');

​        } else {

​            showStatus('已停止生成', 'warning');

​        }

​    } finally {

​        typingIndicator.classList.add('hidden');

​        analyzeButton.disabled = false;

​        stopButton.classList.add('hidden');

​        isStreaming = false;

​        abortController = null;

​    }

}



function stopAnalysis() {

​    if (isStreaming && abortController) {

​        abortController.abort();

​    }

}



async function callAIStreaming(prompt) {

​    const response = await fetch('https://api.deepseek.com/chat/completions', {

​        method: 'POST',

​        headers: {

​            'Content-Type': 'application/json',

​            'Authorization': 'Bearer ' + getApiKey()

​        },

​        body: JSON.stringify({

​            model: 'deepseek-chat',

​            messages: [{ role: 'user', content: prompt }],

​            stream: true

​        }),

​        signal: abortController?.signal

​    });



​    if (!response.ok) {

​        const errorText = await response.text();

​        throw new Error(`AI 请求失败: ${response.status} - ${errorText}`);

​    }



​    const reader = response.body.getReader();

​    const decoder = new TextDecoder('utf-8');

​    let result = '';



​    while (isStreaming) {

​        const { done, value } = await reader.read();

​        if (done) break;



​        const chunk = decoder.decode(value, { stream: true });

​        const lines = chunk.split('\n');



​        for (const line of lines) {

​            if (line.startsWith('data: ')) {

​                const data = line.slice(6);

​                if (data === '[DONE]') continue;



​                try {

​                    const parsed = JSON.parse(data);

​                    const content = parsed.choices[0]?.delta?.content || '';



​                    if (content) {

​                        result += content;

​                        aiContent.innerHTML = marked.parse(result);

​                        // 自动滚动到底部

​                        aiContent.scrollIntoView({ behavior: 'smooth', block: 'end' });

​                    }

​                } catch (e) {

​                    console.error('解析错误:', e);

​                }

​            }

​        }

​    }

}



function buildFullPrompt(userPrompt, context) {

​    // 基础系统提示

​    let prompt = `你是一个钢材缺陷分析专家，请根据用户请求分析钢材缺陷数据。\n\n`;



​    // 添加数据上下文

​    if (context) {

​        prompt += `当前数据概况:\n`;

​        prompt += `- 总检测样本数: ${context.totalSamples}\n`;

​        prompt += `- 主要缺陷类型: ${context.mainDefects.join(', ')}\n`;

​        prompt += `- 平均检测时间: ${context.avgDetectionTime}秒\n\n`;

​    }



​    // 添加用户请求

​    prompt += `用户请求:\n${userPrompt}\n\n`;

​    prompt += `请用专业但易懂的语言回答，使用Markdown格式，包含以下部分:\n`;

​    prompt += `1. 主要发现\n2. 趋势分析\n3. 改进建议`;



​    return prompt;

}



function getApiKey() {

​    return localStorage.getItem('ai_api_key') || 'sk-c6c11ae0a25a4e1ea64ff97e98d4057a';

}



function showStatus(message, type = 'info') {

​    statusDiv.textContent = message;

​    statusDiv.className = 'mt-4 text-sm ' +

​        (type === 'error' ? 'text-red-500' :

​            type === 'success' ? 'text-green-500' :

​                type === 'warning' ? 'text-yellow-500' :

​                    'text-gray-500');

}



async function fetchQuickData() {

​    try {

​        const response = await fetch('http://localhost:8080/api/data/getRecent');

​        if (!response.ok) throw new Error('获取数据失败');

​        const data = await response.json();

​        console.log('获取到的数据:', data);

​    

​    } catch (error) {

​        console.error('获取数据错误:', error);

​        showStatus('获取数据失败，请稍后重试。', 'error');

​    }

}



// 页面加载时初始化

document.addEventListener('DOMContentLoaded', () => {

​    fetchQuickData();



​    // 示例提示词

​    promptInput.value = "请分析最近一周的缺陷数据，指出主要问题类型和变化趋势，并提出改进建议。";



​    // 初始化Marked.js渲染器

​    const renderer = new marked.Renderer();

​    renderer.code = (code, language) => {

​        return `<pre><code class="language-${language}">${code}</code></pre>`;

​    };

​    marked.setOptions({ renderer });

});取最近数据，然后发送给AI，记得稍微在旁边添点信息和图表，> % curl http://localhost:8080/api/data/getRecent\?limit\=10 | jq

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current

​                                 Dload  Upload   Total   Spent    Left  Speed

100  1221    0  1221    0     0   113k      0 --:--:-- --:--:-- --:--:--  119k

[

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "1.90",

​    "label": "[False False  True False]",

​    "num": "1",

​    "dice": null

  },

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "1.91",

​    "label": "[False False  True False]",

​    "num": "1",

​    "dice": null

  },

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "0.08",

​    "label": "[ True False False False]",

​    "num": "1",

​    "dice": null

  },

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "0.08",

​    "label": "[False False  True False]",

​    "num": "1",

​    "dice": null

  },

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "0.08",

​    "label": "[False False  True False]",

​    "num": "1",

​    "dice": null

  },

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "0.08",

​    "label": "[False False False False]",

​    "num": "0",

​    "dice": null

  },

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "0.08",

​    "label": "[False False  True False]",

​    "num": "1",

​    "dice": null

  },

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "0.08",

​    "label": "[False False  True False]",

​    "num": "1",

​    "dice": null

  },

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "0.08",

​    "label": "[False False  True False]",

​    "num": "1",

​    "dice": null

  },

  {

​    "figId": 0,

​    "name": null,

​    "resFig": null,

​    "date": null,

​    "time": "0.08",

​    "label": "[ True False  True False]",

​    "num": "0",

​    "dice": null

  }

]

cacc@paradiso [03:30:14 PM] [~/Documents/Journals/logs] [PAR *]

-> % 

记得要先解析一下标签字符串function parseLabel(labelStr) {

```js
function parseLabel(labelStr) {
    try {
        const defectDict = ["夹杂物", "补丁", "划痕", "其他"];

        const boolArray = labelStr.replace(/\[|\]/g, '').trim().split(/\s+/).map(v => v.toLowerCase() === 'true');
        const labels = boolArray.map((val, index) => val ? defectDict[index] : null).filter(v => v !== null);

        return labels.map(label => {
            const index = defectDict.indexOf(label);
            return { label};
        });
    } catch (e) {
        return [{ label: '解析错误'}];
    }
}
```



