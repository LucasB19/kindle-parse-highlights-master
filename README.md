# Kindle Highlights Manager

This Python script organizes and saves highlights from e-books (like Kindle) into separate Markdown files per book, making it easier to review and share your favorite passages.

## Features

- **Automated Extraction**: Organizes highlights by book title.
- **Markdown Output**: Saves highlights in easy-to-read Markdown files.
- **Flexible Selection**: Choose to process individual books or all at once.

## Prerequisites

Before you begin, ensure you have Python 3.x installed on your system. You can verify this by running `python --version` or `python3 --version` in your terminal or command prompt.

## Getting Started

### 1. Installation

First, clone the repository to your local machine:

```bash
git clone https://github.com/your_username/your_project.git
```

Navigate into the project directory:
```bash
cd your_project
```


### 2. Prepare Your Highlights File
Place your clippings.txt file, which contains the highlights you wish to organize, in the root directory of the project. The format should resemble the following:

Book Title by Author Name
- Your Highlight on page X | Location Y-Z | Added on Date

Highlight text here.

==========

### 3. Run the Script
```bash
python kindle.py
```
