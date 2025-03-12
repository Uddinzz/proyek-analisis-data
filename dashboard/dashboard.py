import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark') 

def create_users_in_season(df):
    users_in_season = df.groupby(by='season').cnt.mean().sort_values().reset_index()

    return users_in_season

def create_users_in_year(df):
    users_in_year = df.groupby('yr')['cnt'].mean().reset_index()

    return users_in_year

def create_users_in_hour(df):
    users_in_hour = df.groupby('hr')['cnt'].mean().reset_index()

    return users_in_hour

# Membaca file CSV
data_project1 = pd.read_csv("data_project1.csv")

datetime_columns = ["dteday"]
data_project1.sort_values(by="dteday", inplace=True)
data_project1.reset_index(inplace=True)

for column in datetime_columns:
    data_project1[column] = pd.to_datetime(data_project1[column])

# Membuat Komponen Filter
min_date = data_project1["dteday"].min()
max_date = data_project1["dteday"].max()

with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
 
for column in datetime_columns:
    data_project1[column] = pd.to_datetime(data_project1[column])

main_df = data_project1[(data_project1["dteday"] >= str(start_date)) & 
                (data_project1["dteday"] <= str(end_date))]


users_in_season = create_users_in_season(main_df)
users_in_hour = create_users_in_hour(main_df)
users_in_year = create_users_in_year(main_df)

# Header
st.header('Bike Sharing Dashboard')

st.subheader('Users in Season')


fig = plt.figure(figsize=(8, 6))
sns.barplot(x=users_in_season['season'], y='cnt', data=users_in_season)
plt.title('Tingkat Rata-rata Jumlah Penyewa Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewa')

plt.show()
st.pyplot(fig)

st.subheader('Users in Year')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x=users_in_year['yr'], y="cnt", data=users_in_year)

plt.title("Perbandingan Rata-rata Penggunaan Sewa Sepeda pada Tahun 2011 & 2012")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Penyewa")
plt.grid(True)

plt.show()
st.pyplot(fig)

st.subheader('Users in Hour')

fig = plt.figure(figsize=(10, 6))
sns.lineplot(x="hr", y="cnt", data=users_in_hour, marker="o", linestyle="-", color='g')

plt.title("Jumlah Penyewa Sepeda Berdasarkan Jam", fontsize=14)
plt.xlabel("Jam")
plt.ylabel("Jumlah Penyewa")
plt.xticks(range(0, 24))
plt.grid(True)

plt.show()
st.pyplot(fig)

st.caption('Copyright (c) MC227D5Y1203 2025')