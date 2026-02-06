import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. 加载 .env 文件里的配置
load_dotenv()

# 2. 获取环境变量
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
model_name = os.getenv("MODEL_NAME", "deepseek-chat")

print(f"正在尝试连接 DeepSeek...")
print(f"API Key: {api_key[:6]}******") # 只打印前几位，确保读到了
print(f"Base URL: {base_url}")

# 3. 初始化客户端
try:
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    # 4. 发送测试消息
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "你好，DeepSeek！请回复一句话证明你在线。"},
        ],
        stream=False
    )

    # 5. 打印结果
    print("\n✅ 连接成功！模型回复如下：")
    print("-" * 30)
    print(response.choices[0].message.content)
    print("-" * 30)

except Exception as e:
    print("\n❌ 连接失败，报错信息如下：")
    print(e)