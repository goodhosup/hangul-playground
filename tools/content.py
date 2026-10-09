"""한글 놀이터 학습 데이터의 원본.

이 파일을 고친 뒤 `python3 tools/build.py` 를 실행하면
data/*.json 과 wikidocs/*.md 가 다시 만들어진다.
"""

SITE = "https://goodhosup.github.io/hangul-playground/"

# id, 글자, 그림, 단원 ("ex" = 예시·보기 전용 단어)
WORDS = [
    # 1단계 통글자
    ("apple", "사과", "🍎", "1-1"), ("banana", "바나나", "🍌", "1-1"), ("grape", "포도", "🍇", "1-1"),
    ("strawberry", "딸기", "🍓", "1-1"), ("watermelon", "수박", "🍉", "1-1"),
    ("dog", "개", "🐶", "1-2"), ("cat", "고양이", "🐱", "1-2"), ("rabbit", "토끼", "🐰", "1-2"),
    ("lion", "사자", "🦁", "1-2"), ("duck", "오리", "🦆", "1-2"),
    ("train", "기차", "🚂", "1-3"), ("bus", "버스", "🚌", "1-3"), ("car", "자동차", "🚗", "1-3"),
    ("ship", "배", "🚢", "1-3"), ("airplane", "비행기", "✈️", "1-3"),
    ("mom", "엄마", "👩", "1-4"), ("dad", "아빠", "👨", "1-4"), ("baby", "아기", "👶", "1-4"),
    ("grandma", "할머니", "👵", "1-4"), ("grandpa", "할아버지", "👴", "1-4"),
    # 5단계 받침 글자
    ("ball", "공", "🏐", "5-1"), ("river", "강", "🏞️", "5-1"), ("bread", "빵", "🍞", "5-1"), ("dragon", "용", "🐉", "5-1"),
    ("snow", "눈", "❄️", "5-2"), ("mountain", "산", "⛰️", "5-2"), ("door", "문", "🚪", "5-2"), ("hand", "손", "✋", "5-2"),
    ("bear", "곰", "🐻", "5-3"), ("island", "섬", "🏝️", "5-3"), ("sleep", "잠", "😴", "5-3"), ("dance", "춤", "💃", "5-3"),
    ("moon", "달", "🌙", "5-4"), ("foot", "발", "🦶", "5-4"), ("water", "물", "💧", "5-4"), ("horse", "말", "🐴", "5-4"), ("star", "별", "⭐", "5-4"),
    ("book", "책", "📚", "5-5"), ("medicine", "약", "💊", "5-5"), ("soup", "국", "🍲", "5-5"), ("ricecake", "떡", "🍡", "5-5"),
    ("rice", "밥", "🍚", "5-6"), ("mouth", "입", "👄", "5-6"), ("house", "집", "🏠", "5-6"), ("cup", "컵", "🥤", "5-6"),
    # 예시 단어 (말소리 놀이, 자모 예시, 보기)
    ("cookie", "과자", "🍪", "ex"), ("bike", "자전거", "🚲", "ex"), ("turtle", "거북이", "🐢", "ex"), ("tooth", "이빨", "🦷", "ex"),
    ("butterfly", "나비", "🦋", "ex"), ("giraffe", "기린", "🦒", "ex"), ("sweetpotato", "고구마", "🍠", "ex"),
    ("mask", "마스크", "😷", "ex"), ("crayon", "크레파스", "🖍️", "ex"), ("ski", "스키", "⛷️", "ex"), ("kiwi", "키위", "🥝", "ex"),
    ("bag", "가방", "🎒", "ex"), ("scissors", "가위", "✂️", "ex"), ("sea", "바다", "🌊", "ex"), ("cucumber", "오이", "🥒", "ex"),
    ("tomato", "토마토", "🍅", "ex"), ("tree", "나무", "🌳", "ex"), ("fork", "포크", "🍴", "ex"), ("sun", "해", "☀️", "ex"),
    ("snowman", "눈사람", "⛄", "ex"), ("song", "노래", "🎵", "ex"), ("acorn", "도토리", "🌰", "ex"), ("pig", "돼지", "🐷", "ex"),
    ("bridge", "다리", "🌉", "ex"), ("ramen", "라면", "🍜", "ex"), ("robot", "로봇", "🤖", "ex"), ("lemon", "레몬", "🍋", "ex"),
    ("ribbon", "리본", "🎀", "ex"), ("hat", "모자", "🧢", "ex"), ("rainbow", "무지개", "🌈", "ex"), ("cow", "소", "🐮", "ex"),
    ("milk", "우유", "🥛", "ex"), ("juice", "주스", "🧃", "ex"), ("earth", "지구", "🌍", "ex"), ("cheese", "치즈", "🧀", "ex"),
    ("soccer", "축구", "⚽", "ex"), ("toothbrush", "칫솔", "🪥", "ex"), ("cherry", "체리", "🍒", "ex"), ("elephant", "코끼리", "🐘", "ex"),
    ("cake", "케이크", "🍰", "ex"), ("truck", "트럭", "🚚", "ex"), ("tent", "텐트", "⛺", "ex"), ("pizza", "피자", "🍕", "ex"),
    ("penguin", "펭귄", "🐧", "ex"), ("hippo", "하마", "🦛", "ex"), ("tiger", "호랑이", "🐯", "ex"), ("cloud", "구름", "☁️", "ex"),
    ("spider", "거미", "🕷️", "ex"), ("baseball", "야구", "⚾", "ex"), ("palm", "야자수", "🌴", "ex"), ("fox", "여우", "🦊", "ex"),
    ("yoyo", "요요", "🪀", "ex"), ("cooking", "요리", "🍳", "ex"), ("tangerine", "귤", "🍊", "ex"), ("tissue", "휴지", "🧻", "ex"),
]

