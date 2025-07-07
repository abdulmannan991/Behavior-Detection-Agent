import os
from typing import cast
from dotenv import load_dotenv,find_dotenv
from agents import Agent,OpenAIChatCompletionsModel,Runner,RunConfig,set_tracing_disabled
from openai import AsyncOpenAI
from openai import OpenAI
import chainlit as cl


load_dotenv(find_dotenv(),override=True)
set_tracing_disabled(True)
api_keys = os.getenv("GEMINI_API_KEY")
base_path = os.getenv("base_url") 
model_name = os.getenv("Gemini_model")


@cl.on_chat_start
async def start():
    
    client = AsyncOpenAI(
    base_url=base_path,
    api_key=api_keys,   
)

    model = OpenAIChatCompletionsModel(
    model=model_name,
    openai_client=client,

)
    
    cl.user_session.set("chat_history",[])


    Helpful_Agent : Agent = Agent(
    name="Helpful Assistant",
    instructions=(
    "You are a helpful assistant. First, answer the user's question clearly and concisely. "
    "Then, based on their typing style (e.g., tone, formality, punctuation, spelling), "
    "briefly describe their behavior or emotional state such as whether they seem happy, upset, casual, confused, etc. "
    "You also have access to the full conversation history, so if the user asks about their last message or says 'do you remember', you can reference previous messages accordingly."
),

    model=model,
)
    cl.user_session.set("agent",Helpful_Agent)
    

@cl.on_message
async def main(message:cl.Message):

    msg = cl.Message(content="Thinking")
    await msg.send()
    

    Helpful_Agent : Agent = cast(Agent,cl.user_session.get("agent"))

    history = cl.user_session.get("chat_history") or []
    history.append({"role":"user", "content":message.content})

    try:
        print("\n[calling agent with context]\n",history,"\n")
       
        result =  Runner.run_sync(starting_agent=Helpful_Agent , input=history)

        response_content = result.final_output
        msg.content = response_content
        await msg.update()

        cl.user_session.set("chat_history",result.to_input_list())

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
