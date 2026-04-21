from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv(".env")

llm = OpenAIChat(id="gpt-5-mini")

#add user id 
user_id = "user_1"

#create an in-memory database instance
db = SqliteDb(db_file="chat_history_db/demo.db")

#build an agent 
agent = Agent(
    name="agent_with_memory",
    db=db,
    model=llm,
    add_history_to_context=True,
    num_history_runs=5,
    markdown=True,
    stream=True
)

#create session 
session_transformes = "session_transformer"
session_rag = "session_rag"

#conversation 1 --> session_id = session_transformes
# agent.print_response("hi,can you tell me about transformers architecture in 100 words ? make is simple ",
#                      session_id=session_transformes)

# agent.print_response("what is self attention. explain in a single Paragraph ?",
#                      session_id=session_transformes)

# agent.print_response("what is this conversation all about ?",session_id=session_transformes)


#conversation 2 --> session_id = session_rag

# agent.print_response("What is the role of RAG in AI. Explain in 100 words.",session_id=session_rag)

# agent.print_response("what does RAG Stands for ?",session_id=session_rag)

# agent.print_response("What is this conversation all about ?",session_id=session_rag)

agent.print_response("Can you list down the advantages of RAG you talked earlier. " \
"Only list down from previous chat",session_id=session_rag)

print()
print()
print()


print("==================Transformer Messages========================")
messages_1 = agent.get_chat_history(session_transformes)

for message in messages_1:
    role,content = message.role,message.content
    if role == "system":
        continue
    else:
        print(f"Role: {role}, Message: \n{content}")



print("\n\n==================RAG Messages========================")
messages_2 = agent.get_chat_history(session_rag)

for message in messages_2:
    role,content = message.role,message.content
    if role == "system":
        continue
    else:
        print(f"Role: {role}, Message: \n{content}")