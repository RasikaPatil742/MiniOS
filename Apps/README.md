# Forge OS — Community Apps

Drop-in applications for Forge OS live here. Each app is a **folder** with two files:

| File | Purpose |
|------|---------|
| `app.json` | Name, command, description, author, version |
| `command.py` | A `BaseCommand` subclass that runs the app |

## Quick example

```
Apps/
└── my-app/
    ├── app.json
    └── command.py
```

After you add a folder, restart Forge OS and run:

```text
apps          # list all applications
my-app-cmd    # run your app (command name from app.json)
```

## Full guide

See **[CONTRIBUTIONS.md](../CONTRIBUTIONS.md)** for step-by-step instructions, GitHub workflow, and review checklist.

Copy **`Apps/_example/`** as a starting template (folders starting with `_` are not loaded).