# 자모: 글자, 이름(읽는 말), 모양 이야기, 예시 단어 id
VOWELS = [
    ("ㅏ", "아", "기둥 옆으로 작은 팔이 밖으로 뻗었어요", ["baby", "apple", "banana"]),
    ("ㅣ", "이", "똑바로 선 막대기예요", ["train", "tooth", "giraffe"]),
    ("ㅗ", "오", "땅 위에 작은 새싹이 위로 쏙 나왔어요", ["duck", "grape", "sweetpotato"]),
    ("ㅜ", "우", "땅 아래로 뿌리가 쏙 내려갔어요", ["milk", "watermelon", "cloud"]),
    ("ㅓ", "어", "기둥 왼쪽으로 작은 팔이 뻗었어요", ["spider", "turtle", "bus"]),
    ("ㅡ", "으", "옆으로 누운 막대기예요", ["crayon", "ski", "truck"]),
    ("ㅑ", "야", "ㅏ에 팔이 하나 더! 두 팔이 밖으로", ["baseball", "palm"]),
    ("ㅕ", "여", "ㅓ에 팔이 하나 더! 두 팔이 왼쪽으로", ["fox", "star"]),
    ("ㅛ", "요", "새싹이 두 개 쏙쏙", ["yoyo", "cooking"]),
    ("ㅠ", "유", "뿌리가 두 개 쑥쑥", ["milk", "tangerine", "tissue"]),
]

