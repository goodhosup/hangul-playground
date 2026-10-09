// 공통 도우미: 데이터 불러오기, 주소 파라미터, 상단 바, 칭찬 효과
const ACTS = {
  learn:     { page: 'learn.html',  icon: '👶', label: '처음 배우기' },
  cards:     { page: 'cards.html',  icon: '🃏', label: '그림 카드' },
  match:     { page: 'match.html',  icon: '🎯', label: '짝 맞추기' },
  chain:     { page: 'listen.html', icon: '🔗', label: '끝말 잇기' },
  first:     { page: 'listen.html', icon: '👂', label: '첫소리 찾기' },
  clap:      { page: 'listen.html', icon: '👏', label: '손뼉 치기' },
  name:      { page: 'name.html',   icon: '📛', label: '내 이름' },
  bingo:     { page: 'bingo.html',  icon: '🎲', label: '빙고' },
  sound:     { page: 'sound.html',  icon: '🔊', label: '소리 버튼' },
  quiz:      { page: 'quiz.html',   icon: '❓', label: '소리 퀴즈' },
  trace:     { page: 'trace.html',  icon: '✍️', label: '따라 쓰기' },
  blocks:    { page: 'blocks.html', icon: '🧱', label: '글자 블록' },
  blockquiz: { page: 'blocks.html', icon: '🏆', label: '블록 퀴즈', extra: '&quiz=1' },
  table:     { page: 'table.html',  icon: '🔤', label: '가나다표' },
  split:     { page: 'split.html',  icon: '✂️', label: '쪼개기' },
  read:      { page: 'read.html',   icon: '📖', label: '문장 읽기' }
};

function actHref(act, unit) {
  const a = ACTS[act];
  return a.page + '?unit=' + unit + (a.extra || '') + (a.page === 'listen.html' ? '&mode=' + act : '');
}

const _cache = {};
async function loadJSON(path) {
  if (!_cache[path]) _cache[path] = fetch(path).then(r => r.json());
  return _cache[path];
}

function param(name) {
  return new URLSearchParams(location.search).get(name);
}

async function getUnit(unitId) {
  const units = await loadJSON('data/units.json');
  return units.find(u => u.unit === unitId) || units[0];
}

// 단원에서 쓸 단어: 복습 단원이면 같은 단계 전체
async function wordsFor(u) {
  const all = await loadJSON('data/words.json');
  return all.filter(w => u.review ? w.stage === u.stage : w.unit === u.unit);
}

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

// 단원 제목: 아이콘이 제목 첫 글자와 같으면 한 번만
function unitTitle(u) {
  return u.title.startsWith(u.icon) ? u.title : u.icon + ' ' + u.title;
}

// 상단 바: 처음으로 / 제목 / 스티커
function topbar(title) {
  const el = document.getElementById('topbar');
  if (!el) return;
  el.className = 'topbar';
  el.innerHTML = '<a class="icon-btn" href="index.html" aria-label="처음으로">🏠</a>' +
    '<div class="title" id="title"></div>' +
    '<a class="sticker-pill" href="stickers.html" aria-label="스티커판">🏅 <span data-sticker-count>0</span></a>';
  document.getElementById('title').textContent = title || '';
  stickerCount();
}

function stickerCount() {
  document.querySelectorAll('[data-sticker-count]').forEach(el => { el.textContent = Progress.get().stickers; });
}

// 첫 터치가 있어야 소리가 나는 기기(iOS)를 위한 시작 화면
function startCover(icon) {
  return new Promise(resolve => {
    const cover = document.createElement('div');
    cover.className = 'start-cover';
    cover.innerHTML = '<div class="big"></div><button class="big-btn">시작!</button>';
    cover.querySelector('.big').textContent = icon || '⭐';
    document.body.appendChild(cover);
    cover.querySelector('button').onclick = () => { cover.remove(); resolve(); };
  });
}

// 화면에 별을 흩뿌린다
function celebrate(big = false) {
  const n = big ? 24 : 10;
  for (let i = 0; i < n; i++) {
    const s = document.createElement('div');
    s.className = 'burst';
    s.textContent = ['⭐', '🌟', '✨', '💛'][i % 4];
    s.style.left = 10 + Math.random() * 80 + 'vw';
    s.style.top = 20 + Math.random() * 50 + 'vh';
    s.style.animationDelay = Math.random() * 0.3 + 's';
    document.body.appendChild(s);
    setTimeout(() => s.remove(), 1600);
  }
}

const PRAISE = ['우와, 맞았어!', '최고야!', '잘 찾았어!', '대단해!', '정답이야!'];
function praise() { return PRAISE[Math.floor(Math.random() * PRAISE.length)]; }

// 처음 배우는 아이 모드 (부모방에서 끌 수 있다): 보기 수를 줄이고 바로 힌트를 준다
function beginner() { return Progress.get().beginner !== false; }
function choiceCount() { return beginner() ? 2 : 3; }

// 틀렸을 때: 흔들고 부드럽게 다시. correct 가 있으면 정답을 반짝여 알려 준다
// (처음 배우는 아이 모드는 1번, 아니면 2번 틀린 뒤)
function wrong(btn, correct) {
  btn.classList.remove('shake');
  void btn.offsetWidth;
  btn.classList.add('shake');
  if (correct) {
    const misses = Number(correct.dataset.misses || 0) + 1;
    correct.dataset.misses = misses;
    if (misses >= (beginner() ? 1 : 2)) {
      correct.classList.add('hint');
      Speak.tts('반짝이는 걸 눌러 봐!');
      return;
    }
  }
  Speak.tts('다시 찾아볼까?');
}

// 끝낸 놀이인지 (단원별)
function isDone(act, unit) { return Progress.isDone(act + '-' + unit); }

// 스티커를 받았을 때 크게 보여 준다
function showStickerToast() {
  const t = document.createElement('div');
  t.className = 'toast';
  t.innerHTML = '<span class="toast-icon">🏅</span><span>스티커 받았어요!</span>';
  document.body.appendChild(t);
  celebrate(true);
  Speak.tts('우와, 스티커를 받았어요!');
  stickerCount();
  setTimeout(() => t.remove(), 2600);
}

// 활동을 끝냈을 때: 스티커(하루 한 번) + 다시 하기 버튼
function finishActivity(key, container) {
  if (Progress.reward(key)) showStickerToast();
  else { celebrate(true); Speak.tts('다 했어! 정말 잘했어!'); }
  if (container) {
    container.innerHTML =
      '<div class="end-btns"><button class="big-btn" onclick="location.reload()">한 번 더!</button>' +
      '<a class="big-btn alt" href="index.html">처음으로</a></div>';
  }
}

document.addEventListener('DOMContentLoaded', stickerCount);
