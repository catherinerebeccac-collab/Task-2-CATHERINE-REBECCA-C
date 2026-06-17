# Chain-of-Thought (CoT) Logic Engine using Ollama

## Project Overview
This project demonstrates the implementation of a **Chain-of-Thought (CoT) Logic Engine** using **Prompt Engineering** with a locally hosted **Llama 3** model through **Ollama**. The objective is to guide a Large Language Model (LLM) to solve complex logical reasoning problems by enforcing structured reasoning, verification, and self-correction before producing the final answer.

Unlike traditional prompting, this project focuses on reducing hallucinations and improving reasoning accuracy through carefully designed prompts.
---
# Objectives

- Implement Chain-of-Thought Prompting.
- Force the model to reason step-by-step.
- Reduce hallucinations through structured prompts.
- Implement a self-correction mechanism.
- Evaluate the model using logical reasoning problems and riddles.
- Execute the entire project locally using Ollama without requiring cloud-based APIs.
---
# Features

- Step-by-step reasoning generation
- Problem understanding phase
- Verification of reasoning
- Self-correction phase
- Final answer generation
- Local execution using Ollama
- Automatic output generation
- Multiple logic test cases
---
# Technologies Used

- Python 3.11+
- Ollama
- Llama 3
- Requests Library
- VS Code
---
# Project Structure
```
CoT_Logic_Engine/
│
├── main.py
├── prompt_template.py
├── ollama_client.py
├── test_cases.py
├── utils.py
├── requirements.txt
├── README.md
│
├── outputs/
│     ├── output_1.txt
│     ├── output_2.txt
│     └── ...output_7.txt
```
# System Requirements

- Windows, Linux, or macOS
- Python 3.11 or above
- Ollama installed
- Internet connection (only required for downloading the model)
- VS Code (Recommended)
---
# Installation Guide

## Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```
## Step 2: Install Ollama

Download Ollama from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```
## Step 3: Download the Llama 3 Model

Open the terminal and execute:

```bash
ollama pull llama3
```

Wait until the model is completely downloaded.

---
## Step 4: Start Ollama Server

```bash
ollama serve
```

The server starts at:

```
http://localhost:11434
```

Keep this terminal running.

---
## Step 5: Clone or Create the Project Folder

```bash
mkdir CoT_Logic_Engine
cd CoT_Logic_Engine
```
## Step 6: Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```
## Step 7: Install Dependencies

```bash
pip install -r requirements.txt
```
# Running the Project

Execute:

```bash
python main.py
```

The application will:

- Load all logic test cases
- Generate structured reasoning
- Perform verification
- Perform self-correction
- Display the final answer
- Save every output inside the outputs folder

---
# Prompt Engineering Workflow

The prompt is designed in five structured phases.

## Phase 1 — Problem Understanding

The model first identifies what the question is asking.

## Phase 2 — Step-by-Step Reasoning

The model decomposes the problem into logical reasoning steps.

## Phase 3 — Verification

Every reasoning step is checked for consistency.

## Phase 4 — Self-Correction

The model reviews its reasoning and corrects mistakes if necessary.

## Phase 5 — Final Answer

The corrected final answer is presented.

# Test Cases
Example logic problems include:

- Farmer and Sheep Problem
- Bat and Ball Problem
- Minute and Moment Puzzle
- Three Switches Puzzle
- Polar Bear Puzzle
- Machine Production Puzzle
- Logical Reasoning Questions

# Sample Output

```
================================================================================

TEST CASE 1

QUESTION

A farmer has 17 sheep.
All but 9 die.

PROBLEM UNDERSTANDING

The statement means every sheep except nine dies.

STEP-BY-STEP REASONING

Initial sheep = 17

All except 9 die.

Remaining sheep = 9

VERIFICATION

The statement is interpreted correctly.

SELF-CORRECTION

No contradiction found.

FINAL ANSWER

9 sheep remain.
```
# Files Description

## main.py

Controls the complete execution flow of the project.

## prompt_template.py

Contains the Chain-of-Thought prompt template used for reasoning.

## ollama_client.py

Connects Python with the local Ollama API.

## test_cases.py

Contains all logical reasoning questions.

## utils.py

Provides helper functions for creating folders and saving outputs.

## outputs/

Stores all generated reasoning results.

# Commands Used

Start Ollama

```bash
ollama serve
```

Download Model

```bash
ollama pull llama3
```

View Installed Models

```bash
ollama list
```

Run Model Interactively

```bash
ollama run llama3
```

Execute Project

```bash
python main.py
```

---
# Expected Learning Outcomes

After completing this project, the following concepts are understood:

- Prompt Engineering
- Chain-of-Thought Prompting
- Hallucination Reduction
- Logical Reasoning
- Self-Correction Prompting
- Local LLM Deployment
- Ollama API Integration
- Python API Communication

# Future Improvements

- Add graphical user interface (GUI)
- Support multiple Ollama models
- Add PDF report generation
- Include benchmarking metrics
- Integrate with Streamlit or Gradio
- Add evaluation scores for reasoning quality

---
# Author

**Name:** CATHERINE REBECCA C

**Project:** Chain-of-Thought (CoT) Logic Engine

**Technology:** Python + Ollama + Llama 3

**Institution:** DecodeLabs Industrial Training Kit – Prompt Engineering Project 2

---
