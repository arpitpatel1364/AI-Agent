# 🤝 Contributing Guide

Thank you for your interest in contributing! We welcome contributions of all kinds — code, documentation, bug reports, ideas, and more.

Please take a moment to read this guide before getting started.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Submitting Code](#submitting-code)
  - [Improving Documentation](#improving-documentation)
- [Development Setup](#development-setup)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Commit Message Convention](#commit-message-convention)
- [Code Style](#code-style)
- [Getting Help](#getting-help)

---

## 🧭 Code of Conduct

By participating in this project, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful, inclusive, and constructive in all interactions.

---

## 🚀 Getting Started

1. **Fork** the repository by clicking the "Fork" button on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/arpitpatel1364/AI-Agent.git
   cd AI-Agent
   ```
3. **Add the upstream remote** to keep your fork in sync:
   ```bash
   git remote add upstream https://github.com/arpitpatel1364/AI-Agent.git
   ```
4. **Install dependencies** (see [Development Setup](#development-setup)).

---

## 🛠 How to Contribute

### 🐛 Reporting Bugs

Found a bug? Please [open an issue](https://github.com/original-owner/project-name/issues/new?template=bug_report.md) and include:

- A clear and descriptive title
- Steps to reproduce the problem
- Expected vs. actual behavior
- Screenshots or logs if applicable
- Your environment (OS, version, browser, etc.)

> ⚠️ Please search existing issues before opening a new one to avoid duplicates.

---

### 💡 Suggesting Features

Have an idea? We'd love to hear it! [Open a feature request](https://github.com/original-owner/project-name/issues/new?template=feature_request.md) and include:

- A clear description of the feature
- Why it would be useful
- Any alternatives you've considered

---

### 💻 Submitting Code

1. **Check existing issues** — look for open issues labeled `good first issue` or `help wanted`.
2. **Comment on the issue** to let others know you're working on it.
3. **Create a branch** from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```
4. **Make your changes** and write/update tests as needed.
5. **Run tests** to make sure everything passes:
   ```bash
   # Replace with your test command
   npm test
   ```
6. **Commit your changes** following the [commit convention](#commit-message-convention).
7. **Push** to your fork:
   ```bash
   git push origin feat/your-feature-name
   ```
8. **Open a Pull Request** against the `main` branch.

---

### 📝 Improving Documentation

Documentation improvements are always welcome! This includes:

- Fixing typos or grammar
- Clarifying unclear sections
- Adding examples or usage notes
- Translating docs

---

## ⚙️ Development Setup

```bash
# 1. Install dependencies
npm install

# 2. Copy environment variables
cp .env.example .env

# 3. Start the development server
(For linux users)
python3 main.py
(For Windows users)
python main.py
```

> Replace the above with the actual setup steps for your project.

---

## 📬 Pull Request Guidelines

- Keep PRs **focused** — one feature or fix per PR.
- **Link the related issue** in the PR description (e.g., `Closes #42`).
- Include a clear description of **what** you changed and **why**.
- Make sure all **tests pass** and add new ones if needed.
- Keep your branch **up to date** with `main` before submitting:
  ```bash
  git fetch upstream
  git rebase upstream/main
  ```
- Be responsive to **review feedback** — maintainers may request changes.

---
<type>(<scope>): <short summary>
```

| Type | When to use |
|------|-------------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only changes |
| `style` | Formatting, missing semicolons, etc. |
| `refactor` | Code change that's not a fix or feature |
| `test` | Adding or updating tests |
| `chore` | Build process, dependency updates, etc. |

## 💬 Getting Help
- 📧 Email the maintainer: `arpitbhojani.contact@gmail.com`

---

We appreciate every contribution, no matter how small. Thank you for helping make this project better! 🎉
