# Python

From first script to production. 26 weeks, plus optional data science.

| Stage | Weeks | Focus |
|:--|:--|:--|
| 1 | 1–4 | Foundations |
| 2 | 5–6 | Object-oriented programming |
| 3 | 7–10 | Advanced Python |
| 4 | 11–16 | Web development |
| 5 | 17–20 | Databases |
| 6 | 21–24 | DevOps and deployment |
| 7 | 25–26 | Testing and quality |
| 8 | 27–32 | Data science and ML (optional) |

Want more depth? Take the [mastery track](#mastery-track) instead of stages 1–3.

## 1. Foundations

Weeks 1–4.

**Core**
- [ ] Install Python 3.11+ and set up the environment
- [ ] Variables, data types, operators
- [ ] if/else and loops
- [ ] Lists, tuples, dictionaries, sets
- [ ] Functions and scope
- [ ] Files and I/O
- [ ] Errors and exceptions

**Tools**
- [ ] VS Code, PyCharm or Jupyter
- [ ] Git and GitHub basics
- [ ] pip
- [ ] Virtual environments: venv, conda

**Learn:** [Official Python docs](https://docs.python.org/) · *Python Crash Course* by Eric Matthes · freeCodeCamp Python course

## 2. Object-oriented programming

Weeks 5–6.

- [ ] Classes and objects
- [ ] Encapsulation
- [ ] Inheritance and polymorphism
- [ ] Magic methods and operator overloading
- [ ] Abstract classes and interfaces
- [ ] Design patterns: factory, observer, singleton

## 3. Advanced Python

Weeks 7–10.

**Features**
- [ ] Decorators and context managers: logging, auth, caching
- [ ] Generators and iterators: memory-light data pipelines
- [ ] Threads and processes: concurrent tasks, scraping
- [ ] asyncio: I/O-heavy and real-time apps
- [ ] Comprehensions and lambdas
- [ ] Metaclasses and descriptors: frameworks, ORMs

**Data**
- [ ] NumPy
- [ ] Pandas
- [ ] Matplotlib and Seaborn
- [ ] JSON, CSV, XML

## 4. Web development

Weeks 11–16.

**Frontend basics**
- [ ] HTML, CSS, JavaScript
- [ ] Bootstrap or Tailwind CSS
- [ ] REST API concepts

**Backend.** Master one framework first.

| Framework | Learning curve | Best for |
|:--|:--|:--|
| FastAPI | Medium | APIs, modern apps. Best first pick. |
| Django | Steep | Full applications |
| Flask | Easy | Prototypes, microservices |

- [ ] FastAPI: basics, Pydantic validation, Swagger docs, auth
- [ ] Django: MVT pattern, models and ORM, views and templates, auth, admin
- [ ] Flask: basics, routing and blueprints, Jinja2 templates, extensions

## 5. Databases

Weeks 17–20.

**SQL**
- [ ] SELECT, INSERT, UPDATE, DELETE
- [ ] Joins and relationships
- [ ] Database design and normalization

**From Python**
- [ ] SQLite with `sqlite3`
- [ ] PostgreSQL with `psycopg2`
- [ ] MySQL with PyMySQL
- [ ] SQLAlchemy ORM
- [ ] Alembic migrations

**NoSQL**
- [ ] MongoDB with PyMongo
- [ ] Redis for caching

| Use | Pick |
|:--|:--|
| Complex apps | PostgreSQL |
| Flexible schema | MongoDB |
| Sessions and cache | Redis |
| Development and tests | SQLite |

## 6. DevOps and deployment

Weeks 21–24.

**Containers**
- [ ] Docker and Dockerfiles
- [ ] Docker Compose
- [ ] Kubernetes basics

**Hosting**
- [ ] Heroku
- [ ] AWS basics: EC2, S3, RDS
- [ ] DigitalOcean droplets
- [ ] Vercel serverless functions
- Later: GCP, Azure

**CI/CD**
- [ ] GitHub Actions
- [ ] GitLab CI
- [ ] Jenkins basics

## 7. Testing and quality

Weeks 25–26. Many fast unit tests, some integration tests, few end-to-end tests.

**Testing**
- [ ] unittest
- [ ] pytest
- [ ] Mocks and fixtures
- [ ] Coverage reports
- [ ] Integration tests

**Code quality**
- [ ] PEP 8
- [ ] flake8 or pylint
- [ ] Black
- [ ] Type hints and mypy
- [ ] Complexity checks

## 8. Data science and ML

Weeks 27–32. Optional.

- [ ] Jupyter
- [ ] Statistics with SciPy
- [ ] Advanced visualization
- [ ] Data cleaning
- [ ] scikit-learn
- [ ] Deep learning with TensorFlow or PyTorch
- [ ] Model evaluation and validation
- [ ] MLOps basics

## Mastery track

12 weeks. For deep Python before [DSA](DSA.md). About 15 hours a week, one track at a time.

### Week 1: Setup

- [ ] Python 3.12+, pyenv or venv, VS Code
- [ ] ruff, black, pytest, mypy, pre-commit
- [ ] CLI template: argparse, logging, timers
- [ ] Benchmark harness: `timeit`, `perf_counter`, property tests

**Gate:** Repo bootstrapped with CI for lint and tests.

### Weeks 2–4: Data model and idioms

- [ ] Mutability, slicing, iterators, generators
- [ ] `__iter__`, `__len__`, `__getitem__`, ordering, hashing, equality
- [ ] `list`, `dict`, `set`, `heapq`, `deque`, `bisect` and their complexities
- [ ] Build from scratch: dynamic array with amortized analysis, hash map, `OrderedDict`

**Gate:** Explain why `dict` lookup is O(1) on average.

### Weeks 5–6: OOP, protocols, typing

- [ ] OOP vs duck typing, `@dataclass`, ABCs, generics
- [ ] SOLID principles in Python
- [ ] Build from scratch: plugin system, typed `Vector[T]`

**Gate:** A mini library passes `mypy --strict`.

### Weeks 7–8: Standard library and performance

- [ ] `collections`, `math`, `functools`, `itertools`, `pathlib`, concurrency
- [ ] Profiling with `cProfile` and `snakeviz`
- [ ] Build from scratch: parallel map with a process pool

**Gate:** Cut runtime by 25% or more through profiling.

### Weeks 9–10: Testing, debugging, packaging

- [ ] Unit, property and golden tests, mocking, coverage targets
- [ ] Debugging with `pdb` and VS Code, structured logging
- [ ] Packaging: `pyproject.toml`, semver, CLI entry points

**Gate:** A local package with 90%+ test coverage.

### Weeks 11–12: Competitive programming Python

- [ ] Recursion limits, iterative DP, fast I/O, custom sort keys
- [ ] Build from scratch: stable mergesort, counting sort, radix sort

**Gate:** Pick the best built-in structure for any scenario.

## Pick a path

| Path | Focus |
|:--|:--|
| Web developer | Advanced Django or FastAPI, microservices, GraphQL, WebSockets |
| Data scientist | Advanced ML, Spark and Hadoop, statistical modeling, A/B testing |
| DevOps engineer | Terraform, monitoring and logging, security, cloud architecture |
| Automation engineer | Web scraping with BeautifulSoup and Scrapy, process automation, API integration, scheduling |
| Other | Games, desktop apps, cybersecurity, blockchain |

Career ladders: junior developer to senior developer to tech lead · data analyst to data scientist · DevOps associate to cloud architect.

## Projects

**Beginner**
- Console calculator
- To-do list app
- Guess the number, rock-paper-scissors
- CSV data processor

**Intermediate**
- Blog with Django or Flask
- Data dashboard
- Job listings scraper
- Expense tracker with a database

**Advanced**
- Online store
- REST API with auth
- ML model deployment
- Real-time chat
- Microservices app

## Resources

**Books:** *Python Crash Course* (Eric Matthes) · [*Fluent Python*](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) · [*Effective Python*](https://effectivepython.com/) (Brett Slatkin) · *Clean Code* (Robert Martin) · *Python Tricks* (Dan Bader) · *Architecture Patterns with Python*

**Courses:** CS50P (Harvard) · Python for Everybody · FastAPI course · Django course

**Sites:** [Real Python](https://realpython.com/) · [Python docs](https://docs.python.org/) · GeeksforGeeks · [LeetCode](https://leetcode.com/) · [HackerRank](https://www.hackerrank.com/)

**YouTube:** Corey Schafer · Programming with Mosh · Tech With Tim · ArjanCodes · Python Engineer

**Community:** [r/Python](https://reddit.com/r/Python) · [Python Discord](https://discord.gg/python) · [Stack Overflow](https://stackoverflow.com/questions/tagged/python) · [DEV Python](https://dev.to/t/python) · PyCon · Django and Flask meetups · local Python groups

**Stay current:** Python Weekly newsletter · PEPs · Python developers on Twitter · new libraries · online conferences

**Certifications:** PCEP (entry) · PCAP (associate) · PCPP (professional) · AWS Certified Developer or another cloud certification

## Habits

- Code 1–2 hours every day.
- Build while you learn: 80% doing, 20% reading.
- Done beats perfect. Ship, then improve.
- Use Git from day one. Commit early and often.
- Find a coding buddy. Ask for help when stuck.
- Read other people's code.
- Prefer official docs and recent content. Check publish dates.
- Don't rush the basics. Don't learn everything at once.
