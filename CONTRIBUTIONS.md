# Contributing Apps to Forge OS

Thank you for helping grow [Forge OS](https://github.com/axk42-op/ForgeOS)! This guide explains how to add a new application to the **`Apps/`** folder and submit it on GitHub.

---

## What is an app?

In Forge OS, an **app** is a shell command that users can run from the terminal or Start menu. Community apps live in the **`Apps/`** directory at the repo root. Each app is a folder with:

| File | Required | Purpose |
|------|----------|---------|
| `app.json` | Yes | Metadata (name, command, description, author) |
| `command.py` | Yes | Python code — a `BaseCommand` subclass |

Built-in apps (`calc`, `fortune`, `logo`, etc.) live in `shell/commands/apps/`. **New contributions should go in `Apps/`** so they are easy to find and review.

---

## Step 1 — Fork and clone the repository

1. Open [https://github.com/axk42-op/ForgeOS](https://github.com/axk42-op/ForgeOS)
2. Click **Fork** (top right) to copy the repo to your GitHub account
3. Clone your fork locally:

```bash
git clone https://github.com/YOUR-USERNAME/ForgeOS.git
cd ForgeOS
```

4. Add the upstream remote (optional but recommended):

```bash
git remote add upstream https://github.com/axk42-op/ForgeOS.git
```

---

## Step 2 — Set up Forge OS locally

**Windows**

```cmd
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe boot.py
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python boot.py
```

---

## Step 3 — Create your app folder

1. Copy the template:

```text
Apps/_example/  →  Apps/your-app-name/
```

2. Use a **lowercase, hyphenated folder name** (e.g. `Apps/word-game/`, `Apps/ascii-art/`)

3. Folders starting with `_` or `.` are **ignored** (so `_example` is never loaded)

---

## Step 4 — Write `app.json`

Example:

```json
{
  "name": "Word Game",
  "command": "wordgame",
  "description": "Guess the hidden word",
  "author": "Your Name",
  "version": "1.0.0",
  "website": "https://github.com/YOUR-USERNAME/ForgeOS"
}
```

| Field | Rules |
|-------|-------|
| `name` | Human-readable title shown in `apps` and the Start menu |
| `command` | Shell command users type (lowercase, no spaces, must be unique) |
| `description` | One line shown in `apps` and `help` |
| `author` | Your name or GitHub username |
| `version` | Semver string, e.g. `1.0.0` |
| `website` | Optional link to your profile or app page |

The `command` in `app.json` **must match** the `name` on your `BaseCommand` class in `command.py`.

---

## Step 5 — Write `command.py`

Your app must define one class that extends `BaseCommand`:

```python
from typing import Any

from shell.commands.base import BaseCommand, CommandResult


class WordGameCommand(BaseCommand):
    name = "wordgame"
    category = "apps"
    description = "Guess the hidden word"
    syntax = "wordgame"
    examples = ("wordgame",)

    def execute(self, args: list[str], context: dict[str, Any]) -> CommandResult:
        return CommandResult(output="You win! (implement your app here)")
```

### Tips

- Use `category = "apps"` for all community apps
- Use `context["console"]` for Rich output, or return `CommandResult(renderable=...)` for panels/tables
- Use `context["session"]` for the current user
- Keep dependencies minimal — stick to the [requirements.txt](requirements.txt) packages when possible
- Do **not** import from other apps in `Apps/` (each app should stand alone)

See [Apps/_example/command.py](Apps/_example/command.py) and [Apps/hello/command.py](Apps/hello/command.py) for working examples.

---

## Step 6 — Test your app

1. **Restart Forge OS** (apps are loaded at boot)
2. Run:

```text
apps              # list built-in + community apps
apps info wordgame
wordgame          # run your app directly
help wordgame     # show syntax and examples
```

3. Confirm your app appears in the **Start menu** after login

---

## Step 7 — Commit and push

```bash
git checkout -b add-wordgame-app
git add Apps/your-app-name/
git commit -m "Add Word Game app to Apps/"
git push origin add-wordgame-app
```

---

## Step 8 — Open a Pull Request on GitHub

1. Go to your fork on GitHub
2. Click **Compare & pull request**
3. Set base repository: `axk42-op/ForgeOS` → base: `main`
4. Fill in the PR template:

**Title:** `Add app: Word Game`

**Description:**

```markdown
## App
- **Command:** wordgame
- **Folder:** Apps/word-game/

## What it does
Brief description of the app.

## How to test
1. `python boot.py`
2. Run `apps` — should list Word Game
3. Run `wordgame` — should ...
```

5. Click **Create pull request**

Maintainers will review for naming conflicts, code quality, and safety. We may ask for small changes before merging.

---

## Review checklist (for you and reviewers)

- [ ] Folder is under `Apps/` with a clear name (not `_` or `.` prefixed)
- [ ] `app.json` and `command.py` are both present
- [ ] `command` in JSON matches `BaseCommand.name`
- [ ] Command name does not clash with existing shell commands
- [ ] App runs without errors after a fresh boot
- [ ] No secrets, network calls to untrusted hosts, or destructive host-OS behavior
- [ ] Code is readable and commented only where logic is non-obvious

---

## Ideas for apps

- Games (guess the number, trivia, hangman)
- Utilities (unit converter, timer, stopwatch)
- Fun (ASCII art, quotes, mad libs)
- Learning (Python quiz, OS trivia)
- Tools (markdown preview, JSON formatter)

See **Planned Applications** in [README.md](README.md) for long-term goals.

---

## Questions?

- Open a [GitHub Issue](https://github.com/axk42-op/ForgeOS/issues)
- Wiki: [https://github.com/axk42-op/ForgeOS/wiki/Docs](https://github.com/axk42-op/ForgeOS/wiki/Docs)
- In Forge OS shell: `docs` · `source`

Happy forging!
