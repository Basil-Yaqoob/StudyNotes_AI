from crewai import Crew, Process
from agents import video_researcher, content_manager, note_writer
from tasks import video_research_task, content_manager_task, note_writer_task

# Set up the Crew with Agents and Tasks
crew = Crew(
    agents=[video_researcher, content_manager, note_writer],
    tasks=[video_research_task, content_manager_task, note_writer_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Kick off the workflow with the given topic
result = crew.kickoff(inputs={'topic': 'Super Key,Candidate Key, Primary Key in DBMS'})

# Output the result
print(result)
