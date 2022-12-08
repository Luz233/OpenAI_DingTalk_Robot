# OpenAI_DingTalk_Robot 一个简单的基于OpenAI的钉钉机器人
## 使用条件
1. 拥有一个公网服务器，或拥有公网地址（含映射）的PC，供钉钉机器人收到消息后回调
2. 拥有一个OpenAI的账号，并且获取key
3. 创建一个带交互功能的钉钉机器人

## 使用方式
1. 安装OpenAI相关的python环境，OpenAI官网有说明
2. 修改程序中的 os.environ['OPENAI_API_KEY'] ='你的openAI key' ，填写自己的key
3. 修改钉钉机器人的HTTP回调地址为http://你的服务器IP:8880/dingrecv
4. 发送测试消息

## 模型及参数修改
1. 可以从OpenAI官网测试其他模型与参数的效果，并修改响应代码

## 测试效果
![c537770fd826c879018b1542b10dbdf](https://user-images.githubusercontent.com/58980928/206437335-beff885a-e167-472f-a2ff-8b0c779f762e.jpg)
![bbbba9c263da2671ee943885b125a7a](https://user-images.githubusercontent.com/58980928/206437756-8f7231c0-d62b-4ca6-afd9-cd88149b11a3.jpg)

