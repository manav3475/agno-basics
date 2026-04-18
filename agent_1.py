from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv(".env")

llm = OpenAIChat(id="gpt-5-mini")

#build an agent 
agent = Agent(
    name="My_Agent",
    model=llm,
    markdown=True,
    stream=True
)

agent.print_response("I need short answers on AI market right now, it's all most 100 words.")

agent.print_response("tell what topic am I taking about?")