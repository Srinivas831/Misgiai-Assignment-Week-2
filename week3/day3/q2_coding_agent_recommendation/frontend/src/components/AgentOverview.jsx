import React from 'react';
import { motion } from 'framer-motion';
import { Code, Zap, Shield, Users, Target, Award, Sparkles, Eye } from 'lucide-react';

const AgentOverview = ({ agents }) => {
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

  const getAgentColor = (agentName) => {
    const colors = {
      'Copilot': 'from-blue-500 to-blue-600',
      'CodeWhisperer': 'from-orange-500 to-orange-600',
      'Cursor': 'from-purple-500 to-purple-600',
      'Replit': 'from-green-500 to-green-600',
      'Tabnine': 'from-indigo-500 to-indigo-600',
      'Amazon Q': 'from-yellow-500 to-yellow-600',
      'CodeGeeX': 'from-pink-500 to-pink-600'
    };
    return colors[agentName] || 'from-gray-500 to-gray-600';
  };

  return (
    <div className="space-y-6">
      <motion.div
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <div className="flex items-center justify-center space-x-2 mb-4">
          <Eye className="w-6 h-6 text-primary-600" />
          <h2 className="text-2xl font-bold text-gray-800">
            Available AI Coding Agents
          </h2>
        </div>
        <p className="text-gray-600">
          Explore our curated collection of {Object.keys(agents).length} AI coding assistants
        </p>
      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {Object.entries(agents).map(([name, agent], index) => (
          <motion.div
            key={name}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            className="card p-6 hover:scale-105 transition-transform duration-300"
          >
            <div className="space-y-4">
              {/* Agent Header */}
              <div className="flex items-center space-x-3">
                <div className={`p-3 bg-gradient-to-r ${getAgentColor(name)} rounded-xl text-white`}>
                  {getAgentIcon(name)}
                </div>
                <div>
                  <h3 className="text-lg font-bold text-gray-800">{name}</h3>
                  <div className="flex items-center space-x-2 text-xs">
                    <div className={`w-2 h-2 rounded-full ${agent.requires_setup ? 'bg-yellow-400' : 'bg-green-400'}`}></div>
                    <span className="text-gray-600">
                      {agent.requires_setup ? 'Setup Required' : 'Ready to Use'}
                    </span>
                  </div>
                </div>
              </div>

              {/* Languages */}
              <div>
                <h4 className="text-sm font-semibold text-gray-700 mb-2">Languages</h4>
                <div className="flex flex-wrap gap-1">
                  {agent.languages.slice(0, 3).map((lang, idx) => (
                    <span key={idx} className="px-2 py-1 bg-blue-100 text-blue-700 text-xs rounded">
                      {lang}
                    </span>
                  ))}
                  {agent.languages.length > 3 && (
                    <span className="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded">
                      +{agent.languages.length - 3} more
                    </span>
                  )}
                </div>
              </div>

              {/* Top Strengths */}
              <div>
                <h4 className="text-sm font-semibold text-gray-700 mb-2">Key Strengths</h4>
                <div className="space-y-1">
                  {agent.strengths.slice(0, 2).map((strength, idx) => (
                    <div key={idx} className="flex items-center space-x-2">
                      <div className="w-1.5 h-1.5 bg-green-400 rounded-full"></div>
                      <span className="text-xs text-gray-600">{strength}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Features */}
              <div className="flex justify-between items-center pt-2 border-t border-gray-100">
                <div className="flex items-center space-x-4 text-xs">
                  <div className="flex items-center space-x-1">
                    <div className={`w-2 h-2 rounded-full ${agent.offline_support ? 'bg-green-400' : 'bg-red-400'}`}></div>
                    <span className="text-gray-600">
                      {agent.offline_support ? 'Offline' : 'Online'}
                    </span>
                  </div>
                </div>
                <div className="text-xs text-gray-500">
                  {agent.ideal_tasks.length} ideal tasks
                </div>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="text-center text-gray-600 text-sm bg-gray-50 rounded-xl p-4"
      >
        💡 <strong>Tip:</strong> Describe your coding task above to get personalized recommendations from these agents!
      </motion.div>
    </div>
  );
};

export default AgentOverview;
