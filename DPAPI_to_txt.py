import re
import os
from openai import OpenAI


def sanitize_filename(filename):
    """处理文件名中的非法字符"""
    return re.sub(r'[\\/*?:"<>|]', '', filename)


def save_result(question, reasoning, answer, save_dir=os.path.join(os.path.expanduser("~"), "Documents", "output")):
    """保存结果到文件"""
    os.makedirs(save_dir, exist_ok=True)
    filename = f"{sanitize_filename(question)}.txt"
    file_path = os.path.join(save_dir, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"思考链：\n{reasoning}\n\n答案：\n{answer}")


def call_deepseek_api(question):
    """调用DeepSeek API"""
    try:
        client = OpenAI(api_key="xxx", base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": question}
            ],
            stream=False
        )

        result_content = response.choices[0].message.content
        # 这里简单将结果同时作为思考链和答案，可根据实际调整
        reasoning = result_content
        answer = result_content
        return reasoning, answer

    except Exception as e:
        print(f"API调用失败: {e}")
        return None, None


if __name__ == "__main__":
    question = "如何用Python实现斐波那契数列？"  # 替换为实际问题

    reasoning, answer = call_deepseek_api(question)

    if reasoning and answer:
        save_result(question, reasoning, answer)
        print(f"结果已保存到{os.path.join(os.path.expanduser('~'), 'Documents', 'output', sanitize_filename(question))}.txt")
    else:
        print("处理失败")