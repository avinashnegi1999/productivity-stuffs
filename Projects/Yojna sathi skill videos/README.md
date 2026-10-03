# Yojana Sathi — Basics Learning Map

**Goal:** understand the basics of every tool in Yojana Sathi well enough to **explain the project** and to **change the backend logic** safely.
**Not the goal:** deep expertise or frontend skills. The code was written with AI (Claude Code). My aim is backend roles, so frontend is marked optional and I don't claim it.

**How to use this file**
- Go **top to bottom**: the table is already sorted in the order to learn.
- **Watch only the part noted** in "Watch only". Long courses are for reference, not to finish.
- If a link stops working, search YouTube for the **YouTuber** and **video title** written in the table.
- Tick ☐ → ☑ when done.

**Level:** 🟢 Easy · 🟡 Medium · 🔴 Hard (for a beginner)
**Sources:** freeCodeCamp first; otherwise a large, well-known channel. View counts and lengths were checked on 3 Oct 2026.

---

## 1. Learning order

### Stage 1 · Read the code (Python basics)

| # | Topic | Level | Why I need it | Video (title) | YouTuber | Length · Views | Watch only | ☐ |
|---|---|---|---|---|---|---|---|---|
| 1 | Python | 🟢 | Everything is Python's standard library, no extra packages | [Learn Python - Full Course for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 4h27m · 49.4M | First 2 hours: variables, if, loops, functions, dicts, classes | ☐ |
| 2 | TOML | 🟢 | Each scheme's rules live in a `.toml` file. This is where most changes happen | [Learn TOML in 10 Minutes (Tutorial)](https://www.youtube.com/watch?v=D_Jb52jw2HY) | [Indently](https://www.youtube.com/@Indently) | 11m · 50K | All | ☐ |
| 3 | SQL | 🟢 | Read and query the event log | [SQL Tutorial - Full Database Course for Beginners](https://www.youtube.com/watch?v=HXV3zeQKqGY) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 4h21m · 21.0M | First 1.5 hours: SELECT, WHERE, INSERT, tables | ☐ |
| 4 | SQLite with Python | 🟢 | How the app saves events (`sqlite3`) | [SQLite Databases With Python - Full Course](https://www.youtube.com/watch?v=byHcYRpMgI4) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 1h30m · 816K | First 45 min | ☐ |
| 5 | Testing | 🟡 | Run `check.py` after every change; read a failing test | [Python Tutorial: Unit Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI) | [Corey Schafer](https://www.youtube.com/@coreyms) | 39m · 1.5M | All | ☐ |

### Stage 2 · How a message reaches the app

| # | Topic | Level | Why I need it | Video (title) | YouTuber | Length · Views | Watch only | ☐ |
|---|---|---|---|---|---|---|---|---|
| 6 | APIs | 🟢 | The app talks to Telegram and Meta through APIs (HTTP + JSON) | [APIs for Beginners - How to use an API (Full Course / Tutorial)](https://www.youtube.com/watch?v=WXsD0ZgxjRw) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 3h07m · 4.4M | First hour | ☐ |
| 7 | Polling vs webhooks | 🟢 | Why Telegram uses long polling and WhatsApp uses a webhook. A common interview question | [Short Polling vs Long Polling vs WebSockets - System Design](https://www.youtube.com/watch?v=ZBM28ZPlin8) | [Be A Better Dev](https://www.youtube.com/@BeABetterDev) | 5m · 129K | All | ☐ |
| 8 | Telegram bots | 🟢 | How the Telegram door works (bot token, getUpdates) | [How To Create A Telegram Bot With Python](https://www.youtube.com/watch?v=NwBWW8cNCP4) | [CS Dojo](https://www.youtube.com/@CSDojo) | 20m · 675K | All | ☐ |
| 9 | Webhooks | 🟢 | How the WhatsApp door works: Meta calls my server | [What are Webhooks? Explained with simple terms & diagram](https://www.youtube.com/watch?v=Q_VPL6KrH2o) | [Code Tour](https://www.youtube.com/@codetour) | 2m · 25K | All. Longer option: [Webhooks for Beginners - Full Course](https://www.youtube.com/watch?v=41NOoEz3Tzc), freeCodeCamp, first 30 min | ☐ |
| 10 | HMAC signatures | 🟡 | Why the WhatsApp service checks a signature before trusting a message | [Securing Stream Ciphers (HMAC) - Computerphile](https://www.youtube.com/watch?v=wlSG3pEiQdc) | [Computerphile](https://www.youtube.com/@Computerphile) | 9m · 342K | All | ☐ |

### Stage 3 · Change the code and ship it

| # | Topic | Level | Why I need it | Video (title) | YouTuber | Length · Views | Watch only | ☐ |
|---|---|---|---|---|---|---|---|---|
| 11 | Git & GitHub | 🟢 | Save changes, push, read history | [Git and GitHub for Beginners - Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 1h09m · 5.1M | All | ☐ |
| 12 | GitHub Actions | 🟡 | Every push runs all the checks automatically | [GitHub Actions Tutorial - Basic Concepts and CI/CD Pipeline with Docker](https://www.youtube.com/watch?v=R8_veQiYBjI) | [TechWorld with Nana](https://www.youtube.com/@TechWorldwithNana) | 32m · 2.3M | First 15 min | ☐ |
| 13 | Docker | 🟡 | The app is also packaged as an image that tests itself while building | [Docker Tutorial for Beginners - A Full DevOps Course on How to Run Applications in Containers](https://www.youtube.com/watch?v=fqMOX6JJhGo) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 2h10m · 2.9M | First 45 min | ☐ |

### Stage 4 · The server it runs on

| # | Topic | Level | Why I need it | Video (title) | YouTuber | Length · Views | Watch only | ☐ |
|---|---|---|---|---|---|---|---|---|
| 14 | Linux commands | 🟢 | Move around the server, read files and logs | [The 50 Most Popular Linux & Terminal Commands - Full Course for Beginners](https://www.youtube.com/watch?v=ZtqBQ68cfJc) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 5h00m · 2.9M | First hour | ☐ |
| 15 | SSH | 🟢 | How I log in to the server and deploy | [Linux Crash Course - Connecting to Linux Servers via SSH](https://www.youtube.com/watch?v=kjFz7Lp8Qjk) | [Learn Linux TV](https://www.youtube.com/@LearnLinuxTV) | 16m · 142K | All | ☐ |
| 16 | AWS basics | 🟡 | What a cloud account, region, IAM and a budget alert are | [AWS Certified Cloud Practitioner Training 2020 - Full Course](https://www.youtube.com/watch?v=3hLmDS179YE) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 3h58m · 7.6M | Only the parts on regions, IAM, EC2 and billing (use the chapter list) | ☐ |
| 17 | AWS EC2 | 🟡 | The one virtual server the bot runs on | [AWS EC2 Tutorial Beginners to Advance - Full course with Hands On Labs](https://www.youtube.com/watch?v=8SQnGqp3YZM) | [Cloud Champ](https://www.youtube.com/@cloudchamp) | 40m · 72K | First 20 min | ☐ |
| 18 | systemd | 🟡 | Keeps the 3 services running and restarts them; a timer runs the nightly backup | [systemd on Linux 1: Intro and Unit Files](https://www.youtube.com/watch?v=N1vgvhiyq0E) | [tutoriaLinux](https://www.youtube.com/@tutoriaLinux) | 14m · 185K | All | ☐ |
| 19 | HTTPS / TLS | 🟡 | What the padlock means and how certificates work | [TLS Handshake - EVERYTHING that happens when you visit an HTTPS website](https://www.youtube.com/watch?v=ZkL10eoG1PY) | [Practical Networking](https://www.youtube.com/@PracticalNetworking) | 28m · 226K | First 10 min | ☐ |
| 20 | Caddy | 🟢 | The front door: HTTPS on port 443, sending each request to the right service | [Reverse Proxy and Automatic SSL for Free with Open Source Caddy!](https://www.youtube.com/watch?v=CzdenRkjMQY) | [Shawn Powers](https://www.youtube.com/@shawnp0wers) | 8m · 39K | All. 30-second version: [Caddy - Automatic HTTPS in 28s](https://www.youtube.com/watch?v=nk4EWHvvZtI), by Matthew Holt, Caddy's creator | ☐ |
| 21 | DNS | 🟢 | How my domain name points to the server | [How DNS Works - Computerphile](https://www.youtube.com/watch?v=uOfonONtIuk) | [Computerphile](https://www.youtube.com/@Computerphile) | 8m · 504K | All | ☐ |

### Stage 5 · Talk about it

| # | Topic | Level | Why I need it | Video (title) | YouTuber | Length · Views | Watch only | ☐ |
|---|---|---|---|---|---|---|---|---|
| 22 | System design basics | 🟡 | Explain the whole picture: 3 doors → 1 rule engine → 1 database | [System Design for Beginners Course](https://www.youtube.com/watch?v=m8Icp_Cid5o) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 1h25m · 2.0M | First 40 min | ☐ |
| 23 | Claude Code | 🟢 | The AI tool that wrote most of the code: how I directed and checked it | [Claude Code for Beginners Tutorial [Full Course]](https://www.youtube.com/watch?v=gh2_PhgZGsM) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 4h28m · 274K | First hour | ☐ |

### Optional (only if needed)

| # | Topic | Level | When | Video (title) | YouTuber | Length · Views | ☐ |
|---|---|---|---|---|---|---|---|
| 24 | Bash scripting | 🟡 | To edit the deploy and provisioning scripts | [Bash Scripting Tutorial for Beginners](https://www.youtube.com/watch?v=tK9Oc6AEnR4) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 48m · 1.2M | ☐ |
| 25 | Python threading | 🔴 | To change how WhatsApp messages are queued | [Python Threading Tutorial: Run Code Concurrently Using the Threading Module](https://www.youtube.com/watch?v=IEEhzQoKtQU) | [Corey Schafer](https://www.youtube.com/@coreyms) | 36m · 923K | ☐ |
| 26 | WhatsApp Cloud API | 🟡 | Before taking WhatsApp beyond the test number | [Getting Started with WhatsApp Cloud APIs in 2026](https://www.youtube.com/watch?v=8hKEbOHWyQk) | [Programming Make Sense](https://www.youtube.com/@pms_code) | 6m · 40K | ☐ |
| 27 | AWS CLI | 🟢 | To read or change `provision-aws.sh` | [AWS CLI for Beginners](https://www.youtube.com/watch?v=9oYd5KQM8AQ) | [BrainTrust Digital](https://www.youtube.com/@BrainTrustDigital) | 7m · 17K | ☐ |
| 28 | Frontend (HTML, CSS, JS) | 🟡 | Not my target role; only to tweak the website | [Frontend Web Development Bootcamp Course (JavaScript, HTML, CSS)](https://www.youtube.com/watch?v=zJSY8tbf_ys) | [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) | 21h · 3.7M | ☐ |

**Total for stages 1–5, watching only the parts noted: about 15 hours.**

---

## 2. Where the backend logic lives (what to open to change what)

A message travels: **channel → router → conversation → rules engine → reply.**

| I want to… | Open this | What it does |
|---|---|---|
| Change a scheme's rules (age, income, documents) | `data/schemes/*.toml` (e.g. `apy.toml`) | One file per scheme; each value has its official source beside it. **Most changes happen here.** |
| Add a new scheme | Copy `data/schemes/_TEMPLATE.toml` | Fill it in; it answers "unknown" until a person signs it |
| Change how eligibility is decided | `sathi/rules/engine.py`, `sathi/rules/operators.py` | The **only** place a verdict is made. No AI is allowed in here |
| Change the questions or their order | `sathi/conversation/flow.py` | The step-by-step intake; asks questions, decides nothing |
| Change the wording (Hindi / English) | `data/strings_hi.toml`, `data/strings_en.toml` | All text the user sees |
| Change consent | `sathi/conversation/consent.py` | Asked first, before anything is recorded |
| Change Telegram behaviour | `sathi/channels/telegram.py` | Thin adapter, long polling |
| Change WhatsApp behaviour | `sathi/channels/whatsapp.py` | Thin adapter, webhook plus signature check |
| Change shared chat logic (both apps) | `sathi/channels/router.py` | Everything about a conversation except the wire |
| Change the one-page sheet / checklist | `sathi/pack/` | What to carry and where to go |
| Change what gets counted | `sathi/metrics/events.py`, `schema.sql` | The SQLite event log (coarse facts only) |
| Run it on my laptop | `python3 -m sathi.main` | One screening in the terminal |
| Check nothing broke | `python3 check.py` | Runs every self-check and test. **Run it after every change** |

**The safe-change routine:** edit → `python3 check.py` → commit and push (GitHub Actions re-checks) → deploy (the server runs all tests again before restarting).

---

## 3. 30-second answers to practise

- **Why only Python's standard library?** Nothing to install means nothing breaks on deploy day, and fewer security risks.
- **Why TOML for rules?** A non-programmer can check a rule against its source; Python reads TOML without extra libraries.
- **Why SQLite?** One file, no database server. It stores only coarse facts, so there's no personal data to leak.
- **Long polling vs webhook?** Telegram: my server asks and waits, so no public address is needed. WhatsApp: Meta calls my server, so it needs HTTPS and a signature check.
- **What does Caddy do?** One public HTTPS door on port 443 that routes to three local services, and it removes private data from its logs.
- **How do the services stay up?** systemd restarts them if they crash; a timer backs up the database every night.
- **How do you deploy safely?** All tests run on the server first; if one fails, the live version is untouched.
- **Where are the secrets?** In a root-only file on the server, never in GitHub.
- **Why AWS and not Azure?** I first planned Azure (the repo still has `provision-azure.sh`), but I had about $140 of AWS credit left, so I used AWS: an EC2 t4g.micro in Mumbai, the region closest to the users.
- **What did AI do, and what did you do?** AI (Claude Code) wrote most of the code. I made the decisions, checked every source, set up and run the server, and decided what was safe to ship. My focus is backend; I don't claim frontend skills.
