### Session 1 | part 1

> Programming is about solving problems, not just writing code. Labs are not a race; they are a marathon, so take your time. Do not copy and run blindly. Think first, and if you get stuck, ask Stelios.

#### 1. Goal

In this first tutorial, we will prepare your workspace. Pay attention, as you will need to follow these steps in future classes.

#### 2. Workspace setup

1. Install Git if it is not already installed from [here](https://git-scm.com/install/). For Mac: `brew install git`. For Windows: download and install it.
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

You will need a virtual environment to install the required packages. 

> [!TIP]
>
> Make sure you are in the correct folder before creating it. You can create one environment per session (recommended), or use one environment for the entire `bda` project. 
>
> Navigate to the folder using `cd session1`.

Create a virtual environment (Mac or Windows):

```powershell
python -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

> On Windows (VS Code terminal):
>
> - PowerShell: `.venv\Scripts\Activate.ps1` (may be blocked by execution policy on some machines)
> - Optional temporary PowerShell bypass (current session only):
>   `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
>   Then run: `.venv\Scripts\Activate.ps1`
> - If activation is blocked, run scripts directly with: `.venv\Scripts\python.exe your_script.py`

Deactivate it when needed:

```bash
deactivate
```

Now check the `requirements.txt` file. It contains the dependencies we need:

```txt
huggingface_hub==0.23.4
datasets==2.20.0
requests==2.32.3
quizmd
```

> [!TIP]
>
> A **`requirements.txt`** file lists all Python packages a project needs. It helps everyone recreate the same environment. It’s better to specify exact versions.

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

Check the output to ensure everything installed successfully. Don't worry about warnings. You are now ready to proceed. You can use the `clear` command to clear the terminal. Try it out.

#### 7. Exercise 1

For now, minimise the current VS Code window. On your Desktop (or any folder you prefer), create a new folder called `test-folder`.

1. Open a new VS Code window and open the `test-folder`.
2. Create and activate a virtual environment.
3. Create a `requirements.txt` file, add the `requests` library (`2.32.3`), and install it.
4. Create a file named `solution_part1.py` and run the script below.

File: `test-folder/solution_part1.py`

```python
import re
from urllib.request import urlopen

url = "https://www.google.com"
with urlopen(url) as response:
    html = response.read().decode("utf-8", errors="ignore")

match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
print(match.group(1).strip() if match else "No title found")
```

This exerice is more about learning how to manage your `.venv`. When finished, keep `solution_part1.py` as your solution file.

> [!TIP]
>
> Why dot in `.venv`? 
>
> The `.` makes the folder hidden by default, keeping your project directory clean.

#### 8. Quiz

`quizmd` is a command-line interface (CLI) to run interactive quizzes in the lab (made by Stelios 🙂). You can still install it like this.

```bash
pip install quizmd
```

>  Run the quiz in your terminal and ask Stelios for help if you’re unsure. Solutions are in the `quizzes` folder but don't see them yet.
>

Start the quiz by selecting a theme that matches your terminal:

Use the default theme (no --theme needed)
```
quizmd quizzes/python-workspace-setup-quiz.md
```
Or choose a theme

Use `--theme light` if your terminal has a light background or `--theme dark` if your terminal has a dark background.

```
quizmd --theme light quizzes/python-workspace-setup-quiz.md
quizmd --theme dark quizzes/python-workspace-setup-quiz.md
```

For a focus-mode, try:

```
quizmd --full-screen --theme dark quizzes/python-workspace-setup-quiz.md
```

For accessibility use this: `quizmd --no-color quizzes/python-workspace-setup-quiz.md`

> [!IMPORTANT]
>
> Review the quiz rules before you start. 
>
> Use the `space bar` to select an option, then `press Enter` to move to the next question. Go ahead and complete the quiz 🎉!

Move to the next tutorial.
