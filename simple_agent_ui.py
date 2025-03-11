# Copyright (c) Microsoft. All rights reserved.

import asyncio
import chainlit as cl

from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import ChatHistory
from simple_agent_tools import agent

# agent = ChatCompletionAgent(
#     service=AzureChatCompletion(),
#     name="Assistant",
#     instructions="Answer the user's questions.",
# )

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("chat_history", ChatHistory())

@cl.on_message
async def on_message(message: cl.Message):
    chat_history: ChatHistory = cl.user_session.get("chat_history")

    msg = cl.Message(content="", author=agent.name)

    chat_history.add_user_message(message.content)
    async for message in agent.invoke_stream(chat_history):
        await msg.stream_token(message.content)
        print(f"{message.content}", end="", flush=True)
    #response = await agent.get_response(history=chat_history)

    cl.user_session.set("chat_history", chat_history)
    await msg.update()

    #await cl.Message(content=response.content, author=agent.name).send()