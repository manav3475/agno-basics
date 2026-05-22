# Agno Basics

A comprehensive project demonstrating the fundamentals of building intelligent agents using the **Agno framework** with OpenAI models.

## 📋 Project Overview

This project explores various features and capabilities of the Agno framework, including:

- **Basic Agents** - Simple agent creation and interaction
- **Agents with Memory** - Persistent chat history and context management
- **Agents with State** - Session-based state management
- **Agents with Tools** - Integration with web search and custom tools
- **Database Integration** - SQLite-based conversation storage

## 🛠️ Tech Stack

- **Python** 3.13+
- **Agno** 2.5.17+ - Agent framework
- **OpenAI** - GPT-4o and GPT-5-mini models
- **DuckDuckGo** - Web search tool
- **SQLite** - Database for chat history
- **SQLAlchemy** - ORM for database operations
- **Python-dotenv** - Environment variable management

## 📁 Project Structure

```
agno-basics/
├── agent.py                    # Basic agent with web search tools
├── agent_with_memory_*.py      # Agents with conversation memory (3 variations)
├── agent_with_state_*.py       # Agents with session state management (4 variations)
├── agent_with_tools.py         # Agent with DuckDuckGo web search integration
├── main.py                     # Version information script
├── test.py                     # Testing agent configurations
├── chat_history_db/            # SQLite database for chat history
├── session_state_db/           # Database for session state
├── .env                        # Environment variables (API keys)
├── .gitignore                  # Git ignore rules
└── pyproject.toml              # Project dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- OpenAI API key
- HuggingFace API token (optional)
- Qdrant API key (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/manav3475/agno-basics.git
cd agno-basics
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -e .
# or
uv sync
```

4. Create `.env` file with your API keys:
```bash
OPENAI_API_KEY="your-openai-api-key"
HUGGINGFACEHUB_ACCESS_TOKEN="your-huggingface-token"  # Optional
QDRANT_URL="your-qdrant-url"  # Optional
QDRANT_API_KEY="your-qdrant-api-key"  # Optional
```

## 📚 Examples

### Basic Agent
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(model=OpenAIChat(id="gpt-4o"))
agent.print_response("What's the latest about AI?")
```

### Agent with Web Search
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools(enable_search=True, enable_news=False)],
)
agent.print_response("What are the latest headlines?")
```

### Agent with Memory
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

db = SqliteDb(db_file="chat_history.db")
agent = Agent(
    db=db,
    model=OpenAIChat(id="gpt-4o"),
    session_id="session_1",
    add_history_to_context=True,
)
```

### Agent with Session State
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    session_state={"key_points": []}  # Persistent state
)
```

## 📖 Features

### Memory Management
- **Conversation History** - Stores and retrieves past interactions
- **Context Awareness** - Uses historical context for better responses
- **Multiple Sessions** - Manage separate conversation threads

### State Management
- **Session State** - Maintain data across conversation turns
- **Run Context** - Access to runtime execution context
- **Custom Tools** - Create domain-specific tools

### Web Integration
- **DuckDuckGo Search** - Real-time web search capabilities
- **News Search** - Access latest news and headlines
- **Multiple Backends** - Support for Yandex and other search providers

## 🔧 Running Examples

Run specific scripts:

```bash
# Basic agent
python agent.py

# Agent with memory
python agent_with_memory_1.py

# Agent with state management
python agent_with_state_1.py

# Agent with web search
python agent_with_tools.py

# Run tests
python test.py
```

## 📝 Script Descriptions

| Script | Purpose |
|--------|---------|
| `agent.py` | Demonstrates basic agent with web search tools |
| `agent_with_memory_1.py` | Simple conversation memory implementation |
| `agent_with_memory_2.py` | Enhanced memory with context integration |
| `agent_with_memory_3.py` | Advanced memory with retrieval and chat history |
| `agent_with_state_1.py` | Basic session state management |
| `agent_with_state_2.py` | State with custom tools |
| `agent_with_state_3.py` | Complex state operations |
| `agent_with_state_4.py` | Advanced state patterns |
| `agent_with_tools.py` | Web search integration with news capabilities |
| `test.py` | Configuration testing and examples |

## 🐛 Troubleshooting

### "No results found" Error
- This occurs when DuckDuckGo search fails
- **Solution**: Use `enable_search=True, enable_news=False` for better coverage
- Try with simpler queries
- Check internet connection

### API Key Issues
- Ensure `.env` file is in the project root
- Verify API keys are valid and not expired
- Check environment variables are loaded with `load_dotenv()`

### Database Errors
- Ensure `chat_history_db/` and `session_state_db/` directories exist
- Check SQLite permissions
- Clear database files if corrupted

## 🚨 Security Notes

- Never commit `.env` file containing API keys
- Use environment variables for all sensitive data
- `.gitignore` already excludes `.env` and `*.db` files
- Rotate API keys regularly

## 📦 Dependencies

All dependencies are managed in `pyproject.toml`:

```toml
agno>=2.5.17          # Core agent framework
ddgs>=9.14.1          # DuckDuckGo search
openai>=2.31.0        # OpenAI API client
python-dotenv>=1.2.2  # Environment variable management
sqlalchemy>=2.0.49    # Database ORM
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Resources

- [Agno Documentation](https://docs.agno.ai)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [DuckDuckGo Search API](https://duckduckgo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org)

## 👨‍💻 Author

Created by Manav Shah

---

**Last Updated**: May 2026
