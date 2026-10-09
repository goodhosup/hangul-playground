// 소리 재생: 녹음 파일이 있으면 그것을, 없으면 브라우저 한국어 음성합성을 사용한다.
const Speak = (() => {
  let koVoice = null;

  function pickVoice() {
    if (!('speechSynthesis' in window)) return;
    const voices = speechSynthesis.getVoices();
    koVoice = voices.find(v => v.lang === 'ko-KR') || voices.find(v => v.lang.startsWith('ko')) || null;
  }
  if ('speechSynthesis' in window) {
    pickVoice();
    speechSynthesis.onvoiceschanged = pickVoice;
  }

  function enabled() {
    return Progress.get().soundOn !== false;
  }

  function tts(text, rate = 0.8) {
    return new Promise(resolve => {
      if (!enabled() || !('speechSynthesis' in window)) return resolve();
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'ko-KR';
      if (koVoice) u.voice = koVoice;
      u.rate = rate;
      u.pitch = 1.1;
      u.onend = resolve;
      u.onerror = resolve;
      speechSynthesis.speak(u);
    });
  }

  function file(src) {
    return new Promise(resolve => {
      const a = new Audio(src);
      a.onended = resolve;
      a.onerror = resolve;
      a.play().catch(resolve);
    });
  }

  // item: 단어 객체 또는 문자열
  function say(item, rate) {
    if (typeof item === 'string') return tts(item, rate);
    if (item.audio && enabled()) return file(item.audio);
    return tts(item.word, rate);
  }

  function hasKorean() {
    return !!koVoice;
  }

  return { say, tts, hasKorean };
})();
