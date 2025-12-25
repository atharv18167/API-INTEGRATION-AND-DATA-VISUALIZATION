import requests
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

API_KEY = "b1695ed0a0045d0a6be61ad13d344714"

st.title("Weather Visualization Dashboard")

city = st.text_input("Enter City Name", "Mumbai")

if st.button("Get Weather Data"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

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

    st.subheader("Temperature Trend")
    fig1 = plt.figure()
    sns.lineplot(x="Date", y="Temperature", data=df)
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    st.subheader("Humidity Trend")
    fig2 = plt.figure()
    sns.lineplot(x="Date", y="Humidity", data=df)
    plt.xticks(rotation=45)
    st.pyplot(fig2)
