from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

#build a database
db = SqliteDb(db_file="session_state_db/chat_session_state.db")

#give a session id and user id 
session_id = "1"
user_id = "user_a"

#create a LLM
llm = OpenAIChat(id="gpt-4.1-mini")

#create a session state
user_info = {"name":"Manav","age":25}


#Create the agent
agent = Agent(
    name="agent_with_state",
    model=llm,
    session_id=session_id,
    session_state=user_info,
    user_id=user_id,
    db=db,
    stream=True,
    markdown=True,    
    add_session_state_to_context=True
)


agent.print_response(input="Can you tell me my name and age ? ",
                     session_state={"name":"Shreya","age":27})


