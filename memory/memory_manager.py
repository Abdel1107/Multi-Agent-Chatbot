from langchain.memory import ConversationBufferMemory

memory_store = {
    "general": ConversationBufferMemory(return_messages=True),
    "ai": ConversationBufferMemory(return_messages=True),
    "admission": ConversationBufferMemory(return_messages=True),
}

# Track user-agent history
user_last_agent = {}

def get_memory(agent_type: str):
    return memory_store.get(agent_type)

def set_last_agent(user_id: str, agent_type: str):
    user_last_agent[user_id] = agent_type

def get_last_agent(user_id: str):
    return user_last_agent.get(user_id)
