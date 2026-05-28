import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. 페이지 설정
st.set_page_config(page_title="MBTI별 상위 국가 분석", layout="centered")
st.title("📊 MBTI별 비율 상위 10개국 분석기")
st.markdown("특정 MBTI 유형을 선택하면, 전 세계에서 해당 성향의 비율이 가장 높은 10개 나라를 확인하실 수 있습니다.")

# 2. 데이터 로드 (캐싱 처리)
@st.cache_data
def load_data():
    # 데이터 불러오기 (데이터 파일이 app.py와 같은 위치에 있어야 합니다)
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

try:
    df = load_data()

    # 데이터프레임에서 MBTI 16가지 유형 목록 추출 (첫 번째 컬럼인 Country 제외)
    mbti_types = list(df.columns[1:])
    
    # 3. 사이드바 - MBTI 유형 선택
    selected_mbti = st.sidebar.selectbox("🧩 분석할 MBTI 유형을 선택하세요:", mbti_types)

    # 4. 선택한 MBTI 기준 상위 10개국 데이터 추출 및 정렬
    # % 단위 변환을 위해 해당 컬럼에 100을 곱해줍니다.
    top10_df = df[['Country', selected_mbti]].copy()
    top10_df[selected_mbti] = top10_df[selected_mbti] * 100
    
    # 내림차순 정렬 후 상위 10개 추출
    top10_df = top10_df.sort_values(by=selected_mbti, ascending=False).head(10).reset_index(drop=True)

    # 5. 그라데이션 색상 배열 생성 (1등은 빨강, 나머지는 파랑 그라데이션)
    # 총 10개 국가: 1등(빨강) + 2등~10등(점점 흐려지는 파랑 9단계)
    colors = []
    for i in range(10):
        if i == 0:
            colors.append("rgba(238, 75, 43, 1)")  # 1등: 진한 빨간색 (Red)
        else:
            # 2등부터 10등까지 불투명도(alpha)를 0.9에서 0.2까지 서서히 줄임
            alpha = 0.9 - (i - 1) * (0.7 / 8)
            colors.append(f"rgba(30, 144, 255, {alpha})")  # 파란색 (DodgerBlue) 그라데이션

    # 6. Plotly 막대그래프 시각화
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=top10_df['Country'],
        y=top10_df[selected_mbti],
        marker_color=colors,
        text=top10_df[selected_mbti].round(2).astype(str) + '%',
        textposition='outside',
        hovertemplate="<b>%{x}</b>: %{y:.2f}%<extra></extra>"
    ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=f"🏆 전 세계 {selected_mbti} 비율 상위 10개국",
        xaxis_title="국가 (Country)",
        yaxis_title="비율 (%)",
        yaxis=dict(range=[0, top10_df[selected_mbti].max() * 1.15]), # 텍스트가 잘리지 않게 상단 여유 공간 확보
        template="plotly_white",
        height=500,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    # 스트림릿에 그래프 출력
    st.plotly_chart(fig, use_container_width=True)

    # 7. 추가 정보 (데이터 테이블 요약)
    with st.expander("📄 상위 10개국 상세 데이터 보기"):
        st.dataframe(
            top10_df.rename(columns={'Country': '국가', selected_mbti: f'{selected_mbti} 비율 (%)'}),
            use_container_width=True
        )

except FileNotFoundError:
    st.error("🚨 `countriesMBTI_16types.csv` 파일을 찾을 수 없습니다. 파일 이름을 확인하거나 app.py와 같은 폴더에 업로드해 주세요.")
except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")
