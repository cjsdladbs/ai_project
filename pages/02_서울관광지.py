import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. 킹왕짱 화려한 페이지 레이아웃 세팅
st.set_page_config(page_title="🎨 외국인 PICK 서울 핫플 TOP 10", page_icon="🗺️", layout="centered")

st.title("🗺️ 외국인 취향 저격! 서울 관광지 TOP 10 치트키 🗺️")
st.write("안녕? 친구들! 서울에 놀러 온 외국인 친구에게 어디를 소개해줄지 고민 완전 끝! ✌️ "
         "지도의 **노란색 마커** 위에 마우스를 올리면 가장 가까운 지하철역이 툴팁으로 짜잔 나타나! "
         "지도 아래에 있는 꿀잼 놀거리 가이드까지 싹 다 정리해뒀으니 많관부~! 🔥")

# 2. 서울 주요 관광지 TOP 10 데이터베이스 (위도, 경도, 지하철역, 놀거리)
seoul_spots = [
    {"name": "경복궁 🏯", "lat": 37.5796, "lng": 126.9770, "subway": "경복궁역 (3호선)", "play": "한복 폼 미치게 빌려 입고 조선시대 공주/왕자 빙의해서 인생샷 건지기! 📸"},
    {"name": "N서울타워 🗼", "lat": 37.5512, "lng": 126.9882, "subway": "명동역 (4호선)", "play": "남산 케이블카 타고 올라가서 사랑의 자물쇠 걸고 서울 시내 야경 정주행하기! ✨"},
    {"name": "명동 쇼핑거리 🛍️", "lat": 37.5635, "lng": 126.9815, "subway": "명동역 (4호선)", "play": "K-푸드 길거리 음식(닭꼬치, 십원빵) 먹방 찍고 K-뷰티 화장품 매장 털기! 💸"},
    {"name": "북촌한옥마을 🏡", "lat": 37.5829, "lng": 126.9835, "subway": "안국역 (3호선)", "play": "고즈넉한 한옥 골목길 산책하며 감성 낭낭한 전통 찻집에서 차 한잔의 여유 🍵"},
    {"name": "동대문디자인플라자 (DDP) 🛸", "lat": 37.5665, "lng": 127.0092, "subway": "동대문역사문화공원역 (2, 4, 5호선)", "play": "우주선 모양 역대급 건축물 앞에서 인스타 감성 샷 찍고 전시회 구경 가기! 🎨"},
    {"name": "홍대 걷고싶은거리 🎸", "lat": 37.5567, "lng": 126.9234, "subway": "홍대입구역 (2호선, 공항철도)", "play": "눈귀 호강하는 길거리 버스킹 직관하고 힙한 소품샵이랑 네컷사진 조지기! 🎤"},
    {"name": "롯데월드타워 & 석촌호수 🎢", "lat": 37.5126, "lng": 127.1025, "subway": "잠실역 (2, 8호선)", "play": "123층 서울스카이 전망대에서 스릴 만점 유리 바닥 걷고 호수 산책하기! 🌊"},
    {"name": "인사동 쌈지길 🎨", "lat": 37.5743, "lng": 126.9847, "subway": "안국역 (3호선)", "play": "아기자기한 K-공예품 플렉스하고 내 이름 새겨진 한글 도장 만들기! 💮"},
    {"name": "스타필드 코엑스몰 별마당 도서관 🌟", "lat": 37.5111, "lng": 127.0595, "subway": "삼성역 (2호선)", "play": "우주 끝까지 닿을 듯한 초대형 거대 책장 앞에서 무조건 인증샷 남기기! 📸"},
    {"name": "광장시장 🥞", "lat": 37.5701, "lng": 127.0010, "subway": "종로5가역 (1호선)", "play": "넷플릭스에 나온 칼국수, 두툼한 녹두빈대떡, 육회까지 배 터질 때까지 먹방! 😋"}
]

# 3. 폴리움 지도 생성 (서울 중심부 좌표로 세팅)
m = folium.Map(location=[37.555, 126.992], zoom_start=12)

# 4. 지도 위에 "완벽한 노란색" 커스텀 마커 및 마우스 오버(Tooltip) 설정
for spot in seoul_spots:
    # 마우스를 마커 위에 올렸을 때 뜰 텍스트 
    tooltip_text = f"🚇 가장 가까운 역: {spot['subway']}"
    
    # 순수 옐로우 컬러를 구현하기 위해 HTML 아이콘 플러그인 사용 (folium 기본 제공 색상 한계 돌파!)
    icon_html = """
    <div style="
        background-color: #FFDE4D; 
        width: 14px; 
        height: 14px; 
        border-radius: 50%; 
        border: 2px solid #333333;
        box-shadow: 0px 0px 5px #888888;">
    </div>
    """
    
    folium.Marker(
        location=[spot['lat'], spot['lng']],
        popup=spot['name'], # 클릭하면 이름이 나옴!
        tooltip=tooltip_text, # 마우스 올리면 지하철역이 나옴!
        icon=folium.DivIcon(html=icon_html)
    ).add_to(m)

# 5. 스트림릿에 지도 렌더링하기
st_folium(m, width=700, height=500)

st.markdown("---")

# 6. 하단 관광지 상세 정보 및 꿀잼 놀거리 설명 가이드
st.subheader("🚀 방구석 서울 핫플 가이드 (지하철역 & 놀거리 팩폭)")

for i, spot in enumerate(seoul_spots, 1):
    with st.expander(f"{i}. {spot['name']}", expanded=False):
        st.markdown(f"**🚇 가장 가까운 지하철역:** `{spot['subway']}`")
        st.markdown(f"**🎉 가서 뭐하고 놀까?:** {spot['play']}")

# 7. 귀여운 마무리 멘트
st.markdown("---")
st.caption("중꺾마 정신으로 서울 투어 가자구~! 친구들에게 배포 링크 공유하면 완전 인싸 확정! 🤙")
