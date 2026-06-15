import streamlit as st

# 1. image_00591d.jpg의 기주 분류 및 레시피 용량을 완벽히 반영한 데이터셋
COCKTAILS = {
    "데킬라 베이스": {
        "마가리타": {
            "method": "Shake", "glass": "칵테일", "garnish": "소금 리밍",
            "ingredients": ["데킬라 1 1/2 oz", "트리플섹 1/2 oz", "라임주스 1/2 oz"]
        },
        "데킬라선라이즈": {
            "method": "Build", "glass": "풋티드 필스너", "garnish": "X",
            "ingredients": ["데킬라 1 1/2 oz", "오렌지주스 Fill", "그라나딘 1/2 oz"]
        }
    },
    "위스키 베이스": {
        "올드패션드": {
            "method": "Build", "glass": "올드패션드", "garnish": "오렌지 + 체리",
            "ingredients": ["버번위스키 1 1/2 oz", "파우더슈가 1 tsp", "앙.비터 1 dash", "소다수 1/2 oz"]
        },
        "위스키샤워": {
            "method": "Shake & Build", "glass": "샤워", "garnish": "레몬 + 체리",
            "ingredients": ["버번위스키 1 1/2 oz", "레몬주스 1/2 oz", "파우더슈가 1 tsp", "소다수 1 oz"]
        },
        "뉴욕": {
            "method": "Shake", "glass": "칵테일", "garnish": "X",
            "ingredients": ["버번위스키 1 1/2 oz", "라임주스 1/2 oz", "파우더슈가 1 tsp", "그라나딘 1/2 tsp"]
        },
        "맨하탄": {
            "method": "Stir", "glass": "칵테일", "garnish": "체리",
            "ingredients": ["버번위스키 1 1/2 oz", "스윗베르무트 3/4 oz", "앙.비터 1 dash"]
        },
        "러스티네일": {
            "method": "Build", "glass": "올드패션드", "garnish": "X",
            "ingredients": ["스카치위스키 1 1/2 oz", "드람뷔 1/2 oz"]
        }
    },
    "럼 베이스": {
        "다이키리": {
            "method": "Shake", "glass": "칵테일", "garnish": "X",
            "ingredients": ["럼 1 3/4 oz", "라임주스 3/4 oz", "파우더슈가 1 tsp"]
        },
        "바카디": {
            "method": "Shake", "glass": "칵테일", "garnish": "X",
            "ingredients": ["럼 1 3/4 oz", "라임주스 3/4 oz", "그라나딘 1 tsp"]
        },
        "쿠바리브레": {
            "method": "Build", "glass": "하이볼", "garnish": "웨지레몬",
            "ingredients": ["럼 1 1/2 oz", "라임주스 1/2 oz", "콜라 Fill"]
        },
        "마이타이": {
            "method": "Blend", "glass": "풋티드 필스너", "garnish": "파인애플 + 체리",
            "ingredients": ["럼 1 1/4 oz", "트리플섹 3/4 oz", "라임주스 3/4 oz"]
        },
        "피나콜라다": {
            "method": "Blend", "glass": "풋티드 필스너", "garnish": "파인애플 + 체리",
            "ingredients": ["럼 1 1/4 oz", "피나콜라다믹스 2 oz", "파인애플주스 2 oz"]
        },
        "블루하와이안": {
            "method": "Blend", "glass": "풋티드 필스너", "garnish": "파인애플 + 체리",
            "ingredients": ["럼 1 oz", "블루큐라소 1 oz", "코코넛럼 1 oz", "파인애플주스 2 1/2 oz"]
        }
    },
    "보드카 베이스": {
        "시브리즈": {
            "method": "Build", "glass": "하이볼", "garnish": "웨지레몬 / 라임",
            "ingredients": ["보드카 1 1/2 oz", "크랜베리주스 3 oz", "자몽주스 1/2 oz"]
        },
        "모스크뮬": {
            "method": "Build", "glass": "하이볼", "garnish": "슬라이스레몬 / 라임",
            "ingredients": ["보드카 1 1/2 oz", "라임주스 1/2 oz", "진저에일 Fill"]
        },
        "블랙러시안": {
            "method": "Build", "glass": "올드패션드", "garnish": "X",
            "ingredients": ["보드카 1 oz", "커피리큐르 1/2 oz"]
        },
        "애플마티니": {
            "method": "Shake", "glass": "칵테일", "garnish": "사과슬라이스",
            "ingredients": ["보드카 1 oz", "애플퍼커 1 oz", "라임주스 1/2 oz"]
        },
        "코스모폴리탄": {
            "method": "Shake", "glass": "칵테일", "garnish": "레몬필",
            "ingredients": ["보드카 1 oz", "트리플섹 1/2 oz", "라임주스 1/2 oz", "크랜베리주스 1/2 oz"]
        }
    },
    "진 베이스": {
        "드라이마티니": {
            "method": "Stir", "glass": "칵테일", "garnish": "그린올리브",
            "ingredients": ["드라이진 2 oz", "드라이베르무트 1/3 oz"]
        },
        "싱가폴슬링": {
            "method": "Shake & Build", "glass": "풋티드 필스너", "garnish": "오렌지 + 체리",
            "ingredients": ["드라이진 1 1/2 oz", "레몬주스 1/2 oz", "파우더슈가 1 tsp", "소다수 Fill", "체리브랜디 1/2 oz"]
        },
        "진피즈": {
            "method": "Shake & Build", "glass": "하이볼", "garnish": "레몬슬라이스",
            "ingredients": ["드라이진 1 1/2 oz", "레몬주스 1/2 oz", "파우더슈가 1 tsp", "소다수 Fill"]
        },
        "네그로니": {
            "method": "Build", "glass": "올드패션드", "garnish": "레몬필",
            "ingredients": ["드라이진 3/4 oz", "스윗베르무트 3/4 oz", "캄파리 3/4 oz"]
        }
    },
    "전통주 베이스": {
        "고창": {
            "method": "Stir", "glass": "플루트샴페인", "garnish": "X",
            "ingredients": ["진도홍주 1 oz", "트리플섹 1/2 oz", "애플퍼커 1/2 oz", "라임주스 1/3 oz"]
        },
        "힐링": {
            "method": "Shake", "glass": "칵테일", "garnish": "레몬필",
            "ingredients": ["감홍로 1 1/2 oz", "베네딕틴 1/3 oz", "크림드카시스 1/3 oz", "스윗사워 1 oz"]
        },
        "금산": {
            "method": "Shake", "glass": "칵테일", "garnish": "X",
            "ingredients": ["금산인삼주 1 1/2 oz", "커피리큐르 1/2 oz", "애플퍼커 1/2 oz", "라임주스 1 tsp"]
        },
        "진도": {
            "method": "Shake", "glass": "칵테일", "garnish": "X",
            "ingredients": ["복분자와인 2 oz", "트리플섹 1/2 oz", "스프라이트 2 oz"]
        },
        "풋사랑": {
            "method": "Shake", "glass": "칵테일", "garnish": "사과슬라이스",
            "ingredients": ["안동소주 1 oz", "트리플섹 1/3 oz", "애플퍼커 1 oz", "라임주스 1/3 oz"]
        }
    },
    "브랜디 베이스": {
        "사이드카": {
            "method": "Shake", "glass": "칵테일", "garnish": "X",
            "ingredients": ["브랜디 1 oz", "트리플섹 1 oz", "레몬주스 1/4 oz"]
        },
        "허니문": {
            "method": "Shake", "glass": "칵테일", "garnish": "X",
            "ingredients": ["애플브랜디 3/4 oz", "베네딕틴 3/4 oz", "트리플섹 1/4 oz", "레몬주스 1/2 oz"]
        },
        "브랜디 알렉산더": {
            "method": "Shake", "glass": "칵테일", "garnish": "넛멕가루",
            "ingredients": ["브랜디 3/4 oz", "크림드카카오 3/4 oz", "우유 3/4 oz"]
        },
        "푸스카페": {
            "method": "Float", "glass": "스탠드 리큐어", "garnish": "X",
            "ingredients": ["그라나딘 1/3 part", "크림드멘트(그린) 1/3 part", "브랜디 1/3 part"]
        }
    },
    "기타 베이스": {
        "롱아일랜드아이스티": {
            "method": "Build", "glass": "콜린스", "garnish": "웨지레몬",
            "ingredients": ["진,럼,보드카,테킬라 1/2 oz씩", "트리플섹 1/2 oz", "스윗사워 1 1/2 oz", "콜라 Fill"]
        },
        "키르": {
            "method": "Build", "glass": "화이트와인", "garnish": "레몬필",
            "ingredients": ["화이트와인 3 oz", "크림드카시스 1/2 oz"]
        },
        "애프리콧": {
            "method": "Shake", "glass": "칵테일", "garnish": "X",
            "ingredients": ["애프리콧브랜디 1 1/2 oz", "드라이진 1 tsp", "레몬주스 1/2 oz", "오렌지주스 1/2 oz"]
        },
        "준벅": {
            "method": "Shake", "glass": "콜린스", "garnish": "파인애플 + 체리",
            "ingredients": ["미도리 1 oz", "말리부 1/2 oz", "바나나리큐르 1/2 oz", "파인애플주스 2 oz", "스윗사워 2 oz"]
        },
        "그라스하퍼": {
            "method": "Shake", "glass": "칵테일", "garnish": "X",
            "ingredients": ["크림드멘트(그린) 1 oz", "크림드카카오(화이트) 1 oz", "우유 1 oz"]
        },
        "B-52": {
            "method": "Build", "glass": "쉐리(2온즈)", "garnish": "X",
            "ingredients": ["커피리큐르 1/3 part", "베일리스 1/3 part", "그랑마니에르 1/3 part"]
        }
    },
    "논알콜 베이스": {
        "프레시레몬스쿼시": {
            "method": "Build", "glass": "하이볼", "garnish": "레몬슬라이스",
            "ingredients": ["프레시스퀴즈레몬 1/2 ea", "파우더슈가 2 tsp", "소다수 Fill"]
        },
        "버진프루트펀치": {
            "method": "Blend", "glass": "풋티드 필스너", "garnish": "파인애플 + 체리",
            "ingredients": ["오렌지주스 1 oz", "파인애플주스 1 oz", "크랜베리주스 1 oz"]
        }
    }
}

