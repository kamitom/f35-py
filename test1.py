from openai import OpenAI


client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",  # gpt-3.5-turbo gpt-4o-mini
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "我想知道2000年後的世界杯足球賽的歷年冠軍名單."
        }
    ],
    max_tokens=500
)

print(completion.choices[0].message)
