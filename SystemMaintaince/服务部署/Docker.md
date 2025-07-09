## 安装docker

```bash
sudo apt install docker docker-compose
```





# Docker 使用说明

通过指令检查docker是否安装成功

```bash
docker version
# 出现client则说明安装成功
# 出现server则说明正在运行 
```

## 创建Dockerfile

写入

```dock
FROM node:14-alpine
# 基础镜像，选择了安装了node的alpine系统

COPY index.js /index.js

CMD node /index.js
```

```powe
docker build -t HelloDocker .
```



