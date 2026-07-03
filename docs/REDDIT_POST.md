# Reddit Post — Forge OS Community Apps Call for Contributors

Use this draft on subreddits such as **r/Python**, **r/learnprogramming**, **r/opensource**, or **r/coolgithubprojects**. Adjust the title and tone for each community's rules.

---

## Suggested title

**I built a Python virtual OS (Forge OS v2.0) — you can now add apps by dropping a folder in `Apps/`. Looking for contributors!**

---

## Post body (copy and paste)

Hey everyone,

I've been building **[Forge OS](https://github.com/axk42-op/ForgeOS)** — a Python-based virtual operating system for learning, coding, and experimenting with OS concepts without touching real hardware.

**v2.0** adds a desktop GUI (taskbar, Start menu, windowed terminal), and I just opened up a **community Apps folder** so anyone can contribute small applications.

### What Forge OS has today

- Custom shell with 65+ commands (auto-discovered)
- Virtual filesystem, user login, package manager
- Desktop environment (tkinter) with draggable terminal
- Built-in apps: calculator, fortune, system info, and more

### What's new — the `Apps/` folder

You can add an app by creating a folder with two files:

```text
Apps/
└── my-cool-app/
    ├── app.json      # name, command, description, author
    └── command.py    # your Python command (extends BaseCommand)
```

Restart Forge OS, run `apps` to see it listed, then run your command by name. Community apps also show up in the **Start menu**.

There's a sample app at `Apps/hello/` and a copy-paste template at `Apps/_example/`.

### How to contribute (step by step)

1. **Fork** the repo: [github.com/axk42-op/ForgeOS](https://github.com/axk42-op/ForgeOS)
2. **Clone** your fork: `git clone https://github.com/YOUR-USERNAME/ForgeOS.git`
3. **Install**: `pip install -r requirements.txt` and `pip install -e .`
4. **Run**: `python boot.py` (or double-click `boot.bat` on Windows)
5. **Copy** `Apps/_example/` to `Apps/your-app-name/`
6. **Edit** `app.json` (metadata) and `command.py` (your logic)
7. **Test**: run `apps`, then run your command
8. **Push** a branch and open a **Pull Request**

Full guide: **[CONTRIBUTIONS.md](https://github.com/axk42-op/ForgeOS/blob/main/CONTRIBUTIONS.md)** on GitHub.

### What kind of apps?

Games, trivia, timers, ASCII art, quizzes, tiny utilities — anything that fits in a single Python command. Great for beginners who want a fun first open-source PR.

### Links

- **Repo:** https://github.com/axk42-op/ForgeOS
- **Docs wiki:** https://github.com/axk42-op/ForgeOS/wiki/Docs
- **License:** MIT

If you try it or submit an app, I'd love feedback in the comments or on GitHub Issues. Thanks!

---

## Posting tips

### Step 1 — Pick a subreddit

| Subreddit | Why |
|-----------|-----|
| r/Python | Core audience; show the `BaseCommand` pattern |
| r/learnprogramming | Emphasize "good first PR" |
| r/opensource | Emphasize MIT license and contribution flow |
| r/coolgithubprojects | Lead with desktop GUI + virtual OS demo |

Check each subreddit's rules before posting (some require flair or restrict self-promotion).

### Step 2 — Add a screenshot or GIF (recommended)

Record a short clip showing:

1. Boot → login → desktop
2. Terminal: type `apps`
3. Run `hello` or your own app
4. Start menu with your app listed

Upload to Reddit or Imgur and link in the post.

### Step 3 — Post at a good time

Weekday mornings (US Eastern) often get more visibility. Avoid posting the same text to multiple subs on the same day — rewrite slightly for each.

### Step 4 — Reply to comments

- **"How is this different from Docker/WSL?"** — Forge OS is a learning project: Python shell, in-memory VFS, no real kernel. Safe sandbox for OS concepts.
- **"Can I use tkinter in my app?"** — Yes, but start with terminal output via `CommandResult`; GUI apps are welcome in PRs.
- **"Is this production-ready?"** — It's a learning/experimentation platform, not a replacement OS.

### Step 5 — Pin the contribution link

In follow-up comments, link directly to:

https://github.com/axk42-op/ForgeOS/blob/main/CONTRIBUTIONS.md

---

## Short version (for Twitter/X or comment threads)

> Forge OS v2.0 — Python virtual OS with a desktop GUI. Add apps by dropping a folder in `Apps/` (app.json + command.py). Run `apps` to list them. MIT licensed. PRs welcome: github.com/axk42-op/ForgeOS

---

## Hashtags (optional)

`#Python` `#OpenSource` `#LearnToCode` `#GitHub` `#IndieDev`
