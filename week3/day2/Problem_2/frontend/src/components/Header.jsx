import React from 'react';
import { Brain, Sparkles } from 'lucide-react';

const Header = () => {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-center">
          <div className="flex items-center space-x-3">
            <div className="relative">
              <Brain className="w-8 h-8 text-primary-600" />
              <Sparkles className="w-4 h-4 text-yellow-500 absolute -top-1 -right-1" />
            </div>
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                Multimodal QA Agent
              </h1>
              <p className="text-gray-600 text-sm">
                Powered by GPT-4o Vision • Ask questions about any image
              </p>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
