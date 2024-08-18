import streamlit as st
import random

# 질문 및 답변 데이터
questions = [
    {
        "question": "럭키비키의 뜻은?",
        "options": [
            "무엇인가를 매우 잘했을 때 사용하는 표현",
            "행운의 여신이 찾아온 상황",
            "갑자기 운이 좋아지는 현상",
            "비키니를 입고 운동하는 사람"
        ],
        "answer": "무엇인가를 매우 잘했을 때 사용하는 표현"
    },
    {
        "question": "민지적 사고의 뜻은?",
        "options": [
            "민주주의적 사고방식",
            "MZ세대가 생각하는 특유의 사고방식",
            "민첩하고 지적인 사고력",
            "민감한 주제에 대한 지적 탐구"
        ],
        "answer": "MZ세대가 생각하는 특유의 사고방식"
    },
    {
        "question": "킵고잉의 뜻은?",
        "options": [
            "계속해서 물건을 보관하는 행위",
            "영어 공부를 지속하는 것",
            "힘들어도 계속 나아가자는 의미",
            "키보드로 계속 타이핑하는 것"
        ],
        "answer": "힘들어도 계속 나아가자는 의미"
    },
    {
        "question": "요아소비 빠따정의 뜻은?",
        "options": [
            "요가와 아이스크림을 즐기는 모임",
            "요리하는 아이돌 팬덤",
            "일본 그룹 요아소비와 관련된 밈",
            "요즘 아이들의 소비 패턴"
        ],
        "answer": "일본 그룹 요아소비와 관련된 밈"
    },
    {
        "question": "기습숭배의 뜻은?",
        "options": [
            "갑자기 유행하는 종교 활동",
            "예상치 못한 찬양을 의미하는 말",
            "기습적으로 팬이 되는 현상",
            "숭고한 가치를 갑자기 깨닫는 순간"
        ],
        "answer": "예상치 못한 찬양을 의미하는 말"
    },
    {
        "question": "아마개똥의 뜻은?",
        "options": [
            "아마존에서 발견된 새로운 동물 배설물",
            "아마추어가 만든 형편없는 결과물",
            "에스파의 신곡 '아마겟돈'에서 파생된 말",
            "아이돌의 실수를 귀엽게 표현하는 말"
        ],
        "answer": "에스파의 신곡 '아마겟돈'에서 파생된 말"
    },
    {
        "question": "도미라클의 뜻은?",
        "options": [
            "도미노 피자의 새로운 메뉴",
            "도미니카 공화국의 경제 기적",
            "도미노 효과처럼 연쇄적으로 좋은 일이 일어나는 현상",
            "도마뱀이 꼬리를 재생하는 신기한 현상"
        ],
        "answer": "도미노 효과처럼 연쇄적으로 좋은 일이 일어나는 현상"
    },
    {
        "question": "핑프의 뜻은?",
        "options": [
            "핑크색 프릴 장식",
            "핑거 프린트의 줄임말",
            "핑계 대는 프로 선수",
            "핑계 없는 프리패스, 즉 변명할 필요가 없을 때 사용"
        ],
        "answer": "핑계 없는 프리패스, 즉 변명할 필요가 없을 때 사용"
    },
    {
        "question": "직관력 만렙의 뜻은?",
        "options": [
            "직접 관찰하는 능력이 최고조에 달한 상태",
            "직관적으로 상황을 잘 이해할 때 사용하는 말",
            "직업을 통해 얻은 통찰력이 최고 수준",
            "직선적으로 생각하는 능력이 뛰어난 사람"
        ],
        "answer": "직관적으로 상황을 잘 이해할 때 사용하는 말"
    },
    {
        "question": "빙산의 일각의 뜻은?",
        "options": [
            "빙수의 맨 위 부분",
            "빙하의 가장 높은 꼭대기",
            "겉으로 드러난 것은 극히 일부라는 의미",
            "빙판길에서 가장 미끄러운 부분"
        ],
        "answer": "겉으로 드러난 것은 극히 일부라는 의미"
    },
    {
        "question": "크루키의 뜻은?",
        "options": [
            "크루즈선의 쿠키 모양 디저트",
            "크루(crew)와 쿠키(cookies)를 합친 말, 단체 활동에서 자주 사용",
            "크루엘라의 새끼 강아지",
            "크루저 바이크의 키 모양"
        ],
        "answer": "크루(crew)와 쿠키(cookies)를 합친 말, 단체 활동에서 자주 사용"
    },
    {
        "question": "취미부자의 뜻은?",
        "options": [
            "취미로 돈을 많이 버는 사람",
            "취미가 아주 많은 사람을 의미",
            "취한 상태에서 부자가 된 것 같은 착각",
            "취미 생활에 돈을 많이 쓰는 사람"
        ],
        "answer": "취미가 아주 많은 사람을 의미"
    },
    {
        "question": "잡덕의 뜻은?",
        "options": [
            "잡지를 수집하는 덕후",
            "잡다한 물건을 모으는 사람",
            "여러 취미나 분야에 폭넓은 관심을 가진 사람",
            "잡기술을 가진 전문가"
        ],
        "answer": "여러 취미나 분야에 폭넓은 관심을 가진 사람"
    },
    {
        "question": "퇴사각의 뜻은?",
        "options": [
            "퇴근 시간에 회사를 나가는 각도",
            "퇴직금을 받을 때의 기분",
            "퇴사를 진지하게 고민하는 상황을 의미",
            "퇴근 후 사우나에 가는 습관"
        ],
        "answer": "퇴사를 진지하게 고민하는 상황을 의미"
    },
    {
        "question": "플렉스의 뜻은?",
        "options": [
            "근육을 과시하는 행위",
            "자신이 가진 것을 자랑할 때 사용하는 말",
            "유연성 있는 근무 형태",
            "플라스틱으로 만든 고급 제품"
        ],
        "answer": "자신이 가진 것을 자랑할 때 사용하는 말"
    },
    {
        "question": "할말하않의 뜻은?",
        "options": [
            "할머니의 말씀을 하지 않음",
            "할 일을 말로만 하고 실천하지 않음",
            "할 말은 많지만 하지 않겠다는 의미",
            "할인 행사를 말로 홍보하지 않음"
        ],
        "answer": "할 말은 많지만 하지 않겠다는 의미"
    },
    {
        "question": "잠만보의 뜻은?",
        "options": [
            "잠자는 모습만 보이는 사람",
            "잠깐만 보고 오겠다는 의미",
            "매우 게으른 사람을 가리키는 말",
            "잠들기 전에 마지막으로 보는 것"
        ],
        "answer": "매우 게으른 사람을 가리키는 말"
    },
    {
        "question": "문찐의 뜻은?",
        "options": [
            "문학을 좋아하는 괴짜",
            "문을 자주 여닫는 사람",
            "문화를 잘 따라가지 못하는 사람",
            "문제를 잘 푸는 천재"
        ],
        "answer": "문화를 잘 따라가지 못하는 사람"
    },
    {
        "question": "현타의 뜻은?",
        "options": [
            "현금으로 물건을 구매하는 타이밍",
            "현재에 만족하는 타입의 사람",
            "현관문을 닫는 타이밍",
            "현실 자각 타임, 이상과 현실의 괴리를 느낄 때 사용하는 말"
        ],
        "answer": "현실 자각 타임, 이상과 현실의 괴리를 느낄 때 사용하는 말"
    },
    {
        "question": "알잘딱깔센의 뜻은?",
        "options": [
            "알뜰하고 잘생긴 딱부리와 깔끔한 센스",
            "알아서 잘 딱 깔끔하고 센스 있게 해주는 사람을 의미",
            "알록달록한 색으로 잘 꾸민 깔끔한 센터",
            "알바생이 잘하는 딱 맞는 깔끔한 서비스"
        ],
        "answer": "알아서 잘 딱 깔끔하고 센스 있게 해주는 사람을 의미"
    }
]

