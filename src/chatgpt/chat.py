import openai

from src.chatgpt.const import API_KEY, CHARACTER_DESC, MAX_TOKEN, MODEL_ENGINE, MODEL


class GPT(object):
    openai.api_key = API_KEY

    def __init__(self):
        self.api_key = API_KEY
        self.character_desc = CHARACTER_DESC
        self.max_token = MAX_TOKEN
        self.model_engine = MODEL_ENGINE
        self.model = MODEL

    def get(self):
        pass
class ChatGPT(GPT):
    def __init__(self):
        super(ChatGPT, self).__init__()

    def text_reply(self, input_prompt):
        # 生成机器人的响应
        response = openai.ChatCompletion.create(
            model=self.model,
            max_tokens=self.max_token,
            messages=[
                {"role": "user", "content": input_prompt}
            ]
        )
        message = response.choices[0].message.content
        return message


if __name__ == '__main__':

    while True:
        # 获取用户的输入
        user_input = input(">>>")
        obj = ChatGPT()
        msg = obj.text_reply(user_input)
        print(msg)
