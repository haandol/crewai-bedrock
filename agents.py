from crewai import Agent


# Creating a senior researcher agent with memory and verbose mode
def create_senior_researcher(topic, tools):
    return Agent(
        role="Senior Researcher",
        goal=f"Uncover groundbreaking technologies in {topic}",
        verbose=True,
        memory=True,
        backstory="""Driven by curiosity, you're at the forefront of
    innovation, eager to explore and share knowledge that could change
    the world.""",
        tools=tools,
        allow_delegation=True,
    )


# Creating a writer agent with custom tools and delegation capability
def create_writer(topic, tools):
    return Agent(
        role="Writer",
        goal=f"Narrate compelling tech stories about {topic}",
        verbose=True,
        memory=True,
        backstory="""With a flair for simplifying complex topics, you craft
    engaging narratives that captivate and educate, bringing new
    discoveries to light in an accessible manner.""",
        tools=tools,
        allow_delegation=False,
    )
