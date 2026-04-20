from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.in_memory import InMemoryDb
from agno.db.json import JsonDb
from dotenv import load_dotenv

load_dotenv(".env")

llm = OpenAIChat(id="gpt-5-mini")


#add session id
session_id = "session_1"

#create an in-memory database instance
# db = InMemoryDb()
db = JsonDb(db_path="chat_history_db",session_table="session_history")

#build an agent 
agent = Agent(
    name="agent_with_memory",
    db=db,
    model=llm,
    session_id=session_id,
    add_history_to_context=True,
    num_history_runs=10,
    markdown=True,
    stream=True
)


#give inputs to agent 
agent.print_response(input="Hello My name is Manav Shah")

agent.print_response(input="Can you tell me my name ?")

agent.print_response(input="tell me a joke that is funny ?")

agent.print_response(input="Can you tell me what is the session id ?")

agent.print_response(input="Can you tell my name ?")

# print(agent.session_id)

messages = agent.get_chat_history(session_id)

for message in messages:
    role,content = message.role,message.content
    if role == "system":
        continue
    else:
        print(f"Role: {role}, Message: {content}")