import base64

import openai
import requests
from flask import render_template, Response, jsonify, request

from .chat import ChatGPT
from .const import API_KEY, CHARACTER_DESC, MAX_TOKEN, MODEL_ENGINE, MODEL
from .image import ImageGPT


def show_chatgpt():
    return render_template('chatgpt.html')


def get_chatgpt_text():
    if request.method == 'POST':
        input_text = request.form.get('input', '')
        obj = ChatGPT()
        output_text = obj.text_reply(input_text)
        return jsonify({'output': output_text})


def show_chatgpt_image():
    return render_template('chatgpt_image.html')


def get_chatgpt_image():
    if request.method == 'POST':
        input_prompt = request.form.get('input_prompt', '')
        select_size = request.form.get('select_size', '1024x1024')
        obj = ImageGPT()
        url = obj.image_reply(input_prompt, size=select_size)
        print(url)
        # 发送 GET 请求获取图片数据
        response = requests.get(url)
        # 将图片数据转换成Base64编码字符串
        image_data = response.content
        base64_data = base64.b64encode(image_data).decode('utf-8')
        # 构造包含Base64编码字符串的JSON响应
        data = {'image': 'data:image/jpeg;base64,' + base64_data}
        return jsonify(data)
