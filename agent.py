from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb 
from textwrap import dedent
from agno.run import RunContext
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv(".env")

llm = OpenAIChat(id="gpt-5-mini")

#create a database instance
db = SqliteDb(db_file="chat_history_db/chat_history.db")

#session ID creation 
session_id = "chat_history_for_agent_for_data_science"

#create tool for web search
web_search = DuckDuckGoTools()

def add_key_point(run_context: RunContext,point:str)->str:
    """
    Tool to add key points to the session state
    """
    #fetch the list
    points_list = run_context.session_state["key_points"]
    #add point to the points list 
    points_list.append(point)

    return f"Point: {point} added to the session state"


#build an agent 
agent = Agent(
    name="My_Agent",
    model=llm,
    db=db,
    session_id=session_id,
    user_id="Manav",
    session_state={'key_points':[]},
    tools=[add_key_point,web_search],
    instructions=dedent("""
            You are an expert assistant. Your task is to:
            1. Create summary on the topic and stick to the word count if provided
            2. You have access to a tool called as 'add_key_point' which adds a key_point
                from the summary to the session state.
            3. You have the capability to access the web using web search tool. 
                try to generate summary with the latest information.             
            4. Add key point only when asked for.
            5. The Summary created should include both advantages and disadvantages.
                        """),
    add_history_to_context=True,
    add_session_state_to_context=True,
    num_history_runs=5,
    markdown=True,
    stream=True
)

agent.print_response("I need short answers on topic of AI Agents and its future, it's all most 300 words.")

agent.print_response("add key points from the summary generated above. The number of points depends on the summary.")

agent.print_response("tell what topic am I taking about?")

agent.print_response("List Down the key points from the recent summary generated for me in proper format")

print(agent.get_session_state(session_id)) 