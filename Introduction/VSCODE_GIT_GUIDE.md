# 🚀 Git & GitHub with VS Code for Computational Physics

> Complete guide for version control using Visual Studio Code in physics research. Optimized for Python, C++, and scientific computing workflows.

[![VS Code](https://img.shields.io/badge/VS%20Code-1.80+-blue?logo=visualstudiocode)](https://code.visualstudio.com/)
[![Git](https://img.shields.io/badge/Git-2.40+-orange?logo=git)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Integrated-black?logo=github)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C++-11/14/17-00599C?logo=cplusplus)](https://isocpp.org/)

---

## 📑 Table of Contents

- [Introduction](#-introduction)
- [Installation & Setup](#-installation--setup)
- [VS Code Git Interface](#-vs-code-git-interface)
- [Essential Extensions](#-essential-extensions)
- [Basic Operations](#-basic-operations)
- [Branching & Merging](#-branching--merging)
- [GitHub Integration](#-github-integration)
- [Advanced Features](#-advanced-features)
- [Physics Workflow](#-physics-workflow)
- [Shortcuts & Productivity](#-shortcuts--productivity)
- [Troubleshooting](#-troubleshooting)
- [Best Practices](#-best-practices)

---

## 🎯 Introduction

### Why VS Code for Git in Physics?

- ✅ **Visual Interface** - No need to memorize commands
- ✅ **Integrated Terminal** - Command line when needed
- ✅ **Diff Viewer** - Side-by-side comparison
- ✅ **GitHub Integration** - Pull requests, issues, actions
- ✅ **Multi-platform** - Same experience on macOS and Windows
- ✅ **Extensions** - Python, C++, Jupyter support
- ✅ **IntelliSense** - Autocomplete for code and Git

### What You'll Learn

- Set up Git in VS Code from scratch
- Use Source Control panel efficiently
- Manage branches visually
- Resolve merge conflicts with ease
- Integrate with GitHub seamlessly
- Optimize workflow for physics projects

---

## 🔧 Installation & Setup

### Step 1: Install VS Code

<details>
<summary><b>macOS</b></summary>

```bash
# Download from https://code.visualstudio.com
# Or install via Homebrew
brew install --cask visual-studio-code

# Verify installation
code --version
```
</details>

<details>
<summary><b>Windows 11</b></summary>

```bash
# Download from https://code.visualstudio.com
# Or install via winget
winget install Microsoft.VisualStudioCode

# Verify installation
code --version
```
</details>

### Step 2: Install Git

```bash
# macOS
brew install git

# Windows
winget install --id Git.Git -e --source winget

# Verify
git --version
```

### Step 3: Configure Git in VS Code

**Open VS Code Settings** (`Cmd+,` on macOS, `Ctrl+,` on Windows)

Search for "git" and configure:

```json
{
  "git.enabled": true,
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  "git.suggestSmartCommit": true,
  "terminal.integrated.defaultProfile.osx": "bash",
  "terminal.integrated.defaultProfile.windows": "Git Bash"
}
```

**Or use Terminal** (`Ctrl+`\` or `Cmd+`\`):

```bash
# Configure user
git config --global user.name "Your Name"
git config --global user.email "your.email@university.edu"

# Set VS Code as default editor
git config --global core.editor "code --wait"

# Set default branch
git config --global init.defaultBranch main

# Enable colors
git config --global color.ui auto
```

### Step 4: Sign in to GitHub

1. Click on **Accounts** icon (bottom left)
2. Select **Sign in to Sync Settings**
3. Choose **Sign in with GitHub**
4. Authorize VS Code in browser
5. Done! ✅

---

## 🎨 VS Code Git Interface

### Source Control Panel

**Open**: Click Source Control icon in Activity Bar or press `Ctrl+Shift+G` (Windows) / `Cmd+Shift+G` (macOS)

```
┌─────────────────────────────────────────┐
│  SOURCE CONTROL                    ⟳ ⋯  │  ← Refresh, More actions
├─────────────────────────────────────────┤
│  Message: "Your commit message"         │  ← Commit message
│  ✓ Commit  ▼                            │  ← Commit button + options
├─────────────────────────────────────────┤
│  CHANGES (3)                        ⊕   │  ← Stage all
│    M  simulation.py                 +   │  ← Modified, stage
│    A  new_model.cpp                 +   │  ← Added, stage
│    D  old_test.py                   +   │  ← Deleted, stage
├─────────────────────────────────────────┤
│  STAGED CHANGES (2)                 −   │  ← Unstage all
│    M  analysis.py                   −   │  ← Staged, unstage
│    A  README.md                     −   │
└─────────────────────────────────────────┘
```

### File Status Indicators

| Symbol | Meaning | Color |
|--------|---------|-------|
| **M** | Modified | 🟡 Orange |
| **A** | Added (new) | 🟢 Green |
| **D** | Deleted | 🔴 Red |
| **U** | Untracked | 🟢 Green |
| **C** | Conflict | 🔴 Red |
| **R** | Renamed | 🟢 Green |

### Timeline View

**See file history**: Right-click file → **Open Timeline**

Shows:
- All commits affecting the file
- Who made changes
- When changes occurred
- Click to see diff

---

## 🔌 Essential Extensions

### Install via Extensions Panel

Press `Ctrl+Shift+X` (Windows) / `Cmd+Shift+X` (macOS)

#### Git & GitHub Extensions

```bash
# Install via terminal
code --install-extension eamodio.gitlens
code --install-extension github.vscode-pull-request-github
code --install-extension mhutchie.git-graph
code --install-extension donjayamanne.githistory
```

**Or search in Extensions panel:**

1. **GitLens** (`eamodio.gitlens`) ⭐ ESSENTIAL
   - Blame annotations inline
   - Rich commit history
   - Compare branches
   - File history

2. **GitHub Pull Requests** (`github.vscode-pull-request-github`)
   - Create/review PRs
   - Manage issues
   - GitHub Actions status

3. **Git Graph** (`mhutchie.git-graph`)
   - Visual commit graph
   - Branch visualization
   - Interactive history

4. **Git History** (`donjayamanne.githistory`)
   - View/search history
   - Compare commits
   - Cherry pick support

#### Physics-Specific Extensions

```bash
# Python
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter

# C++
code --install-extension ms-vscode.cpptools
code --install-extension ms-vscode.cmake-tools

# Data & Visualization
code --install-extension randomfractalsinc.vscode-data-preview
code --install-extension hediet.vscode-drawio

# Markdown
code --install-extension yzhang.markdown-all-in-one
code --install-extension bierner.markdown-mermaid
```

---

## 📦 Basic Operations

### Initialize Repository

#### Method 1: Using Source Control Panel

1. Open folder: `File → Open Folder...`
2. Open Source Control: `Ctrl+Shift+G` / `Cmd+Shift+G`
3. Click **Initialize Repository**
4. Done! ✅

#### Method 2: Using Terminal

```bash
# Open terminal: Ctrl+` or Cmd+`
git init
```

### Clone Repository

#### Method 1: Command Palette

1. Press `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Type: `Git: Clone`
3. Enter URL: `https://github.com/user/project.git`
4. Select destination folder
5. Choose **Open** or **Add to Workspace**

#### Method 2: Terminal

```bash
git clone https://github.com/user/physics-project.git
cd physics-project
code .  # Opens in VS Code
```

### Stage Changes

#### Visual Method

1. Open Source Control panel
2. Hover over file
3. Click **+** icon to stage
4. Or click **+** next to "CHANGES" to stage all

#### Shortcuts

- **Stage file**: Click **+** icon
- **Stage all**: `Ctrl+Shift+G` then `Ctrl+A` then `+`
- **Unstage file**: Click **−** icon in STAGED CHANGES

#### Partial Staging (Stage Lines)

1. Open file
2. Select lines to stage
3. Right-click → **Stage Selected Ranges**

### Commit Changes

#### Visual Method

1. Stage files
2. Enter commit message in text box
3. Press `Ctrl+Enter` / `Cmd+Enter` or click **✓ Commit**

#### With Options

Click **▼** next to Commit for:
- **Commit & Push**
- **Commit & Sync**
- **Commit Staged**
- **Commit All**

#### Keyboard Shortcut

With Source Control focused: `Ctrl+Enter` / `Cmd+Enter`

### View Changes (Diff)

#### Compare with Last Commit

- Click on **M** (modified) file in Source Control
- Side-by-side diff opens automatically
- **Red** = Removed lines
- **Green** = Added lines

#### Inline Diff

In editor, you'll see:
```python
# Line with changes shown inline
old_value = 100  # ← Red highlighting
new_value = 200  # ← Green highlighting
```

#### GitLens Inline Blame

Each line shows:
```python
def simulate():  # ← Your Name, 2 hours ago • feat: add simulation
    pass
```

Click blame to see full commit details.

### Discard Changes

#### Single File

1. Right-click file in Source Control
2. Select **Discard Changes**
3. Confirm

#### All Changes

1. Click **⋯** (More Actions) in Source Control
2. Select **Discard All Changes**
3. Confirm

⚠️ **Warning**: This is permanent!

---

## 🌿 Branching & Merging

### Branch Indicator

Look at **bottom-left corner** of VS Code:

```
🔀 main ↓1 ↑2
```
- `main` = current branch
- `↓1` = 1 commit behind remote
- `↑2` = 2 commits ahead of remote

### Create Branch

#### Method 1: Branch Indicator

1. Click branch name (bottom-left)
2. Select **Create new branch...**
3. Enter name: `feature/tensor-networks`
4. Press Enter

#### Method 2: Command Palette

1. `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Type: `Git: Create Branch...`
3. Enter branch name

#### Method 3: Git Graph

1. Open Git Graph: `Ctrl+Shift+P` → `Git Graph: View`
2. Right-click commit
3. Select **Create Branch...**

### Switch Branch

#### Method 1: Branch Indicator

1. Click branch name (bottom-left)
2. Select branch from list

#### Method 2: Command Palette

1. `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Type: `Git: Checkout to...`
3. Select branch

### Merge Branches

#### Visual Merge

1. Switch to target branch (e.g., `main`)
2. Command Palette: `Git: Merge Branch...`
3. Select source branch to merge
4. Resolve conflicts if any

#### Git Graph Method

1. Open Git Graph
2. Right-click target branch
3. Select **Merge into current branch**

### Resolve Merge Conflicts

When conflicts occur, VS Code shows:

```python
<<<<<<< HEAD (Current Change)
def calculate_energy(self):
    return self.hamiltonian()
=======
def calculate_energy(self):
    return self.total_energy()
>>>>>>> feature/new-model (Incoming Change)
```

**Options appear above conflict**:
- **Accept Current Change** - Keep HEAD version
- **Accept Incoming Change** - Keep feature branch version
- **Accept Both Changes** - Keep both
- **Compare Changes** - Side-by-side view

**Steps**:
1. Click appropriate action button
2. Repeat for all conflicts
3. Save file
4. Stage resolved file
5. Commit merge

---

## 🐙 GitHub Integration

### Connect to GitHub

Already done if you signed in! If not:

1. Click **Accounts** icon (bottom-left)
2. **Sign in with GitHub**
3. Authorize in browser

### Publish Repository

#### First Time Push

1. Make some commits locally
2. Click **Publish Branch** in Source Control
3. Choose **Public** or **Private**
4. Confirm repository name
5. Done! Repo created on GitHub

### Push & Pull

#### Push Changes

**Option 1**: Click **⋯** → **Push**

**Option 2**: Click sync icon (↻) in status bar

**Option 3**: `Ctrl+Shift+P` → `Git: Push`

#### Pull Changes

**Option 1**: Click **⋯** → **Pull**

**Option 2**: Click sync icon (↻) in status bar

**Option 3**: `Ctrl+Shift+P` → `Git: Pull`

#### Sync (Pull + Push)

Click **↻** icon in status bar (bottom-left)

### Pull Requests

With **GitHub Pull Requests** extension:

#### Create PR

1. Push branch to GitHub
2. Click **GitHub** icon in Activity Bar
3. Click **Create Pull Request**
4. Fill in details:
   - Title
   - Description
   - Reviewers
   - Labels
5. Click **Create**

#### Review PR

1. Click **GitHub** icon
2. Select PR from list
3. Review changes
4. Add comments
5. Approve or Request Changes

#### Merge PR

1. Open PR in GitHub panel
2. Click **Merge Pull Request**
3. Choose merge method:
   - Create a merge commit
   - Squash and merge
   - Rebase and merge

### GitHub Issues

1. Click **GitHub** icon
2. View issues
3. Create new issue
4. Reference in commits: `#123`

### GitHub Actions

View CI/CD status:
1. Click **GitHub** icon
2. Select **Actions** tab
3. View workflow runs
4. Check logs

---

## ⚡ Advanced Features

### GitLens Features

#### Blame Annotations

**Current Line Blame**: Shows automatically at end of line

**File Annotations**: 
- `Ctrl+Shift+P` → `GitLens: Toggle File Blame`
- Shows blame for every line

**Heatmap**:
- `Ctrl+Shift+P` → `GitLens: Toggle File Heatmap`
- Colors show change recency

#### Compare Features

1. **Compare with Branch**:
   - Right-click file
   - **GitLens → Compare File with Branch...**

2. **Compare with Revision**:
   - Right-click file
   - **GitLens → Compare File with Revision...**

3. **Compare with Working File**:
   - In Timeline, click commit
   - Select **Compare with Working File**

### Stash Changes

#### Create Stash

1. Click **⋯** in Source Control
2. Select **Stash → Stash (Include Untracked)**
3. Enter stash message (optional)

#### Apply Stash

1. Click **⋯** → **Stash → Apply Stash...**
2. Select stash to apply
3. Changes restored!

#### Stash Panel

- View all stashes in Source Control
- Apply, Pop, or Delete from panel

### Interactive Rebase

1. Open Git Graph
2. Right-click commit
3. Select **Rebase current branch on this commit...**
4. Choose **Interactive**
5. Edit commits:
   - **Pick** - Use commit
   - **Reword** - Edit message
   - **Edit** - Modify commit
   - **Squash** - Combine with previous
   - **Drop** - Remove commit

### Cherry Pick

1. Open Git Graph
2. Right-click commit from another branch
3. Select **Cherry Pick...**
4. Commit is applied to current branch

### Tags

#### Create Tag

1. Command Palette: `Git: Create Tag`
2. Enter tag name: `v1.0.0`
3. Enter message (optional)

#### Push Tags

1. Click **⋯** → **Push Tags**

#### View Tags

- Git Graph shows tags on commits
- Timeline shows tags

### Git History (Extension)

1. Right-click file
2. **Git: View File History**
3. Visual history opens
4. Click commit to see changes
5. Compare, checkout, or create branch

---

## 🔬 Physics Workflow in VS Code

### Project Setup

#### Recommended Workspace Structure

```
physics-project/
├── .vscode/
│   ├── settings.json          # Project settings
│   ├── launch.json            # Debug configs
│   ├── tasks.json             # Build tasks
│   └── extensions.json        # Recommended extensions
├── .git/
├── .gitignore
├── src/
├── notebooks/
├── tests/
└── data/
```

#### Configure .vscode/settings.json

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests"],
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "data/raw/*": true,
    "results/*": true
  },
  "git.ignoreLimitWarning": true
}
```

### Create .gitignore

1. Create `.gitignore` file
2. Use template:

```gitignore
# Python
__pycache__/
*.py[cod]
venv/
*.egg-info/

# Jupyter
.ipynb_checkpoints/

# Physics data
*.hdf5
*.h5
*.dat
data/raw/*
data/processed/*
results/
output/

# C++
*.o
*.out
*.exe

# ML models
*.pth
*.pkl
models/*.pth

# IDE
.vscode/settings.json  # If personalized
.DS_Store
```

3. Commit:
```bash
git add .gitignore
git commit -m "Add .gitignore for physics project"
```

### Commit Message Templates

#### Set Template

Create `.gitmessage`:

```
# Type(scope): Short description (max 50 chars)
#
# Detailed explanation
#
# Physical motivation:
#
# Results:
#
# Refs: #issue
```

Configure:
```bash
git config --global commit.template .gitmessage
```

#### Commit Prefix Snippet

Add to VS Code settings:

```json
{
  "git.inputValidation": "always",
  "git.inputValidationLength": 72,
  "git.inputValidationSubjectLength": 50
}
```

### Working with Jupyter Notebooks

#### Install nbdime

```bash
pip install nbdime
nbdime config-git --enable --global
```

#### Clear Outputs Before Commit

1. Install extension: **Jupyter Notebook Renderers**
2. Open notebook
3. **Clear All Outputs**: Click **⋯** → **Clear All Outputs**
4. Save and commit

#### Or Use Extension

Install: **Jupyter Notebook Cleaner**
- Automatically clears outputs on save
- Configurable in settings

### Git LFS in VS Code

```bash
# Install Git LFS
brew install git-lfs  # macOS
# Or download for Windows

# Initialize
git lfs install

# Track large files
git lfs track "*.hdf5"
git lfs track "*.pth"
git lfs track "data/raw/*"

# Commit .gitattributes
git add .gitattributes
git commit -m "Configure Git LFS"
```

**Track in VS Code**:
- `.gitattributes` file shows tracked patterns
- LFS files show with icon in Source Control
- Push/pull works automatically

### Multi-root Workspaces

For multiple related projects:

1. **File → Add Folder to Workspace...**
2. Add multiple projects
3. **File → Save Workspace As...**
4. Each project has own Git repo
5. Source Control shows all repos

### Task Automation

Create `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Simulation",
      "type": "shell",
      "command": "python",
      "args": ["${workspaceFolder}/src/run_simulation.py"],
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "pytest",
      "args": ["tests/"],
      "problemMatcher": []
    },
    {
      "label": "Format Code",
      "type": "shell",
      "command": "black",
      "args": ["src/"]
    }
  ]
}
```

Run: `Ctrl+Shift+B` / `Cmd+Shift+B`

---

## ⌨️ Shortcuts & Productivity

### Essential Keyboard Shortcuts

#### Windows / Linux

| Action | Shortcut |
|--------|----------|
| Open Source Control | `Ctrl+Shift+G` |
| Open Terminal | `` Ctrl+` `` |
| Command Palette | `Ctrl+Shift+P` |
| Quick Open | `Ctrl+P` |
| Commit | `Ctrl+Enter` (in Source Control) |
| Stage File | `Ctrl+Enter` (on file) |
| Search Files | `Ctrl+Shift+F` |
| Open Git Graph | `Ctrl+Shift+G`, then click icon |

#### macOS

| Action | Shortcut |
|--------|----------|
| Open Source Control | `Cmd+Shift+G` |
| Open Terminal | `` Cmd+` `` |
| Command Palette | `Cmd+Shift+P` |
| Quick Open | `Cmd+P` |
| Commit | `Cmd+Enter` (in Source Control) |
| Stage File | `Cmd+Enter` (on file) |
| Search Files | `Cmd+Shift+F` |

### Custom Keybindings

**File → Preferences → Keyboard Shortcuts** (`Ctrl+K Ctrl+S` / `Cmd+K Cmd+S`)

Add custom bindings:

```json
{
  "key": "ctrl+shift+g g",
  "command": "git-graph.view",
  "when": "!inDebugMode"
},
{
  "key": "ctrl+shift+g p",
  "command": "git.push",
  "when": "!inDebugMode"
},
{
  "key": "ctrl+shift+g f",
  "command": "git.fetch",
  "when": "!inDebugMode"
}
```

### Command Palette Aliases

Frequently used commands:
- `Git: Clone` - Clone repository
- `Git: Pull` - Pull from remote
- `Git: Push` - Push to remote
- `Git: Create Branch` - New branch
- `Git: Checkout to` - Switch branch
- `Git: Merge Branch` - Merge branches
- `Git: Stash` - Stash changes
- `Git Graph: View` - Open Git Graph

### GitLens Commands

- `GitLens: Show File History` - File timeline
- `GitLens: Compare with Branch` - Compare files
- `GitLens: Toggle File Blame` - Show blame
- `GitLens: Show Quick Commit Details` - Commit info

---

## 🔍 Troubleshooting

### Git Not Detected

**Problem**: VS Code shows "Git not found"

**Solution**:
1. Install Git (see installation section)
2. Restart VS Code
3. If still not detected, set path manually:
   ```json
   {
     "git.path": "C:\\Program Files\\Git\\bin\\git.exe"  // Windows
     "git.path": "/usr/local/bin/git"  // macOS
   }
   ```

### Authentication Issues

**Problem**: Can't push/pull, authentication fails

**Solution**:

#### HTTPS (Token-based)

1. Generate Personal Access Token on GitHub:
   - Settings → Developer settings → Personal access tokens
   - Generate new token (classic)
   - Select scopes: `repo`, `workflow`
2. Use token as password when prompted

#### SSH (Recommended)

```bash
# Generate key
ssh-keygen -t ed25519 -C "your.email@university.edu"

# Start ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: Settings → SSH keys → New SSH key
```

Then change remote to SSH:
```bash
git remote set-url origin git@github.com:user/repo.git
```

### Merge Conflicts Not Showing

**Problem**: Can't see conflict resolution options

**Solution**:
1. Ensure file is open in editor
2. Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Click **Accept Current** / **Accept Incoming** above markers
4. If not showing, install extension: **Merge Conflict**

### Large File Issues

**Problem**: Can't push large files (>100MB)

**Solution**:
1. Install Git LFS:
   ```bash
   brew install git-lfs  # macOS
   git lfs install
   ```
2. Track large files:
   ```bash
   git lfs track "*.hdf5"
   git add .gitattributes
   ```
3. Add and commit file normally

### Source Control Panel Empty

**Problem**: No files showing in Source Control

**Solution**:
1. Ensure folder is a Git repository:
   ```bash
   git status
   ```
2. If not: Initialize repository
3. Check `.gitignore` - files might be ignored
4. Refresh: Click **↻** in Source Control panel

### GitLens Not Working

**Problem**: GitLens features not appearing

**Solution**:
1. Check extension is enabled
2. Reload window: `Ctrl+Shift+P` → `Reload Window`
3. Check GitLens settings:
   ```json
   {
     "gitlens.advanced.messages": {
       "suppressShowKeyBindingsNotice": true
     }
   }
   ```

---

## ✅ Best Practices

### Daily Workflow

```
Morning:
1. Open VS Code
2. Pull latest changes (Ctrl+Shift+P → Git: Pull)
3. Create feature branch
4. Start coding

During Work:
1. Save frequently (Ctrl+S / Cmd+S)
2. Check Source Control panel often
3. Commit small, logical changes
4. Write descriptive messages

End of Day:
1. Commit any WIP (Work In Progress)
2. Push to remote backup
3. Or stash if not ready to commit
```

### Commit Message Convention

Use **Conventional Commits**:

```
feat: add Monte Carlo simulation
fix: correct energy calculation
docs: update theory documentation
style: format code with black
refactor: reorganize field classes
test: add conservation law tests
perf: optimize main loop
chore: update dependencies
```

**VS Code snippet** - Add to `.vscode/physics.code-snippets`:

```json
{
  "Git Commit": {
    "prefix": "gitcommit",
    "body": [
      "${1|feat,fix,docs,style,refactor,test,perf,chore|}: ${2:description}",
      "",
      "${3:detailed explanation}",
      "",
      "Refs: #${4:issue}"
    ]
  }
}
```

### Branch Naming

```
feature/     → feature/neural-network
bugfix/      → bugfix/energy-calculation
experiment/  → experiment/temperature-sweep
hotfix/      → hotfix/critical-error
paper/       → paper/prl-submission
refactor/    → refactor/simulation-core
```

### Code Review Workflow

1. **Push feature branch**
2. **Create PR** via GitHub panel
3. **Request reviewers**
4. **Address comments** in VS Code
5. **Push updates** automatically update PR
6. **Merge** when approved

### Workspace Organization

```
My-Physics-Research.code-workspace
├── Project 1: Ising Model
├── Project 2: MCMC Optimization
├── Project 3: Neural Network QFT
└── Shared: Common Libraries
```

Each project has own Git repo, all in one workspace.

---

## 🎓 Advanced Tips for Physics

### 1. Semantic Commits with Task Lists

```markdown
feat: implement Metropolis-Hastings algorithm

- [x] Add proposal distribution
- [x] Implement acceptance criterion
- [x] Add temperature parameter
- [ ] Optimize for large systems
- [ ] Add parallel tempering

Closes #42
```

### 2. GitLens for Code Review

Before submitting:
1. Toggle File Blame
2. Review your changes line-by-line
3. Check each change makes sense
4. Commit only related changes

### 3. Comparing Results

When experimenting:
```bash
# Create experiment branch
git checkout -b exp/params-v2

# Make changes, run simulation
python run_simulation.py

# Compare output with main branch
git checkout main
python run_simulation.py

# Use VS Code diff to compare result files
```

### 4. Documentation in Commits

Link to papers, equations, methods:

```bash
git commit -m "feat: implement RK4 integrator

Uses 4th order Runge-Kutta method for ODEs.
See: Numerical Recipes §16.1

Equations:
k1 = f(t, y)
k2 = f(t + h/2, y + h*k1/2)
...

Refs: #15"
```

### 5. Pre-commit Checks

Install extension: **Pre-Commit**

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.0.0
    hooks:
      - id: black
  
  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
  
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
```

Runs automatically before each commit!

### 6. Jupyter Notebook Best Practices

**Clear outputs before commit**:
1. Install extension: **Jupyter Notebook Renderers**
2. Command Palette: `Jupyter: Clear All Outputs`
3. Save and commit

**Or automate**:
```json
// settings.json
{
  "jupyter.alwaysTrustNotebooks": true,
  "jupyter.askForKernelRestart": false,
  "notebook.output.textLineLimit": 30
}
```

### 7. Multi-File Search with GitLens

Search across all branches:
1. `Ctrl+Shift+F` / `Cmd+Shift+F`
2. Enable **Use Git Graph Search**
3. Search shows results from all branches
4. Click to checkout and view

### 8. Custom Git Commands in Terminal

Add aliases to `.bashrc` or `.zshrc`:

```bash
# Quick aliases
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline --graph'
alias gco='git checkout'
alias gcb='git checkout -b'

# Physics-specific
alias gexp='git checkout -b exp/$(date +%Y%m%d)'
alias gpaper='git checkout -b paper/'
```

Use in VS Code integrated terminal!

### 9. Timeline for File History

**Quick history view**:
1. Right-click file in Explorer
2. Select **Open Timeline**
3. See all changes to file
4. Click commit to see diff
5. Right-click commit to:
   - Restore file
   - Compare with working
   - Copy commit SHA

### 10. Workspace Snippets for Commits

Create `.vscode/git-commits.code-snippets`:

```json
{
  "Physics Feature Commit": {
    "prefix": "gfeat",
    "body": [
      "feat(${1|simulation,analysis,model,algorithm|}): ${2:description}",
      "",
      "${3:Detailed explanation}",
      "",
      "Physical context: ${4:context}",
      "",
      "Parameters:",
      "- ${5:parameter}: ${6:value}",
      "",
      "Results: ${7:results}",
      "",
      "Refs: #${8:issue}"
    ],
    "description": "Physics feature commit template"
  },
  "Physics Fix Commit": {
    "prefix": "gfix",
    "body": [
      "fix(${1|calculation,simulation,analysis|}): ${2:description}",
      "",
      "Problem: ${3:what was wrong}",
      "",
      "Solution: ${4:how it was fixed}",
      "",
      "Impact: ${5:what changed in results}",
      "",
      "Refs: #${6:issue}"
    ],
    "description": "Physics fix commit template"
  },
  "Experiment Commit": {
    "prefix": "gexp",
    "body": [
      "exp: ${1:experiment description}",
      "",
      "Hypothesis: ${2:what we're testing}",
      "",
      "Parameters:",
      "- Temperature: ${3:T}",
      "- System size: ${4:N}",
      "- Steps: ${5:steps}",
      "",
      "Results: ${6:outcome}",
      "",
      "Conclusion: ${7:interpretation}"
    ],
    "description": "Experiment commit template"
  }
}
```

---

## 📊 Git Graph Visualization

### Install Git Graph Extension

```bash
code --install-extension mhutchie.git-graph
```

### Features

**Visual commit history**:
```
* a1b2c3d (HEAD -> main) feat: add simulation
|
| * d4e5f6g (feature/new) refactor: optimize loop
|/
* g7h8i9j docs: update README
|
* j0k1l2m Initial commit
```

**Actions available**:
- Right-click commit → Create branch
- Right-click commit → Cherry pick
- Right-click commit → Revert
- Right-click branch → Merge
- Right-click branch → Rebase
- Drag and drop to rebase

### Customize Git Graph

Settings → Search "Git Graph":

```json
{
  "git-graph.repository.commits.initialLoad": 300,
  "git-graph.repository.commits.showSignatureStatus": true,
  "git-graph.date.format": "ISO Date & Time",
  "git-graph.graph.colours": [
    "#0085d9",
    "#d73a4a",
    "#6f42c1",
    "#28a745",
    "#e36209"
  ],
  "git-graph.graph.style": "rounded"
}
```

---

## 🎨 Customizing Git in VS Code

### Color Theme for Git

Recommended themes with great Git diff colors:
- **One Dark Pro**
- **Material Theme**
- **Night Owl**
- **Dracula Official**

Install: `Ctrl+Shift+X` / `Cmd+Shift+X` → Search theme

### Custom Diff Colors

Add to `settings.json`:

```json
{
  "workbench.colorCustomizations": {
    "diffEditor.insertedTextBackground": "#28a74522",
    "diffEditor.removedTextBackground": "#d73a4a22",
    "diffEditor.insertedLineBackground": "#28a74511",
    "diffEditor.removedLineBackground": "#d73a4a11",
    "gitDecoration.modifiedResourceForeground": "#e2c08d",
    "gitDecoration.deletedResourceForeground": "#c74e39",
    "gitDecoration.untrackedResourceForeground": "#73c991",
    "gitDecoration.conflictingResourceForeground": "#e4676b"
  }
}
```

### Status Bar Customization

```json
{
  "git.decorations.enabled": true,
  "git.enableStatusBarSync": true,
  "scm.diffDecorationsGutterVisibility": "always",
  "scm.diffDecorationsGutterWidth": 4
}
```

---

## 🔐 Security & Privacy

### Exclude Sensitive Files

Create `.gitignore`:

```gitignore
# Credentials
secrets.py
config_local.py
.env
*.key
*.pem

# API keys
api_keys.json
credentials.json

# Private data
data/private/*
results/unpublished/*

# Personal notes
NOTES.md
TODO_private.md
```

### Git Hooks in VS Code

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash

# Check for sensitive data
if git diff --cached | grep -i "password\|secret\|api.key\|token"; then
    echo "⚠️  WARNING: Possible sensitive data detected!"
    echo "Review changes and ensure no secrets are committed."
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check for large files
for file in $(git diff --cached --name-only); do
    size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
    if [ $size -gt 104857600 ]; then  # 100MB
        echo "❌ Error: $file is larger than 100MB"
        echo "Consider using Git LFS for large files"
        exit 1
    fi
done

echo "✅ Pre-commit checks passed"
```

Make executable:
```bash
chmod +x .git/hooks/pre-commit
```

### Review Before Push

Always review before pushing:
1. Open Source Control
2. Check **Commits** section
3. Click each commit
4. Review all changes
5. Ensure no sensitive data
6. Then push

---

## 📈 Performance Optimization

### For Large Repositories

```json
{
  "git.autorefresh": true,
  "git.autofetch": false,  // Disable for large repos
  "git.decorations.enabled": true,
  "search.followSymlinks": false,
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/node_modules/**": true,
    "**/data/**": true,
    "**/results/**": true
  }
}
```

### Exclude Large Folders

```json
{
  "files.exclude": {
    "**/.git": true,
    "**/__pycache__": true,
    "**/data/raw": true,
    "**/results": true
  }
}
```

### Git Performance Settings

```bash
# In terminal
git config --global core.preloadindex true
git config --global core.fscache true
git config --global gc.auto 256
```

---

## 🚀 Quick Reference Card

### Essential VS Code Git Shortcuts

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| **Source Control Panel** | `Ctrl+Shift+G` | `Cmd+Shift+G` |
| **Commit** | `Ctrl+Enter` | `Cmd+Enter` |
| **Terminal** | `` Ctrl+` `` | `` Cmd+` `` |
| **Command Palette** | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| **Quick Open** | `Ctrl+P` | `Cmd+P` |
| **Search** | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| **View Changes** | Click file | Click file |
| **Stage File** | `+` icon | `+` icon |
| **Unstage** | `-` icon | `-` icon |
| **Discard Changes** | Right-click | Right-click |

### Common Commands (Terminal)

```bash
# Basic
git status
git add .
git commit -m "message"
git push
git pull

# Branching
git checkout -b new-branch
git checkout main
git merge feature-branch

# Undo
git restore file
git reset --soft HEAD~1
git stash

# History
git log --oneline
git diff
git show commit-id
```

### GitLens Shortcuts

| Action | Command |
|--------|---------|
| **File History** | Right-click → GitLens → File History |
| **Blame** | `Ctrl+Shift+P` → Toggle File Blame |
| **Compare** | Right-click → GitLens → Compare |
| **Line History** | Click blame annotation |

---

## 📚 Resources & Learning

### Official Documentation
- [VS Code Git Documentation](https://code.visualstudio.com/docs/editor/versioncontrol)
- [GitLens Documentation](https://gitlens.amod.io)
- [GitHub in VS Code](https://code.visualstudio.com/docs/editor/github)

### Video Tutorials
- **VS Code Git Tutorial** - YouTube search
- **GitLens Features** - Official channel
- **GitHub in VS Code** - Microsoft Learn

### Extensions to Explore
- **Git History** - View file/line history
- **Git File History** - Alternative history viewer
- **GitLab Workflow** - For GitLab users
- **Conventional Commits** - Commit message helper

### Cheat Sheets
- [VS Code Keyboard Shortcuts PDF](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

---

## 💻 Complete Setup Example

### Full Configuration for Physics Project

**1. Install Everything:**

```bash
# macOS
brew install --cask visual-studio-code
brew install git git-lfs python

# Windows
winget install Microsoft.VisualStudioCode
winget install Git.Git
winget install Python.Python.3.11
```

**2. Configure Git:**

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@university.edu"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
```

**3. Install Extensions:**

```bash
# Essential
code --install-extension eamodio.gitlens
code --install-extension github.vscode-pull-request-github
code --install-extension mhutchie.git-graph

# Python
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter

# C++
code --install-extension ms-vscode.cpptools

# Utilities
code --install-extension yzhang.markdown-all-in-one
```

**4. VS Code Settings** (`settings.json`):

```json
{
  "git.enabled": true,
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  "gitlens.hovers.currentLine.over": "line",
  "gitlens.currentLine.enabled": true,
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "editor.formatOnSave": true,
  "files.autoSave": "afterDelay",
  "files.exclude": {
    "**/__pycache__": true,
    "**/.git": false,
    "data/raw/*": true
  }
}
```

**5. Create Project:**

```bash
mkdir quantum-simulation
cd quantum-simulation
code .

# In VS Code terminal:
git init
python -m venv venv
source venv/bin/activate  # macOS
# or
.\venv\Scripts\activate  # Windows

pip install numpy scipy matplotlib jupyter pytest black
pip freeze > requirements.txt

# Create structure
mkdir -p src tests notebooks data results

# Create .gitignore
curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore -o .gitignore
echo -e "\n# Physics specific\n*.hdf5\ndata/\nresults/" >> .gitignore

# Initial commit
git add .
git commit -m "Initial project setup"
```

**6. Connect to GitHub:**

```bash
# Create repo on GitHub, then:
git remote add origin git@github.com:username/quantum-simulation.git
git push -u origin main
```

**Done! Ready for physics computing! 🚀**

---

## 🎯 Workflow Summary

### Daily Routine

```
🌅 Morning
├── Open VS Code
├── Pull latest: Ctrl+Shift+P → Git: Pull
└── Create branch: Click branch indicator

💻 During Work
├── Code → Save → See changes in Source Control
├── Stage specific files: Click + on file
├── Commit: Type message, Ctrl+Enter
├── Push frequently: Click sync icon
└── Open terminal when needed: Ctrl+`

🌙 Evening
├── Review day's work: Git Graph
├── Push all changes
└── Clean up branches if needed
```

### For Experiments

```
🔬 Experiment Workflow
├── Create exp branch: exp/parameter-sweep
├── Modify code, run simulations
├── Commit results with parameters
├── Compare with main using GitLens
├── If successful → Merge to develop
└── If not → Keep branch for reference
```

### For Papers

```
📄 Paper Workflow
├── Create paper branch: paper/prl-2025
├── Commit analysis code
├── Commit figure generation scripts
├── Tag version: v1.0-paper
├── Archive when published
└── Keep branch indefinitely
```

---

## ✨ Pro Tips

### 1. Use Multi-Cursor for Conflicts

When resolving many similar conflicts:
1. `Alt+Click` / `Option+Click` to add cursors
2. Select **Accept Current** on all at once
3. Saves tons of time!

### 2. Compare Any Files

Right-click file → **Select for Compare**
Right-click another → **Compare with Selected**

Great for comparing simulation outputs!

### 3. Fold Git Output

In Source Control commit message box:
- `Ctrl+K Ctrl+0` - Fold all
- `Ctrl+K Ctrl+J` - Unfold all

### 4. Search in Git History

`Ctrl+Shift+F` → Click "..." → **Search in Git History**

Find when specific code was added!

### 5. Peek Definition in Diff

When viewing diff:
- `Alt+F12` / `Option+F12` - Peek definition
- See context without leaving diff!

---

## 🎓 Learning Path

### Week 1: Basics
- ✅ Install VS Code + Git
- ✅ Configure settings
- ✅ Learn Source Control panel
- ✅ Practice commit/push/pull

### Week 2: Branching
- ✅ Create branches
- ✅ Switch branches
- ✅ Merge branches
- ✅ Resolve conflicts

### Week 3: Tools
- ✅ Install GitLens
- ✅ Learn Git Graph
- ✅ Use GitHub integration
- ✅ Try Pull Requests

### Week 4: Advanced
- ✅ Interactive rebase
- ✅ Cherry pick
- ✅ Stash management
- ✅ Custom workflows

---

## 🏆 You're Ready!

You now have everything needed to use Git & GitHub efficiently in VS Code for your physics computing projects!

**Key Takeaways:**
- ✅ VS Code makes Git visual and intuitive
- ✅ GitLens supercharges Git features
- ✅ Keyboard shortcuts boost productivity
- ✅ GitHub integration enables collaboration
- ✅ Extensions customize for physics work

**Next Steps:**
1. Set up your first project
2. Practice daily workflow
3. Explore GitLens features
4. Customize to your needs
5. Share with your research group!

---

## 📬 Feedback & Contributions

Found something missing? Want to add physics-specific examples?

Open an issue or submit a pull request!

---

**Happy Coding & Computing! 🚀🔬**

*Version 1.0 - October 2025*
*Optimized for Physics Research on macOS & Windows 11*
