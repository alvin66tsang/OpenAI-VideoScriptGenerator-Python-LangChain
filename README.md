# OPENAI Video Script Generator

**AI-powered Python tool using LangChain, OpenAI, and Streamlit to generate video scripts from Wikipedia based on a user-provided title.**

## Features
- Generates well-structured video scripts from any topic using OpenAI.
- Fetches relevant content from Wikipedia to ensure informative scripts.
- Simple and interactive interface using Streamlit.
- Powered by LangChain for modular and flexible prompt handling.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/alvin66tsang/OpenAI-VideoScriptGenerator-Python-LangChain.git
   cd ./video-script-generator

2.  Install dependencies: pip install -r ./requirement.txt

## Usage

1.  Run the Streamlit app: streamlit run main.py
2.  Open your browser and go to: http://localhost:8501
3.  In the sidebar:
    Enter your OpenAI API key.
    Enter the title for the video script.
4.  Click the Generate Script button and wait for the script to appear.

## Requirements
Python 3.11+
OpenAI account and API key
Streamlit
LangChain
Wikipedia library (if using wikipedia API)