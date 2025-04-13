```html
<div class="mb-4 flex items-center">
    <div class="flex-1">
        <label for="captchaInput" class="block text-sm font-bold text-gray-600">验证码</label>
        <input type="text" id="captchaInput" required
               class="mt-1 w-full p-3 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
    </div>
    <div class="ml-4">
        <canvas id="captchaCanvas" width="100" height="40" class="mt-5 border rounded-md cursor-pointer"></canvas>
    </div>
</div>
```

```js
let captchaCode = '';

// 生成验证码
function generateCaptcha() {
const canvas = document.getElementById('captchaCanvas');
const ctx = canvas.getContext('2d');
const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
captchaCode = '';

// 清空画布并绘制背景
ctx.fillStyle = '#f0f0f0';
ctx.fillRect(0, 0, canvas.width, canvas.height);

// 生成随机验证码（4位）
for (let i = 0; i < 4; i++) { const char=chars[Math.floor(Math.random() * chars.length)]; captchaCode +=char;
  ctx.font='20px Arial' ; ctx.fillStyle=`hsl(${Math.random() * 360}, 70%, 50%)`; ctx.fillText(char, 10 + i * 25, 30 +
  (Math.random() * 10 - 5)); } // 添加干扰线 for (let i=0; i < 3; i++) { ctx.beginPath(); ctx.moveTo(Math.random() *
  canvas.width, Math.random() * canvas.height); ctx.lineTo(Math.random() * canvas.width, Math.random() * canvas.height);
  ctx.strokeStyle=`hsl(${Math.random() * 360}, 50%, 50%)`; ctx.stroke(); } } // 点击验证码刷新
  document.addEventListener('DOMContentLoaded', ()=> {
  generateCaptcha();
  document.getElementById('captchaCanvas').addEventListener('click', generateCaptcha);
  });

  // 验证函数（可在表单提交时调用）
  function isCaptchaValid() {
  const input = document.getElementById('captchaInput').value;
  return input.toLowerCase() === captchaCode.toLowerCase();
  }
```

