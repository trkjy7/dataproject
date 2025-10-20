import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.colors as pc

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

st.set_page_config(page_title="국가별 MBTI 비율 시각화", page_icon="🌍", layout="wide")

st.title("🌍 국가별 MBTI 비율 시각화")
st.markdown("**국가를 선택하면 MBTI 16유형 비율이 막대 그래프로 표시됩니다.**")

# 국가 선택
country = st.selectbox("국가를 선택하세요", sorted(df["Country"].unique()))

# 선택한 국가 데이터 추출
country_data = df[df["Country"] == country].drop(columns=["Country"]).melt(
    var_name="MBTI", value_name="비율"
)

# 비율 기준 내림차순 정렬
country_data = country_data.sort_values(by="비율", ascending=False)

# 색상 설정 (1등은 빨강, 나머지는 파스텔 그라데이션)
base_colors = pc.sample_colorscale("Blues", [i/15 for i in range(16)])
colors = [base_colors[i] for i in range(len(country_data))]
colors[0] = "red"  # 1등만 빨간색

# 그래프 생성
fig = px.bar(
    country_data,
    x="MBTI",
    y="비율",
    text="비율",
    color=country_data["MBTI"],
    color_discrete_sequence=colors,
)

fig.update_traces(
    texttemplate="%{y:.2%}",
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>비율: %{y:.2%}<extra></extra>"
)

fig.update_layout(
    title=f"🇨🇭 {country}의 MBTI 유형 분포",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    showlegend=False,
    plot_bgcolor="white",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor="lightgray"),
    margin=dict(l=40, r=40, t=60, b=40)
)

st.plotly_chart(fig, use_container_width=True)

# 하단 부가정보
st.caption("📊 데이터 출처: countriesMBTI_16types.csv | 시각화: Plotly + Streamlit")
