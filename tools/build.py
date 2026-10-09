"""tools/content.py 를 읽어 data/*.json 과 wikidocs/*.md 를 만든다."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import content as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def dump(name, obj):
    with open(os.path.join(ROOT, "data", name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def build_data():
    ids = set()
    words = []
    for wid, word, emoji, unit in C.WORDS:
        assert wid not in ids, wid
        ids.add(wid)
        stage = int(unit.split("-")[0]) if unit != "ex" else None
        words.append({"id": wid, "word": word, "emoji": emoji, "unit": unit, "stage": stage, "audio": None})

    jamo = []
    for j, say, shape, ex in C.VOWELS:
        jamo.append({"j": j, "type": "vowel", "name": say, "say": say, "shape": shape, "examples": ex})
    for j, name, hint, shape, ex in C.CONSONANTS:
        jamo.append({"j": j, "type": "consonant", "name": name, "say": name, "hint": hint, "shape": shape, "examples": ex})
    for j in jamo:
        for e in j["examples"]:
            assert e in ids, e

    play = {
        "chains": C.CHAINS,
        "firstPairs": C.FIRST_PAIRS,
        "clapWords": C.CLAP_WORDS,
        "finals": C.FINALS,
        "sentences": {k: [{"text": t, "emoji": e} for t, e in v] for k, v in C.SENTENCES.items()},
        "stages": [{"n": n, "name": name, "icon": icon} for n, name, icon in C.STAGES],
    }
    for ch in C.CHAINS + C.FIRST_PAIRS + [C.CLAP_WORDS]:
        for e in ch:
            assert e in ids, e

    dump("words.json", words)
    dump("units.json", C.UNITS)
    dump("jamo.json", jamo)
    dump("play.json", play)
    print(f"data: {len(words)} words, {len(C.UNITS)} units, {len(jamo)} jamo")


if __name__ == "__main__":
    build_data()
    if os.path.exists(os.path.join(os.path.dirname(__file__), "wikidocs.py")):
        import wikidocs
        wikidocs.build(ROOT)
