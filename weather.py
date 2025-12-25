import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "b1695ed0a0045d0a6be61ad13d344714"
CITY = "Mumbai"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()
print(data)

dates = []
temps = []
humidity = []

for item in data["list"]:
    dates.append(item["dt_txt"])
    temps.append(item["main"]["temp"])
    humidity.append(item["main"]["humidity"])

df = pd.DataFrame({
    "Date": dates,
    "Temperature": temps,
    "Humidity": humidity
})

plt.figure()
sns.lineplot(x="Date", y="Temperature", data=df)
plt.xticks(rotation=45)
plt.title("Temperature Forecast")
plt.tight_layout()
plt.show()
