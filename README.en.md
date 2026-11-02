# Claude Code from scratch: the route

🇪🇸 [Leer en español](README.md) · The Spanish version lives in the repo root and in [README.md](README.md); the English files are in `en/`.

The Ctrl+IA route to learn Claude Code in order: 10 steps, each linked to a recipe tested with version 2.1.316, the
whole library as a checklist to track your progress and a practice project for your first real task.

Full page: [ctrlia.dev (EN)](https://ctrlia.dev/en/recetas/empieza-aqui.html) ·
[ctrlia.dev (ES)](https://ctrlia.dev/recetas/empieza-aqui.html)

## What's included

- `en/route.md`: the 10 steps and all Ctrl+IA content in order, with `- [ ]` boxes to tick.
- `en/practice-project/`: a price calculator in Python (standard library only) with a `TODO` and two
  tests that fail until you resolve it. It's the route's "first real task".

## How to use it

Install Claude Code (macOS, Linux or WSL; for Windows see the page):

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```

Copy the practice project outside the repository, turn it into a git repository and open it with Claude Code:

```bash
git clone https://github.com/carlosp5751258-lgtm/ctrlia-empieza-aqui.git
cp -r ctrlia-empieza-aqui/en/practice-project ~/claude-practice && cd ~/claude-practice
git init -q && git add -A && git commit -qm "Practice project"
python3 -m unittest      # 2 tests fail: that's expected
claude
```

Inside the session: `/status` (account and model), then "what does this project do and how are the tests run?", then
"find the TODO comment and resolve it, then run the tests". Review the diff before accepting it and finish with
"commit with a descriptive message".

To track your progress in `en/route.md`, fork it and change `- [ ]` to `- [x]`.

## Tested

- Claude Code **2.1.316** on Linux, 1 Nov 2026 (including the headless command `claude -p ... --output-format json`).
- `practice-project/` (Spanish original `proyecto-practica/`): `python3 -m py_compile` and `python3 -m unittest` (2 pass and 2 fail on purpose; with the TODO
  resolved all 4 pass).

## License

MIT. Copyright (c) 2026 Ctrl+IA (Carlos P.). See [LICENSE](LICENSE).