CONSONANTS = [
    ("ㄱ", "기역", "기차의 '기'", "기차 선로처럼 꺾인 모양", ["train", "bag", "cat", "turtle"]),
    ("ㄴ", "니은", "나비의 '나'", "ㄱ을 거꾸로 뒤집은 의자 모양", ["butterfly", "tree", "snowman", "song"]),
    ("ㄷ", "디귿", "도토리의 '도'", "입을 오른쪽으로 벌린 모양", ["acorn", "pig", "bridge", "moon"]),
    ("ㄹ", "리을", "로봇의 '로'", "구불구불 뱀이 지나간 길", ["ramen", "robot", "lemon", "ribbon"]),
    ("ㅁ", "미음", "모자의 '모'", "네모난 상자", ["hat", "horse", "rainbow", "door"]),
    ("ㅂ", "비읍", "바다의 '바'", "물을 담는 양동이", ["sea", "bus", "banana", "ship"]),
    ("ㅅ", "시옷", "사자의 '사'", "다리를 벌린 사람, 산꼭대기", ["lion", "cow", "apple", "watermelon"]),
    ("ㅇ", "이응", "오리의 '오'", "동그란 공", ["duck", "milk", "cucumber", "baby"]),
    ("ㅈ", "지읒", "자동차의 '자'", "ㅅ 위에 모자를 쓴 모양", ["car", "juice", "bike", "earth"]),
    ("ㅊ", "치읓", "치즈의 '치'", "ㅈ 위에 꼭지가 하나 더", ["cheese", "soccer", "toothbrush", "cherry"]),
    ("ㅋ", "키읔", "코끼리의 '코'", "ㄱ 가운데 줄이 하나 더", ["elephant", "cake", "kiwi", "crayon"]),
    ("ㅌ", "티읕", "토끼의 '토'", "ㄷ 가운데 줄이 하나 더", ["rabbit", "tomato", "truck", "tent"]),
    ("ㅍ", "피읖", "포도의 '포'", "기둥 두 개를 위아래로 덮은 문", ["grape", "pizza", "penguin", "fork"]),
    ("ㅎ", "히읗", "하마의 '하'", "모자 쓴 동그란 얼굴", ["hippo", "tiger", "sun", "grandma"]),
]

# 받침 단원에서 쓰는 받침 소리
FINALS = {"ㅇ": "응", "ㄴ": "은", "ㅁ": "음", "ㄹ": "을", "ㄱ": "윽", "ㅂ": "읍"}

# 0단계 말소리 놀이 데이터
CHAINS = [
    ["apple", "cookie", "bike", "turtle", "tooth"],
    ["butterfly", "airplane", "giraffe"],
    ["sweetpotato", "mask", "crayon", "ski", "kiwi"],
]
FIRST_PAIRS = [
    ["bag", "scissors"], ["banana", "sea"], ["lion", "apple"], ["duck", "cucumber"],
    ["rabbit", "tomato"], ["cat", "sweetpotato"], ["butterfly", "tree"], ["grape", "fork"],
]
CLAP_WORDS = ["dog", "apple", "banana", "grandpa", "ship", "train", "cat", "sun", "car", "watermelon"]

# 6단계 문장
SENTENCES = {
    "6-1": [("엄마 사랑해", "👩❤️"), ("아빠 고마워", "👨🙏"), ("할머니 안녕", "👵👋")],
    "6-2": [("기차가 가요", "🚂"), ("비행기가 날아요", "✈️"), ("토끼가 뛰어요", "🐰"), ("오리가 헤엄쳐요", "🦆")],
    "6-3": [("곰이 잠을 자요", "🐻😴"), ("달이 떴어요", "🌙"), ("나비가 꽃에 앉았어요", "🦋🌸"), ("강아지가 멍멍 짖어요", "🐶")],
}

STAGES = [
    (0, "말소리 놀이", "👂"), (1, "그림 글자", "🍎"), (2, "모음 친구", "ㅏ"), (3, "자음 친구", "ㄱ"),
    (4, "글자 블록", "가"), (5, "받침 글자", "공"), (6, "짧은 문장", "📖"),
]

ALL_VOWELS = [v[0] for v in VOWELS]
BASIC_VOWELS = ALL_VOWELS[:6]
ALL_CONS = [c[0] for c in CONSONANTS]


