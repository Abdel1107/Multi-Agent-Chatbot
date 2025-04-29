from Agents.general_agent import get_response as general_response
from Agents.ai_agent import get_response as ai_response
from Agents.admission_agent import get_response as admission_response
from memory.memory_manager import set_last_agent, get_last_agent
from langchain.llms import Ollama

# LLM used for intent classification
classifier_llm = Ollama(model="llama3.2")

def classify_intent(message: str) -> str:
    prompt = f"""
You are an intent classifier for a chatbot. Your job is to decide which category this message belongs to:
- "general" for anything casual, jokes, greetings, or random questions
- "ai" for anything about artificial intelligence or machine learning
- "admission" for anything about Concordia University or applying to CS programs

Message: "{message}"
Respond with only one word: general, ai, or admission.
"""
    response = classifier_llm.invoke(prompt).strip().lower()
    if response in ["general", "ai", "admission"]:
        return response
    return "general"  # fallback if unclear

def route_message(message: str, user_id: str = "default") -> str:
    # Step 1: Try to classify message intent using LLM
    intent = classify_intent(message)

    # Step 2: Fallback to last agent if intent is too vague (general)
    if intent == "general":
        last_agent = get_last_agent(user_id)
        if last_agent:
            intent = last_agent

    # Step 3: Save this agent as the most recent one used by this user
    set_last_agent(user_id, intent)

    # Step 4: Route to the correct agent
    if intent == "ai":
        return ai_response(message)
    elif intent == "admission":
        return admission_response(message)
    else:
        return general_response(message)
