# 한글 놀이터

만 4세 아이가 부모와 함께 하루 10분씩 한글을 익히는 놀이형 웹페이지입니다.
위키독스 학습책『우리 아이 첫 한글: 4살 한글 놀이책』과 단원 번호(예: `1-1`)로 연결됩니다.

- 놀이터: https://goodhosup.github.io/hangul-playground/
- 위키독스 원고: [`wikidocs/`](wikidocs/README.md)

## 단계와 놀이

| 단계 | 단원 | 놀이 페이지 |
|---|---|---|
| 0 말소리 놀이 | 0-1 ~ 0-3 | `listen.html` (끝말 잇기·첫소리 찾기·손뼉 치기) |
| 1 그림 통글자 | 1-1 ~ 1-6 | `cards.html`, `match.html`, `name.html`, `bingo.html` |
| 2 모음 친구 | 2-1 ~ 2-5 | `sound.html`, `quiz.html`, `trace.html` |
| 3 자음 친구 | 3-1 ~ 3-11 | `sound.html`, `quiz.html`, `trace.html` |
| 4 글자 블록 | 4-1 ~ 4-4 | `blocks.html`, `table.html`, `split.html` |
| 5 받침 글자 | 5-1 ~ 5-7 | `cards.html`, `blocks.html`, `match.html` |
| 6 짧은 문장 | 6-1 ~ 6-3 | `read.html` |

그 밖에 `index.html`(놀이터 지도), `stickers.html`(스티커판), `parent.html`(부모방: 아이 이름, 소리 테스트, 열어 둘 단계, 진도, 초기화)이 있습니다.

## 내용 고치기

학습 데이터와 위키독스 원고는 한 곳에서 만들어집니다.

1. `tools/content.py` — 낱말, 자모, 단원, 문장
2. `tools/wikidocs_text.py` — 위키독스 단원 본문(손으로 쓴 부분)
3. `python3 tools/build.py` 실행 → `data/*.json` 과 `wikidocs/*.md` 가 다시 만들어집니다.

## 소리

브라우저의 한국어 음성합성을 씁니다. 직접 녹음한 mp3를 `audio/`에 넣고 `data/words.json`의 `audio` 값에 경로를 적으면 그 파일을 먼저 재생합니다.

## 개인정보

진도와 아이 이름은 사용하는 기기의 브라우저에만 저장되며 어디에도 전송되지 않습니다.

## 그림

그림은 기기 내장 이모지를 사용합니다.
