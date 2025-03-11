import asyncio

from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import ChatHistory

# 1. Create the agent by specifying the service
agent = ChatCompletionAgent(
    service=AzureChatCompletion(),
    name="Assistant",
    instructions="Answer the user's questions.",
)

async def main():

    user_input = "Why is the sky blue?"

    # 2. Create a chat history to hold the conversation
    chat_history = ChatHistory()

    # 3. Add the user input to the chat history
    chat_history.add_user_message(user_input)
    print(f"# User: {user_input}")

    # 4. Invoke the agent for a response
    response = await agent.get_response(chat_history)
    print(f"# {response.name}: {response}")

    # 5. Add the agent response to the chat history
    chat_history.add_message(response)


if __name__ == "__main__":
    asyncio.run(main())