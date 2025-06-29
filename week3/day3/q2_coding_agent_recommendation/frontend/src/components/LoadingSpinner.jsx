import React from 'react';
import { motion } from 'framer-motion';
import { Brain, Sparkles, Zap } from 'lucide-react';

const LoadingSpinner = () => {
  return (
    <div className="flex flex-col items-center justify-center space-y-6 py-8">
      <motion.div
        className="relative"
        initial={{ opacity: 0, scale: 0 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
      >
        {/* Outer Ring */}
        <motion.div
          className="w-20 h-20 border-4 border-primary-200 rounded-full"
          animate={{ rotate: 360 }}
          transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
        />
        
        {/* Inner Brain */}
        <div className="absolute inset-0 flex items-center justify-center">
          <motion.div
            animate={{ scale: [1, 1.1, 1], rotate: [0, 5, -5, 0] }}
            transition={{ duration: 1.5, repeat: Infinity }}
          >
            <Brain className="w-8 h-8 text-primary-600" />
          </motion.div>
        </div>

        {/* Floating Sparkles */}
        <motion.div
          className="absolute -top-2 -right-2"
          animate={{ 
            y: [-5, -15, -5], 
            opacity: [0.5, 1, 0.5],
            rotate: [0, 180, 360] 
          }}
          transition={{ duration: 2, repeat: Infinity }}
        >
          <Sparkles className="w-5 h-5 text-yellow-500" />
        </motion.div>

        <motion.div
          className="absolute -bottom-1 -left-1"
          animate={{ 
            x: [-3, 3, -3], 
            opacity: [0.3, 1, 0.3],
            scale: [0.8, 1.2, 0.8]
          }}
          transition={{ duration: 1.8, repeat: Infinity, delay: 0.5 }}
        >
          <Zap className="w-4 h-4 text-accent-500" />
        </motion.div>
      </motion.div>
      
      <motion.div
        className="text-center space-y-3"
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
      >
        <h3 className="text-xl font-semibold text-gray-800">
          Analyzing Your Task...
        </h3>
        
        <motion.div 
          className="space-y-2"
          variants={{
            animate: {
              transition: {
                staggerChildren: 0.2
              }
            }
          }}
          initial="initial"
          animate="animate"
        >
          {[
            "🤖 Matching against 7 AI coding agents",
            "⚡ Analyzing task complexity and requirements", 
            "🎯 Calculating compatibility scores",
            "📊 Preparing recommendations"
          ].map((text, index) => (
            <motion.p
              key={index}
              className="text-sm text-gray-600"
              variants={{
                initial: { opacity: 0, x: -20 },
                animate: { opacity: 1, x: 0 }
              }}
              transition={{ delay: index * 0.3 }}
            >
              {text}
            </motion.p>
          ))}
        </motion.div>
      </motion.div>
      
      {/* Animated Dots */}
      <div className="flex space-x-2">
        {[0, 1, 2].map((index) => (
          <motion.div
            key={index}
            className="w-3 h-3 bg-primary-400 rounded-full"
            animate={{
              scale: [1, 1.5, 1],
              opacity: [0.5, 1, 0.5]
            }}
            transition={{
              duration: 1.5,
              repeat: Infinity,
              delay: index * 0.2
            }}
          />
        ))}
      </div>
    </div>
  );
};

export default LoadingSpinner;
