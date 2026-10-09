// 한글 자모 조합·분해 (유니코드 공식: 0xAC00 + (초성 × 21 + 중성) × 28 + 종성)
const Hangul = (() => {
  const CHO = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'.split('');
  const JUNG = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'.split('');
  const JONG = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ',
    'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'];

  function compose(cho, jung, jong = '') {
    const c = CHO.indexOf(cho), j = JUNG.indexOf(jung), k = JONG.indexOf(jong || '');
    if (c < 0 || j < 0 || k < 0) return null;
    return String.fromCharCode(0xAC00 + (c * 21 + j) * 28 + k);
  }

  function decompose(ch) {
    const code = ch.charCodeAt(0) - 0xAC00;
    if (code < 0 || code > 11171) return null;
    return { cho: CHO[Math.floor(code / 588)], jung: JUNG[Math.floor((code % 588) / 28)], jong: JONG[code % 28] };
  }

  // ㅘ 같은 겹모음을 아이가 아는 기본 모음으로 풀어 보여 준다
  const SPLIT_VOWEL = { 'ㅘ': ['ㅗ', 'ㅏ'], 'ㅙ': ['ㅗ', 'ㅐ'], 'ㅚ': ['ㅗ', 'ㅣ'], 'ㅝ': ['ㅜ', 'ㅓ'], 'ㅞ': ['ㅜ', 'ㅔ'], 'ㅟ': ['ㅜ', 'ㅣ'], 'ㅢ': ['ㅡ', 'ㅣ'] };

  return { CHO, JUNG, JONG, compose, decompose, SPLIT_VOWEL };
})();
