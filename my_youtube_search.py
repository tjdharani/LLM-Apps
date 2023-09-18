
from langchain.tools import YouTubeSearchTool
from langchain.agents import AgentType, initialize_agent, Tool
from langchain.llms import OpenAI
from langchain import LLMMathChain, SerpAPIWrapper
import os
from apikey import OPENAI_API_KEY

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY


tool = YouTubeSearchTool()

tools = [
    Tool(
        name="Search",
        func=tool.run,
        description="Useful for when you need to give links to youtube videos. Remember to put https://youtube.com/ in front of every link to complete it",
    )
]

agent = initialize_agent(
    tools,
    OpenAI(temperature=0),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent.run('give a new video about agi')