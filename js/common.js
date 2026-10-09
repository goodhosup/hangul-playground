// 공통 도우미: 데이터 불러오기, 주소 파라미터, 칭찬 효과
async function loadJSON(path) {
  const res = await fetch(path);
  return res.json();
}

function param(name) {
  return new URLSearchParams(location.search).get(name);
}

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function stickerCount() {
  const el = document.querySelector('[data-sticker-count]');
  if (el) el.textContent = Progress.get().stickers;
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

document.addEventListener('DOMContentLoaded', stickerCount);
