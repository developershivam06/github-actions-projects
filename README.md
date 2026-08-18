# GitHub Actions Project 1 — Python Test & Reporting CI

## 📌 Overview

This project is my first hands-on GitHub Actions project.

The goal is to build a CI workflow that automatically:

- Runs Python tests using `pytest`
- Generates JUnit XML test results
- Generates an HTML test report
- Uploads test reports as GitHub Actions artifacts
- Parses test results dynamically
- Displays test results in the GitHub Actions Summary
- Passes data between steps using `GITHUB_OUTPUT`
- Passes environment variables between steps using `GITHUB_ENV`
- Passes data between jobs using Job Outputs
- Uses conditional execution with `if:`
- Handles failed tests using `always()`
- Creates dependencies between jobs using `needs:`

This project is intentionally simple so that the focus remains on understanding
GitHub Actions concepts rather than application complexity.

---

# 🏗️ Project Structure

```text
github-actions-projects/
│
├── .github/
│   └── workflows/
│       └── tests.yaml
│
├── src/
│   ├── __init__.py
│   └── calculator.py
│
├── tests/
│   └── test_calculator.py
│
├── scripts/
│   └── parse_results.py
│
├── reports/
│
├── requirements.txt
│
└── README.md

# WORKFLOW
                        GitHub
                          │
                    Push / Pull Request
                          │
                          ▼
                  ┌───────────────┐
                  │   TEST JOB    │
                  └───────┬───────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
         Checkout     Python Setup   Dependencies
             │
             ▼
          pytest
             │
       ┌─────┴─────┐
       ▼           ▼
      HTML         JUnit XML
       │              │
       ▼              ▼
    Artifact     parse_results.py
                      │
              ┌───────┴────────┐
              ▼                ▼
       Step Outputs      Step Summary
              │
              ▼
         Job Outputs
              │
              ▼
       ┌───────────────┐
       │  REPORT JOB   │
       └───────┬───────┘
               │
               ▼
         Final Report

```

