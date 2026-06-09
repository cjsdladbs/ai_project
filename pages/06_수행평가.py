import streamlit as st
import urllib.parse

# 1. 블로그 기반 40가지 칵테일 데이터 구축
COCKTAILS = {
    "1. 푸스카페 (Pousse Cafe)": {
        "glass": "리큐르 글라스", "method": "플로팅 (Floating)",
        "ingredients": ["그레나딘 시럽 1/3", "크렘 드 멘트 그린 1/3", "브랜디 1/3층 쌓기 (지거 계량 후 바스푼 이용)"],
        "tip": "재료가 섞이지 않도록 지거는 매번 씻어주기."
    },
    "2. 맨하탄 (Manhattan)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "스터 (Stir)",
        "ingredients": ["버번 위스키 1.5 oz", "스윗 베르무트 0.75 oz", "앙고스투라 비터스 1 dash"],
        "garnish": "체리 픽", "tip": "믹싱글라스에 얼음과 재료를 넣고 저은 후 잔에 따름."
    },
    "3. 드라이 마티니 (Dry Martini)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "스터 (Stir)",
        "ingredients": ["드라이 진 2 oz", "드라이 베르무트 1/3 oz (10 ml)"],
        "garnish": "그린 올리브", "tip": "믹싱글라스에 얼음과 재료를 넣고 저은 후 잔에 따름."
    },
    "4. 올드 패션드 (Old Fashioned)": {
        "glass": "올드 패션드 글라스", "method": "빌드 (Build)",
        "ingredients": ["가루 설탕 1 tsp", "앙고스투라 비터스 1 dash", "소다수 0.5 oz (15 ml)", "버번 위스키 1.5 oz"],
        "garnish": "체리 & 오렌지 슬라이스", "tip": "설탕, 비터스, 소다수를 먼저 저어 녹인 뒤 얼음과 위스키를 넣고 젓는다."
    },
    "5. 브랜디 알렉산더 (Brandy Alexander)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["브랜디 3/4 oz", "크렘 드 카카오 (브라운) 3/4 oz", "우유 3/4 oz"],
        "garnish": "넛멕 파우더", "tip": "알렉산더 대왕님은 코코아를 좋아해 (3/4 oz 묶음)"
    },
    "6. 싱가폴 슬링 (Singapore Sling)": {
        "glass": "필스너 글라스 (얼음 가득)", "method": "셰이킹 & 빌드",
        "ingredients": ["드라이 진 1.5 oz", "레몬 주스 0.5 oz", "설탕 1 tsp", "소다수 fill up", "체리 브랜디 0.5 oz (플로팅)"],
        "garnish": "체리 & 오렌지 슬라이스", "tip": "진, 레몬주스, 설탕 셰이킹 후 잔에 따름 -> 소다수 fill up -> 체리 브랜디 0.5 oz 빌드(플로팅)"
    },
    "7. 블랙러시안 (Black Russian)": {
        "glass": "올드 패션드 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["보드카 1 oz", "깔루아 0.5 oz"],
        "tip": "블랙 = 깔루아 / 러시안 = 보드카. 넣고 바스푼으로 저어주기."
    },
    "8. 마가리타 (Margarita)": {
        "glass": "칵테일 글라스 (잔 칠링 + 소금 리밍)", "method": "셰이킹 (Shaking)",
        "ingredients": ["데킬라 1.5 oz", "트리플 섹 0.5 oz", "라임 주스 0.5 oz"],
        "tip": "레몬 조각을 이용해 잔 테두리에 소금을 묻혀 준비."
    },
    "9. 러스티네일 (Rusty Nail)": {
        "glass": "올드 패션드 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["스카치 위스키 1 oz", "드람뷔 0.5 oz"],
        "tip": "드람뷔 노래 듣는 달팽이. 넣고 바스푼으로 저어주기."
    },
    "10. 위스키사워 (Whiskey Sour)": {
        "glass": "사워 글라스 (잔 칠링)", "method": "셰이킹 & 빌드",
        "ingredients": ["버번 위스키 1.5 oz", "레몬 주스 0.5 oz", "설탕 1 tsp", "소다수 1 oz"],
        "garnish": "체리 & レ몬 슬라이스", "tip": "소다수 제외하고 셰이킹 후 잔에 따름 -> 소다수 1 oz 넣어 빌드해 젓기."
    },
    "11. 뉴욕 (New York)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["버번 위스키 1.5 oz", "라임 주스 0.5 oz", "설탕 1 tsp", "그레나딘 시럽 0.5 tsp"],
        "garnish": "레몬 필 트위스트"
    },
    "12. 다이키리 (Daiquiri)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["화이트 럼 1.75 oz", "라임 주스 0.75 oz", "설탕 1 tsp"],
        "tip": "자유를 찾아서 바카디와 비슷"
    },
    "13. B-52": {
        "glass": "셰리 글라스", "method": "플로팅 (Floating)",
        "ingredients": ["깔루아 층 쌓기", "베일리스 층 쌓기", "그랑 마르니에 층 쌓기"],
        "tip": "그랑마르니에 유일 사용. 지거 계량 후 바스푼 이용, 지거는 매번 씻기."
    },
    "14. 준벅 (June Bug)": {
        "glass": "콜린스 글라스 (얼음 가득)", "method": "셰이킹 (Shaking)",
        "ingredients": ["미도리 1 oz", "말리부 0.5 oz", "바나나 리큐르 0.5 oz", "파인애플 주스 2 oz", "스윗 사워 믹스 2 oz"],
        "garnish": "체리 & 파인애플 웨지"
    },
    "15. 바카디 (Bacardi)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["바카디 럼 1.75 oz", "라임 주스 0.75 oz", "그레나딘 시럽 1 tsp"],
        "tip": "자유를 찾아서 다이키리와 비슷"
    },
    "16. 쿠바리브레 (Cuba Libre)": {
        "glass": "하이볼 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["화이트 럼 1.5 oz", "라임 주스 0.5 oz", "콜라 fill up"],
        "garnish": "레몬 웨지", "tip": "쿠바리브레 시브리즈 모스코뮬 (묶어서 암기)"
    },
    "17. 그래스호퍼 (Grasshopper)": {
        "glass": "소서 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["크렘 드 민트 (그린) 1 oz", "크렘 드 카카오 (화이트) 1 oz", "우유 1 oz"]
    },
    "18. 시브리즈 (Sea Breeze)": {
        "glass": "하이볼 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["보드카 1.5 oz", "자몽 주스 0.5 oz", "크랜베리 주스 3 oz"],
        "garnish": "레몬 웨지", "tip": "넣고 바스푼으로 살짝 저어주기."
    },
    "19. 애플마티니 (Apple Martini)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["보드카 1 oz", "애플 푸커 1 oz", "라임 주스 0.5 oz"],
        "garnish": "사과 슬라이스"
    },
    "20. 네그로니 (Negroni)": {
        "glass": "올드 패션드 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["드라이 진 3/4 oz", "스윗 베르무트 3/4 oz", "캄파리 3/4 oz"],
        "garnish": "레몬 필 트위스트", "tip": "전부 3/4 oz 동일 분량."
    },
    "21. 롱 아일랜드 아이스티 (Long Island Iced Tea)": {
        "glass": "필스너 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["드라이 진 0.5 oz", "화이트 럼 0.5 oz", "보드카 0.5 oz", "데킬라 0.5 oz", "트리플 섹 0.5 oz", "스윗 사워 믹스 1.5 oz", "콜라 fill up"],
        "garnish": "레몬 웨지", "tip": "콜라를 넣기 전에 바스푼으로 먼저 저어준 뒤 콜라를 채운다."
    },
    "22. 사이드카 (Sidecar)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["브랜디 1 oz", "트리플 섹 1 oz", "레몬 주스 0.25 oz"]
    },
    "23. 마이타이 (Mai-Tai)": {
        "glass": "필스너 글라스 (잔 칠링)", "method": "블렌딩 (Blending)",
        "ingredients": ["화이트 럼 1.25 oz", "트리플 섹 0.75 oz", "라임 주스 1 oz", "파인애플 주스 1 oz", "오렌지 주스 1 oz", "그레나딘 시럽 0.25 oz"],
        "garnish": "체리 & 파인애플 웨지", "tip": "블렌더에 얼음 한 스쿱을 넣고 10초간 블렌딩. (암기팁: 빨주노초)"
    },
    "24. 피나콜라다 (Pina Colada)": {
        "glass": "필스너 글라스 (잔 칠링)", "method": "블렌딩 (Blending)",
        "ingredients": ["화이트 럼 1.25 oz", "피나콜라다 믹스 2 oz", "파인애플 주스 2 oz"],
        "garnish": "체리 & 파인애플 웨지", "tip": "블렌더에 얼음 한 스쿱을 넣고 10초간 블렌딩."
    },
    "25. 코스모폴리탄 (Cosmopolitan)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["보드카 1 oz", "트리플 섹 0.5 oz", "라임 주스 0.5 oz", "크랜베리 주스 0.5 oz"],
        "garnish": "레몬 필 트위스트", "tip": "보트라크 (보드카, 트리플섹, 라임, 크랜베리)"
    },
    "26. 모스코뮬 (Moscow Mule)": {
        "glass": "하이볼 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["보드카 1.5 oz", "라임 주스 0.5 oz", "진저에일 fill up"],
        "garnish": "레몬 슬라이스", "tip": "진저라임하이볼 스타일. 살짝 저어주기."
    },
    "27. 애프리콧 (Apricot)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["애프리콧 브랜디 1.5 oz", "드라이 진 1 tsp", "레몬 주스 0.5 oz", "오렌지 주스 0.5 oz"]
    },
    "28. 허니문 (Honeymoon)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["애플 브랜디 3/4 oz", "베네딕틴 D.O.M. 3/4 oz", "트리플 섹 1/4 oz", "레몬 주스 2/4 oz"]
    },
    "29. 블루하와이안 (Blue Hawaiian)": {
        "glass": "필스너 글라스 (잔 칠링)", "method": "블렌딩 (Blending)",
        "ingredients": ["화이트 럼 1 oz", "블루 큐라소 1 oz", "말리부 1 oz", "파인애플 주스 2 oz"],
        "garnish": "체리 & 파인애플 웨지", "tip": "블렌더에 얼음 한 스쿱을 넣고 10초간 블렌딩."
    },
    "30. 키르 (Kir)": {
        "glass": "화이트 와인 글라스 (얼음 없음 ❌)", "method": "빌드 (Build)",
        "ingredients": ["화이트 와인 3 oz", "크렘 드 카시스 0.5 oz"],
        "garnish": "레몬 트위스트 필"
    },
    "31. 데킬라 선라이즈 (Tequila Sunrise)": {
        "glass": "푸티드 필스너 글라스 (얼음 가득)", "method": "빌드 & 플로팅",
        "ingredients": ["데킬라 1.5 oz", "오렌지 주스 fill up", "그레나딘 시럽 0.5 oz (플로팅)"],
        "tip": "데킬라와 오렌지 주스를 젓고 난 후에 그레나딘 시럽을 띄워 바닥에 가라앉힘."
    },
    "32. 진피즈 (Gin Fizz)": {
        "glass": "하이볼 글라스 (얼음 가득)", "method": "셰이킹 & 빌드",
        "ingredients": ["드라이 진 1.5 oz", "레몬 주스 0.5 oz", "설탕 1 tsp", "소다수 fill up"],
        "garnish": "레몬 슬라이스"
    },
    "33. 불바디에 (Boulevardier)": {
        "glass": "올드 패션드 글라스 (얼음 넣음, 잔 칠링)", "method": "스터 (Stir)",
        "ingredients": ["버번 위스키 1 oz", "캄파리 1 oz", "스윗 베르무트 1 oz"],
        "garnish": "오렌지 트위스트 필", "tip": "네그로니의 버번 위스키 버전. 믹싱글라스 스터 후 스트레이너 사용."
    },
    "34. 힐링 (Healing)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["감홍로 1.5 oz", "베네딕틴 1/3 oz", "크렘 드 카시스 1/3 oz", "스윗 사워 믹스 1 oz"],
        "garnish": "레몬 트위스트 필", "tip": "암기: 하는데 (감)놔라 (베)놔라 (카)더라 (스)트레스"
    },
    "35. 진도 (Jindo)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["진도 홍주 1 oz", "크렘 드 민트 화이트 0.5 oz", "청포도 주스 0.75 oz", "라즈베리 시럽 0.5 oz"],
        "tip": "암기: (홍)색 미(민트)쳤(청)냐(라)"
    },
    "36. 풋사랑 (Puppy Love)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["안동소주 1 oz", "트리플 섹 1/3 oz", "애플 퍼커 1 oz", "라임 주스 1/3 oz"],
        "garnish": "사과 슬라이스", "tip": "암기: (안)(섹)이 (애)바(라)"
    },
    "37. 금산 (Geumsan)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["인삼주 1.5 oz", "깔루아 0.5 oz", "애플 퍼커 0.5 oz", "라임 주스 1 tsp"],
        "tip": "암기: (금)색 (인)선 눈(깔)(애)바(라)"
    },
    "38. 고창 (Gochang)": {
        "glass": "플루트 샴페인 글라스 (잔 칠링)", "method": "스터 (Stir)",
        "ingredients": ["복분자 와인 2 oz", "트리플 섹 0.5 oz", "스프라이트 2 oz"],
        "tip": "암기: 복2섹0.5스2. 믹싱 글라스 스터 후 잔에 따름."
    },
    "39. 버진 프루트 펀치 (Virgin Fruit Punch)": {
        "glass": "필스너 글라스 (얼음 가득)", "method": "셰이킹 & 빌드",
        "ingredients": ["오렌지 주스 1.5 oz", "파인애플 주스 1.5 oz", "크랜베리 주스 0.5 oz", "자몽 주스 0.5 oz", "레몬 주스 0.5 oz", "그레나딘 시럽 0.5 oz"],
        "tip": "암기: 논알콜 오파크자 레그. 그레나딘 제외 셰이킹 후 잔에 따르고 그레나딘은 가라앉힘."
    },
    "40. 프레시 レ몬 스쿼시 (Fresh Lemon Squash)": {
        "glass": "하이볼 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["생레몬 1/2개 스퀴즈 주스", "가루 설탕(또는 시럽) 2 tsp", "소다수 fill up"],
        "garnish": "레몬 슬라이스"
    }
}

