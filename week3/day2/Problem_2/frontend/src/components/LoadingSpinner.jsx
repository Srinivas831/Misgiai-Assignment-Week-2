import React from 'react';
import { Loader2, Brain } from 'lucide-react';

const LoadingSpinner = () => {
  return (
    <div className="flex flex-col items-center justify-center space-y-4">
      <div className="relative">
        <div className="w-16 h-16 border-4 border-primary-200 rounded-full animate-pulse"></div>
        <div className="absolute inset-0 flex items-center justify-center">
          <Brain className="w-8 h-8 text-primary-600 animate-pulse" />
        </div>
        <Loader2 className="w-6 h-6 text-primary-600 animate-spin absolute -bottom-1 -right-1" />
      </div>
      
      <div className="text-center">
        <h3 className="text-lg font-semibold text-gray-800 mb-2">
          Analyzing your image...
        </h3>
        <div className="space-y-1">
          <p className="text-sm text-gray-600">
            🧠 Processing with GPT-4o Vision
          </p>
          <p className="text-sm text-gray-600">
            ✨ Understanding the visual content
          </p>
          <p className="text-sm text-gray-600">
            💭 Generating intelligent response
          </p>
        </div>
      </div>
      
      <div className="flex space-x-1">
        <div className="w-2 h-2 bg-primary-400 rounded-full animate-bounce" style={{animationDelay: '0ms'}}></div>
        <div className="w-2 h-2 bg-primary-400 rounded-full animate-bounce" style={{animationDelay: '150ms'}}></div>
        <div className="w-2 h-2 bg-primary-400 rounded-full animate-bounce" style={{animationDelay: '300ms'}}></div>
      </div>
    </div>
  );
};

export default LoadingSpinner;
