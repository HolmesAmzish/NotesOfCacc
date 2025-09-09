# Vite

## 创建项目

```bash
npm create vite
```

随后输入设置





## 项目设置

vite.config.ts

前端修改代理，通过将

```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server:{
    proxy:{
      '/api':{
        target:'http://localhost:8080',
        changeOrigin: true,
        rewrite: (path) => path,
      }
    }
  }
})

```