st.set_page_config(page_title="조주기능사 40개 레시피 마스터", page_icon="🍸")
st.title("🍸 조주기능사 실기 레시피 40가지 마스터")
st.caption("블로그 암기 팁과 온스(oz) 계량이 완벽 반영된 수험생용 뷰어 앱입니다.")

# 2. 사이드바 또는 메인에서 칵테일 선택
selected_name = st.selectbox("👉 분석할 칵테일을 선택하세요", list(COCKTAILS.keys()))
data = COCKTAILS[selected_name]

st.markdown("---")

# 3. 구글 검색 이미지를 우회하여 불러오는 무료 이미지 소스 활용
# Unsplash 소스 또는 직관적인 위키백과 이미지 활용을 위해 쿼리 인코딩 수행
search_query = selected_name.split(". ")[1].split(" (")[0]  # 영문명 또는 국문 한글 이름 추출
encoded_query = urllib.parse.quote(search_query)

# Unsplash Source API 또는 DuckDuckGo 이미지 프록시 주소 매칭하여 상단 배치
image_url = f"https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600&auto=format&fit=crop&q=60" # 기본 이미지 바인딩 예시
if "마티니" in selected_name or "Martini" in selected_name:
    image_url = "https://images.unsplash.com/photo-1575444758702-4a6b9222336e?w=600"
elif "모스코뮬" in selected_name or "Mule" in selected_name:
    image_url = "https://images.unsplash.com/photo-1530991808291-7e157454758c?w=600"
elif "블루하와이안" in selected_name or "Blue" in selected_name:
    image_url = "https://images.unsplash.com/photo-1546171753-97d7676e4602?w=600"
elif "피나콜라다" in selected_name:
    image_url = "https://images.unsplash.com/photo-1541658016709-82535e94bc69?w=600"

st.image(image_url, caption=f"📸 {search_query} 연출 예시 이미지", use_container_width=True)

# 4. 상세 설명 표기 (요청 조건 적용)
# 글라스는 파란색으로 표시
st.markdown(f"### 🥂 글라스: <span style='color:blue; font-weight:bold;'>{data['glass']}</span>", unsafe_allow_html=True)
st.write(f"**조주 기법:** {data['method']}")

st.markdown("#### 📐 레시피 (oz 규격)")
for ing in data["ingredients"]:
    st.markdown(f"- {ing}")

if "garnish" in data:
    st.markdown(f"**🍒 가니시:** {data['garnish']}")

if "tip" in data:
    st.info(f"💡 **블로그 암기/조주 팁:** {data['tip']}")
