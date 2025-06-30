# prompt_optimizer.py
# This file contains the core optimization logic that rewrites prompts for specific AI tools

from tool_knowledge import ToolKnowledge  # Import our tool knowledge base
from prompt_analyzer import PromptAnalyzer  # Import our prompt analyzer

class PromptOptimizer:
    """
    This class takes a user's prompt and optimizes it for a specific AI coding tool.
    It uses the analysis from PromptAnalyzer and applies rules from ToolKnowledge.
    """
    
    def __init__(self):
        """
        Constructor - creates the optimizer with access to knowledge base and analyzer
        """
        # Create instances of our other components
        self.tool_knowledge = ToolKnowledge()  # Access to tool information
        self.prompt_analyzer = PromptAnalyzer()  # Access to prompt analysis
    
    def optimize_prompt(self, original_prompt, target_tool):
        """
        Main method that optimizes a prompt for a specific tool.
        
        Parameters:
        original_prompt (string): The user's original prompt
        target_tool (string): The tool to optimize for (e.g., "copilot", "cursor")
        
        Returns:
        dictionary: Complete optimization results with explanations
        """
        # Step 1: Analyze the original prompt
        analysis = self.prompt_analyzer.analyze_prompt(original_prompt)
        
        # Step 2: Get tool information
        tool_info = self.tool_knowledge.get_tool_info(target_tool)
        
        # Step 3: Check if tool is supported
        if not tool_info:
            return {
                "error": f"Tool '{target_tool}' is not supported",
                "supported_tools": self.tool_knowledge.get_all_tools()
            }
        
        # Step 4: Apply tool-specific optimizations
        optimized_prompt = self._apply_optimizations(original_prompt, analysis, tool_info)
        
        # Step 5: Generate explanations for the changes made
        explanations = self._generate_explanations(original_prompt, optimized_prompt, analysis, tool_info)
        
        # Step 6: Return complete results
        return {
            "original_prompt": original_prompt,
            "optimized_prompt": optimized_prompt,
            "target_tool": tool_info["name"],
            "analysis": analysis,
            "explanations": explanations,
            "improvements_made": len(explanations),
            "optimization_success": True
        }
    
    def _apply_optimizations(self, original_prompt, analysis, tool_info):
        """
        Private method that applies specific optimizations based on the tool and analysis.
        
        Parameters:
        original_prompt (string): Original user prompt
        analysis (dict): Analysis results from PromptAnalyzer
        tool_info (dict): Information about the target tool
        
        Returns:
        string: The optimized prompt
        """
        # Start with the original prompt
        optimized = original_prompt
        
        # Get tool-specific optimization rules
        optimization_rules = tool_info["optimization_rules"]
        tool_name = tool_info["name"].lower()
        
        # Apply optimizations based on the target tool
        if "copilot" in tool_name:
            optimized = self._optimize_for_copilot(optimized, analysis)
        elif "cursor" in tool_name:
            optimized = self._optimize_for_cursor(optimized, analysis)
        # We can add more tools here later
        
        return optimized
    
    def _optimize_for_copilot(self, prompt, analysis):
        """
        Private method that applies GitHub Copilot-specific optimizations.
        
        Parameters:
        prompt (string): Current prompt
        analysis (dict): Analysis results
        
        Returns:
        string: Prompt optimized for Copilot
        """
        optimized = prompt
        
        # Rule 1: Add programming language if not specified
        if analysis["detected_language"] == "unknown" and analysis["intent"] == "generate":
            # If we're generating code but no language specified, ask for Python (common default)
            optimized = f"Write a Python {optimized.lower()}"
        elif analysis["detected_language"] != "unknown":
            # If language is detected, make sure it's clearly stated at the beginning
            language = analysis["detected_language"]
            if language.lower() not in optimized.lower()[:20]:  # Check first 20 characters
                optimized = f"Write a {language.title()} {optimized.lower()}"
        
        # Rule 2: Add specificity for code generation
        if analysis["intent"] == "generate":
            # Make the request more specific
            if "function" not in optimized.lower() and analysis["complexity_level"] == "medium":
                optimized = optimized.replace("Write a", "Write a detailed function to")
        
        # Rule 3: Request comments if not already mentioned
        if "comment" not in optimized.lower() and analysis["intent"] == "generate":
            optimized += ". Include detailed comments explaining each step."
        
        # Rule 4: Add context request for better code completion
        if analysis["intent"] == "generate" and not analysis["has_code_context"]:
            optimized += " Provide a complete, working example."
        
        return optimized
    
    def _optimize_for_cursor(self, prompt, analysis):
        """
        Private method that applies Cursor-specific optimizations.
        
        Parameters:
        prompt (string): Current prompt
        analysis (dict): Analysis results
        
        Returns:
        string: Prompt optimized for Cursor
        """
        optimized = prompt
        
        # Rule 1: Use more natural, conversational language
        # Replace formal commands with conversational requests
        optimized = optimized.replace("Write a", "I need you to create a")
        optimized = optimized.replace("Create a", "Please help me build a")
        
        # Rule 2: Add file context for editing tasks
        if analysis["intent"] in ["refactor", "debug"] or analysis["has_code_context"]:
            if "file" not in optimized.lower():
                optimized += " Please work with the current file context."
        
        # Rule 3: Be more specific about editing instructions
        if analysis["intent"] == "refactor":
            optimized += " Focus on improving code structure and readability."
        elif analysis["intent"] == "debug":
            optimized += " Identify the specific issue and provide a fix."
        
        # Rule 4: Add collaboration hints (Cursor is good at iterative work)
        if analysis["complexity_level"] == "complex":
            optimized += " Let's work through this step by step."
        
        return optimized
    
    def _generate_explanations(self, original, optimized, analysis, tool_info):
        """
        Private method that explains what changes were made and why.
        
        Parameters:
        original (string): Original prompt
        optimized (string): Optimized prompt
        analysis (dict): Analysis results
        tool_info (dict): Tool information
        
        Returns:
        list: List of explanation strings
        """
        explanations = []
        tool_name = tool_info["name"]
        
        # Check what changes were made and explain them
        
        # Language addition explanation
        if analysis["detected_language"] == "unknown" and "Python" in optimized and "Python" not in original:
            explanations.append(f"Added 'Python' specification because {tool_name} works better with explicit language mentions")
        
        # Comments addition explanation
        if "comment" in optimized.lower() and "comment" not in original.lower():
            explanations.append(f"Added comment request because {tool_name} excels at generating well-documented code")
        
        # Specificity improvements
        if "detailed" in optimized and "detailed" not in original:
            explanations.append(f"Added 'detailed' to make the request more specific, which helps {tool_name} generate better code")
        
        # Complete example request
        if "complete" in optimized and "complete" not in original:
            explanations.append(f"Requested complete example because {tool_name} performs better with full context")
        
        # Conversational language (for Cursor)
        if "I need you to" in optimized or "Please help me" in optimized:
            explanations.append(f"Made language more conversational because {tool_name} responds well to natural dialogue")
        
        # File context addition
        if "file context" in optimized:
            explanations.append(f"Added file context reference because {tool_name} is excellent at working with existing code")
        
        # Step-by-step approach
        if "step by step" in optimized:
            explanations.append(f"Added step-by-step request because {tool_name} handles complex tasks better when broken down")
        
        # If no specific changes detected, provide general explanation
        if not explanations:
            explanations.append(f"Optimized prompt structure and clarity for {tool_name}'s specific capabilities")
        
        return explanations


