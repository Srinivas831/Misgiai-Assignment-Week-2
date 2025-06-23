# These are like our "functions/tools"

def python_exec(code: str) -> str:
    """Run some math code using eval and return its result as a string."""
    try:
        result = eval(code)  # Eval only for math expressions
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def noop(_input: str) -> str:
    """A tool that does nothing."""
    return ""

def agent(user_message: str) -> str:
    """Very simple agent:
       - Counts character if it's a 'count' query.
       - Evaluates math expressions.
       - Otherwise replies normally.
    """
    user_message_lower = user_message.lower()

    # STEP A: Check if it's a counting request
    if "count" in user_message_lower or "how many" in user_message_lower:
        if " in " in user_message_lower:
            target_char = user_message_lower.split("'")[1]
            text = user_message_lower.split("'")[3]
            result = text.count(target_char)  # <-- DIRECT PYTHON COUNT METHOD
            return f"There are {result} '{target_char}' character(s) in \"{text}\"."

    # STEP B: Try to evaluate as math
    try:
        result = python_exec(user_message)
        return f"The result is {result}."
    except:
        pass

    # STEP C: Fallback
    return "I don’t understand."

if __name__ == "__main__":
    # 3 counting examples
    print(agent("How many 'r' in 'strawberry'?"))
    print(agent("How many 'a' in 'bananas'?"))
    print(agent("How many 't' in 'tattered'?"))

    # 2 math examples
    print(agent("2 + 3 * 5"))
    print(agent("100 / 4"))
