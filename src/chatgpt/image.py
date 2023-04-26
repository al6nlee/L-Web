import os
import time

import openai
import requests

from src.chatgpt.chat import GPT


class ImageGPT(GPT):
    def __init__(self):
        super(ImageGPT, self).__init__()

    def image_reply(self, input_prompt, size="1024x1024"):
        response = openai.Image.create(
            prompt=input_prompt,
            n=1,
            size=size
        )
        data = response.data
        url = data[0].get("url") if data else ""
        return url

    def export_image(self, input_prompt, size="1024x1024"):
        url = self.image_reply(input_prompt, size=size)
        print(url)
        st = time.time()
        if not os.path.exists("temp"):
            os.mkdir("temp")
        filename = f'temp/image_{st}.jpg'  # 文件名以.jpg结尾
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'{filename} saved successfully.')
        else:
            print(f'Failed to download {url}')

    def get_image(self):
        pass

    def edit_image(self, input_prompt, size="1024x1024"):
        pass


if __name__ == '__main__':

    while True:
        # 获取用户的输入
        user_input = input("图片描述>>>")
        size = input("图片尺寸>>>")
        obj = ImageGPT()
        msg = obj.export_image(user_input)
