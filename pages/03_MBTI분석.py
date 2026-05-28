import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. 페이지 설정
st.set_page_config(page_title="국가별 MBTI 분포 분석", layout="centered")
st.title("🌍 국가별 MBTI 비율 분석기")
st.markdown("국가를 선택하면 해당 국가의 MBTI 비율을 한눈에 확인할 수 있습니다.")

# 2. 데이터 로드 (캐싱 처리로 속도 향상)
@st.cache_data
def load_data():
    # 데이터 불러오기 (데이터 파일이 app.py와 같은 위치에 있어야 합니다)
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

try:
    df = load_data()

    # 3. 사이드바 - 국가 선택
    countries = df['Country'].unique()
    selected_country = st.sidebar.selectbox("📍 분석할 국가를 선택하세요:", countries)

    # 4. 선택한 국가의 데이터 추출 및 정렬
    country_data = df[df['Country'] == selected_country].iloc[0, 1:]
    
    # % 단위로 변환하고 내림차순 정렬
    country_df = pd.DataFrame({
        'MBTI': country_data.index,
        'Percentage': country_data.values * 100
    }).sort_values(by='Percentage', ascending=False).reset_index(drop=True)

    # 5. 그라데이션 색상 배열 생성 (1등은 빨강, 나머지는 파랑 그라데이션)
    # 총 16개 유형: 1등(빨강) + 2등~16등(점점 흐려지는 파랑 15단계)
    colors = []
    for i in range(16):
        if i == 0:
            colors.append("rgba(238, 75, 43, 1)")  # 1등: 진한 빨간색 (Red)
        else:
            # 2등부터 16등까지 불투명도(alpha)를 0.9에서 0.15까지 서서히 줄임
            alpha = 0.9 - (i - 1) * (0.75 / 14)
            colors.append(f"rgba(30, 144, 255, {alpha})")  # 파란색 (DodgerBlue) 그라데이션

    # 6. Plotly 막대그래프 시각화
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=country_df['MBTI'],
        y=country_df['Percentage'],
        marker_color=colors,
        text=country_df['Percentage'].round(2).astype(str) + '%',
        textposition='outside',
        hovertemplate="<b>%{x}</b>: %{y:.2f}%<extra></extra>"
    ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=f"📊 {selected_country}의 MBTI 유형별 비율 (내림차순)",
        xaxis_title="MBTI 유형",
        yaxis_title="비율 (%)",
        yaxis=dict(range=[0, country_df['Percentage'].max() * 1.15]), # 텍스트가 잘리지 않게 여유 공간 확보
        template="plotly_white",
        height=500,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    # 스트림릿에 그래프 출력
    st.plotly_chart(fig, use_container_width=True)

    # 7. 추가 정보 (데이터 테이블 요약)
    with st.expander("📄 원본 데이터 보기"):
        st.dataframe(country_df.rename(columns={'Percentage': '비율 (%)'}))

except FileNotFoundError:
    st.error("🚨 `countriesMBTI_16types.csv` 파일을 찾을 수 없습니다. 파일 이름을 확인하거나 app.py와 같은 폴더에 업로드해 주세요.")
except Exception as e:
    st.error(format(e))
