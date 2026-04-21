from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb 
from dotenv import load_dotenv

load_dotenv(".env")

llm = OpenAIChat(id="gpt-5-mini")

#create a database instance
db = SqliteDb(db_file="chat_history_db/chat_history.db")

#session ID creation 
session_id = "chat_history_for_agent"

#build an agent 
agent = Agent(
    name="My_Agent",
    model=llm,
    db=db,
    session_id=session_id,
    user_id="Manav",
    add_history_to_context=True,
    num_history_runs=5,
    markdown=True,
    stream=True
)

agent.print_response("I need short answers on AI market right now, it's all most 100 words.")

agent.print_response("tell what topic am I taking about?")