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


# 大約 6 個月前，
# 我收到了這隻手錶作為禮物。我給它 5 顆星，
# 因為我喜歡它的睡眠追蹤功能和智慧喚醒功能。
# 我也透過步行來鍛鍊身體。
# 今天早上我出去散步，它記錄了我 2 英里徒步旅行的每一步。這是一次城市徒步旅行。
# 當我繞一圈時，我就達到了目標心率。直到今天我才知道這是2英哩。
# 據我了解，它在 iPhone 上的表現不太好。我有一台運行 Android 系統的 Pixel 6，
# 沒有遇到任何問題。我不明白的一件事是，有些人對它的整體評分低於我的預期。
# 我認為這可能與手腕尺寸有關。我將錶帶設置為最大，它戴在手腕背面有點鬆。
# 讓感測器在那種緊密程度（好吧，鬆散程度）下工作從來沒有遇到任何問題。
# 它確實配備了兩種不同尺寸的錶帶，因此如果您的手腕尺寸為中到小，您可能想嘗試兩種尺寸。
# 我的手錶從未出現過任何品質問題。我喜歡睡眠追蹤器。
# 它可以追蹤到最接近的分鐘，透過 Fitbit 應用程序，您可以查看清醒時間、快速動眼睡眠、淺度睡眠和深度睡眠的時間。
# 我最需要它來了解我何時睡覺以及睡眠品質。我對此完全沒有任何問題。
# 我幾乎給了它 4 顆星，因為它的螢幕又小又窄，
# 為了使用某些功能，你必須滾動。上、下、左、右、多螢幕。我不需要這些功能中的大部分，
# 但擁有它們很好。我了解到我有正常的竇性心律，我沒有過度壓力。
# 無論如何，我可以寫更多，但你明白了。您可能應該閱讀一些評論，以獲得更好的印象（不僅僅是五星級的評論）。
