<p align="center">
	<img alt="logo" src="favicon.png">
</p>
<h1 align="center" style="margin: 30px 0 30px; font-weight: bold;">openai v0.0.1</h1>
<h4 align="center">AI大模型生产接口</h4>
<p align="center">
	<a href="https://gitee.com/webusi/openai/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"></a>
</p>

## 平台简介

白嫖生产AI大模型，让开发调测更逼真。<p/>


已支持大模型：
百度AI大模型-DeepSeek-R1

技术栈<br>
* 前端采用Python3.9、Flask。

## 团队产品
https://www.webusi.net

## 使用方法
前提条件：已安装python3.9+

git clone https://gitee.com/webusi/openai.git <br>
cd openai <br>
python -m venv openai <br>
source openai/bin/activate <br>
pip install -r requirements.txt <br>
python api.py <br>

启动结果：<br>
 * Running on http://127.0.0.1:5000 <br>

调用接口：<br>
curl --location --request POST 'http://127.0.0.1:5000/ai' \ <br>
--header 'Content-Type: application/json' \ <br>
--data-raw '{"text": "查询今年参加高考人数，只需要输出文本"}' <br>

## 微信交流
<tr>
    <td><img width="200" height="200" src="code.png"/></td>
</tr>

## 更新日志
### 0.0.1 2025-10-08
1.  百度AI大模型: DeepSeek-R1
