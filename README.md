# Sentry 告警通知
sentry 告警通知到 telegram 的插件不维护了，所以自己写了个。

原理是读取 sentry 的 json 格式告警数据，发送到 telegram。

## telegram token 申请
省略，可自行寻找方法。
## 启动
### 方法1:直接运行
**安装依赖**

`pip3 install -r requirements.txt`

**启动**

`python3 main.py`

### 方法2:使用 docker
```
docker build -t sentry-tg:v1.0 .

docker run -tid --restart=always -p 8000:8000 sentry-tg:v1.0
```

## sentry 配置

1. 创建一个 webhooks，按下图所示填写

![img_1.png](docs%2Fimages%2Fimg_1.png)

2. 配置告警条件，然后选择通知到配置的 webhooks 

## 效果
![img_4.png](docs%2Fimages%2Fimg_4.png)
