// 진도 저장: 이 기기의 localStorage에만 저장한다.
const Progress = (() => {
  const KEY = 'hangul-progress';
  const DEFAULT = { childName: '', unlockedStage: 1, stickers: 0, seen: {}, rewarded: {}, soundOn: true, lastPlayed: null };

  function get() {
    try {
      return Object.assign({}, DEFAULT, JSON.parse(localStorage.getItem(KEY) || '{}'));
    } catch (e) {
      return Object.assign({}, DEFAULT);
    }
  }

  function save(p) {
    p.lastPlayed = new Date().toISOString().slice(0, 10);
    try { localStorage.setItem(KEY, JSON.stringify(p)); } catch (e) {}
    return p;
  }

  function update(fn) {
    const p = get();
    fn(p);
    return save(p);
  }

  function markSeen(id) {
    update(p => { p.seen[id] = (p.seen[id] || 0) + 1; });
  }

  // 같은 활동은 하루에 한 번만 스티커를 준다. 받았으면 true.
  function reward(activityKey) {
    const today = new Date().toISOString().slice(0, 10);
    const key = activityKey + '@' + today;
    let given = false;
    update(p => {
      if (!p.rewarded[key]) {
        p.rewarded[key] = true;
        p.stickers += 1;
        given = true;
      }
    });
    return given;
  }

  function reset() {
    try { localStorage.removeItem(KEY); } catch (e) {}
  }

  return { get, save, update, markSeen, reward, reset };
})();
