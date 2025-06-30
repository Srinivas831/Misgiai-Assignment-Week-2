# prompt_analyzer.py
# This file analyzes user prompts to understand their intent, complexity, and requirements

import re  # Regular expressions - helps us find patterns in text

class PromptAnalyzer:
    """
    This class analyzes user prompts to understand:
    1. What the user wants to do (intent)
    2. How complex the request is
    3. What programming language they might be using
    4. What specific requirements they have
    """
    
    def __init__(self):
        """
        Constructor - sets up our analyzer with predefined patterns and keywords
        """
        # Intent categories - what users typically want to do
        self.intent_keywords = {
            # Code Generation - user wants to create new code
            "generate": ["write", "create", "generate", "build", "make", "implement", "develop"],
            
            # Code Debugging - user has a problem to fix
            "debug": ["debug", "fix", "error", "bug", "issue", "problem", "troubleshoot"],
            
            # Code Explanation - user wants to understand code
            "explain": ["explain", "understand", "how does", "what is", "describe", "clarify"],
            
            # Code Refactoring - user wants to improve existing code
            "refactor": ["refactor", "improve", "optimize", "clean", "reorganize", "restructure"],
            
            # Code Review - user wants feedback on code
            "review": ["review", "check", "analyze", "evaluate", "assess", "feedback"]
        }
        
        # Programming languages - helps us detect what language they're working with
        self.language_keywords = {
            "python": ["python", "py", "def", "import", "pip", "pandas", "numpy"],
            "javascript": ["javascript", "js", "node", "npm", "react", "vue", "angular"],
            "java": ["java", "class", "public static", "maven", "spring"],
            "cpp": ["c++", "cpp", "include", "std::", "vector", "cout"],
            "csharp": ["c#", "csharp", "using", "namespace", "public class"],
            "html": ["html", "div", "span", "body", "head", "css"],
            "css": ["css", "style", "color", "background", "margin", "padding"],
            "sql": ["sql", "select", "from", "where", "join", "database"]
        }
        
        # Complexity indicators - words that suggest how complex the task is
        self.complexity_indicators = {
            # Simple tasks
            "simple": ["simple", "basic", "easy", "quick", "small", "short"],
            
            # Medium complexity tasks
            "medium": ["function", "class", "method", "feature", "component"],
            
            # Complex tasks  
            "complex": ["system", "application", "framework", "architecture", "complex", 
                       "advanced", "multiple", "integrate", "scalable"]
        }
    
    def analyze_prompt(self, prompt):
        """
        Main method that analyzes the entire prompt and returns comprehensive analysis.
        
        Parameters:
        prompt (string): The user's input prompt to analyze
        
        Returns:
        dictionary: Complete analysis results
        """
        # Convert prompt to lowercase for easier analysis
        prompt_lower = prompt.lower()
        
        # Perform different types of analysis
        intent = self._detect_intent(prompt_lower)
        language = self._detect_language(prompt_lower)
        complexity = self._assess_complexity(prompt_lower)
        requirements = self._extract_requirements(prompt)
        
        # Return all analysis results as a dictionary
        return {
            "original_prompt": prompt,  # Keep the original prompt
            "intent": intent,  # What the user wants to do
            "detected_language": language,  # Programming language detected
            "complexity_level": complexity,  # How complex the task is
            "requirements": requirements,  # Specific requirements found
            "word_count": len(prompt.split()),  # How many words in the prompt
            "has_code_context": self._has_code_context(prompt)  # Does prompt include code?
        }
    
    def _detect_intent(self, prompt_lower):
        """
        Private method to detect what the user wants to do.
        
        Parameters:
        prompt_lower (string): Lowercase version of the prompt
        
        Returns:
        string: The detected intent category
        """
        # Count how many keywords from each intent category appear in the prompt
        intent_scores = {}
        
        # Check each intent category
        for intent_type, keywords in self.intent_keywords.items():
            score = 0  # Start with score of 0
            
            # Count how many keywords from this category are in the prompt
            for keyword in keywords:
                if keyword in prompt_lower:
                    score += 1  # Add 1 for each keyword found
            
            intent_scores[intent_type] = score  # Store the score
        
        # Find the intent with the highest score
        if max(intent_scores.values()) > 0:  # If we found any keywords
            return max(intent_scores, key=intent_scores.get)  # Return highest scoring intent
        else:
            return "generate"  # Default to "generate" if no clear intent
    
    def _detect_language(self, prompt_lower):
        """
        Private method to detect programming language mentioned in the prompt.
        
        Parameters:
        prompt_lower (string): Lowercase version of the prompt
        
        Returns:
        string: Detected programming language or "unknown"
        """
        # Check each programming language
        for language, keywords in self.language_keywords.items():
            # If any keyword for this language is in the prompt
            for keyword in keywords:
                if keyword in prompt_lower:
                    return language  # Return the first language we find
        
        return "unknown"  # No specific language detected
    
    def _assess_complexity(self, prompt_lower):
        """
        Private method to assess how complex the user's request is.
        
        Parameters:
        prompt_lower (string): Lowercase version of the prompt
        
        Returns:
        string: Complexity level (simple, medium, complex)
        """
        # Count complexity indicators
        complexity_scores = {}
        
        for complexity_level, keywords in self.complexity_indicators.items():
            score = 0
            for keyword in keywords:
                if keyword in prompt_lower:
                    score += 1
            complexity_scores[complexity_level] = score
        
        # Determine complexity based on scores and prompt length
        word_count = len(prompt_lower.split())
        
        # If prompt is very short, it's probably simple
        if word_count < 5:
            return "simple"
        
        # If we have complexity indicators, use them
        if max(complexity_scores.values()) > 0:
            return max(complexity_scores, key=complexity_scores.get)
        
        # Otherwise, judge by length
        if word_count < 10:
            return "simple"
        elif word_count < 20:
            return "medium"
        else:
            return "complex"
    
    def _extract_requirements(self, prompt):
        """
        Private method to extract specific requirements from the prompt.
        
        Parameters:
        prompt (string): Original prompt (keeping case)
        
        Returns:
        list: List of specific requirements found
        """
        requirements = []
        prompt_lower = prompt.lower()
        
        # Check for specific requirement patterns
        
        # Comments requirement
        if any(word in prompt_lower for word in ["comment", "comments", "documented"]):
            requirements.append("Include comments in code")
        
        # Error handling requirement
        if any(word in prompt_lower for word in ["error", "exception", "try", "catch"]):
            requirements.append("Include error handling")
        
        # Testing requirement
        if any(word in prompt_lower for word in ["test", "testing", "unit test"]):
            requirements.append("Include tests")
        
        # Performance requirement
        if any(word in prompt_lower for word in ["fast", "efficient", "optimize", "performance"]):
            requirements.append("Focus on performance")
        
        # Documentation requirement
        if any(word in prompt_lower for word in ["document", "documentation", "readme"]):
            requirements.append("Include documentation")
        
        return requirements
    
    def _has_code_context(self, prompt):
        """
        Private method to check if the prompt already contains code examples.
        
        Parameters:
        prompt (string): Original prompt
        
        Returns:
        boolean: True if code context is present, False otherwise
        """
        # Look for common code patterns
        code_patterns = [
            r'def\s+\w+',  # Python function definition
            r'function\s+\w+',  # JavaScript function
            r'class\s+\w+',  # Class definition
            r'import\s+\w+',  # Import statement
            r'#include',  # C++ include
            r'<.*>',  # HTML tags or C++ includes
            r'\{.*\}',  # Code blocks with braces
            r'```'  # Markdown code blocks
        ]
        
        # Check if any code pattern is found
        for pattern in code_patterns:
            if re.search(pattern, prompt):
                return True
        
        return False


# Test section
if __name__ == "__main__":
    """
    Test our prompt analyzer with different types of prompts
    """
    # Create analyzer object
    analyzer = PromptAnalyzer()
    
    # Test prompts
    test_prompts = [
        "Write a Python function to calculate factorial",
        "Debug this JavaScript code that has an error",
        "Explain how this complex sorting algorithm works",
        "Create a simple HTML page with CSS styling"
    ]
    
    # Analyze each test prompt
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n--- Test {i} ---")
        print(f"Prompt: {prompt}")
        
        result = analyzer.analyze_prompt(prompt)
        
        print(f"Intent: {result['intent']}")
        print(f"Language: {result['detected_language']}")
        print(f"Complexity: {result['complexity_level']}")
        print(f"Requirements: {result['requirements']}")
        print(f"Word count: {result['word_count']}")
        print(f"Has code context: {result['has_code_context']}")
