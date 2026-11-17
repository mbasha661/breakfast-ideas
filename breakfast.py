"""
Ask LangChain for 5 Breakfast Ideas - Social Eagle Week 2 Day 5.

Run twice and compare: if the five ideas differ between runs, that is the
model's temperature at work. The API key comes from the environment, never
hard-coded:

    export OPENAI_API_KEY="your-key"     # Windows: $env:OPENAI_API_KEY="your-key"
    python breakfast.py
"""

import os

from langchain_openai import ChatOpenAI

if not os.environ.get("OPENAI_API_KEY"):
    raise SystemExit("Set the OPENAI_API_KEY environment variable first.")

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = (
    "Give me exactly 5 healthy South Indian breakfast ideas. "
    "Rules: numbered 1 to 5, one line each, just the dish name with a "
    "5-10 word reason it is healthy, and no preamble or closing line."
)

reply = llm.invoke(prompt)

# reply is an AIMessage object, not a string. Print it once to see the whole
# object; the part you actually want is .content:
# print(reply)
print(reply.content)
