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

## 镜像管理

通过Dockerfile 构建镜像，写入

```dock
FROM node:14-alpine
# 基础镜像，选择了安装了node的alpine系统

COPY index.js /index.js

CMD node /index.js
```

```powe
docker build -t HelloDocker .
```

```bash
docker images  # List local images of docker
docker rmi <imgage>  # Delete local image
docker pull <image>  # Pull remote image
docker push <image>  # Push local image
```



## 容器管理

```bash
docker run <image>
docker run -it <image> /bin/bash  # Run docker image interactively and enter terminal
docker run -d -p 80:80 <image>  # Port
docker ps
docker ps -a
docker stop <container>
docker start <container>
docker restart <container>
docker rm <container>
docker exec -it <container> /bin/bash
docker logs <container>
```

```bash
docker system prune
docker volume prune
docker image prune
docker container prune
```

