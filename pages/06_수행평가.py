import streamlit as st

# 1. 조주기능사 실기 40가지 칵테일 완벽 데이터 (개별 이미지 주소 필드 포함)
COCKTAILS = {
    "1. 푸스카페 (Pousse Cafe)": {
        "glass": "리큐르 글라스", "method": "플로팅 (Floating)",
        "ingredients": ["그레나딘 시럽 1/3", "크렘 드 멘트 그린 1/3", "브랜디 1/3층 쌓기 (지거 계량 후 바스푼 이용)"],
        "tip": "재료가 섞이지 않도록 지거는 매번 씻어주기.",
        "taste": "🌈 극도의 달콤함과 강렬한 허브·민트 향, 묵직한 브랜디의 알코올감이 층층이 느껴짐",
        "story": "프랑스어로 '커피를 밀어내다'라는 뜻으로, 식후에 커피를 마신 뒤 입가심으로 마시던 것에서 유래했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "2. 맨하탄 (Manhattan)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "스터 (Stir)",
        "ingredients": ["버번 위스키 1.5 oz", "스윗 베르무트 0.75 oz", "앙고스투라 비터스 1 dash"],
        "garnish": "체리 픽", "tip": "믹싱글라스에 얼음과 재료를 넣고 저은 후 잔에 따름.",
        "taste": "🥃 위스키의 부드럽고 매콤한 타격감에 달콤하고 한약재 같은 쌉싸름함이 감도는 어른의 맛",
        "story": "‘칵테일의 여왕’이라는 별명을 가졌습니다. 19세기 후반 뉴욕 맨해튼 클럽의 연회에서 처음 선보였다는 설이 유명합니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "3. 드라이 마티니 (Dry Martini)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "스터 (Stir)",
        "ingredients": ["드라이 진 2 oz", "드라이 베르무트 1/3 oz (10 ml)"],
        "garnish": "그린 올리브", "tip": "믹싱글라스에 얼음과 재료를 넣고 저은 후 잔에 따름.",
        "taste": "🍸 진의 강렬한 솔향과 허브 향이 지배적이며, 달지 않고 매우 깔끔하고 드라이함",
        "story": "‘칵테일의 왕’으로 불립니다. 제임스 본드가 '저어서 말고 흔들어서'라고 외친 바로 그 칵테일입니다.",
        "image": "https://images.unsplash.com/photo-1575444758702-4a6b9222336e?w=600"
    },
    "4. 올드 패션드 (Old Fashioned)": {
        "glass": "올드 패션드 글라스", "method": "빌드 (Build)",
        "ingredients": ["가루 설탕 1 tsp", "앙고스투라 비터스 1 dash", "소다수 0.5 oz (15 ml)", "버번 위스키 1.5 oz"],
        "garnish": "체리 & 오렌지 슬라이스", "tip": "설탕, 비터스, 소다수를 먼저 저어 녹인 뒤 얼음과 위스키를 넣고 젓는다.",
        "taste": "🍊 오렌지 시트러스 향 뒤로 설탕의 달콤함과 버번 위스키의 진한 오크 향이 묵직하게 다가옴",
        "story": "경마 팬들이 모이던 켄터키주의 한 클럽에서 바텐더가 만든 것이 시초입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "5. 브랜디 알렉산더 (Brandy Alexander)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["브랜디 3/4 oz", "크렘 드 카카오 (브라운) 3/4 oz", "우유 3/4 oz"],
        "garnish": "넛멕 파우더", "tip": "알렉산더 대왕님은 코코아를 좋아해 (3/4 oz 묶음)",
        "taste": "🍫 초콜릿 우유처럼 부드럽고 달콤하지만, 은근히 치고 올라오는 브랜디의 독한 도수",
        "story": "영국 국왕 에드워드 7세와 알렉산드라 왕비의 결혼식을 축하하기 위해 바텐더가 헌정한 칵테일입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "6. 사이드카 (Sidecar)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["브랜디 1 oz", "코인트로우 (또는 트리플 섹) 1 oz", "레몬 주스 1/4 oz"],
        "taste": "🍋 브랜디의 고급스러운 풍미에 오렌지 리큐르와 레몬의 새콤달콤함이 정교하게 어우러짐",
        "story": "제1차 세계대전 당시 매번 사이드카(오토바이 옆자리)를 타고 바에 오던 장교를 위해 만들어졌다는 설이 있습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "7. 핑크 레이디 (Pink Lady)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["드라이 진 1.5 oz", "그레나딘 시럽 1 tsp", "우유 0.5 oz (시험장에서 우유 지급 시)"],
        "taste": "🍓 부드러운 우유 느낌 뒤로 은은한 진의 향과 그레나딘 시럽의 달콤함이 예쁜 핑크빛으로 감돎",
        "story": "런던에서 개최된 연극 '핑크 레이디'의 종연 파티에서 여주인공 헤이즐 돈에게 헌정되었습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "8. 뉴욕 (New York)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["버번 위스키 1.5 oz", "라임 주스 0.5 oz", "그레나딘 시럽 1 tsp"],
        "garnish": "트위스트 레몬 필",
        "taste": "🏙 뉴욕의 노을을 닮은 붉은 빛깔, 버번의 거친 느낌을 라임과 그레나딘 시럽이 상큼하게 잡아줌",
        "story": "세계적인 대도시 뉴욕의 이름을 딴 칵테일로, 도시의 화려함과 노을빛을 형상화했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "9. 블랙 러시안 (Black Russian)": {
        "glass": "올드 패션드 글라스 (얼음 포함)", "method": "빌드 (Build)",
        "ingredients": ["보드카 1 oz", "깔루아 (커피 리큐르) 0.5 oz"],
        "tip": "도수가 매우 높으니 기법 후 살짝만 저어주기.",
        "taste": "☕ 달콤하고 진한 에스프레소 맛 뒤로 보드카의 강렬하고 깔끔한 알코올 도수가 묵직하게 다가옴",
        "story": "러시아를 상징하는 보드카와 공산주의의 어두운 이미지를 커피 리큐르의 검은색에 빗대어 탄생했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "10. 화이트 러시안 (White Russian)": {
        "glass": "올드 패션드 글라스 (얼음 포함)", "method": "빌드 또는 플로팅",
        "ingredients": ["보드카 1 oz", "깔루아 0.5 oz", "우유(또는 크림) 0.5 oz를 위에 띄우거나 섞음"],
        "taste": "🥛 블랙 러시안에 우유가 더해져 부드러운 라떼 같은 목 넘김을 자랑하지만 여전히 도수가 높음",
        "story": "블랙 러시안의 자매 칵테일로, 우유나 크림이 들어가 하얀색을 띠게 되면서 화이트 러시안이 되었습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "11. 마이타이 (Mai-Tai)": {
        "glass": "필스너 또는 발이 달린 큰 글라스", "method": "셰이킹 후 크러시드 아이스 빌드",
        "ingredients": ["화이트 럼 1.25 oz", "트리플 섹 0.75 oz", "라임 주스 0.5 oz", "파인애플 주스 1 oz", "오렌지 주스 1 oz", "그레나딘 시럽 0.25 oz (색 내기)"],
        "garnish": "파인애플 웨지 & 체리",
        "taste": "🍹 트로피컬 칵테일의 거장답게 파인애플과 오렌지의 상큼함, 럼의 달콤한 사탕수수 향이 폭발함",
        "story": "타히티어로 '최고(Mai-tai)'라는 뜻입니다. 하와이나 휴양지에서 가장 사랑받는 대표적인 트로피컬 음료입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "12. 피나 콜라다 (Pina Colada)": {
        "glass": "필스너 글라스", "method": "블렌딩 (Blenders 이용)",
        "ingredients": ["화이트 럼 1.25 oz", "피나콜라다 믹스(또는 코코넛 크림) 2 oz", "파인애플 주스 2 oz", "크러시드 아이스 1스쿱"],
        "garnish": "파인애플 웨지 & 체리",
        "taste": "🥥 코코넛의 밀키하고 고소한 풍미와 파인애플의 새콤함이 얼음과 갈려 부드러운 슬러시처럼 즐김",
        "story": "스페인어로 '파인애플이 우거진 언덕' 또는 '즙을 낸 파인애플'을 뜻하며, 푸에르토리코의 대표 칵테일입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "13. 싱가폴 슬링 (Singapore Sling)": {
        "glass": "필스너 글라스", "method": "셰이킹 후 소다수 빌드",
        "ingredients": ["드라이 진 1 oz", "체리 브랜디 0.5 oz", "레몬 주스 0.5 oz", "가루 설탕 1 tsp", "소다수 fill up"],
        "garnish": "오렌지 슬라이스 & 체리",
        "taste": "🍒 체리 브랜디의 깊은 과일 향과 레몬의 상큼함, 탄산수의 청량감이 진과 조화롭게 섞인 맛",
        "story": "싱가포르의 래플스 호텔에서 저녁 노을을 표현하기 위해 만들어진 세계적인 명작 칵테일입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "14. 키스 오브 파이어 (Kiss of Fire)": {
        "glass": "칵테일 글라스 (설탕 리밍 필수)", "method": "셰이킹 (Shaking)",
        "ingredients": ["보드카 0.75 oz", "슬로 진 0.75 oz", "드라이 베르무트 0.75 oz", "레몬 주스 1 tsp"],
        "tip": "설탕 리밍(Rimming) 먼저 하고 조주하기.",
        "taste": "🔥 입술에 닿는 설탕의 달콤함 뒤로 슬로진의 베리 향과 보드카의 화끈하고 매콤한 알코올 펀치가 옴",
        "story": "일본 바텐더가 심사위원들의 마음을 사로잡기 위해 만든 칵테일로, 뜨거운 연인들의 키스를 형상화했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "15. 키르 (Kir)": {
        "glass": "화이트 와인 글라스", "method": "빌드 (Build)",
        "ingredients": ["화이트 와인 3 oz", "크렘 드 카시스 0.5 oz"],
        "taste": "🍇 드라이한 와인의 산미 속으로 카시스(블랙커런트) 특유의 짙고 쌉싸름한 베리 달콤함이 퍼짐",
        "story": "프랑스 디종 시의 시장이었던 펠릭스 키르가 지역 특산품인 화이트 와인과 카시스를 홍보하기 위해 만들었습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "16. 네그로니 (Negroni)": {
        "glass": "올드 패션드 글라스 (얼음 포함)", "method": "빌드 (Build)",
        "ingredients": ["드라이 진 0.75 oz", "스윗 베르무트 0.75 oz", "캠파리 0.75 oz"],
        "garnish": "트위스트 오렌지 필",
        "taste": "🍊 캠파리 특유의 한약재 같은 씁쓸함이 오렌지 향, 진의 솔향과 만나 중독성 있는 쌉싸름함을 냄",
        "story": "이탈리아의 네그로니 백작이 카미파리 음료에 진을 넣어 달라고 단골 바에 주문하면서 탄생했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "17. 러스티 네일 (Rusty Nail)": {
        "glass": "올드 패션드 글라스 (얼음 포함)", "method": "빌드 (Build)",
        "ingredients": ["스카치 위스키 1 oz", "드람뷔 (Drambuie) 0.5 oz"],
        "taste": "🍯 위스키의 무거운 스모키함에 꿀과 허브로 만든 드람뷔의 진득한 달콤함이 녹아든 녹슨 못 같은 맛",
        "story": "영국 속어로 '녹슨 못'을 뜻하며, 옛날 바텐더들이 이 음료를 녹슨 못으로 저었다는 장난 섞인 야사가 있습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "18. 블랙 앤 탄 (Black and Tan)": {
        "glass": "파인트 글라스 또는 비어 글라스", "method": "빌드 및 플로팅 (Floating)",
        "ingredients": ["라거 맥주 (Pale Ale) 1/2 잔 채우기", "기네스 흑맥주 1/2 잔 스푼 이용해 층 쌓기"],
        "taste": "🍺 청량하고 가벼운 라거 맥주의 청량감 위로 쌉싸름하고 구수한 흑맥주의 초콜릿 풍미가 얹어짐",
        "story": "밝은색 탄(Tan) 맥주와 검은색 맥주를 섞어 마시던 영국 전통 스타일에서 유래했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "19. 준벅 (June Bug)": {
        "glass": "콜린스 또는 필스너 글라스", "method": "셰이킹 (Shaking)",
        "ingredients": ["멜론 리큐르 1 oz", "바나나 리큐르 0.5 oz", "말리부 럼 0.5 oz", "파인애플 주스 2 oz", "스윗 사워 믹스 1 oz"],
        "garnish": "파인애플 웨지 & 체리",
        "taste": "🍏 한국인이 가장 사랑하는 맛 중 하나로, 메로나와 바나나, 코코넛이 섞인 듯 청량하고 달콤함",
        "story": "6월의 초록색 벌레라는 뜻으로, 부산의 한 유명 바에서 한국 바텐더가 개발하여 세계로 뻗어나간 칵테일입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "20. 시 브리즈 (Sea Breeze)": {
        "glass": "하이볼 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["보드카 1.5 oz", "크랜베리 주스 3 oz", "자몽 주스 0.5 oz"],
        "garnish": "레몬 웨지",
        "taste": "🌊 이름처럼 바닷바람 같은 청량함, 크랜베리의 떫은 단맛과 자몽의 쌉싸름함이 보드카와 만나 깔끔함",
        "story": "1920년대 미국에서 유래했으며, 해변이나 휴양지에서 갈증 해소용으로 엄청난 인기를 누린 주스 스타일 칵테일입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "21. 롱 아일랜드 아이스티 (Long Island Iced Tea)": {
        "glass": "필스너 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["드라이 진 0.5 oz", "화이트 럼 0.5 oz", "보드카 0.5 oz", "데킬라 0.5 oz", "트리플 섹 0.5 oz", "스윗 사워 믹스 1.5 oz", "콜라 fill up"],
        "garnish": "레몬 웨지", "tip": "콜라를 넣기 전에 바스푼으로 먼저 저어준 뒤 콜라를 채운다.",
        "taste": "🍋 홍차는 1방울도 안 들어갔지만 신기하게 아이스티 맛이 나며, 높은 도수 대비 목 넘김이 너무 좋아 일명 '작업주'로 통함",
        "story": "1970년대 뉴욕 롱아일랜드의 바텐더가 개발했습니다. 미국 금주법 시대에 술이 아닌 홍차인 척 위장하여 마셨다는 야사도 가지고 있습니다.",
        "image": "https://experiences.alma-resort.com/wp-content/uploads/cuisine/in-room/drink-menu/long-island-iced-tea.webp"
    },
    "22. 블루 하와이 (Blue Hawaii)": {
        "glass": "필스너 또는 발이 달린 큰 글라스", "method": "셰이킹 또는 빌드",
        "ingredients": ["화이트 럼 1 oz", "블루 큐라소 0.5 oz", "라임 주스 0.5 oz", "파인애플 주스 2 oz"],
        "garnish": "파인애플 웨지 & 체리",
        "taste": "🐬 푸른 하와이 바다를 잔에 담은 비주얼, 달콤한 럼과 파인애플 맛 뒤로 오렌지 향이 살짝 스침",
        "story": "하와이 호놀룰루 카이저 와이키키 리조트의 바텐더가 하와이의 아름다운 바다를 널리 알리기 위해 고안했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "23. 코스모폴리탄 (Cosmopolitan)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["보드카 1 oz", "트리플 섹 0.5 oz", "라임 주스 0.5 oz", "크랜베리 주스 0.5 oz (예쁜 분홍빛)"],
        "garnish": "트위스트 레몬 필",
        "taste": "💋 세련되고 도시적인 맛, 크랜베리와 라임의 새콤함이 보드카의 알코올 향을 세련되게 감싸 안음",
        "story": "드라마 '섹스 앤 더 시티'에서 여주인공 캐리가 바에서 항상 주문하면서 전 세계 뉴요커들의 아이콘이 되었습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "24. 마가리타 (Margarita)": {
        "glass": "칵테일 글라스 (소금 리밍 필수)", "method": "셰이킹 (Shaking)",
        "ingredients": ["데킬라 1.5 oz", "트리플 섹 0.5 oz", "라임 주스 0.5 oz"],
        "taste": "🌵 잔 가장자리의 짭조름한 소금과 데킬라 특유의 선인장 향, 라임의 짜릿한 신맛이 입안에서 폭발함",
        "story": "바텐더가 불의의 사고로 세상을 떠난 그의 연인 '마가리타'를 기리며 그녀가 좋아하던 데킬라와 소금으로 만들었습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "25. 테킬라 선라이즈 (Tequila Sunrise)": {
        "glass": "필스너 또는 하이볼 글라스 (얼음 가득)", "method": "빌드 후 그레나딘 플로팅",
        "ingredients": ["데킬라 1.5 oz", "오렌지 주스 fill up (잔의 80%)", "그레나딘 시럽 0.5 oz 바닥으로 가라앉히기"],
        "taste": "🌅 멕시코의 강렬한 태양이 떠오르는 비주얼, 상큼한 오렌지 주스 맛으로 시작해 바닥의 달콤한 시럽으로 끝남",
        "story": "멕시코의 일출을 형상화한 칵테일로, 록 밴드 이글스(Eagles)가 동명의 노래를 발표하면서 전 세계적으로 메가 히트를 쳤습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "26. 쿠바 리브레 (Cuba Libre)": {
        "glass": "하이볼 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["화이트 럼 1.5 oz", "라임 주스 0.5 oz", "콜라 fill up"],
        "garnish": "레몬 또는 라임 웨지",
        "taste": "🇨🇺 콜라의 친숙한 청량감에 라임의 상큼함, 럼의 이국적인 사탕수수 풍미가 더해진 완벽한 밸런스",
        "story": "스페인으로부터 쿠바가 독립할 때 '자유 쿠바 만세!(Viva Cuba Libre!)'라는 건배사에서 유래된 역사적인 칵테일입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "27. 모히토 (Mojito)": {
        "glass": "하이볼 또는 하이볼 글라스", "method": "머들링 후 빌드",
        "ingredients": ["민트 잎 6~8장", "라임 1/2개 슬라이스", "가루 설탕 2 tsp (머들러로 으깨기)", "화이트 럼 1.5 oz", "소다수 fill up"],
        "taste": "🌿 민트의 극강의 신선함과 라임의 시트러스 향, 탄산수가 결합해 한 입 마시는 순간 온몸이 시원해지는 맛",
        "story": "쿠바의 전통 음료로, 대문호 어니스트 헤밍웨이가 쿠바에 머물며 '내 모히토는 라 보데기타에 있다'며 극찬했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "28. 다이키리 (Daiquiri)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["화이트 럼 1.75 oz", "라임 주스 0.75 oz", "가루 설탕 또는 시럽 1 tsp"],
        "taste": "🍋 사탕수수로 만든 럼의 은은한 단맛과 신선한 라임즙의 산미가 군더더기 없이 깔끔하게 떨어지는 맛",
        "story": "쿠바의 다이키리라는 광산에서 일하던 미국인 기술자들이 더위를 쫓기 위해 주변의 럼과 라임을 섞어 마시던 것에서 시작되었습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "29. 바카디 (Bacardi)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["바카디 화이트 럼 1.75 oz", "라임 주스 0.75 oz", "그레나딘 시럽 1 tsp (연한 핑크빛)"],
        "taste": "🍹 다이키리와 비슷하지만 그레나딘 시럽이 추가되어 은은한 석류 향과 부드러운 핑크빛 색감이 매력적임",
        "story": "뉴욕 재판소에서 '바카디 칵테일에는 반드시 바카디 사의 럼을 사용해야 한다'는 정식 판결을 내려 이름을 지켜낸 일화가 있습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "30. 가미가제 (Kamikaze)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["보드카 1 oz", "트리플 섹 0.5 oz", "라임 주스 0.5 oz"],
        "taste": "✈️ 단맛이 거의 없고 라임의 찌릿한 신맛 뒤로 보드카가 목줄기를 강하게 치고 내려가는 드라이한 타격감",
        "story": "제2차 세계대전 당시 일본의 자살 특공대 이름을 땄으며, 한 잔 마시면 정신이 번쩍 들 정도로 강렬하다는 의미입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "31. 하비 월뱅어 (Harvey Wallbanger)": {
        "glass": "하이볼 글라스 (얼음 가득)", "method": "빌드 후 갈리아노 플로팅",
        "ingredients": ["보드카 1 oz", "오렌지 주스 fill up", "갈리아노 (이탈리아 리큐르) 0.25 oz 위에 띄우기"],
        "taste": "🪵 스크루드라이버 상위 호환 버전으로, 오렌지 주스 맛 뒤로 바닐라와 아니스(향신료)의 독특한 허브 향이 감돎",
        "story": "하비라는 서퍼가 시합에 진 후 이 술을 너무 많이 마셔 바의 벽(Wall)을 쿵쿵 치며(Bang) 걸어 나갔다는 서부 야사에서 유래했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "32. 애플 마티니 (Apple Martini)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["보드카 1 oz", "애플 퍼커 (사과 리큐르) 1 oz", "라임 주스 0.25 oz"],
        "garnish": "사과 슬라이스",
        "taste": "🍏 초록빛 투명한 색감, 청사과를 한 입 베어 문 것처럼 상큼하고 달콤하며 인공적인 느낌 없이 화사함",
        "story": "전통 마티니의 변형 중 가장 성공한 버전으로, 1990년대 후반 할리우드와 트렌디한 바를 휩쓸며 모던 클래식이 되었습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "33. 슬로 진 피즈 (Sloe Gin Fizz)": {
        "glass": "하이볼 또는 콜린스 글라스", "method": "셰이킹 후 소다수 빌드",
        "ingredients": ["슬로 진 1.5 oz", "레몬 주스 0.5 oz", "가루 설탕 1 tsp", "소다수 fill up"],
        "garnish": "레몬 슬라이스",
        "taste": "🫧 자두와 베리류의 달콤 쌉싸름한 슬로진 풍미에 레몬의 산미와 탄산의 짜릿함이 어우러진 최고의 리프레셔",
        "story": "‘피즈(Fizz)’는 탄산수가 터지는 소리입니다. 야생 오얏(Sloe) 열매로 만든 진을 사용해 달콤함을 극대화했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "34. 아프리코트 (Apricot)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["살구 브랜디 (Apricot) 1.5 oz", "드라이 진 1 tsp", "레몬 주스 0.5 oz", "오렌지 주스 1 tsp"],
        "taste": "🍑 살구의 진득하고 달콤한 과육 향이 지배적이며, 아주 미량 들어간 진이 칵테일의 중심을 잡아줌",
        "story": "유럽에서 풍요를 상징하는 과일인 살구(Apricot)의 에센스를 그대로 담아내어 축하 파티에서 자주 쓰이던 음료입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "35. 위스키 사워 (Whisky Sour)": {
        "glass": "사워 글라스 (또는 소형 하이볼)", "method": "셰이킹 후 소다수 빌드 (시험장 기준 소다수 유무 확인)",
        "ingredients": ["버번 위스키 1.5 oz", "레몬 주스 0.75 oz", "가루 설탕 1 tsp", "소다수 1 oz (가볍게 터치)"],
        "garnish": "레몬 슬라이스 & 체리",
        "taste": "🍋 버번 고유의 바닐라·오크 풍미에 레몬즙의 쨍한 신맛, 설탕의 단맛이 완벽한 정삼각형을 이루는 마스터피스",
        "story": "19세기 대서양을 항해하던 선원들이 괴혈병을 예방하기 위해 위스키에 레몬을 섞어 마시던 것에서 발전했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "36. 브랜디 사워 (Brandy Sour)": {
        "glass": "사워 글라스", "method": "셰이킹 후 소다수 빌드",
        "ingredients": ["브랜디 1.5 oz", "레몬 주스 0.75 oz", "가루 설탕 1 tsp", "소다수 1 oz"],
        "garnish": "레몬 슬라이스 & 체리",
        "taste": "🍇 위스키 사워보다 포도로 만든 브랜디 특유의 고급스럽고 화사한 과일 향이 산뜻하게 피어오름",
        "story": "위스키 사워의 형제 격인 칵테일로, 영국 왕실과 귀족들이 사냥 후 휴식을 취하며 즐겨 마셨습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "37. 길벗 (Gimlet)": {
        "glass": "칵테일 글라스 (잔 칠링)", "method": "셰이킹 (Shaking)",
        "ingredients": ["드라이 진 1.5 oz", "라임 주스 (또는 코디얼) 0.5 oz", "가루 설탕 1 tsp (라임 주스가 달면 생략 가능)"],
        "garnish": "라임 슬라이스",
        "taste": "⚔️ 칼날처럼 예리하고 날카로운 솔향과 라임의 산미가 혀를 찌르는 듯한 극강의 깔끔함을 보여줌",
        "story": "영국 해군 의사였던 '김렛(Gimlet) 경'이 선원들이 진을 너무 독하게 마시는 것을 우려해 라임을 섞어 마시게 권장한 것에서 탄생했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "38. 프렌치 75 (French 75)": {
        "glass": "샴페인 플루트 글라스", "method": "셰이킹 후 샴페인 빌드",
        "ingredients": ["드라이 진 1 oz", "레몬 주스 0.5 oz", "가루 설탕 1 tsp", "샴페인(또는 스파클링 와인) fill up"],
        "garnish": "트위스트 레몬 필",
        "taste": "🍾 고급스러운 샴페인의 탄산 기포 속에서 진의 솔향과 레몬의 상큼함이 톡톡 터지며 청량감의 끝을 보여줌",
        "story": "제1차 세계대전 당시 프랑스군이 사용하던 강력한 '75mm 야포'처럼 마시면 한 방에 훅 간다는 뜻에서 붙여진 이름입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "39. 힐링 (Healing)": {
        "glass": "칵테일 또는 하이볼 글라스", "method": "셰이킹 또는 빌드",
        "ingredients": ["감홍로 (또는 전통 약재 리큐르) 1 oz", "베네딕틴 D.O.M 0.5 oz", "크랜베리 주스 fill up"],
        "taste": "🪵 한국 전통주의 은은한 약재·계피 향과 프랑스 수도원 비법 술 베네딕틴의 허브 단맛이 크랜베리와 만나 묘한 안정감을 줌",
        "story": "조주기능사 실기 시험에 도입된 한국 전통주 베이스 칵테일 중 하나로, 지친 현대인을 치유(Healing)한다는 의미입니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    },
    "40. 프레시 레몬 스쿼시 (Fresh Lemon Squash)": {
        "glass": "하이볼 글라스 (얼음 가득)", "method": "빌드 (Build)",
        "ingredients": ["생레몬 1/2개 스퀴즈 주스", "가루 설탕(또는 시럽) 2 tsp", "소다수 fill up"],
        "garnish": "레몬 슬라이스",
        "taste": "🍋 인공 시럽이 아닌 진짜 생레몬을 짜 넣어 머리가 띵할 정도로 신선하고 짜릿한 천연 레모네이드 맛",
        "story": "‘스쿼시(Squash)’는 과일을 '쥐어짜다'라는 뜻입니다. 신선한 비타민을 그대로 섭취하기 위해 바에서 즉석으로 짜주던 음료에서 유래했습니다.",
        "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
    }
}

st.set_page_config(page_title="조주기능사 40개 레시피 마스터", page_icon="🍸", layout="centered")
st.title("🍸 조주기능사 실기 레시피 40가지 마스터")

# 2. 칵테일 선택 대화상자
selected_name = st.selectbox("👉 분석할 칵테일을 선택하세요", list(COCKTAILS.keys()))
data = COCKTAILS[selected_name]

st.markdown("---")

# 3. 데이터에 등록된 개별 이미지 주소를 다이렉트로 호출 (없으면 기본 이미지 바인딩)
search_query = selected_name.split(". ")[1].split(" (")[0]
default_image = "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"
image_url = data.get("image", default_image)

st.image(image_url, caption=f"📸 {search_query} 연출 예시 이미지", use_container_width=True)

# 4. 상세 설명 표기
st.markdown(f"### 🥂 글라스: <span style='color:blue; font-weight:bold;'>{data['glass']}</span>", unsafe_allow_html=True)
st.write(f"**🎬 조주 기법:** {data['method']}")

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### 👅 어떤 맛인가요?")
    st.caption(data["taste"])
with col2:
    st.markdown("#### 📜 어떤 유래가 있나요?")
    st.caption(data["story"])
st.markdown("---")

st.markdown("#### 📐 레시피 (oz 규격)")
for ing in data["ingredients"]:
    st.markdown(f"- {ing}")

if "garnish" in data:
    st.markdown(f"**🍒 가니시:** {data['garnish']}")

if "tip" in data:
    st.info(f"💡 **블로그 암기/조주 팁:** {data['tip']}")
