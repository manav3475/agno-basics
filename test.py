from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIResponses
from agno.run import RunContext
from dotenv import load_dotenv

load_dotenv()

# Define a tool that adds an item to the shopping list
def add_item(run_context: RunContext, item: str) -> str:
    """Add an item to the shopping list."""

    # We access the session state via run_context.session_state
    run_context.session_state["shopping_list"].append(item)

    return f"The shopping list is now {run_context.session_state['shopping_list']}"


# Create an Agent that maintains state
agent = Agent(
    model=OpenAIResponses(id="gpt-5.2"),
    # Database to store sessions and their state
    db=SqliteDb(db_file="tmp/agents.db"),
    # Initialize the session state with an empty shopping list. This will be the default state for all sessions.
    session_state={"shopping_list": []},
    tools=[add_item],
    # You can use variables from the session state in the instructions
    instructions="Current state (shopping list) is: {shopping_list}",
    markdown=True,
)

# Example usage
agent.print_response("Add milk, eggs, and bread to the shopping list", stream=True)
print(f"Final session state: {agent.get_session_state()}")