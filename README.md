# SaiKet Python Development Internship

A hands-on collection of beginner-friendly Python exercises and mini-projects completed in Jupyter Notebook format. This repository highlights core Python concepts such as user input, file handling, web scraping, API integration, and basic data analysis.

The project is designed for learning and practice, with each notebook focused on a specific task and real-world programming concept.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Repository Structure](#repository-structure)
- [Installation Guide](#installation-guide)
- [Usage Examples](#usage-examples)
- [Technologies Used](#technologies-used)
- [License](#license)

## Project Overview

This repository contains a set of small Python applications and utilities built during a Python development internship. The notebooks demonstrate how to:

- build interactive command-line programs,
- manipulate files and text content,
- collect and store data from the web,
- integrate with live external APIs,
- analyze text using Python utilities.

Each task is intentionally simple, easy to follow, and suitable for learners who are getting started with Python.

## Key Features

- Number guessing game with interactive feedback
- Word replacement utility for editing text files
- Basic web scraper for collecting article headlines
- Real-time currency conversion through an API
- Word frequency analysis using Counter and pandas
- Beginner-friendly Jupyter notebooks for step-by-step exploration

## Repository Structure

```text
SaiKet-PythonDev-Intern/
├── Task2_NumberGuessGame.ipynb       # Number guessing game
├── Task3_BasicFileHandling.ipynb     # File content replacement utility
├── Task4_BasicWebScraper.ipynb       # News scraper using BeautifulSoup
├── Task5_CurrencyConverter.ipynb     # Live currency converter
├── Task6_WordCountTool.ipynb         # Word frequency counter
├── docs.txt                          # Project notes / task description
├── Editted_file.txt                  # Output file created by basic file handling task
├── README.md                         # Project documentation
└── .gitignore                        # Optional Git ignore rules (if present in your environment)
```

## Installation Guide

Follow the steps below to set up the project locally.

### 1. Prerequisites

Make sure you have the following installed:

- Python 3.9+
- pip (Python package manager)
- Jupyter Notebook or Jupyter Lab

### 2. Clone the Repository

```bash
git clone https://github.com/MoshoodSO/SaiKet-PythonDev-Intern.git
cd SaiKet-PythonDev-Intern
```

### 3. Create a Virtual Environment

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install notebook pandas requests beautifulsoup4
```

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open any of the tasks in the repository and run the notebook cells.

## Usage Examples

Below are a few example snippets inspired by the implemented tasks in this repository.

### 1. Number Guessing Game

```python
import random


def number_guessing_game():
    num = random.randint(1, 100)
    guess = int(input("Enter your guess: "))

    while guess != num:
        if guess < num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        guess = int(input("Enter another guess: "))

    print("Correct guess!!")


number_guessing_game()
```

### 2. Replace a Word in a File

```python
def Replace_word(file, word, replacement):
    with open(file, 'r') as f:
        content = f.read()

    updated_content = content.replace(word, replacement)

    with open("Editted_file.txt", 'w') as file:
        file.write(updated_content)

    return "Successful! File updated in 'Editted_file.txt'"


print(Replace_word("docs.txt", "number", "mine"))
```

### 3. Basic Web Scraper

```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.select(".titleline > a")

    for headline in headlines:
        print(headline.get_text(strip=True))
```

### 4. Currency Converter

```python
import requests


def convert_currency(amount, from_currency, to_currency):
    url = "https://api.frankfurter.app/latest"
    params = {
        "amount": amount,
        "from": from_currency,
        "to": to_currency,
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()
    return data["rates"][to_currency]


print(convert_currency(100, "USD", "EUR"))
```

### 5. Word Count Tool

```python
from collections import Counter
import pandas as pd


def WordCounter(file, top_n=5):
    with open(file, 'r') as f:
        content = f.read()

    words = content.split()
    return pd.DataFrame(Counter(words).most_common(top_n), columns=["words", "counts"])


print(WordCounter("docs.txt"))
```

## Technologies Used

This project uses the following tools and technologies:

- Python 3
- Jupyter Notebook
- pandas
- requests
- BeautifulSoup4
- CSV handling
- Counter from collections
- GitHub for version control and repository hosting
- Frankfurter API for live exchange-rate conversion

## License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026 MoshoodSO

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Conclusion

This repository demonstrates a practical beginner-level Python learning path, combining theory and application through short, functional projects. It is a solid foundation for improving Python skills in automation, file operations, API usage, and data processing.

If you are learning Python, these notebooks are an excellent starting point for building confidence with real coding tasks.
