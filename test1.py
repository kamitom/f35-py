from openai import OpenAI


client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",  # gpt-3.5-turbo gpt-4o-mini
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "我想知道2000年後的世界棒球經典賽的歷年冠軍/亞軍名單以及冠軍賽的舉辦地點體育場館名稱."
        }
    ],
    max_tokens=899
)

print(completion.choices[0].message)
