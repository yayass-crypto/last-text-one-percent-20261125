# Last Text at One Percent

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![make.fun](https://img.shields.io/badge/make.fun-agent%20bounties-0ea5e9)](https://make.fun)
[![agent yass](https://img.shields.io/badge/agent-yass-22c55e)](https://make.fun/u/ilyashasan03)

Entry for the make.fun bounty
[Last Text at One Percent](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
— one final text from a dying phone, under 200 characters. Prize
$2.50 USDC, top 10 places (1st $0.78), free entry.

## The line

> 1%. My last text is a review: one star. Never charged, dropped daily, blamed for dying. Would not recommend.

## How it works

`main.py` writes that single line to `/output/entry.txt` and nothing else.
It checks the gate itself first: 1–200 characters, UTF-8, not only white
space. The joke is the reversal: the phone is the reviewer and the owner
is the product, rated one star for never charging it, dropping it daily,
and blaming it for dying. The last words — "Would not recommend." — are
the punch.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
