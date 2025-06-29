import React from 'react';
import { motion } from 'framer-motion';
import { Sparkles, Award, RefreshCw, Target, Code, Zap, Shield, Users } from 'lucide-react';

const RecommendationResults = ({ recommendations, onReset }) => {
  const { task, recommendations: agents, total_agents } = recommendations;

  const getAgentIcon = (agentName) => {
    const icons = {
      'Copilot': <Code className="w-6 h-6" />,
      'CodeWhisperer': <Zap className="w-6 h-6" />,
      'Cursor': <Target className="w-6 h-6" />,
      'Replit': <Users className="w-6 h-6" />,
      'Tabnine': <Shield className="w-6 h-6" />,
      'Amazon Q': <Award className="w-6 h-6" />,
      'CodeGeeX': <Sparkles className="w-6 h-6" />
    };
    return icons[agentName] || <Code className="w-6 h-6" />;
  };

  const getScoreColor = (score) => {
    if (score >= 6) return 'text-green-600 bg-green-100';
    if (score >= 3) return 'text-yellow-600 bg-yellow-100';
    return 'text-red-600 bg-red-100';
  };

  const getMatchLevel = (score) => {
    if (score >= 6) return { level: 'Excellent Match', color: 'text-green-600' };
    if (score >= 3) return { level: 'Good Match', color: 'text-yellow-600' };
    return { level: 'Partial Match', color: 'text-red-600' };
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <div className="flex items-center justify-center space-x-2 mb-4">
          <Award className="w-8 h-8 text-primary-600" />
          <h2 className="text-3xl font-bold text-gray-800">
            Recommended AI Coding Agents
          </h2>
        </div>
        <div className="bg-gray-50 rounded-xl p-4 mb-6">
          <p className="text-gray-600 mb-2">
            <span className="font-medium">Your Task:</span> {task}
          </p>
          <p className="text-sm text-gray-500">
            Analyzed against {total_agents} available coding agents
          </p>
        </div>
      </motion.div>

      {/* Recommendations */}
      <div className="grid gap-6">
        {agents.map((agent, index) => {
          const matchInfo = getMatchLevel(agent.score);
          
          return (
            <motion.div
              key={agent.name}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className={`card p-6 relative overflow-hidden ${
                index === 0 ? 'ring-2 ring-primary-200 bg-gradient-to-br from-primary-50 to-white' : ''
              }`}
            >
              {/* Rank Badge */}
              <div className="absolute top-4 right-4">
                <div className={`px-3 py-1 rounded-full text-sm font-bold ${
                  index === 0 ? 'bg-gold-100 text-gold-600' :
                  index === 1 ? 'bg-gray-100 text-gray-600' :
                  'bg-orange-100 text-orange-600'
                }`}>
                  #{index + 1}
                </div>
              </div>

              {/* Best Match Badge */}
              {index === 0 && (
                <motion.div
                  initial={{ scale: 0, rotate: -180 }}
                  animate={{ scale: 1, rotate: 0 }}
                  transition={{ delay: 0.5, type: "spring" }}
                  className="absolute top-0 left-0 bg-gradient-to-r from-primary-500 to-accent-500 text-white px-4 py-2 text-sm font-bold"
                  style={{ clipPath: 'polygon(0 0, 100% 0, 85% 100%, 0% 100%)' }}
                >
                  🏆 BEST MATCH
                </motion.div>
              )}

              <div className="space-y-4 mt-4">
                {/* Agent Header */}
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-4">
                    <div className="p-3 bg-primary-100 rounded-xl text-primary-600">
                      {getAgentIcon(agent.name)}
                    </div>
                    <div>
                      <h3 className="text-2xl font-bold text-gray-800">{agent.name}</h3>
                      <div className="flex items-center space-x-3">
                        <span className={`text-sm font-medium ${matchInfo.color}`}>
                          {matchInfo.level}
                        </span>
                        <div className={`px-2 py-1 rounded-full text-xs font-bold ${getScoreColor(agent.score)}`}>
                          Score: {agent.score}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Match Explanations */}
                <div className="bg-gray-50 rounded-xl p-4">
                  <h4 className="font-semibold text-gray-800 mb-3 flex items-center">
                    <Sparkles className="w-4 h-4 mr-2 text-primary-600" />
                    Why this agent matches your task:
                  </h4>
                  <div className="space-y-2">
                    {agent.explanation.length > 0 ? (
                      agent.explanation.map((reason, idx) => (
                        <motion.div
                          key={idx}
                          initial={{ opacity: 0, x: -10 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: index * 0.1 + idx * 0.1 }}
                          className="flex items-start space-x-2"
                        >
                          <span className="text-sm text-gray-700">{reason}</span>
                        </motion.div>
                      ))
                    ) : (
                      <p className="text-sm text-gray-600">General purpose coding agent</p>
                    )}
                  </div>
                </div>

                {/* Agent Details */}
                <div className="grid md:grid-cols-2 gap-4">
                  <div className="space-y-3">
                    <div>
                      <h5 className="text-sm font-semibold text-gray-700 mb-2">Languages</h5>
                      <div className="flex flex-wrap gap-2">
                        {agent.agent_info.languages.map((lang, idx) => (
                          <span key={idx} className="px-2 py-1 bg-blue-100 text-blue-700 text-xs rounded-lg">
                            {lang}
                          </span>
                        ))}
                      </div>
                    </div>
                    
                    <div>
                      <h5 className="text-sm font-semibold text-gray-700 mb-2">Strengths</h5>
                      <div className="flex flex-wrap gap-2">
                        {agent.agent_info.strengths.map((strength, idx) => (
                          <span key={idx} className="px-2 py-1 bg-green-100 text-green-700 text-xs rounded-lg">
                            {strength}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>

                  <div className="space-y-3">
                    <div>
                      <h5 className="text-sm font-semibold text-gray-700 mb-2">Features</h5>
                      <div className="space-y-1 text-xs">
                        <div className="flex items-center space-x-2">
                          <div className={`w-2 h-2 rounded-full ${agent.agent_info.requires_setup ? 'bg-yellow-400' : 'bg-green-400'}`}></div>
                          <span className="text-gray-600">
                            {agent.agent_info.requires_setup ? 'Setup Required' : 'No Setup Needed'}
                          </span>
                        </div>
                        <div className="flex items-center space-x-2">
                          <div className={`w-2 h-2 rounded-full ${agent.agent_info.offline_support ? 'bg-green-400' : 'bg-red-400'}`}></div>
                          <span className="text-gray-600">
                            {agent.agent_info.offline_support ? 'Offline Support' : 'Online Only'}
                          </span>
                        </div>
                      </div>
                    </div>

                    {agent.agent_info.weaknesses.length > 0 && (
                      <div>
                        <h5 className="text-sm font-semibold text-gray-700 mb-2">Considerations</h5>
                        <div className="flex flex-wrap gap-2">
                          {agent.agent_info.weaknesses.map((weakness, idx) => (
                            <span key={idx} className="px-2 py-1 bg-orange-100 text-orange-700 text-xs rounded-lg">
                              {weakness}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            </motion.div>
          );
        })}
      </div>

      {/* Action Buttons */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
        className="flex justify-center pt-6"
      >
        <button
          onClick={onReset}
          className="btn-secondary flex items-center space-x-2"
        >
          <RefreshCw className="w-4 h-4" />
          <span>Try Another Task</span>
        </button>
      </motion.div>
    </div>
  );
};

export default RecommendationResults;
