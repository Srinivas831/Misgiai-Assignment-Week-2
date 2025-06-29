import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Send, Lightbulb, Wand2 } from 'lucide-react';

const TaskInput = ({ task, onTaskChange, onSubmit, loading }) => {
  const [focused, setFocused] = useState(false);

  const exampleTasks = [
    "Build a React dashboard with charts and data visualization",
    "Create a Python web scraper for e-commerce websites",
    "Develop a REST API with authentication using Node.js",
    "Write unit tests for my TypeScript React components",
    "Build a machine learning model for image classification",
    "Create AWS Lambda functions for serverless backend",
    "Develop a mobile app with React Native",
    "Build a CLI tool in Go for file processing"
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    if (task.trim() && !loading) {
      onSubmit();
    }
  };

  const handleExampleClick = (exampleTask) => {
    onTaskChange(exampleTask);
  };

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          className="flex items-center justify-center space-x-2 mb-4"
        >
          <Wand2 className="w-6 h-6 text-primary-600" />
          <h2 className="text-2xl font-bold text-gray-800">
            Describe Your Coding Task
          </h2>
        </motion.div>
        <p className="text-gray-600">
          Tell us what you want to build, and we'll recommend the best AI coding agents for the job
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="relative">
          <motion.textarea
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            value={task}
            onChange={(e) => onTaskChange(e.target.value)}
            onFocus={() => setFocused(true)}
            onBlur={() => setFocused(false)}
            placeholder="e.g., Build a React dashboard with real-time data visualization and user authentication..."
            rows={4}
            className={`input-field resize-none pr-16 text-lg transition-all duration-300 ${
              focused ? 'ring-4 ring-primary-200 border-primary-500 shadow-lg' : ''
            }`}
            disabled={loading}
          />
          <motion.button
            type="submit"
            disabled={loading || !task.trim()}
            className="absolute bottom-4 right-4 btn-primary p-3 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <Send className="w-5 h-5" />
          </motion.button>
        </div>
      </form>

      {/* Example Tasks */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="space-y-4"
      >
        <div className="flex items-center space-x-2 text-sm text-gray-600">
          <Lightbulb className="w-5 h-5 text-yellow-500" />
          <span className="font-medium">Try these example tasks:</span>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {exampleTasks.map((exampleTask, index) => (
            <motion.button
              key={index}
              onClick={() => handleExampleClick(exampleTask)}
              disabled={loading}
              className="text-left p-4 text-sm bg-gray-50 hover:bg-primary-50 rounded-xl border-2 border-gray-100 hover:border-primary-200 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed group"
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.1 * index }}
            >
              <div className="flex items-start space-x-3">
                <div className="w-2 h-2 bg-primary-400 rounded-full mt-2 group-hover:bg-primary-600 transition-colors"></div>
                <span className="text-gray-700 group-hover:text-primary-700 transition-colors">
                  {exampleTask}
                </span>
              </div>
            </motion.button>
          ))}
        </div>
      </motion.div>
    </div>
  );
};

export default TaskInput;
