import React, { useState } from 'react';
import ImageUploader from './components/ImageUploader';
import QuestionForm from './components/QuestionForm';
import ResultDisplay from './components/ResultDisplay';
import Header from './components/Header';
import LoadingSpinner from './components/LoadingSpinner';
import axios from 'axios';

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [question, setQuestion] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleImageSelect = (file) => {
    setSelectedImage(file);
    setError(null);
    setResult(null);
    
    // Create preview URL
    const reader = new FileReader();
    reader.onloadend = () => {
      setImagePreview(reader.result);
    };
    reader.readAsDataURL(file);
  };

  const handleQuestionChange = (newQuestion) => {
    setQuestion(newQuestion);
  };

  const handleSubmit = async () => {
    if (!selectedImage || !question.trim()) {
      setError('Please upload an image and enter a question.');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const formData = new FormData();
      formData.append('image', selectedImage);
      
      // For now, we'll send the question as a separate field
      // You might need to adjust this based on your backend API
      const response = await axios.post('http://localhost:5000/api/analyze', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        params: {
          question: question
        }
      });

      if (response.data.success) {
        setResult({
          answer: response.data.answer,
          question: response.data.question || question
        });
      } else {
        setError(response.data.error || 'An error occurred while analyzing the image.');
      }
    } catch (err) {
      console.error('Error:', err);
      setError(err.response?.data?.error || 'Failed to connect to the server. Please make sure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setSelectedImage(null);
    setImagePreview(null);
    setQuestion('');
    setResult(null);
    setError(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      <Header />
      
      <main className="container mx-auto px-4 py-8 max-w-4xl">
        <div className="space-y-8">
          {/* Image Upload Section */}
          <div className="card p-6 animate-fade-in">
            <h2 className="text-2xl font-bold text-gray-800 mb-4 flex items-center">
              <span className="bg-primary-100 text-primary-600 rounded-full w-8 h-8 flex items-center justify-center text-sm font-bold mr-3">1</span>
              Upload an Image
            </h2>
            <ImageUploader 
              onImageSelect={handleImageSelect}
              imagePreview={imagePreview}
            />
          </div>

          {/* Question Input Section */}
          <div className="card p-6 animate-fade-in">
            <h2 className="text-2xl font-bold text-gray-800 mb-4 flex items-center">
              <span className="bg-primary-100 text-primary-600 rounded-full w-8 h-8 flex items-center justify-center text-sm font-bold mr-3">2</span>
              Ask a Question
            </h2>
            <QuestionForm 
              question={question}
              onQuestionChange={handleQuestionChange}
              onSubmit={handleSubmit}
              disabled={!selectedImage || loading}
            />
          </div>

          {/* Loading State */}
          {loading && (
            <div className="card p-8 animate-fade-in">
              <LoadingSpinner />
            </div>
          )}

          {/* Error Display */}
          {error && (
            <div className="card p-6 animate-fade-in border-red-200 bg-red-50">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <svg className="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div className="ml-3">
                  <h3 className="text-sm font-medium text-red-800">Error</h3>
                  <p className="text-sm text-red-700 mt-1">{error}</p>
                </div>
              </div>
            </div>
          )}

          {/* Results Section */}
          {result && (
            <div className="card p-6 animate-slide-up">
              <h2 className="text-2xl font-bold text-gray-800 mb-4 flex items-center">
                <span className="bg-green-100 text-green-600 rounded-full w-8 h-8 flex items-center justify-center text-sm font-bold mr-3">✓</span>
                Analysis Result
              </h2>
              <ResultDisplay 
                result={result}
                imagePreview={imagePreview}
                onReset={handleReset}
              />
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
