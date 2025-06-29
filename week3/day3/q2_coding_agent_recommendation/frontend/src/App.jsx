import React, { useState } from 'react';
import { motion } from 'framer-motion';
import Header from './components/Header';
import TaskInput from './components/TaskInput';
import RecommendationResults from './components/RecommendationResults';
import AgentOverview from './components/AgentOverview';
import LoadingSpinner from './components/LoadingSpinner';
import axios from 'axios';

function App() {
  const [task, setTask] = useState('');
  const [recommendations, setRecommendations] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [allAgents, setAllAgents] = useState(null);

  const fetchRecommendations = async () => {
    if (!task.trim()) {
      setError('Please enter a task description');
      return;
    }

    setLoading(true);
    setError(null);
    setRecommendations(null);

    try {
      const response = await axios.post('http://localhost:5000/recommend', {
        task: task.trim()
      });

      setRecommendations(response.data);
    } catch (err) {
      console.error('Error:', err);
      setError(
        err.response?.data?.error || 
        'Failed to get recommendations. Please make sure the backend is running.'
      );
    } finally {
      setLoading(false);
    }
  };

  const fetchAllAgents = async () => {
    try {
      const response = await axios.get('http://localhost:5000/agents');
      setAllAgents(response.data.agents);
    } catch (err) {
      console.error('Failed to fetch agents:', err);
    }
  };

  const handleReset = () => {
    setTask('');
    setRecommendations(null);
    setError(null);
  };

  // Fetch all agents on component mount
  React.useEffect(() => {
    fetchAllAgents();
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      <Header />
      
      <main className="container mx-auto px-4 py-8 max-w-6xl">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="space-y-8"
        >
          {/* Task Input Section */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="card p-8"
          >
            <TaskInput
              task={task}
              onTaskChange={setTask}
              onSubmit={fetchRecommendations}
              loading={loading}
            />
          </motion.div>

          {/* Loading State */}
          {loading && (
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="card p-8"
            >
              <LoadingSpinner />
            </motion.div>
          )}

          {/* Error Display */}
          {error && (
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              className="card p-6 border-red-200 bg-red-50"
            >
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
            </motion.div>
          )}

          {/* Recommendations Results */}
          {recommendations && (
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.3 }}
            >
              <RecommendationResults
                recommendations={recommendations}
                onReset={handleReset}
              />
            </motion.div>
          )}

          {/* Agent Overview */}
          {allAgents && !recommendations && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.4 }}
            >
              <AgentOverview agents={allAgents} />
            </motion.div>
          )}
        </motion.div>
      </main>
    </div>
  );
}

export default App;