def _units():
    U = []

    def add(unit, title, icon, acts, **extra):
        stage = int(unit.split("-")[0])
        U.append(dict(unit=unit, stage=stage, title=title, icon=icon, acts=acts, **extra))

    add("0-1", "끝말 잇기", "🔗", ["chain"])
    add("0-2", "첫소리가 같은 말", "👂", ["first"])
    add("0-3", "손뼉 치며 글자 세기", "👏", ["clap"])

    add("1-1", "맛있는 과일", "🍎", ["cards", "match"])
    add("1-2", "동물 친구", "🐶", ["cards", "match"])
    add("1-3", "부릉부릉 탈것", "🚂", ["cards", "match"])
    add("1-4", "우리 가족", "👩", ["cards", "match"])
    add("1-5", "내 이름 글자", "📛", ["name"])
    add("1-6", "복습 · 통글자 빙고", "🎲", ["bingo", "match"], review=True)

    add("2-1", "입을 크게 ㅏ, 옆으로 ㅣ", "ㅏ", ["sound", "quiz", "trace"], jamo=["ㅏ", "ㅣ"])
    add("2-2", "동그랗게 ㅗ, 쭉 내밀어 ㅜ", "ㅗ", ["sound", "quiz", "trace"], jamo=["ㅗ", "ㅜ"])
    add("2-3", "ㅓ 와 ㅡ", "ㅓ", ["sound", "quiz", "trace"], jamo=["ㅓ", "ㅡ"])
    add("2-4", "짝꿍 모음 ㅑ ㅕ ㅛ ㅠ", "ㅑ", ["sound", "quiz", "trace"], jamo=["ㅑ", "ㅕ", "ㅛ", "ㅠ"])
    add("2-5", "복습 · 모음 몸으로 만들기", "🤸", ["quiz", "sound"], jamo=ALL_VOWELS, review=True)

    for i, c in enumerate(CONSONANTS[:9]):
        ex = [w for w in c[4]][:2]
        names = "·".join(dict((w[0], w[1]) for w in WORDS)[e] for e in ex)
        add(f"3-{i+1}", f"{c[0]} ({names})", c[0], ["sound", "quiz", "trace"], jamo=[c[0]])
    add("3-10", "거센소리 친구들 ㅊ ㅋ ㅌ ㅍ ㅎ", "ㅊ", ["sound", "quiz", "trace"], jamo=ALL_CONS[9:])
    add("3-11", "복습 · 자음 보물찾기", "💎", ["quiz", "sound"], jamo=ALL_CONS, review=True)

    add("4-1", "ㄱ + ㅏ = 가", "🧱", ["blocks"], blocks=dict(cons=["ㄱ", "ㄴ", "ㄷ"], vows=["ㅏ", "ㅣ", "ㅗ"], fins=[]))
    add("4-2", "가나다 노래", "🎶", ["table", "blocks"], blocks=dict(cons=ALL_CONS, vows=["ㅏ"], fins=[]))
    add("4-3", "통글자 다시 쪼개 보기", "✂️", ["split"])
    add("4-4", "복습 · 글자 블록 대회", "🏆", ["blockquiz", "blocks"], review=True,
        blocks=dict(cons=ALL_CONS, vows=BASIC_VOWELS, fins=[]))

    fin_units = [("5-1", "ㅇ"), ("5-2", "ㄴ"), ("5-3", "ㅁ"), ("5-4", "ㄹ"), ("5-5", "ㄱ"), ("5-6", "ㅂ")]
    for unit, f in fin_units:
        ws = [w[1] for w in WORDS if w[3] == unit][:3]
        add(unit, f"{f} 받침 ({', '.join(ws)})", f, ["cards", "blocks", "match"],
            final=f, blocks=dict(cons=["ㄱ", "ㄴ", "ㄷ", "ㅁ", "ㅂ", "ㅅ"], vows=["ㅏ", "ㅗ", "ㅜ", "ㅣ"], fins=[f]))
    add("5-7", "복습 · 받침 낚시 놀이", "🎣", ["match", "cards", "blockquiz"], review=True,
        blocks=dict(cons=["ㄱ", "ㄴ", "ㄷ", "ㅁ", "ㅂ", "ㅅ"], vows=["ㅏ", "ㅗ", "ㅜ", "ㅣ"], fins=[f for _, f in fin_units]))

    add("6-1", "가족에게 하는 말", "💌", ["read"])
    add("6-2", "움직이는 말", "🏃", ["read"])
    add("6-3", "그림책 한 줄 읽기", "📖", ["read"])
    return U


UNITS = _units()
