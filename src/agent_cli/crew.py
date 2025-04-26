from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# Create a text file knowledge source
text_source = TextFileKnowledgeSource(
    file_paths=["rules.txt", "user_preference.txt"]
)  

@CrewBase
class AgentCli():
    """AgentCli crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'],
            verbose=True
        )

    @agent
    def product_owner(self) -> Agent:
        return Agent(
            config=self.agents_config['product_owner'],
            verbose=True
        )

    @agent
    def designer(self) -> Agent:
        return Agent(
            config=self.agents_config['designer'],
            verbose=True
        )

    @agent
    def subject_matter_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['subject_matter_expert'],
            verbose=True
        )
    @agent
    def quality_assurance_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_assurance_designer'],
            verbose=True
        )
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def purpose_task(self) -> Task:
        return Task(
            config=self.tasks_config['purpose_task'],
        )
    @task
    def features_task(self) -> Task:
        return Task(
            config=self.tasks_config['features_task'],
        )

    @task
    def subject_matter_expert_task(self) -> Task:
        return Task(
            config=self.tasks_config['subject_matter_expert_task'],
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task'],
        )
    @task
    def product_backlog_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_backlog_task'],
        )
    @task
    def quality_assurance_designer_task(self) -> Task:
        return Task(
            config=self.tasks_config['quality_assurance_designer_task'],
        )
    @task
    def product_requirements_document_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_requirements_document_task'],
        )
        
    @crew
    def crew(self) -> Crew:
        """Creates the AgentCli crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
