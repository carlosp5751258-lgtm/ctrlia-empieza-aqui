# Claude Code from scratch: the Ctrl+IA route

Reviewed on 1 Nov 2026 with Claude Code 2.1.316. Tick each box when you finish it. Page: https://ctrlia.dev/en/recetas/empieza-aqui.html

## The 10 steps

- [ ] **Pick a plan or the API.** Recipe: [Is Claude Code free?](https://ctrlia.dev/en/recetas/claude-code-precio-gratis.html)
- [ ] **Install it.** On macOS, Linux and WSL, `curl -fsSL https://claude.ai/install.sh | bash`. On Windows follow [Install Claude Code on Windows](https://ctrlia.dev/en/recetas/instalar-claude-code-windows.html), which covers PowerShell, CMD and WSL.
- [ ] **First session.** `cd your-project`, `claude`, sign in and ask "explain the structure of this project".
- [ ] **Give it memory.** Create a short CLAUDE.md with `/init` and trim it. Recipe: [A CLAUDE.md that works](https://ctrlia.dev/en/recetas/claude-md-que-funciona.html)
- [ ] **Control what it can do.** Permission modes and allow/ask/deny rules in [Claude Code permissions](https://ctrlia.dev/en/recetas/permisos-claude-code.html), and a hook that blocks dangerous stuff in [Security hooks](https://ctrlia.dev/en/recetas/hooks-seguridad.html).
- [ ] **Work in your editor if you prefer.** Recipe: [Claude Code in VS Code](https://ctrlia.dev/en/recetas/claude-code-vs-code.html)
- [ ] **Save repeated procedures as skills** with [Create your first skill](https://ctrlia.dev/en/recetas/primera-skill.html), and install only the ones worth it: [Skills to install](https://ctrlia.dev/en/recetas/skills-que-instalar.html).
- [ ] **Connect external tools with MCP.** Recipe: [MCP for developers](https://ctrlia.dev/en/recetas/mcp-para-programadores.html)
- [ ] **Split work with subagents** to save context. Recipe: [Subagents](https://ctrlia.dev/en/recetas/subagentes.html)
- [ ] **Automate PR reviews** in GitHub Actions. Recipe: [PR review with GitHub Actions](https://ctrlia.dev/en/recetas/revision-prs-github-actions.html)

## The whole library, in order

### Getting started

- [ ] [Is Claude Code free? Pricing and which plan to pick (2026)](https://ctrlia.dev/en/recetas/claude-code-precio-gratis.html)
- [ ] [Install Claude Code on Windows: native, WSL and common errors](https://ctrlia.dev/en/recetas/instalar-claude-code-windows.html)
- [ ] [Claude Code vs Desktop vs Cowork vs claude.ai: which to use](https://ctrlia.dev/en/recetas/que-claude-abrir.html)
- [ ] [How to start with Claude Code in a project: 15-minute checklist](https://ctrlia.dev/en/recetas/empezar-claude-code-15-minutos.html)
- [ ] [Claude Code in VS Code: extension or terminal, how to install](https://ctrlia.dev/en/recetas/claude-code-vs-code.html)
- [ ] [Claude Code in JetBrains, Visual Studio, Xcode, Zed and Neovim](https://ctrlia.dev/en/recetas/claude-code-otros-editores.html)
- [ ] [Claude Code in Spanish, no fluff: language and the Concise style](https://ctrlia.dev/en/recetas/claude-code-espanol.html)

### Memory and instructions

- [ ] [Free CLAUDE.md and AGENTS.md generator for Claude Code](https://ctrlia.dev/en/recetas/generador-claude-md.html)
- [ ] [How to write a CLAUDE.md that Claude Code actually follows](https://ctrlia.dev/en/recetas/claude-md-que-funciona.html)
- [ ] [AGENTS.md vs CLAUDE.md in Claude Code: which one it reads](https://ctrlia.dev/en/recetas/agents-md.html)
- [ ] [Claude Code project template: a repo set up and safe](https://ctrlia.dev/en/recetas/plantilla-claude-code.html)

### Control and security

- [ ] [Claude Code permissions: stop approving every command](https://ctrlia.dev/en/recetas/permisos-claude-code.html)
- [ ] [Before you give Claude Code permissions: a security checklist](https://ctrlia.dev/en/recetas/checklist-permisos-claude-code.html)
- [ ] [Claude Code auto mode in depth: the classifier and its rules](https://ctrlia.dev/en/recetas/auto-mode.html)
- [ ] [Claude Code hooks: block dangerous commands and secrets](https://ctrlia.dev/en/recetas/hooks-seguridad.html)
- [ ] [Claude Code settings.json checker: find permission risks](https://ctrlia.dev/en/recetas/comprobador-settings.html)

### Day to day

- [ ] [Claude Code plan mode: plan before touching any code](https://ctrlia.dev/en/recetas/modo-plan.html)
- [ ] [/clear vs /compact in Claude Code, and idle compaction](https://ctrlia.dev/en/recetas/clear-vs-compact.html)
- [ ] [Claude Code usage limits: make your 5 h and weekly limit last](https://ctrlia.dev/en/recetas/limite-uso-claude-code.html)
- [ ] [Claude Code statusline: live model, context and usage limits](https://ctrlia.dev/en/recetas/statusline.html)
- [ ] [Opus 5.5 vs Sonnet 5.5 vs Haiku 5.5 in Claude Code: which to use](https://ctrlia.dev/en/recetas/opus-sonnet-haiku.html)
- [ ] [Claude Code Opus 4.8: fast mode ends on 30 Nov, move to 5.5](https://ctrlia.dev/en/recetas/opus-48-modo-rapido.html)
- [ ] [5 must-have Claude Code commands, ready to copy](https://ctrlia.dev/en/recetas/pack-comandos.html)

### Extending Claude Code

- [ ] [Claude Code skills vs hooks, MCP, subagents and plugins](https://ctrlia.dev/en/recetas/que-pieza-usar.html)
- [ ] [Create your first Claude Code skill, step by step](https://ctrlia.dev/en/recetas/primera-skill.html)
- [ ] [Claude Code skills: which to install, how, and which to avoid](https://ctrlia.dev/en/recetas/skills-que-instalar.html)
- [ ] [Before installing plugins, skills or MCP in Claude Code](https://ctrlia.dev/en/recetas/checklist-plugins-claude-code.html)
- [ ] [Create a Claude Code plugin: init, testing, evals and marketplace](https://ctrlia.dev/en/recetas/crear-plugin-claude-code.html)
- [ ] [MCP in Claude Code: connect Playwright, GitHub and your database](https://ctrlia.dev/en/recetas/mcp-para-programadores.html)
- [ ] [Claude Code subagents: split the work and save context](https://ctrlia.dev/en/recetas/subagentes.html)

### Pro workflows

- [ ] [TDD with Claude Code: red, green and refactor with no cheating](https://ctrlia.dev/en/recetas/tdd-claude-code.html)
- [ ] [Debug a bug with Claude Code: from the error to a regression test](https://ctrlia.dev/en/recetas/depurar-bug.html)
- [ ] [Refactor legacy code with Claude Code without breaking anything](https://ctrlia.dev/en/recetas/refactorizar-codigo-legado.html)
- [ ] [Before merging Claude Code's code: a review checklist](https://ctrlia.dev/en/recetas/checklist-revisar-codigo-ia.html)
- [ ] [Claude Code worktree: run agents in parallel without clashes](https://ctrlia.dev/en/recetas/worktrees-paralelo.html)
- [ ] [Claude Code headless: claude -p in scripts and cron, step by step](https://ctrlia.dev/en/recetas/claude-code-headless-cron.html)
- [ ] [Review every pull request with Claude Code in GitHub Actions](https://ctrlia.dev/en/recetas/revision-prs-github-actions.html)
- [ ] [Claude Code on your phone: Remote Control step by step and risks](https://ctrlia.dev/en/recetas/remote-control-movil.html)

### Compare and troubleshoot

- [ ] [Claude Code vs Codex vs Gemini vs Cursor: same task, with data](https://ctrlia.dev/en/recetas/claude-code-vs-codex-gemini-cursor.html)
- [ ] [Claude Code for free with Ollama or OpenRouter: what works](https://ctrlia.dev/en/recetas/claude-code-ollama-openrouter.html)
- [ ] [Claude Code errors: 529, 401, 403, limits and how to fix them](https://ctrlia.dev/en/recetas/errores-comunes-claude-code.html)
