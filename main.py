from crewai import Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

import agents
import tasks


def main(topic):
    search_tool = DuckDuckGoSearchRun()

    tools = [search_tool]
    # setup agents
    researcher = agents.create_senior_researcher(topic, tools)
    writer = agents.create_writer(topic, tools)

    # setup tasks
    research_task = tasks.create_research_task(topic, tools, researcher)
    write_task = tasks.create_write_task(topic, tools, writer)

    # Forming the tech-focused crew with enhanced configurations
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,  # Optional: Sequential task execution is default
    )
    return crew.kickoff()


if __name__ == "__main__":
    topic = "AI in healthcare"

    result = main(topic)
    print(result)
