# main.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Import our custom tools
from tools.math_tools import average, sqrt
from tools.string_tools import count_vowels, count_letters


# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ask the user for a natural language query
query = input("🔍 Enter your question: ")



# Build a chain-of-thought prompt
cot_prompt = f"""
You are an intelligent assistant. Read the user's question and break it down step-by-step.

If a tool is needed, explain why, and write which tool function to use (like math.sqrt or string.count_vowels).
Then finish with: Final Answer: <your final answer>

User Question: {query}
"""



# Call OpenAI with the CoT prompt
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": cot_prompt}
    ],
    temperature=0.3,
    max_tokens=500
)

# Extract reasoning from model
reasoning = response.choices[0].message.content

# Print the reasoning from the LLM
print("\n🤔 Reasoning:\n" + reasoning)

# Now we need to parse the reasoning to find tool calls
tool_calls = []     
for line in reasoning.split('\n'):
    if 'tool' in line.lower():
        tool_calls.append(line.strip())
# Print the tool calls
print("\n🔧 Tool Calls:")
for call in tool_calls:
    print(f"- {call}")
# Execute the tool calls
results = []
for call in tool_calls:
    if 'math.average' in call:
        # Extract numbers from the call
        numbers = [float(num) for num in call.split('(')[1].split(')')[0].split(',')]
        result = average(*numbers)
    elif 'math.sqrt' in call:
        # Extract number from the call
        number = float(call.split('(')[1].split(')')[0])
        result = sqrt(number)
    elif 'string.count_vowels' in call:
        # Extract word from the call
        word = call.split('(')[1].split(')')[0].strip('"')
        result = count_vowels(word)
    elif 'string.count_letters' in call:
        # Extract word from the call
        word = call.split('(')[1].split(')')[0].strip('"')
        result = count_letters(word)
    else:
        result = "Unknown tool call"
    
    results.append(result)
# Print the results of the tool calls
print("\n🔍 Tool Results:")
for call, result in zip(tool_calls, results):
    print(f"- {call}: {result}")
# Print the final answer
final_answer = response.choices[0].message.content.split("Final Answer:")[-1].strip()
print("\n✅ Final Answer:\n" + final_answer)


