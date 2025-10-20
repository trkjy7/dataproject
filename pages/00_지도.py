import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Seoul Top 10 Attractions", layout="wide")

st.title("🌏 외국인이 사랑하는 서울 관광지 TOP 10")
st.markdown("서울의 인기 명소들을 지도에서 살펴보세요!")

# 서울 관광지 Top 10 (좌표 포함)
places = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579617, "lon": 126.977041},
    {"name": "명동 (Myeong-dong)", "lat": 37.563757, "lon": 126.985302},
    {"name": "남산타워 (N Seoul Tower)", "lat": 37.551169, "lon": 126.988227},
    {"name": "홍대 (Hongdae)", "lat": 37.555195, "lon": 126.923828},
    {"name": "인사동 (Insadong)", "lat": 37.574002, "lon": 126.984955},
    {"name": "청계천 (Cheonggyecheon Stream)", "lat": 37.569172, "lon": 126.979862},
    {"name": "롯데월드타워 (Lotte World Tower)", "lat": 37.513068, "lon": 127.102493},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983998},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566477, "lon": 127.009169},
    {"name": "한강공원 (Hangang Park)", "lat": 37.520770, "lon": 126.939084},
]

# 지도 생성 (서울 중심)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 표시
for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=place["name"],
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# Streamlit에 폴리움 지도 표시
st_folium(m, width=900, height=600)
