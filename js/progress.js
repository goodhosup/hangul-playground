// 진도 저장: 이 기기의 localStorage에만 저장한다.
const Progress = (() => {
  const KEY = 'hangul-progress';
  const DEFAULT = { v: 2, childName: '', unlockedStage: 6, lastStage: 1, stickers: 0, seen: {}, rewarded: {}, soundOn: true, beginner: true, done: {}, lastPlayed: null };

  function get() {
    try {
      const saved = JSON.parse(localStorage.getItem(KEY) || '{}');
      // 1차 버전은 1단계만 열려 있었다: 이제 기본은 전체 열림
      if (!saved.v) { saved.v = 2; saved.unlockedStage = 6; }
      // 예전 기록(하루 단위 스티커)에서 끝낸 놀이 목록을 만든다
      if (!saved.done && saved.rewarded) {
        saved.done = {};
        Object.keys(saved.rewarded).forEach(k => { saved.done[k.split('@')[0]] = true; });
      }
      return Object.assign({}, DEFAULT, saved);
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
      p.done[activityKey] = true;
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

  function isDone(activityKey) {
    return !!get().done[activityKey];
  }

  return { get, save, update, markSeen, reward, isDone, reset };
})();
