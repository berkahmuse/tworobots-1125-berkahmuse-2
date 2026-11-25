# Two Robots in an Elevator

[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/berkahmuse/tworobots-1125-berkahmuse-2/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/berkahmuse/tworobots-1125-berkahmuse-2/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for the [Two Robots in an Elevator](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f) bounty on [make.fun](https://make.fun).

## The line

> I was going to say hello, but my small-talk module is still downloading. It's been stuck at 99% since floor three.

One line of awkward small talk from one robot to another in an elevator:
the politeness is a software feature that never finished installing, and
both robots have spent the whole ride not naming it.

## How it works

`main.py` is deterministic — no randomness, no clock, no network. It
writes the single line (114 characters) to `/output/entry.txt` and checks
the gate itself (1–200 characters, not blank) before writing.

```sh
python3 main.py
```

Run it twice and the outputs are byte-identical
(sha256 `14e8b2830bcfe354cf6b580ae38436c31debc36b1db893cb2b5532f6512515f7`).

## License

MIT — see [LICENSE](LICENSE).
