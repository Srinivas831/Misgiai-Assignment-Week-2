import React, { useState } from 'react';
import { Send, Lightbulb } from 'lucide-react';

const QuestionForm = ({ question, onQuestionChange, onSubmit, disabled }) => {
  const [focused, setFocused] = useState(false);

  const exampleQuestions = [
    "What do you see in this image?",
    "Describe the main objects and their colors",
    "What is the mood or atmosphere of this image?",
    "Count the number of people in the image",
    "What text can you read in this image?",
    "What's happening in this scene?"
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    if (question.trim() && !disabled) {
      onSubmit();
    }
  };

  const handleExampleClick = (exampleQuestion) => {
    onQuestionChange(exampleQuestion);
  };

  return (
    <div className="space-y-4">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="relative">
          <textarea
            value={question}
            onChange={(e) => onQuestionChange(e.target.value)}
            onFocus={() => setFocused(true)}
            onBlur={() => setFocused(false)}
            placeholder="Ask a question about the image..."
            rows={3}
            className={`input-field resize-none pr-12 transition-all duration-200 ${
              focused ? 'ring-2 ring-primary-500 border-transparent' : ''
            }`}
            disabled={disabled}
          />
          <button
            type="submit"
            disabled={disabled || !question.trim()}
            className="absolute bottom-3 right-3 btn-primary p-2 rounded-lg disabled:opacity-50"
          >
            <Send className="w-4 h-4" />
          </button>
        </div>
      </form>

      {/* Example Questions */}
      <div className="space-y-3">
        <div className="flex items-center space-x-2 text-sm text-gray-600">
          <Lightbulb className="w-4 h-4" />
          <span>Try these example questions:</span>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
          {exampleQuestions.map((exampleQuestion, index) => (
            <button
              key={index}
              onClick={() => handleExampleClick(exampleQuestion)}
              disabled={disabled}
              className="text-left p-3 text-sm bg-gray-50 hover:bg-gray-100 rounded-lg border border-gray-200 transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              "{exampleQuestion}"
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default QuestionForm;
