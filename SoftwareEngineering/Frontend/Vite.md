前端修改代理

```ts
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:5288', // 后端地址
        changeOrigin: true,              // 修改请求头中的 origin 为目标地址
        rewrite: (path) => path.replace(/^\/api/, '') // 重写路径
      },
    }
  }
})
```

