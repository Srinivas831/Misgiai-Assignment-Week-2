# agents_data.py

agents = {
    "Copilot": {
        "languages": ["Python", "JavaScript", "TypeScript", "Go", "Ruby"],
        "strengths": ["autocomplete", "frontend", "test writing", "VS Code integration"],
        "weaknesses": ["not great with big architectural planning"],
        "ideal_tasks": ["build React UI", "add unit tests", "auto-complete"],
        "requires_setup": True,
        "offline_support": False
    },
    "CodeWhisperer": {
        "languages": ["Java", "Python", "JavaScript"],
        "strengths": ["AWS integration", "backend services", "security suggestions"],
        "weaknesses": ["less polished UI help", "limited outside AWS ecosystem"],
        "ideal_tasks": ["AWS Lambda", "API handler", "IAM config"],
        "requires_setup": False,
        "offline_support": False
    },
    "Cursor": {
        "languages": ["Python", "JavaScript", "TypeScript"],
        "strengths": ["in-context awareness", "code explanation", "refactoring"],
        "weaknesses": ["requires Cursor IDE", "new in market"],
        "ideal_tasks": ["explain code", "refactor functions", "edit long files"],
        "requires_setup": True,
        "offline_support": False
    },
    "Replit": {
        "languages": ["Python", "JavaScript", "C++", "Java"],
        "strengths": ["instant dev environment", "multiplayer coding", "education"],
        "weaknesses": ["less fine-grained suggestions", "less control"],
        "ideal_tasks": ["build quick prototypes", "try snippets", "learn coding"],
        "requires_setup": False,
        "offline_support": True
    },
    "Tabnine": {
        "languages": ["Python", "JavaScript", "Java", "C#", "C++", "TypeScript"],
        "strengths": ["local inference", "privacy-friendly", "fast autocomplete"],
        "weaknesses": ["not good at multi-line completions", "no high-level reasoning"],
        "ideal_tasks": ["auto-complete small blocks", "offline use", "secure environments"],
        "requires_setup": True,
        "offline_support": True
    },
    "Amazon Q": {
        "languages": ["Java", "Python", "JavaScript", "TypeScript"],
        "strengths": ["enterprise context", "secure answers", "AWS-focused tasks"],
        "weaknesses": ["AWS ecosystem specific", "limited general dev UX"],
        "ideal_tasks": ["analyze AWS stack", "suggest AWS solutions", "write backend"],
        "requires_setup": False,
        "offline_support": False
    },
    "CodeGeeX": {
        "languages": ["Python", "Java", "C++", "JavaScript"],
        "strengths": ["multilingual dev", "open-source friendly", "offline option"],
        "weaknesses": ["not as refined UI", "basic suggestions only"],
        "ideal_tasks": ["code completion", "general tasks in multiple languages"],
        "requires_setup": False,
        "offline_support": True
    }
}
