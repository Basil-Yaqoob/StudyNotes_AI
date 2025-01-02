from crewai import Task
from tools import tool1,tool2 
from agents import video_researcher, content_manager, note_writer

# Task for Video Researcher Agent
video_research_task = Task(
    description=(
        "Find and analyze YouTube videos related to the topic: {topic}. "
        "Search for the most relevant videos based on the topic, including the most viewed videos, from various YouTube channels."
    ),
    expected_output=(
        "A list of relevant YouTube videos including key timestamps and video summaries based on the provided topic."
    ),
    tools=[tool1,tool2],
    agent=video_researcher
)

# Task for Content Manager Agent
content_manager_task = Task(
    description=(
        "Analyze the relevant videos for the topic: {topic} and extract the key concepts and core information from these videos. "
        "The goal is to identify the key points for preparing exam notes."
    ),
    expected_output=(
        "A structured summary of key concepts and points derived from the relevant videos for the topic {topic}, which will be used for note preparation."
    ),
    tools=[tool1,tool2],
    agent=content_manager
)

# Task for Note Writer Agent
note_writer_task = Task(
    description=(
        "Using the content provided by the Content Manager for topic {topic}, generate concise and complete notes for students. "
        "The notes should be structured and formatted for easy understanding and exam preparation."
    ),
    expected_output=(
        "A well-organized set of notes that summarize the core concepts from the relevant videos for the topic {topic}, including examples, summaries, and key takeaways."
    ),
    tools=[tool1,tool2],
    agent=note_writer,
    async_execution=False,
    output_file='Exam_Notes(1).md'
)