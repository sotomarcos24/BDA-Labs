### Session 1 | part 1

> Programming is about solving problems, not just writing code. Labs are not a race; they are a marathon, so take your time. Do not copy and run blindly. Think first, and if you get stuck, ask Stelios.

#### 1. Goal

In this first tutorial, we will prepare your workspace. Pay attention, as you will need to follow these steps in future classes.

#### 2. Workspace setup

1. Install Git from [here](https://git-scm.com/install/).
   * For Mac: `brew install git`. For Windows: download and install it.
2. Install [Visual Studio Code](https://code.visualstudio.com/) (or another editor you prefer). I will use VS Code in this module. After installing Git, restart VS Code if it was already open.
3. Open a terminal.
4. Clone the class repository:

```bash
git clone https://github.com/warestack/bda
```

5. Open the project folder in VS Code.
6. Open a terminal inside VS Code.
7. You will need to navigate to folders using the `cd` command.

#### 3. Check Python installation

Check that Python is installed:

```bash
python3 --version
```

On Windows, you can also run:

```powershell
python --version
python3 --version
py --version
```

Depending on your Python installation on Windows, one of the above commands may work while others may not.

This part of the class is a recap of the basics. We will reuse these steps in future sessions.

#### 4. Basics you should know

- `Python`: the programming language, not the snake 🐍.

- `Terminal`: a text-based tool where you run commands like `python3 --version` or `pip install`.
- `cd`: changes directory (moves you into another folder).
- `pwd`: prints your current folder path.
- `Virtual environment (.venv)`: keeps each project’s Python packages separate, so different projects don’t conflict. Different projects often need different package versions; isolation avoids conflicts.
- `pip`: Python’s package manager; it installs libraries like `huggingface_hub` or `datasets`.
- `requirements.txt`: a list of required Python packages for the project. It lets everyone install the same dependencies and reproduce the same setup.
- `README.md`: a simple project file where you document what you built, what worked, and what is pending (useful for tracking progress). Not sure about Markdown syntax? [Check here](https://www.markdownguide.org/basic-syntax/).
- `session_solutions/`: the folder you need to create to store your answers for each tutorial part (no need to submit now, but you can share it with Stelios later, for example for homework).

You will need to navigate folders in the terminal using `cd`.

Quick examples (macOS/Linux):

```bash
pwd
cd session1
pwd
cd ..
```

Quick examples (Windows PowerShell):

```powershell
Get-Location
cd session1
Get-Location
cd ..
```

#### 5. Create and manage a virtual environment

Create a virtual environment:

```bash
python3 -m venv .venv
```

On Windows, you can also run:

```powershell
python -m venv .venv
```

Alternative on some Windows installations:

```powershell
py -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

> On Windows (VS Code terminal):
> - PowerShell: `.venv\Scripts\Activate.ps1` (may be blocked by execution policy on some machines)
> - Command Prompt: `.venv\Scripts\activate.bat`
> - If activation is blocked, run scripts directly with: `.venv\Scripts\python.exe your_script.py`
> - Optional temporary PowerShell bypass (current session only):
>   `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
>   Then run: `.venv\Scripts\Activate.ps1`

Deactivate it when needed:

```bash
deactivate
```

Now check the `requirements.txt` file. It contains the dependencies we need:

```txt
huggingface_hub
datasets
```

> A **`requirements.txt`** file lists all Python packages a project needs. It helps everyone recreate the same environment.
>
> It’s better to specify exact versions:
>
> ```txt
> huggingface_hub==0.23.4
> datasets==2.20.0
> ```

#### 6. Install dependencies

Activate `.venv` again and install dependencies:

```bash
pip install -r requirements.txt
```

If `pip` is missing, run:

```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```

You are now ready.

#### 7. Exercise 1

Create an empty folder called `test-folder` on your Desktop.

1. Open a new VS Code window and select `test-folder`.
2. Create and activate a new virtual environment.
3. Make sure `requests` is installed (included in `requirements.txt`).
4. Create a file named `solution_part1.py` and run the script below.

```python
import re
from urllib.request import urlopen

url = "https://www.google.com"
with urlopen(url) as response:
    html = response.read().decode("utf-8", errors="ignore")

match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
print(match.group(1).strip() if match else "No title found")
```

This exerice is more about learning how to manage your `venv`. When finished, keep `solution_part1.py` as your solution file.

#### 7.1. Create your solutions folder (do this once)

From the `session1` folder, create your solutions folder:

```bash
mkdir -p session_solutions
```

On Windows PowerShell:

```powershell
mkdir session_solutions
```

Store your Session 1 files there, for example:

```txt
session1/session_solutions/session-01-part-01.py
```

#### 8. Quiz

Install `quizmd` directly from PyPI:

```bash
pip install quizmd
```

Or install everything for this session with:

```bash
pip install -r requirements.txt
```

>  `quizmd` is a command-line interface (CLI) to run interactive quizzes in the lab (made by Stelios 🙂). Run the quiz in your terminal and ask Stelios for help if you’re unsure. Solutions are in the `quizzes` folder but don't see them yet.

Install the `requirements.txt`  and the run the quiz by choosing your preferred theme:

```bash
quizmd --theme light quizzes/python-workspace-setup-quiz.md
quizmd --theme dark quizzes/python-workspace-setup-quiz.md
```

- Use `--theme light` if your terminal has a white/light background.
- Use `--theme dark` if your terminal has a dark background.

> For accessibility use this: `quizmd --no-color quizzes/python-workspace-setup-quiz.md`

> [!IMPORTANT]
>
> Review the quiz rules before you start. Use the `space bar` to select the correct option, then `press Enter` to move to the next question.

#### 9. Suggested structure

Store your solutions in separate files, for example:

```txt
session1/
  README.md
  session_solutions/
    session-01-part-01.py
    session-01-part-02.py
    session-01-part-03.py
```

Create a `README.md` and keep track of your progress and solutions.

> This is good professional practice: it helps you stay organized, makes grading easier, and creates a portfolio you can show later.

#### 10. README example

```md
# BDA - Session 1 Solutions

## Environment
- Python version: 3.x.x
- Virtual environment: `.venv`
- Installed packages:
  - huggingface_hub
  - datasets
  - requests

## Files
- `session_solutions/session-01-part-01.py`
  - Goal: verify environment setup and fetch/read CSV with `requests`
  - Status: completed

- `session_solutions/session-01-part-02.py`
  - Goal: counters, loops, and indexing practice
  - Status: add your status here

- `session_solutions/session-01-part-03.py`
  - Goal: read CSV and solve dataset tasks with pure Python
  - Status: add your status here

## Notes
- Main issue faced: `pip` missing initially.
- Fix applied: `python3 -m ensurepip --upgrade`.
- Reflection: understanding virtual environments is essential for clean project setup.
```
