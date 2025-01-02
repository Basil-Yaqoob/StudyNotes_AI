# StudyNotes_AI

**StudyNotes_AI** is a Python-based project that automates the creation of concise and well-structured notes from YouTube videos. This project is built using a variety of tools and frameworks, including OpenAI's GPT models and other utilities, to streamline the process of extracting and summarizing educational content.

---

## Features
- Extracts transcripts from YouTube videos.
- Summarizes content into structured, concise notes suitable for students.
- Handles various topics and formats for better adaptability.
- Built-in support for customizable note formats and detailed analysis.

---

## Prerequisites
Before setting up the project, ensure you have the following:
- Python (>= 3.8)
- Conda (for managing virtual environments)
- Git (for version control)

---

## Setup Guide

### 1. Clone the Repository
```bash
# Clone your GitHub repository to your local machine
git clone https://github.com/your-username/StudyNotes_AI.git
cd StudyNotes_AI
```

### 2. Create a Conda Virtual Environment
```bash
# Create a new Conda environment
conda create --name studynotes_ai python=3.8 -y

# Activate the environment
conda activate studynotes_ai
```

### 3. Install Dependencies
```bash
# Install all required Python libraries
pip install -r requirements.txt
```

### 4. Set Up the `.env` File
Create a `.env` file in the root directory of the project and add your OpenAI API key:
```plaintext
OPENAI_API_KEY=your_openai_api_key
```

Make sure to replace `your_openai_api_key` with your actual OpenAI API key.

### 5. Run the Project
```bash
# Run the main script to start the application
python main.py
```

---

## Project Overview

### Purpose
The purpose of StudyNotes_AI is to simplify the process of creating educational notes from video content. It aims to assist students by summarizing video lectures into digestible and easy-to-understand formats.

### Workflow
1. Input a YouTube video URL.
2. Extract the transcript from the video.
3. Summarize the content into concise points.
4. Format the output into structured notes for study or exam preparation.

### Technologies Used
- **Python**: Core language for development.
- **LangChain**: For managing the processing pipeline.
- **OpenAI GPT API**: For summarization and natural language processing.
- **YouTube Transcript API**: To fetch transcripts from YouTube videos.

---

## Contribution
Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## Troubleshooting
- If you encounter issues with missing dependencies, ensure all packages from `requirements.txt` are installed.
- Verify the `.env` file contains a valid OpenAI API key.
- Ensure the Conda environment is activated when running the project.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contact
For questions or feedback, please reach out to [your email or GitHub profile].

