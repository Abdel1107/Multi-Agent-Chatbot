from langchain.chains import ConversationChain
from langchain.llms import Ollama
from memory.memory_manager import get_memory

llm = Ollama(model="llama3.2"
                   "")

# Get memory for this agent
memory = get_memory("admission")

# Set up the conversation chain
chat_chain = ConversationChain(llm=llm, memory=memory)
def get_response(message: str) -> str:
    response = llm.invoke(f"This is a question about Concordia CS admissions: {message}")
    return f"[Admission Agent] {response}"
