import os
import openai
import chainlit as cl
from langchain import OpenAI, LLMMathChain, SerpAPIWrapper
from langchain.agents import load_tools, initialize_agent, AgentType, AgentExecutor, Tool
from langchain.chat_models import ChatOpenAI
from apikey import OPENAI_API_KEY


os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

@cl.on_chat_start
def start():
    
    llm = ChatOpenAI(temperature=0.5, streaming=True)
    math_llm = OpenAI(temperature=0.5)
    tools = load_tools(
        ["arxiv", "human", "llm-math",],
        llm=math_llm
    )


    agent_chain = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        max_iterations=10,
        verbose=True,
        handle_parsing_errors=True
    )

    cl.user_session.set("agent", agent_chain)


@cl.on_message
async def main(message):
    agent = cl.user_session.get("agent")
    cb = cl.LangchainCallbackHandler(stream_final_answer=True)

    await cl.make_async(agent.run)(message, callbacks=[cb])
