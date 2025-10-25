# 🔬 Git & GitHub Complete Tutorial for Computational Physics

> A comprehensive guide for physicists working with Python, C++, and computational simulations. Optimized for macOS and Windows 11.

[![Git](https://img.shields.io/badge/Git-2.40+-orange?logo=git)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Enabled-blue?logo=github)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C++-11/14/17-00599C?logo=cplusplus)](https://isocpp.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📑 Table of Contents

- [Introduction](#-introduction)
- [Installation & Setup](#-installation--setup)
- [Basic Commands](#-basic-commands)
- [Branching & Collaboration](#-branching--collaboration)
- [Intermediate Operations](#-intermediate-operations)
- [Advanced Workflows](#-advanced-workflows)
- [Physics-Specific Practices](#-physics-specific-practices)
- [Troubleshooting](#-troubleshooting)
- [Best Practices](#-best-practices)
- [Quick Reference](#-quick-reference)
- [Resources](#-resources)

---

## 🎯 Introduction

This tutorial is designed specifically for researchers and students working in:
- **Theoretical Physics** (analytical computations, symbolic math)
- **Computational Physics** (numerical simulations, Monte Carlo methods)
- **Machine Learning for Physics** (neural networks, optimization)
- **Deep Learning Applications** (quantum systems, field theory)

### Why Git for Physics?

- ✅ Version control for code and analysis
- ✅ Reproducibility of scientific results
- ✅ Collaboration with research groups
- ✅ Track experimental parameters
- ✅ Manage multiple paper versions
- ✅ Backup and disaster recovery

---

## 🚀 Installation & Setup

### Installation

<details>
<summary><b>macOS</b></summary>

```bash
# Check if Git is already installed
git --version

# Install via Homebrew (recommended)
brew install git

# Or download from official website
# https://git-scm.com/download/mac
```
</details>

<details>
<summary><b>Windows 11</b></summary>

```bash
# Download Git for Windows with Git Bash
# https://git-scm.com/download/win

# Or install via winget
winget install --id Git.Git -e --source winget

# Verify installation
git --version
```
</details>

### Initial Configuration

```bash
# Set your identity (REQUIRED)
git config --global user.name "Your Name"
git config --global user.email "your.email@university.edu"

# Set default editor
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "nano"         # Nano
git config --global core.editor "vim"          # Vim

# Set default branch name
git config --global init.defaultBranch main

# Enable colors
git config --global color.ui auto

# View all configuration
git config --list
```

### SSH Configuration for GitHub (Recommended)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@university.edu"

# Start ssh-agent and add key
# macOS / Linux / Git Bash (Windows)
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key to clipboard
# macOS:
cat ~/.ssh/id_ed25519.pub | pbcopy

# Windows (Git Bash):
cat ~/.ssh/id_ed25519.pub | clip

# Windows (PowerShell):
Get-Content ~/.ssh/id_ed25519.pub | Set-Clipboard

# Add SSH key to GitHub:
# GitHub → Settings → SSH and GPG keys → New SSH key → Paste

# Test connection
ssh -T git@github.com
```

---

## 📦 Basic Commands

### Creating Repositories

```bash
# Initialize new local repository
mkdir monte-carlo-simulation
cd monte-carlo-simulation
git init

# Clone existing repository
git clone https://github.com/username/physics-project.git
git clone git@github.com:username/physics-project.git  # SSH

# Clone to specific folder
git clone https://github.com/username/project.git my-folder
```

### Basic Workflow

```bash
# Check repository status
git status

# Stage files
git add simulation.py                # Single file
git add src/mcmc.cpp                # File in subdirectory
git add *.py                        # All Python files
git add .                           # All changes
git add -A                          # All (new, modified, deleted)

# Commit changes
git commit -m "Implement Metropolis-Hastings algorithm"
git commit -m "feat: add 2D Ising model simulation"

# Stage and commit in one step (tracked files only)
git commit -am "Optimize energy calculation"

# View commit history
git log
git log --oneline                   # Compact view
git log --graph --oneline --all     # Visual graph
git log --author="Your Name"        # Filter by author
git log --since="2 weeks ago"       # Last 2 weeks
git log -- file.py                  # History of specific file
```

### Working with Remotes

```bash
# View configured remotes
git remote -v

# Add remote
git remote add origin https://github.com/username/project.git
git remote add origin git@github.com:username/project.git  # SSH

# Push changes
git push origin main
git push -u origin main             # First time (set upstream)
git push                            # After upstream is set

# Pull changes
git pull origin main                # Fetch + merge
git pull                            # With tracking

# Fetch without merging
git fetch origin
```

### Creating .gitignore

Essential for physics projects to avoid committing large data files and temporary outputs.

```bash
# Create .gitignore file
touch .gitignore
nano .gitignore
```

**Recommended .gitignore for Physics Projects:**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv/
*.egg-info/
dist/
build/

# Jupyter Notebooks
.ipynb_checkpoints/
*.ipynb_checkpoints

# Large data files (typical in physics)
*.hdf5
*.h5
*.dat
*.csv
data/raw/*
data/processed/*
results/
output/
plots/
figures/
*.npy
*.npz

# C/C++ compiled
*.o
*.out
*.exe
*.a
*.so
*.dylib
a.out
*.mod
*.smod

# Simulation files (usually large)
*.bin
*.trajectory
*.xyz
*.pdb
*.dcd
*.dump

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Local configurations
config_local.py
secrets.py
.env

# ML models (often large)
*.pth
*.pt
*.h5
*.pkl
*.joblib
models/*.pth
checkpoints/
*.ckpt

# LaTeX
*.aux
*.log
*.out
*.toc
*.synctex.gz
*.fls
*.fdb_latexmk

# Fortran
*.mod
*.o
*.a
```

```bash
# Add .gitignore to repository
git add .gitignore
git commit -m "Add .gitignore for physics project"
```

---

## 🌿 Branching & Collaboration

### Working with Branches

```bash
# List branches
git branch                          # Local branches
git branch -r                       # Remote branches
git branch -a                       # All branches

# Create new branch
git branch feature/tensor-networks
git branch experiment/new-model

# Switch branches
git checkout feature/tensor-networks
git switch feature/tensor-networks  # Newer command

# Create and switch in one command
git checkout -b feature/quantum-sim
git switch -c feature/quantum-sim   # Newer command

# Switch to previous branch
git checkout -
git switch -

# Rename branch
git branch -m new-name              # Rename current branch
git branch -m old-name new-name     # Rename specific branch

# Delete branch
git branch -d feature/completed     # Safe delete (if merged)
git branch -D feature/experimental  # Force delete

# Push branch to remote
git push origin feature/tensor-networks
git push -u origin feature/tensor-networks  # With tracking
```

### Merging Branches

```bash
# Merge branch into current
git checkout main
git merge feature/tensor-networks

# Merge without fast-forward (preserves branch history)
git merge --no-ff feature/tensor-networks

# View merged branches
git branch --merged
git branch --no-merged
```

### Rebasing

```bash
# Rebase current branch onto main
git checkout feature/simulation
git rebase main

# If conflicts occur
git add resolved-file.py
git rebase --continue

# Abort rebase
git rebase --abort

# Interactive rebase (combine, edit commits)
git rebase -i HEAD~3                # Last 3 commits
git rebase -i main                  # From main
```

---

## 🔧 Intermediate Operations

### Viewing Differences

```bash
# View unstaged changes
git diff

# View staged changes
git diff --staged
git diff --cached

# Differences between commits
git diff HEAD~1 HEAD                # Last vs previous
git diff abc123 def456              # Between specific commits

# Differences in specific file
git diff file.py
git diff HEAD~1 HEAD file.py

# Statistics only
git diff --stat
```

### Undoing Changes

```bash
# Discard unstaged changes in file
git checkout -- file.py
git restore file.py                 # Newer command

# Unstage file (undo git add)
git reset HEAD file.py
git restore --staged file.py        # Newer command

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert specific commit (creates new commit)
git revert abc123                   # Safer for public history

# Stash changes temporarily
git stash                           # Save changes
git stash list                      # View stashes
git stash pop                       # Apply and remove last stash
git stash apply                     # Apply without removing
git stash drop                      # Remove stash
git stash clear                     # Remove all stashes

# Stash with message
git stash save "WIP: MCMC optimization"
```

### Working with Tags

```bash
# Create lightweight tag
git tag v1.0.0

# Create annotated tag (recommended)
git tag -a v1.0.0 -m "Version 1.0: Complete Ising simulation"

# List tags
git tag
git tag -l "v1.*"                   # Filter

# View tag information
git show v1.0.0

# Push tags to remote
git push origin v1.0.0              # Specific tag
git push origin --tags              # All tags

# Delete tag
git tag -d v1.0.0                   # Local
git push origin --delete v1.0.0     # Remote

# Checkout specific tag
git checkout v1.0.0
```

---

## ⚡ Advanced Workflows

### Cherry Pick

```bash
# Apply specific commit to current branch
git cherry-pick abc123

# Cherry pick multiple commits
git cherry-pick abc123 def456

# Cherry pick without auto-commit
git cherry-pick -n abc123
```

### Rewriting History

```bash
# Change last commit message
git commit --amend -m "New message"

# Add files to last commit
git add forgotten_file.py
git commit --amend --no-edit

# Interactive rebase to rewrite history
git rebase -i HEAD~5

# Commands in editor:
# pick   = use commit
# reword = change message
# edit   = modify commit
# squash = combine with previous
# fixup  = like squash but discard message
# drop   = remove commit
```

### Searching History

```bash
# Search in code
git grep "potential_function"
git grep "Metropolis" $(git rev-list --all)  # All history

# Find who modified line
git blame file.py
git blame -L 100,150 file.py        # Specific lines

# Find commit that introduced bug (bisect)
git bisect start
git bisect bad                      # Current has bug
git bisect good v1.0.0             # This worked
# Test code at bisect point
git bisect bad                      # If has bug
git bisect good                     # If works
# Repeat until finding culprit
git bisect reset                    # End bisect
```

### Submodules

```bash
# Add submodule
git submodule add https://github.com/org/physics-lib.git lib/physics

# Clone with submodules
git clone --recursive https://github.com/user/project.git

# Or if already cloned
git submodule init
git submodule update

# Update submodules
git submodule update --remote
```

### Worktrees

```bash
# Work on multiple branches simultaneously
git worktree add ../project-feature feature/new

# List worktrees
git worktree list

# Remove worktree
git worktree remove ../project-feature
```

---

## 🔬 Physics-Specific Practices

### Recommended Project Structure

```
physics-project/
├── .git/
├── .gitignore
├── .gitattributes          # For Git LFS
├── README.md
├── LICENSE
├── requirements.txt        # Python dependencies
├── environment.yml         # Conda environment
├── CMakeLists.txt         # C++ build
├── Makefile               # Build automation
├── src/
│   ├── __init__.py
│   ├── simulation.py
│   ├── analysis.cpp
│   ├── models.py
│   └── utils/
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_analysis.ipynb
│   └── 03_visualization.ipynb
├── tests/
│   ├── test_simulation.py
│   ├── test_physics.cpp
│   └── test_conservation_laws.py
├── scripts/
│   ├── run_simulation.sh
│   ├── process_data.py
│   └── submit_cluster.sh
├── docs/
│   ├── theory.md
│   ├── api.md
│   └── methods.md
├── data/                   # Add to .gitignore
│   ├── .gitkeep
│   └── README.md          # Document data structure
├── results/                # Add to .gitignore
│   ├── .gitkeep
│   └── README.md
└── figures/
    └── .gitkeep
```

### Semantic Commits for Physics

Use clear, descriptive commit messages:

```bash
# Format: type(scope): description

# Common types:
git commit -m "feat: implement Monte Carlo algorithm"
git commit -m "fix: correct energy calculation in Hamiltonian"
git commit -m "perf: optimize main simulation loop"
git commit -m "docs: add perturbation theory documentation"
git commit -m "test: add energy conservation tests"
git commit -m "refactor: reorganize field class structure"
git commit -m "style: format code per PEP8"
git commit -m "data: add reference dataset"
git commit -m "exp: experiment with new lattice parameters"
```

### Managing Large Files (Git LFS)

```bash
# Install Git LFS
# macOS:
brew install git-lfs

# Windows: included in Git for Windows
# Or download from https://git-lfs.github.com

# Initialize in repository
git lfs install

# Track large file types
git lfs track "*.hdf5"
git lfs track "*.h5"
git lfs track "*.pth"
git lfs track "*.npy"
git lfs track "data/raw/*"

# This creates/updates .gitattributes
git add .gitattributes
git commit -m "Configure Git LFS"

# Use normally
git add large_simulation.hdf5
git commit -m "data: add simulation results"
git push

# View LFS tracked files
git lfs ls-files

# View what will be tracked
git lfs track
```

### Branching Strategy for Experiments

```bash
# Branch structure for physics research
main                                # Stable code
├── develop                        # Integration branch
├── feature/neural-network        # New features
├── exp/params-optimization       # Experiments
├── exp/mcmc-comparison          # Method comparison
└── paper/prl-submission         # Paper-specific code

# Create experiment branch
git checkout -b exp/temperature-sweep
# ... run experiments ...
git add results.ipynb
git commit -m "exp: complete temperature sweep"
git push -u origin exp/temperature-sweep

# If experiment successful, merge to develop
git checkout develop
git merge --no-ff exp/temperature-sweep

# If unsuccessful, keep branch for reference or delete
```

### Working with Jupyter Notebooks

```bash
# Problem: Notebooks cause merge conflicts
# Solution: nbdime

# Install nbdime
pip install nbdime

# Configure for git
nbdime config-git --enable --global

# Clear outputs before commit (recommended)
jupyter nbconvert --clear-output --inplace notebook.ipynb
git add notebook.ipynb
git commit -m "docs: add results analysis"

# Or automate with nbstripout
pip install nbstripout
nbstripout --install
```

### Commit Message Template

```bash
# Create commit template
cat > ~/.gitmessage << 'EOF'
# Type(scope): short description (max 50 chars)
#
# Detailed explanation of change
#
# Physical/Mathematical motivation:
#
# Results/Impact:
#
# References:
# - Paper: 
# - Issue: #
EOF

# Set template
git config --global commit.template ~/.gitmessage
```

---

## 🔍 Troubleshooting

### Merge Conflicts

```bash
# When merge conflict occurs
# Git marks conflicts in files:
# <<<<<<< HEAD
# Your code
# =======
# Other branch code
# >>>>>>> feature/new

# 1. View conflicted files
git status

# 2. Open and resolve manually
# Or use merge tool
git mergetool

# 3. Mark as resolved
git add resolved_file.py

# 4. Complete merge
git commit -m "Resolve conflicts in simulation"

# Abort merge if needed
git merge --abort
```

### Recovering Lost Work

```bash
# View reference history (includes "lost" commits)
git reflog

# Recover commit
git checkout abc123
git cherry-pick abc123
git reset --hard abc123

# Recover deleted file
git checkout HEAD~1 -- deleted_file.py

# Recover deleted branch
git reflog
git checkout -b recovered-branch abc123
```

### Cleaning Repository

```bash
# Clean untracked files
git clean -n                        # Dry run (see what will be deleted)
git clean -f                        # Delete files
git clean -fd                       # Delete files and directories
git clean -fX                       # Only ignored files
git clean -fx                       # Everything including ignored

# Optimize repository
git gc                              # Garbage collection
git gc --aggressive                 # Aggressive optimization
```

### Changing Remote URL

```bash
# View current remote
git remote -v

# Change URL (e.g., HTTPS to SSH)
git remote set-url origin git@github.com:user/project.git

# Verify
git remote -v
```

### Syncing Fork

```bash
# Add upstream remote
git remote add upstream https://github.com/original/repo.git

# Update fork
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

---

## ✅ Best Practices

### Effective Commits

**✅ DO:**
- Make small, atomic commits
- Write descriptive messages
- Commit frequently
- One logical change per commit

```bash
# Good examples
git commit -m "Implement Verlet integration method"
git commit -m "Fix periodic boundary conditions"
git commit -m "Optimize intermolecular force calculation"
```

**❌ AVOID:**
- Massive commits with many changes
- Vague messages: "fix", "update", "changes"
- Leaving code uncommitted for days
- Mixing different features in one commit

### Daily Workflow

```bash
# 1. Start of day
git pull origin main

# 2. Create branch for task
git checkout -b feature/new-algorithm

# 3. Work and commit frequently
git add file.py
git commit -m "feat: add basic structure"
# ... more work ...
git commit -m "feat: implement main logic"

# 4. Update with team changes
git checkout main
git pull
git checkout feature/new-algorithm
git rebase main

# 5. Push to remote
git push -u origin feature/new-algorithm

# 6. Create Pull Request on GitHub

# 7. After merge, cleanup
git checkout main
git pull
git branch -d feature/new-algorithm
```

### Security Best Practices

```bash
# NEVER commit:
# - Passwords or tokens
# - API keys
# - Personal sensitive data
# - Confidential results before publication

# If you accidentally commit secrets:
# 1. Change credentials immediately
# 2. Remove from history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/secret_file.py" \
  --prune-empty --tag-name-filter cat -- --all

# Or use BFG Repo Cleaner (faster)
# https://rtyley.github.io/bfg-repo-cleaner/
```

### Useful Aliases

```bash
# Add to ~/.gitconfig or configure with:

# Pretty log
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Short status
git config --global alias.st "status -s"

# Recent commits
git config --global alias.last "log -1 HEAD"

# Branches with last commit
git config --global alias.branches "branch -vv"

# Undo last commit
git config --global alias.undo "reset HEAD~1 --mixed"

# List files in last commit
git config --global alias.changed "show --name-only"

# Use aliases
git lg
git st
git last
```

### Pre-commit Hook Example

```bash
# Create hook: .git/hooks/pre-commit
#!/bin/bash

# Run tests
python -m pytest tests/ || {
    echo "❌ Tests failed. Commit aborted."
    exit 1
}

# Check Python formatting
black --check src/ || {
    echo "❌ Python code not formatted. Run: black src/"
    exit 1
}

# Check for debug statements
if git diff --cached | grep -i "print.*debug\|TODO\|FIXME"; then
    echo "⚠️  Warning: Debug comments found"
    read -p "Continue with commit? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "✅ Pre-commit checks passed"
```

```bash
# Make executable
chmod +x .git/hooks/pre-commit
```

---

## 📋 Quick Reference

### Essential Commands

```bash
# SETUP
git init                            # Initialize repo
git clone <url>                     # Clone repo

# BASIC
git status                          # View status
git add .                           # Stage changes
git commit -m "message"             # Save changes
git push                            # Upload to remote
git pull                            # Download from remote

# BRANCHES
git branch                          # List branches
git checkout -b new-branch          # Create and switch
git merge branch                    # Merge branch
git branch -d branch                # Delete branch

# UNDO
git restore file                    # Discard changes
git restore --staged file           # Unstage file
git reset --soft HEAD~1             # Undo commit
git stash                           # Save temporarily

# INFO
git log --oneline                   # View history
git diff                            # View differences
git show commit-id                  # View specific commit

# ADVANCED
git rebase main                     # Rebase onto main
git cherry-pick <commit>            # Apply commit
git reflog                          # Complete history
```

### Git Flow for Physics Research

```
┌─────────────────────────────────────────┐
│  main (stable, published code)          │
└──────────┬──────────────────────────────┘
           │
           │ merge after validation
           │
┌──────────▼──────────────────────────────┐
│  develop (integration)                   │
└──┬───────┬───────────────────────────────┘
   │       │
   │       │ merge after review
   │       │
   │  ┌────▼────────────────────────────┐
   │  │ feature/* (new algorithms)      │
   │  └─────────────────────────────────┘
   │
   │ merge or archive
   │
┌──▼──────────────────────────────────────┐
│  exp/* (experiments, keep or discard)    │
└──────────────────────────────────────────┘
```

---

## 📚 Resources

### Documentation
- [Git Official Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com)
- [Pro Git Book (Free)](https://git-scm.com/book/en/v2)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

### Tools for Physics
- [Git LFS](https://git-lfs.github.com) - Large file storage
- [nbdime](https://nbdime.readthedocs.io) - Jupyter notebook diff/merge
- [DVC](https://dvc.org) - Data version control
- [Weights & Biases](https://wandb.ai) - ML experiment tracking

### GitHub Features
- [GitHub Actions](https://github.com/features/actions) - CI/CD
- [GitHub Pages](https://pages.github.com) - Documentation hosting
- [GitHub Codespaces](https://github.com/features/codespaces) - Cloud IDE

### Best Practices
- [Conventional Commits](https://www.conventionalcommits.org)
- [Semantic Versioning](https://semver.org)
- [Keep a Changelog](https://keepachangelog.com)

---

## 💡 Tips for Physicists

1. **Commit frequently** - Especially before risky experiments
2. **Document parameters** - Include important parameters in commit messages
3. **Use tags for versions** - Tag versions used in papers
4. **Clean notebooks** - Clear outputs before committing
5. **Use LFS for large files** - Don't fill repo with binary files
6. **Paper branches** - Create specific branch for each publication
7. **Physics tests** - Verify energy conservation, symmetries, etc.
8. **Backup strategy** - GitHub doesn't replace data backups
9. **Reproducibility** - Include environment files (requirements.txt, environment.yml)
10. **Documentation** - Document theory, methods, and algorithms

---

## 🤝 Contributing

If you find errors or want to add examples relevant to physics computing, feel free to open an issue or pull request.

---

## 📄 License

This tutorial is released under the MIT License. Feel free to use, modify, and distribute.

---

## 📬 Contact

Questions or suggestions? Open an issue or reach out!

---

**Happy Computing! 🚀🔬**

*Version 1.0 - October 2025*