def get_result_message(score, total):
    if score <= 5:
        return "혹시 꼰대신가요?"
    elif score <= 10:
        return "아제라고 불러다오~"
    elif score <= 15:
        return "찾았다 MZ"
    else:
        return "당신은 초인싸군요!"

def main():
    st.title("MZ 신조어 테스트")
    st.write("당신의 MZ 레벨을 알아보세요!")

    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.questions = random.sample(questions, len(questions))

    if st.session_state.question_index < len(st.session_state.questions):
        question = st.session_state.questions[st.session_state.question_index]
        st.write(f"문제 {st.session_state.question_index + 1}")
        st.write(question['question'])

        options = random.sample(question['options'], len(question['options']))
        answer = st.radio("정답을 선택하세요:", options, key=f"question_{st.session_state.question_index}")

        if st.button("다음"):
            if answer == question['answer']:
                st.session_state.score += 1
            st.session_state.question_index += 1
            st.experimental_rerun()

    else:
        st.write("테스트 완료!")
        st.write(f"맞힌 문제: {st.session_state.score} / {len(questions)}")
        result_message = get_result_message(st.session_state.score, len(questions))
        st.write(result_message)

        if st.button("다시 시작"):
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.questions = random.sample(questions, len(questions))
            st.experimental_rerun()

if __name__ == "__main__":
    main()