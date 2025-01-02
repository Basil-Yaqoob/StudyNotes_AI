from crewai import Agent
from tools import tool1,tool2 
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

# Define LLM
from langchain_community.chat_models import ChatOpenAI
llm = ChatOpenAI(
    model="gpt-4-0125-preview",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Video Researcher Agent
video_researcher = Agent(
    role='Video Researcher from Youtube Videos',
    goal='Find Relevant and Most Viewed videos about topic {topic} from youtube videos.',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos for university semester exam preparation and making good notes for students, especially from Indian channels."
    ),
    tools=[tool1,tool2],
    llm=llm,
    allow_delegation=True
)

# Content Manager Agent
content_manager = Agent(
    role='Extract Relevant Content for note preparation from relevant videos',
    goal='From the relevant videos regarding topic {topic}, search for core and key concepts about that topic and decide the notes content.',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in analyzing all relevant videos and extracting key core concepts, finalizing the content for notes preparation for student learning at the university semester level."
    ),
    tools=[tool1,tool2],
    llm=llm,
    allow_delegation=True
)

# Note Writer Agent
note_writer = Agent(
    role='Make Notes from relevant videos on the basis of content provided by content manager',
    goal='From the relevant videos regarding topic {topic} and on the provided content by content manager, write concise and complete notes for university semester exams preparation.',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in analyzing all relevant videos and extracting key core concepts, writing the notes for student learning at the university semester level."
    ),
    tools=[tool1,tool2],
    llm=llm,
    allow_delegation=True
)
