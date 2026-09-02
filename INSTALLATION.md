# Installation Guide

## Requirements

- Python 3.x
- Git
- Virtual environment

## Setup

Create a virtual environment:

python -m venv venv

Activate it:

.\venv\Scripts\activate

Install dependencies:

pip install -r requirement.txt

## Run

Start the application:

uvicorn App.main:app --reload

The dashboard will be available at:

http://127.0.0.1:8000
