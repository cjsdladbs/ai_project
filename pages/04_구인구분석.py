import streamlit as st
import pandas as pd
import plotly.graph_objects as objects
import numpy as np

# 1. 페이지 설정
st.set_page_config(page_title="서울시 자치구별 연령대 인구수 분석", layout="centered")

st.title("📊 서울시 자치구별 연령대 인구 현황")
st.markdown("제공된 인구 데이터를 바탕으로 자치구별 연령대별 인구수를 무지개 그라데이션 꺾은선 그래프로 시각화합니다.")

# 2. 데이터 로드 및 전처리 (캐싱 처리)
@st.cache_data
def load_data():
    # Streamlit Cloud 환경에서 동일 경로에 있는 population.csv 파일을 읽어옵니다.
    df = pd.read_csv("population.csv", encoding="utf-8")
    
    # '행정구역' 컬럼에서 코드를 제외한 자치구 이름만 추출
    df['구이름'] = df['행정구역'].apply(lambda x: x.split('(')[0].strip())
    df['구이름'] = df['구이름'].apply(lambda x: '서울특별시 전체' if x == '서울특별시' else x)
    
    # 숫자형 데이터에 포함된 콤마(,) 제거 후 정수형 변환
    age_cols = [
        '0~9세', '10~19세', '20~29세', '30~39세', '40~49세', 
        '50~59세', '60~69세', '70~79세', '80~89세', '90~99세', '100세 이상'
    ]
    
    for col in age_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(',', '').astype(int)
            
    return df, age_cols

try:
    df, age_cols = load_data()

    # 3. 사이드바 - 자치구 선택 리스트박스
    gu_list = df['구이름'].unique().tolist()
    if '서울특별시 전체' in gu_list:
        gu_list.remove('서울특별시 전체')
        gu_list = ['서울특별시 전체'] + gu_list
        
    selected_gu = st.sidebar.selectbox("🗺️ 분석할 자치구를 선택하세요", gu_list)

    # 4. 선택한 자치구 데이터 추출
    selected_data = df[df['구이름'] == selected_gu].iloc[0]
    population_values = [selected_data[col] for col in age_cols]

    # 5. 무지개 그라데이션 선 구현 (Plotly 세그먼트 보간)
    rainbow_colors = [
        '#FF4B4B', '#FF8533', '#FFD433', '#4BFF4B', '#3399FF', '#1A1AFF', '#7A1AFF'
    ]
    
    x_numeric = np.arange(len(age_cols))
    x_fine = np.linspace(0, len(age_cols) - 1, 200) # 선을 200개 구간으로 쪼개어 그라데이션 표현
    y_fine = np.interp(x_fine, x_numeric, population_values)
    
    # fraction(0~1) 진행도에 따라 RGB 색상을 계산하는 함수
    def get_rainbow_color(fraction):
        idx = fraction * (len(rainbow_colors) - 1)
        idx_low = int(np.floor(idx))
        idx_high = int(np.ceil(idx))
        f = idx - idx_low
        
        c1 = tuple(int(rainbow_colors[idx_low].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        c2 = tuple(int(rainbow_colors[idx_high].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        
        r = int(c1[0] + (c2[0] - c1[0]) * f)
        g = int(c1[1] + (c2[1] - c1[1]) * f)
        b = int(c1[2] + (c2[2] - c1[2]) * f)
        return f'rgb({r},{g},{b})'

    fig = objects.Figure()

    # 조각난 꺾은선을 각각 그리며 그라데이션 효과 적용
    for i in range(len(x_fine) - 1):
        fraction = i / (len(x_fine) - 1)
        fig.add_trace(objects.Scatter(
            x=[x_fine[i], x_fine[i+1]],
            y=[y_fine[i], y_fine[i+1]],
            mode='lines',
            line=dict(color=get_rainbow_color(fraction), width=5),
            hoverinfo='skip',
            showlegend=False
        ))
        
    # 데이터 포인트 마커 및 툴팁 레이어 추가
    fig.add_trace(objects.Scatter(
        x=x_numeric,
        y=population_values,
        mode='markers',
        marker=dict(size=10, color='#333333', symbol='circle'),
        text=[f"{age}: {val:,}명" for age, val in zip(age_cols, population_values)],
        hoverinfo='text',
        name='인구수'
    ))

    # 6. 레이아웃 설정 (바탕색 요구사항 반영)
    fig.update_layout(
        plot_bgcolor='#EFEFEF',      # 그래프 내부 바탕: 연한 회색 설정
        paper_bgcolor='#F8F9FA',     # 외부 배경
        title=dict(
            text=f"📌 {selected_gu} 연령대별 인구 분포",
            font=dict(size=18, color='#111111'),
            x=0.5, xanchor='center'
        ),
        xaxis=dict(
            title="연령대",
            tickmode='array',
            tickvals=x_numeric,
            ticktext=age_cols,
            gridcolor='#FFFFFF',      # 가독성을 위한 흰색 격자선
            showgrid=True
        ),
        yaxis=dict(
            title="인구수 (명)",
            gridcolor='#FFFFFF',
            showgrid=True,
            tickformat=","            # 숫자 단위 콤마
        ),
        margin=dict(l=40, r=40, t=60, b=40),
        showlegend=False
    )

    # 대시보드 화면에 그래프 렌더링
    st.plotly_chart(fig, use_container_width=True)
    
    # 7. 하단 하이라이트 데이터 테이블
    st.markdown("### 📋 상세 데이터 테이블")
    df_display = pd.DataFrame({
        '연령대': age_cols,
        '인구수 (명)': [f"{val:,}" for val in population_values]
    })
    st.dataframe(df_display.set_index('연령대'), use_container_width=True)

except FileNotFoundError:
    st.error("📂 대시보드를 구동하기 위해 `population.csv` 파일이 필요합니다. GitHub 리포지토리에 데이터 파일을 함께 업로드해 주세요.")
