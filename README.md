# Claude Code desde cero: la ruta en español

🇬🇧 [Read in English](README.en.md)

English version: [README.en.md](README.en.md) (archivos en `en/`).

La ruta de Ctrl+IA para aprender Claude Code en orden: 10 pasos, cada uno enlazado a una receta probada con la versión
2.1.316, toda la biblioteca como lista para marcar tu progreso y un proyecto de práctica para tu primera tarea real.

Página completa: [ctrlia.dev (ES)](https://ctrlia.dev/recetas/empieza-aqui.html) ·
[ctrlia.dev (EN)](https://ctrlia.dev/en/recetas/empieza-aqui.html)

## Qué incluye

- `ruta.md` / `en/route.md`: los 10 pasos y todos los contenidos de Ctrl+IA en orden, con casillas `- [ ]` para marcar.
- `proyecto-practica/`: una calculadora de precios en Python (solo biblioteca estándar) con un `TODO` y dos tests que
  fallan hasta que lo resuelves. Es la «primera tarea real» de la ruta.

## Cómo usarlo

Instala Claude Code (macOS, Linux o WSL; en Windows mira la página):

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```

Copia el proyecto de práctica fuera del repositorio, conviértelo en un repositorio git y ábrelo con Claude Code:

```bash
git clone https://github.com/carlosp5751258-lgtm/ctrlia-empieza-aqui.git
cp -r ctrlia-empieza-aqui/proyecto-practica ~/practica-claude && cd ~/practica-claude
git init -q && git add -A && git commit -qm "Proyecto de práctica"
python3 -m unittest      # 2 tests fallan: es lo esperado
claude
```

Dentro de la sesión: `/status` (cuenta y modelo), luego «¿qué hace este proyecto y cómo se ejecutan los tests?», después
«busca el comentario TODO y resuélvelo, luego ejecuta los tests». Revisa el diff antes de aceptarlo y termina con
«haz commit con un mensaje descriptivo».

Para marcar tu progreso en `ruta.md`, haz un fork y cambia `- [ ]` por `- [x]`.

## Probado

- Claude Code **2.1.316** en Linux, 1-nov-2026 (incluido el comando headless `claude -p ... --output-format json`).
- `proyecto-practica/`: `python3 -m py_compile` y `python3 -m unittest` (2 pasan y 2 fallan a propósito; con el TODO
  resuelto pasan los 4).

## Licencia

MIT. Copyright (c) 2026 Ctrl+IA (Carlos P.). Ver [LICENSE](LICENSE).
