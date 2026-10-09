// 자모 도우미: 단어 속에서 자모가 들어 있는 글자 찾기
const Jamo = (() => {
  function contains(syl, j) {
    const d = Hangul.decompose(syl);
    if (!d) return false;
    const vowels = Hangul.SPLIT_VOWEL[d.jung] || [d.jung];
    // 받침은 5단계에서 배우므로 첫소리와 모음만 본다
    return d.cho === j || vowels.includes(j);
  }

  // 자모가 들어 있는 글자를 <b>로 감싼다
  function highlight(word, j) {
    return [...word].map(c => contains(c, j) ? '<b>' + c + '</b>' : c).join('');
  }

  // 단어의 첫 글자의 초성 / 중성
  function firstCho(word) { const d = Hangul.decompose(word[0]); return d && d.cho; }
  function firstJung(word) { const d = Hangul.decompose(word[0]); return d && d.jung; }

  async function load() {
    const [jamo, words] = await Promise.all([loadJSON('data/jamo.json'), loadJSON('data/words.json')]);
    const byJ = {}, byId = {};
    jamo.forEach(j => byJ[j.j] = j);
    words.forEach(w => byId[w.id] = w);
    return { jamo, byJ, byId };
  }

  return { contains, highlight, firstCho, firstJung, load };
})();
