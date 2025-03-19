""" # Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="xxx", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    # model="deepseek-reasoner",   #深度推理模型R1
    model="deepseek-chat",         #聊天模型V3
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "请列举孔子和耶稣谁活的时间长Hello"},
    ],
    stream=False   #不支持流式输出
)

print(response.choices[0].message.content) """

### 更新版


from openai import OpenAI

client = OpenAI(api_key="API key", base_url="https://api.deepseek.com")

# 创建流式响应
response = client.chat.completions.create(
    # model="deepseek-reasoner",   # 深度推理模型R1
    model="deepseek-chat",         # 聊天模型V3
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "请列举孔子和耶稣谁活的时间长Hello"},
    ],
    stream=True  # 开启流式输出
)

# 逐块处理流式响应
for chunk in response:
    # 检查当前块是否包含消息内容
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)

# 打印换行符，使输出格式更美观
print()
