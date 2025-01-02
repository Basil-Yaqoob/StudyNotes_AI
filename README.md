# StudyNotes_AI

StudyNotes_AI is an innovative project designed to automate the process of generating concise and relevant study notes from YouTube videos. By leveraging advanced natural language processing and AI models, this application simplifies learning for students and professionals by extracting key concepts and summarizing information effectively.

## Features

- Extracts meaningful information from YouTube videos.
- Generates concise, well-structured study notes.
- Uses OpenAI API for advanced language processing.
- Built with Python and integrates CrewAI for efficient content generation.
- Supports a modular architecture for future expansions.

---

## Setup Instructions

### Prerequisites

1. Ensure you have Python (>=3.8) installed on your system.
2. Install Conda to create a virtual environment for the project.
3. Clone this repository to your local machine.

### Setting up the Environment

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/StudyNotes_AI.git
   cd StudyNotes_AI
   ```

2. **Create a Conda Virtual Environment**
   ```bash
   conda create --name studynotes_ai python=3.8 -y
   conda activate studynotes_ai
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Additional Configuration for CrewAI**
   - CrewAI is integrated into the project for enhancing content generation.
   - Follow CrewAI's [documentation](https://crewai.com/docs) to configure your API key or access token if required.

### Running the Project

1. Run the main application script:
   ```bash
   python main.py
   ```

2. Follow the on-screen prompts to input your desired YouTube video link and get your study notes.

---

## Project Overview

StudyNotes_AI automates the process of note creation from educational content available on YouTube. The project uses:

- **YouTube Video Analysis:** Extracts relevant sections from videos using semantic search.
- **Natural Language Processing:** Summarizes video content effectively using OpenAI's GPT models.
- **CrewAI Integration:** Enhances note generation with cutting-edge AI-assisted tools.

---

## Contribution Guidelines

We welcome contributions! To get started:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to:

- **OpenAI** for their powerful language models.
- **CrewAI** for their advanced content generation tools.
- All contributors who help improve this project!

