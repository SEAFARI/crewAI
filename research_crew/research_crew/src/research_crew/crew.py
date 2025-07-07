
## To use this YAML configuration in your code (agents.yaml and tasks.yaml), create a crew class that inherits from CrewBase

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ResearchCrew():
    """ResearchCrew crew"""  ## docstring (documentation string)

    agents: List[BaseAgent]
    tasks: List[Task]
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    '''
    agents: List[BaseAgent] is a type hint.
    It indicates that the agents attribute of your ResearchCrew instance will be a list of BaseAgent objects. 
    BaseAgent is the fundamental type for agents in CrewAI.
    '''
    '''
     When you inherit from CrewBase and specify agents_config = "path/to/agents.yaml", 
     the CrewBase infrastructure automatically loads the content of that YAML file into a dictionary-like attribute
     named self.agents_config on your ResearchCrew instance.
     So, self.agents_config holds all the definitions from your agents.yaml.
    '''
    
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResearchCrew crew"""


        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            
        )



### knowledge source is an important topic ( core concept )