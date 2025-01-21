from crewai import Agent

def create_agent(task):
    agent = Agent(task)
    agent.run()
    return agent.get_response()
