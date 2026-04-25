from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from agno.run import RunContext
from dotenv import load_dotenv

load_dotenv()

#build a database
db = SqliteDb(db_file="session_state_db/shopping.db")

#give a session id and user id 
session_id = "2"
user_id = "user_a"

#create a LLM
llm = OpenAIChat(id="gpt-4.1-mini")


# define a tool that adds items to shopping list
def add_item(run_context: RunContext, item: str) -> str:
    """
    Add an item to the shopping list
    """
    #lowercase the item 
    item = item.lower()
    #fetch the shoping list
    shopping_list = run_context.session_state['shopping_list']

    if item in shopping_list:
        return f"{item} Item already in shopping list"
    else:
        run_context.session_state["shopping_list"].append(item)
        return f"{item} added to the shopping list"


#define tool to remove item from shopping list
def removed_item(run_context: RunContext,item:str)->str:
    """
    removed an item to the shopping list
    """
    #lowercase the item 
    item = item.lower()
    #fetch the shopping list
    shopping_list = run_context.session_state['shopping_list']
 
    #check item in list or not 
    if item not in shopping_list:
        return f"{item} not in shopping list. Add the item first."
    else:
        #removed the item shopping list
        shopping_list.remove(item)
        return f"{item} removed from shopping list"
        
#define tool to read items from the list
def list_items(run_context:RunContext)->str:
    """
    List down all the items in shopping list
    """    
    #check whether shopping list is empty or not.
    #fetch the shopping list 
    shopping_list = run_context.session_state["shopping_list"]

    if shopping_list:
        text = "\n".join([f"- {item}" for item in shopping_list])
        return f"The shopping list is: {text}"
    else:
        return "The shopping list is empty"

#define tool to clear the shopping list
def clear_list(run_context:RunContext)->str:
        """
        Clears the shopping list of all items and gives you empty list
        """ 
        shopping_list = run_context.session_state["shopping_list"]

        if shopping_list:
            shopping_list.clear()
            return "Cleared the shopping list of all items"
        else:
            return "The shopping list are already empty"

#Create the agent
agent = Agent(
    model=llm,
    name="agent_with_state",
    session_state={"shopping_list": []},
    session_id=session_id,
    instructions="You job is to manage shopping lists. you start off with an empty list and " \
    "you can add item to the list, remove item from the list,list items in the list or clear the list of all items",
    tools=[add_item,removed_item,list_items,clear_list],
    user_id=user_id,
    db=db,
    stream=True,
    markdown=True
)

agent.print_response("Can you tell me what is on the shopping list")

print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("Add Milk to the shopping list")

print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("Add Eggs and bread to the shopping list")

print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("I have bought milk and egg")

print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("What is on my list ?")

print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("Clear everything from the shopping list and add butter and curd to the list")

print(f"The session state is: {agent.get_session_state(session_id)}")