import os
import openai
import json
from flask import Flask,request
import requests
os.environ['OPENAI_API_KEY'] ='你的openAI key'
print(os.getenv('OPENAI_API_KEY'))
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def get_ai_answer(question): #查询OpenAI
	response = json.loads(str(openai.Completion.create(
	  model="text-davinci-003",
	  prompt=question,
	  temperature=0.8,
	  max_tokens=2000,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0
	)))['choices']
	answer=""
	for i in response:
	    answer=answer+i['text']
	return answer
def ding_send(title,message,webhook):
    data={
    "at": {
        "atDingtalkIds":[
        ],
        "isAtAll": 'false'
    },
    "markdown": {
         "title":title,
         "text":message
    },
    "msgtype":"markdown"
    }
    print(data)
    print(requests.post(webhook,json=data).text)

@app.route('/dingrecv',methods=['GET', 'POST']) #回调接口 http://your_ip:8880/dingrecv
def dingrecv():
    if request.method == 'POST':
        req=request.json['text']['content']
        sessionWebhook=request.json['sessionWebhook']
        print(req,sessionWebhook)
        ding_send('正在查询','正在查询关于'+req+'的问题    若30秒无回复请重新发送问题',sessionWebhook)
        ding_send(req,'关于'+req+'的问题结果如下:  '+get_ai_answer(req)+'    如对本次结果不满意可以重新发送问题',sessionWebhook)
    return '1'
app.run(host='0.0.0.0', port=8880, debug=True)
