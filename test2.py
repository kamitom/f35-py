from openai import OpenAI
import json
client = OpenAI()

prompt = f"""
生成一个由三个虚构的订单信息所组成的列表，以JSON格式进行返回。
JSON列表里的每个元素包含以下信息：
order_id、customer_name、order_item、phone。
所有信息都是字符串。
除了JSON之外，不要输出任何额外的文本。
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
          "role": "user",
          "content": prompt
        }
    ]
)
content = response.choices[0].message.content
print(content)


try:
    data = json.loads(content)
    print(data[0]["customer_name"])
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
except IndexError as e:
    print(f"Index error: {e}")

# json.loads(content)

# json.loads(content)[0]["phone"]
