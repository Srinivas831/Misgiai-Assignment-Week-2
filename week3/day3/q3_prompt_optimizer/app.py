# app.py
# Web application for the Adaptive Prompt Optimizer
# This creates a simple web interface where users can input prompts and get optimized versions

from flask import Flask, render_template, request, jsonify  # Flask web framework
from prompt_optimizer import PromptOptimizer  # Our core optimizer
from tool_knowledge import ToolKnowledge  # Tool knowledge base

# Create Flask application instance
app = Flask(__name__)

# Create our optimizer and tool knowledge instances
optimizer = PromptOptimizer()  # Main optimization engine
tool_knowledge = ToolKnowledge()  # Tool information database

@app.route('/')
def home():
    """
    Home page route - displays the main interface
    This function runs when someone visits the website's main page
    
    Returns:
    HTML template: The main page with input forms
    """
    # Get list of all supported tools for the dropdown menu
    available_tools = tool_knowledge.get_all_tools()
    
    # Render the HTML template and pass the tools list to it
    return render_template('index.html', tools=available_tools)

@app.route('/optimize', methods=['POST'])
def optimize():
    """
    Optimization route - handles the prompt optimization request
    This function runs when the user submits the form
    
    Returns:
    JSON response: Optimization results or error message
    """
    try:
        # Get data from the form submission
        data = request.get_json()  # Get JSON data from the request
        
        # Extract the prompt and tool from the submitted data
        original_prompt = data.get('prompt', '').strip()  # User's input prompt
        target_tool = data.get('tool', '').lower()  # Selected tool
        
        # Validate input - make sure both fields are provided
        if not original_prompt:
            return jsonify({
                'error': 'Please provide a prompt to optimize',
                'success': False
            })
        
        if not target_tool:
            return jsonify({
                'error': 'Please select a target tool',
                'success': False
            })
        
        # Perform the optimization using our optimizer
        result = optimizer.optimize_prompt(original_prompt, target_tool)
        
        # Check if optimization was successful
        if 'error' in result:
            return jsonify({
                'error': result['error'],
                'success': False,
                'supported_tools': result.get('supported_tools', [])
            })
        
        # Return successful optimization results
        return jsonify({
            'success': True,
            'original_prompt': result['original_prompt'],
            'optimized_prompt': result['optimized_prompt'],
            'target_tool': result['target_tool'],
            'analysis': result['analysis'],
            'explanations': result['explanations'],
            'improvements_made': result['improvements_made']
        })
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'success': False
        })

@app.route('/tools')
def get_tools():
    """
    Tools information route - provides details about supported tools
    This can be used to show tool capabilities to users
    
    Returns:
    JSON response: Information about all supported tools
    """
    try:
        # Get all tool names
        tool_names = tool_knowledge.get_all_tools()
        
        # Get detailed information for each tool
        tools_info = {}
        for tool_name in tool_names:
            tool_info = tool_knowledge.get_tool_info(tool_name)
            if tool_info:
                tools_info[tool_name] = {
                    'name': tool_info['name'],
                    'description': tool_info['description'],
                    'strengths': tool_info['strengths']
                }
        
        return jsonify({
            'success': True,
            'tools': tools_info
        })
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'success': False
        })

# Run the application
if __name__ == '__main__':
    """
    This runs when we execute this file directly
    It starts the web server so users can access our application
    """
    print("Starting Adaptive Prompt Optimizer...")
    print("Available tools:", tool_knowledge.get_all_tools())
    print("Opening web interface at: http://localhost:5000")
    
    # Start the Flask development server
    # debug=True means the server will restart automatically when we make changes
    app.run(debug=True, host='0.0.0.0', port=5000)