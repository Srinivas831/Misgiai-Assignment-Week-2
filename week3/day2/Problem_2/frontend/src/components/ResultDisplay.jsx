import React from 'react';
import { MessageSquare, RotateCcw, Copy, Check } from 'lucide-react';

const ResultDisplay = ({ result, imagePreview, onReset }) => {
  const [copied, setCopied] = React.useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(result.answer);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };

  return (
    <div className="space-y-6">
      {/* Question and Image Summary */}
      <div className="bg-gray-50 rounded-lg p-4">
        <div className="flex items-start space-x-4">
          {imagePreview && (
            <div className="flex-shrink-0">
              <img
                src={imagePreview}
                alt="Analyzed image"
                className="w-20 h-20 object-cover rounded-lg border border-gray-200"
              />
            </div>
          )}
          <div className="flex-1">
            <div className="flex items-center space-x-2 mb-2">
              <MessageSquare className="w-4 h-4 text-gray-600" />
              <span className="text-sm font-medium text-gray-600">Your Question:</span>
            </div>
            <p className="text-gray-800 font-medium">{result.question}</p>
          </div>
        </div>
      </div>

      {/* AI Response */}
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <div className="w-6 h-6 bg-primary-600 rounded-full flex items-center justify-center">
              <span className="text-white text-xs font-bold">AI</span>
            </div>
            <span className="font-medium text-gray-800">GPT-4o Analysis:</span>
          </div>
          <button
            onClick={handleCopy}
            className="flex items-center space-x-1 text-sm text-gray-600 hover:text-gray-800 transition-colors duration-200"
            title="Copy to clipboard"
          >
            {copied ? (
              <>
                <Check className="w-4 h-4 text-green-600" />
                <span className="text-green-600">Copied!</span>
              </>
            ) : (
              <>
                <Copy className="w-4 h-4" />
                <span>Copy</span>
              </>
            )}
          </button>
        </div>
        
        <div className="bg-white border border-gray-200 rounded-lg p-4">
          <div className="prose prose-sm max-w-none">
            <p className="text-gray-800 leading-relaxed whitespace-pre-wrap">
              {result.answer}
            </p>
          </div>
        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex items-center justify-center pt-4">
        <button
          onClick={onReset}
          className="btn-secondary flex items-center space-x-2"
        >
          <RotateCcw className="w-4 h-4" />
          <span>Ask Another Question</span>
        </button>
      </div>
    </div>
  );
};

export default ResultDisplay;
