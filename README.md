# Agentic PRD - Product Requirements Documentation Generator

Welcome to the Agentic PRD / (AgentClI) project, powered by [crewAI](https://crewai.com). This project is designed to help you generate comprehensive product requirements documentation using a team of specialized AI agents. The system leverages the powerful and flexible framework provided by crewAI to create detailed, well-structured product documentation through collaborative AI agents.

This is designed to work specifically with Agentic Coding Systems by creating a PRD written with rules that make it suitable for the task. 
From one line description of your app/idea it will make a document that help agentic coders build in the best possible way.

## Features

- Multi-agent system with specialized roles:
  - Product Manager
  - Product Owner
  - Designer
  - Subject Matter Expert
  - Quality Assurance Designer
- Sequential (though with multi-agent review and cyclical process) task processing for structured documentation creation
- Interactive CLI interface for project input
- Comprehensive documentation generation including:
  - Project purpose and goals
  - Feature specifications
  - Design requirements
  - Product backlog
  - Quality assurance guidelines
  - Complete product requirements document
# This will be written in a way that is intended for an Agentic Coder to follow.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Configuration

**Add your `OPENAI_API_KEY` into the `.env` file**

- Review `src/agent_cli/config/agents.yaml` to customize agent roles and behaviors
- Review `src/agent_cli/config/tasks.yaml` to adjust documentation generation tasks
- Review `src/agent_cli/crew.py` to add custom tools and specific arguments
- Review `src/agent_cli/main.py` to customize the CLI interface

## Usage

To generate product requirements documentation, run this from the root folder of your project:

```bash
$ crewai run
```

The system will prompt you to enter your project topic/description, and then the AI agents will collaborate to create comprehensive documentation.

### Additional Commands

- Train the crew: `crewai train <iterations> <filename>`
- Replay from a specific task: `crewai replay <task_id>`
- Test the crew: `crewai test <iterations> <openai_model_name>`

## Understanding Your Crew

The AgentCli Crew is composed of multiple AI agents, each with unique roles and responsibilities:

- **Product Manager**: Oversees the overall documentation process creates the overall vision and reviews all the work that is done.
- **Product Owner**: Defines product vision into stories and requirements
- **Designer**: Creates design specifications and guidelines
- **Subject Matter Expert**: Provides domain-specific expertise
- **Quality Assurance Designer**: Ensures documentation quality and completeness

These agents collaborate on a series of tasks defined in `config/tasks.yaml`, leveraging their collective skills to create comprehensive product documentation.

## Support

For support, questions, or feedback regarding the AgentCli Crew or crewAI:
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create comprehensive product documentation together with the power and simplicity of crewAI.
