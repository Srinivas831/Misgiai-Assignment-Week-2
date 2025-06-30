# tool_knowledge.py
# This file contains the knowledge base about different AI coding tools
# and their specific optimization strategies

class ToolKnowledge:
    """
    This class stores information about AI coding tools and how to optimize prompts for them.
    Think of this as our "manual" or "guidebook" for each tool.
    """
    
    def __init__(self):
        """
        Constructor method - this runs when we create a new ToolKnowledge object.
        It initializes (sets up) our knowledge base with tool information.
        """
        # This is a dictionary (like a real dictionary with word definitions)
        # Key = tool name, Value = information about that tool
        self.tools_data = {
            
            # GitHub Copilot - Popular AI coding assistant by Microsoft/GitHub
            "copilot": {
                "name": "GitHub Copilot",  # Full name of the tool
                "description": "AI pair programmer that suggests code completions",  # What it does
                
                # These are the "rules" we follow to make prompts better for Copilot
                "optimization_rules": [
                    "Be specific and clear about what you want",  # Rule 1
                    "Include programming language in the prompt",  # Rule 2
                    "Add context about the function/class purpose",  # Rule 3
                    "Request comments in code for better understanding"  # Rule 4
                ],
                
                # These are strengths - what Copilot is really good at
                "strengths": [
                    "Code completion and suggestions",
                    "Understanding context from existing code", 
                    "Generating functions with proper syntax",
                    "Adding helpful comments"
                ],
                
                # Keywords that work well with this tool
                "preferred_keywords": [
                    "function", "class", "method", "implement", "create",
                    "write", "generate", "with comments", "step by step"
                ]
            },
            
            # Cursor - AI-first code editor
            "cursor": {
                "name": "Cursor",
                "description": "AI-first code editor with natural language editing",
                
                "optimization_rules": [
                    "Use natural, conversational language",  # Cursor likes human-like prompts
                    "Specify file context and project structure",  # It's good with file operations
                    "Include refactoring and editing instructions",  # Great for code changes
                    "Mention specific lines or sections to modify"  # Very precise editing
                ],
                
                "strengths": [
                    "Natural language code editing",
                    "File and project manipulation", 
                    "Code refactoring and improvements",
                    "Multi-file operations"
                ],
                
                "preferred_keywords": [
                    "edit", "modify", "refactor", "update", "change",
                    "in file", "at line", "replace", "improve"
                ]
            }
            
            # We'll add more tools later step by step
        }
    
    def get_tool_info(self, tool_name):
        """
        This method gets information about a specific tool.
        
        Parameters:
        tool_name (string): The name of the tool we want info about
        
        Returns:
        dictionary: All the information about that tool, or None if tool not found
        """
        # Convert to lowercase to handle different typing (Copilot, COPILOT, copilot)
        tool_name = tool_name.lower()
        
        # Check if the tool exists in our knowledge base
        if tool_name in self.tools_data:
            return self.tools_data[tool_name]  # Return the tool info
        else:
            return None  # Return None if tool not found
    
    def get_all_tools(self):
        """
        This method returns a list of all tools we support.
        
        Returns:
        list: Names of all supported tools
        """
        # Get all the keys (tool names) from our tools_data dictionary
        return list(self.tools_data.keys())
    
    def get_optimization_rules(self, tool_name):
        """
        This method gets just the optimization rules for a specific tool.
        
        Parameters:
        tool_name (string): The tool we want rules for
        
        Returns:
        list: List of optimization rules, or empty list if tool not found
        """
        tool_info = self.get_tool_info(tool_name)  # Get the tool info first
        
        if tool_info:
            return tool_info["optimization_rules"]  # Return just the rules
        else:
            return []  # Return empty list if tool not found


# Test section - this runs only when we run this file directly
if __name__ == "__main__":
    """
    This is a test section that runs when we execute this file directly.
    It helps us verify our code works correctly.
    """
    # Create a new ToolKnowledge object
    tk = ToolKnowledge()
    
    # Test: Get all available tools
    print("Available tools:", tk.get_all_tools())
    
    # Test: Get info about Copilot
    copilot_info = tk.get_tool_info("copilot")
    print("\nCopilot info:", copilot_info)
    
    # Test: Get optimization rules for Cursor
    cursor_rules = tk.get_optimization_rules("cursor")
    print("\nCursor rules:", cursor_rules)
