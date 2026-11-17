# 5 Breakfast Ideas with LangChain - Social Eagle Week 2 Day 5

A short LangChain script that asks the model for exactly 5 healthy breakfast
ideas and prints only the text of the reply.

## Setup and run

```bash
mkdir breakfast && cd breakfast
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt
export OPENAI_API_KEY="your-key"                  # Windows: $env:OPENAI_API_KEY="your-key"
python breakfast.py
```

Run it twice and compare. The prompt pins the format (numbered, one line each,
no preamble) but not the content, so the five ideas can differ between runs -
that is the model's temperature. To get the same five every time you would set
`temperature=0` on ChatOpenAI.

## The two lessons

1. `llm.invoke()` returns an AIMessage object, not a string. Uncomment
   `print(reply)` once to see the whole object; `reply.content` is the part
   you want.
2. "Healthy" had to be defined: the prompt says South Indian and asks for the
   reason each dish is healthy, otherwise the model decides what healthy means.

## Free-tier note

Runs on Groq's free OpenAI-compatible endpoint too:
`export OPENAI_BASE_URL="https://api.groq.com/openai/v1"` with a Groq key, and
change the model name in the file.

## Two runs - did they match?

(Fill after running: same five ideas or different? One line for the community post.)