st.set_page_config(page_title="조주기능사 실기 레시피 대시보드", page_icon="📝", layout="centered")
st.title("📋 조주기능사 실기 레시피북 (정밀 가이드)")
st.caption("제공해주신 레시피 요약 표(image_00591d.jpg)의 분류와 계량을 완벽하게 준수하여 제작되었습니다.")

# 2. 기주(카테고리) 선택
base_list = list(COCKTAILS.keys())
selected_base = st.selectbox("🗂 기주(베이스)를 선택하세요", base_list)

# 3. 해당 기주에 속하는 칵테일 선택
cocktail_list = list(COCKTAILS[selected_base].keys())
selected_cocktail = st.radio("🍸 칵테일을 선택하세요", cocktail_list, horizontal=True)

# 4. 데이터 출력
data = COCKTAILS[selected_base][selected_cocktail]

st.markdown("---")
st.subheader(f"✨ {selected_cocktail}")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🎬 조주 기법 (Method)", value=data["method"])
with col2:
    st.metric(label="🥂 글라스 (Glass)", value=data["glass"])
with col3:
    st.metric(label="🍒 가니시 (Garnish)", value=data["garnish"])

st.markdown("---")
st.markdown("#### 📐 레시피 재료 및 용량")

# 마크다운 리스트 형태로 재료 출력
for ingredient in data["ingredients"]:
    st.markdown(f"- **{ingredient}**")

# 풋사랑 특별 알림 가이드 (과거 믹스업 방지용 안전 장치)
if selected_cocktail == "풋사랑":
    st.warning("⚠️ **시험장 유의사항:** 34번 레시피 이름은 '풋사과'가 아닌 **'풋사랑'**입니다. 안동소주 베이스와 사과슬라이스 가니시를 명확히 숙지하세요.")
