# Claude Code desde cero: la ruta de Ctrl+IA

Revisada el 1-nov-2026 con Claude Code 2.1.316. Marca cada casilla al terminarla. Página: https://ctrlia.dev/recetas/empieza-aqui.html

## Los 10 pasos

- [ ] **Elige plan o API.** Receta: [¿Claude Code es gratis?](https://ctrlia.dev/recetas/claude-code-precio-gratis.html)
- [ ] **Instálalo.** En macOS, Linux y WSL, `curl -fsSL https://claude.ai/install.sh | bash`. En Windows sigue [Instalar Claude Code en Windows](https://ctrlia.dev/recetas/instalar-claude-code-windows.html), que distingue PowerShell, CMD y WSL.
- [ ] **Primera sesión.** `cd tu-proyecto`, `claude`, inicia sesión y pide «explícame la estructura de este proyecto».
- [ ] **Dale memoria.** Crea un CLAUDE.md corto con `/init` y recórtalo. Receta: [Un CLAUDE.md que funciona](https://ctrlia.dev/recetas/claude-md-que-funciona.html)
- [ ] **Controla qué puede hacer.** Modos de permiso y reglas allow/ask/deny en [Permisos de Claude Code](https://ctrlia.dev/recetas/permisos-claude-code.html), y un hook que bloquee lo peligroso en [Hooks de seguridad](https://ctrlia.dev/recetas/hooks-seguridad.html).
- [ ] **Trabaja en tu editor si lo prefieres.** Receta: [Claude Code en VS Code](https://ctrlia.dev/recetas/claude-code-vs-code.html)
- [ ] **Guarda procedimientos repetidos como skills** con [Crea tu primera skill](https://ctrlia.dev/recetas/primera-skill.html), e instala solo las que valen la pena: [Skills que instalar](https://ctrlia.dev/recetas/skills-que-instalar.html).
- [ ] **Conecta herramientas externas con MCP.** Receta: [MCP para programadores](https://ctrlia.dev/recetas/mcp-para-programadores.html)
- [ ] **Divide el trabajo con subagentes** para ahorrar contexto. Receta: [Subagentes](https://ctrlia.dev/recetas/subagentes.html)
- [ ] **Automatiza revisiones de PR** en GitHub Actions. Receta: [Revisión de PR con GitHub Actions](https://ctrlia.dev/recetas/revision-prs-github-actions.html)

## Toda la biblioteca, en orden

### Empezar

- [ ] [¿Claude Code es gratis? Precio y qué plan elegir (2026)](https://ctrlia.dev/recetas/claude-code-precio-gratis.html)
- [ ] [Instalar Claude Code en Windows: nativo, WSL y errores típicos](https://ctrlia.dev/recetas/instalar-claude-code-windows.html)
- [ ] [Claude Code vs Desktop vs Cowork vs claude.ai: cuál usar](https://ctrlia.dev/recetas/que-claude-abrir.html)
- [ ] [Cómo empezar con Claude Code en un proyecto: checklist de 15 min](https://ctrlia.dev/recetas/empezar-claude-code-15-minutos.html)
- [ ] [Claude Code en VS Code: extensión o terminal y cómo instalarlo](https://ctrlia.dev/recetas/claude-code-vs-code.html)
- [ ] [Claude Code en JetBrains, Visual Studio, Xcode, Zed y Neovim](https://ctrlia.dev/recetas/claude-code-otros-editores.html)
- [ ] [Claude Code en español y sin relleno: language y estilo Concise](https://ctrlia.dev/recetas/claude-code-espanol.html)

### Memoria e instrucciones

- [ ] [Generador de CLAUDE.md y AGENTS.md en español, gratis](https://ctrlia.dev/recetas/generador-claude-md.html)
- [ ] [Cómo hacer un CLAUDE.md que Claude Code sí respete](https://ctrlia.dev/recetas/claude-md-que-funciona.html)
- [ ] [AGENTS.md vs CLAUDE.md en Claude Code: cuál lee y cómo usar ambos](https://ctrlia.dev/recetas/agents-md.html)
- [ ] [Plantilla de proyecto para Claude Code: repo listo y seguro](https://ctrlia.dev/recetas/plantilla-claude-code.html)

### Control y seguridad

- [ ] [Permisos de Claude Code: deja de aprobar cada comando](https://ctrlia.dev/recetas/permisos-claude-code.html)
- [ ] [Antes de darle permisos a Claude Code: checklist de seguridad](https://ctrlia.dev/recetas/checklist-permisos-claude-code.html)
- [ ] [Modo automático de Claude Code a fondo: clasificador y reglas](https://ctrlia.dev/recetas/auto-mode.html)
- [ ] [Hooks de Claude Code: bloquea comandos peligrosos y secretos](https://ctrlia.dev/recetas/hooks-seguridad.html)
- [ ] [Comprobador de settings.json de Claude Code: detecta riesgos](https://ctrlia.dev/recetas/comprobador-settings.html)

### El día a día

- [ ] [Modo plan de Claude Code: planifica antes de tocar código](https://ctrlia.dev/recetas/modo-plan.html)
- [ ] [/clear vs /compact en Claude Code y la compactación en reposo](https://ctrlia.dev/recetas/clear-vs-compact.html)
- [ ] [Límite de uso de Claude Code: haz que tus 5 h y la semana duren](https://ctrlia.dev/recetas/limite-uso-claude-code.html)
- [ ] [Statusline de Claude Code: modelo, contexto y límites en vivo](https://ctrlia.dev/recetas/statusline.html)
- [ ] [Opus 5.5 vs Sonnet 5.5 vs Haiku 5.5 en Claude Code: cuál usar](https://ctrlia.dev/recetas/opus-sonnet-haiku.html)
- [ ] [Claude Code Opus 4.8: el modo rápido acaba el 30-nov, pasa a 5.5](https://ctrlia.dev/recetas/opus-48-modo-rapido.html)
- [ ] [5 comandos de Claude Code imprescindibles, listos para copiar](https://ctrlia.dev/recetas/pack-comandos.html)

### Ampliar Claude Code

- [ ] [Claude Code skills vs hooks, MCP, subagentes y plugins: cuál usar](https://ctrlia.dev/recetas/que-pieza-usar.html)
- [ ] [Crea tu primera skill de Claude Code paso a paso](https://ctrlia.dev/recetas/primera-skill.html)
- [ ] [Skills de Claude Code: cuáles instalar, cómo y cuáles evitar](https://ctrlia.dev/recetas/skills-que-instalar.html)
- [ ] [Antes de instalar plugins, skills o MCP en Claude Code: checklist](https://ctrlia.dev/recetas/checklist-plugins-claude-code.html)
- [ ] [Crear un plugin de Claude Code: init, prueba, eval y marketplace](https://ctrlia.dev/recetas/crear-plugin-claude-code.html)
- [ ] [MCP en Claude Code: conecta Playwright, GitHub y tu base de datos](https://ctrlia.dev/recetas/mcp-para-programadores.html)
- [ ] [Subagentes de Claude Code: divide el trabajo y ahorra contexto](https://ctrlia.dev/recetas/subagentes.html)

### Flujos de trabajo pro

- [ ] [TDD con Claude Code: rojo, verde y refactor sin trampas](https://ctrlia.dev/recetas/tdd-claude-code.html)
- [ ] [Depurar un bug con Claude Code: del error al test de regresión](https://ctrlia.dev/recetas/depurar-bug.html)
- [ ] [Refactorizar código legado con Claude Code sin romper nada](https://ctrlia.dev/recetas/refactorizar-codigo-legado.html)
- [ ] [Antes de fusionar código de Claude Code: checklist de revisión](https://ctrlia.dev/recetas/checklist-revisar-codigo-ia.html)
- [ ] [Claude Code worktree: varios agentes en paralelo sin pisarse](https://ctrlia.dev/recetas/worktrees-paralelo.html)
- [ ] [Claude Code headless: claude -p en scripts y cron paso a paso](https://ctrlia.dev/recetas/claude-code-headless-cron.html)
- [ ] [Revisa cada pull request con Claude Code en GitHub Actions](https://ctrlia.dev/recetas/revision-prs-github-actions.html)
- [ ] [Claude Code en el celular: Remote Control paso a paso y riesgos](https://ctrlia.dev/recetas/remote-control-movil.html)

### Comparar y resolver problemas

- [ ] [Claude Code vs Codex vs Gemini vs Cursor: misma tarea, con datos](https://ctrlia.dev/recetas/claude-code-vs-codex-gemini-cursor.html)
- [ ] [Claude Code gratis con Ollama u OpenRouter: qué funciona](https://ctrlia.dev/recetas/claude-code-ollama-openrouter.html)
- [ ] [Errores de Claude Code: 529, 401, 403, límites y cómo arreglarlos](https://ctrlia.dev/recetas/errores-comunes-claude-code.html)