# Test section
if __name__ == "__main__":
    """
    Test our prompt optimizer with different prompts and tools
    """
    # Create optimizer object
    optimizer = PromptOptimizer()
    
    # Test prompts
    test_cases = [
        {
            "prompt": "Write a function to calculate factorial",
            "tool": "copilot"
        },
        {
            "prompt": "Debug this code",
            "tool": "cursor"
        },
        {
            "prompt": "Create a sorting algorithm",
            "tool": "copilot"
        }
    ]
    
    # Test each case
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*50}")
        print(f"TEST {i}: Optimizing for {test_case['tool'].upper()}")
        print(f"{'='*50}")
        
        result = optimizer.optimize_prompt(test_case["prompt"], test_case["tool"])
        
        if "error" in result:
            print(f"Error: {result['error']}")
            continue
        
        print(f"Original: {result['original_prompt']}")
        print(f"Optimized: {result['optimized_prompt']}")
        print(f"\nAnalysis:")
        print(f"  Intent: {result['analysis']['intent']}")
        print(f"  Language: {result['analysis']['detected_language']}")
        print(f"  Complexity: {result['analysis']['complexity_level']}")
        
        print(f"\nExplanations:")
        for j, explanation in enumerate(result['explanations'], 1):
            print(f"  {j}. {explanation}")
        
        print(f"\nImprovements made: {result['improvements_made']}")
