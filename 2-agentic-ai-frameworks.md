# Agentic AI Frameworks (LangGraph, CrewAI, AutoGen, etc.)

Building an **"agentic AI"** system means enabling an AI (LLM) to *act autonomously* – breaking down tasks, invoking tools or code, and handling multi-step reasoning. Several frameworks have emerged to help developers create such AI agents:

## LangGraph

A Python framework focused on **graph-based, stateful workflows** for LLMs.

- Instead of linear chains, LangGraph lets you define a directed acyclic graph (DAG) of steps/nodes that the agent can traverse
- Makes it easy to include conditional branches, loops, and parallel paths in an agent's plan
- You can specify that *"if condition A, go to Node X; otherwise go to Node Y"*, which is more intuitive than forcing everything into a sequential script
- Emphasizes reliability and debugging with "time-travel" debugging that allows rolling back the agent's state to a previous step during development
- Ideal for **complex, deterministic workflows** where you need fine control and robust error handling in an LLM-driven process

## CrewAI

A framework that takes a **role-based collaboration** approach to AI agents.

- In CrewAI, you orchestrate multiple sub-agents each assigned a specific role (e.g., a "Researcher" agent, a "Writer" agent, an "Editor" agent, etc.)
- The idea is to mimic a human team: each agent tackles part of the task and they can pass information to each other
- This often leads to very **comprehensive outputs**, as each role focuses on elaborating its portion of the solution
- CrewAI's role prompts nudge the LLM to approach the task methodically (e.g., the Researcher gathers facts, the Writer composes text, the Editor refines)
- Early versions had limitations in dynamic re-planning – once a plan was set, it was hard to revise mid-execution, and hierarchical delegations sometimes got stuck in loops
- Still, CrewAI introduced a powerful pattern for **multi-agent collaboration** by dividing cognitive labor among specialized agents

## AutoGen

An open-source framework from Microsoft Research for creating **multi-agent AI applications**.

- Provides programming abstractions for spawning agents that can converse with each other (or with humans) to solve tasks cooperatively
- Supports both autonomous agents and agents that can consult humans in the loop
- Emphasizes *deterministic, reproducible workflows* – you can script how agents interact but also allow dynamic dialogue between agents
- Comes with various extensions (e.g., an OpenAI chat completion client, web browsing tools, etc.) and a GUI called AutoGen Studio for no-code setups
- Design makes it straightforward to integrate with external tools: it can wrap functions or system commands as *tools* that agents call
- The community has shown that AutoGen agents can be "supercharged" with MCP – integrating Anthropic's MCP tools in just a few lines of code
- Overall, AutoGen is a flexible **agent orchestration framework** that is production-oriented, with features like multi-agent chat sessions, resource management, and a growing ecosystem of plugin tools

## Other Notable Frameworks

The agentic ecosystem is evolving rapidly:

- **SmolAgents** (by GPT-4 developers) explores agents that dynamically write and execute code (the "CodeAgent" concept) to solve problems
- **Pydantic-AI** is a Python library that uses Pydantic schemas to structure LLM tool interactions
- OpenAI's own early "functions" and experimental Agent APIs (sometimes called "OpenAI Tools" or Agents SDK) provide a simpler built-in way to let an LLM call functions

Each framework has distinct strengths – some excel at planning, others at integration – and often they can be combined with MCP to extend their toolset. For example, LangGraph or CrewAI could potentially use MCP servers as tools, similar to the AutoGen case.
