from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

#create the model
llm = OpenAIChat(id="gpt-5")

#cerate the web search tool
web_search = DuckDuckGoTools()

#create the agent 
agent = Agent(
    name = "agent_with_web_search",
    tools=[web_search],
    instructions="You are an expert in searching web. you have access to web search tool to get the latest information. When searching, use simple and direct queries.",
    model = llm,
    stream=True,
    markdown=True
)


agent.print_response("Tell me about USA ?",markdown=True)
