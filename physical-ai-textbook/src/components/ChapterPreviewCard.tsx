
import React from 'react';
import { motion } from 'framer-motion';
import Link from '@docusaurus/Link';

interface ChapterPreviewCardProps {
  title: string;
  description: string;
  to: string;
}

const ChapterPreviewCard: React.FC<ChapterPreviewCardProps> = ({
  title,
  description,
  to,
}) => {
  return (
    <motion.div
      whileHover={{ scale: 1.03, boxShadow: '0 8px 16px rgba(0, 0, 0, 0.2)' }}
      transition={{ type: 'spring', stiffness: 400, damping: 10 }}
      className="card-glassmorphism p-6 rounded-lg shadow-lg flex flex-col justify-between h-full"
    >
      <Link to={to} className="no-underline hover:no-underline">
        <h3 className="text-xl font-bold mb-2 custom-gradient-text">{title}</h3>
        <p className="text-gray-700 dark:text-gray-300 flex-grow">{description}</p>
      </Link>
      <div className="mt-4">
        <Link
          to={to}
          className="button button--primary button--sm !bg-gradient-to-r from-purple-700 to-cyan-500 text-white font-semibold py-2 px-4 rounded-lg shadow-md hover:shadow-lg transition-all duration-300"
        >
          Read Chapter
        </Link>
      </div>
    </motion.div>
  );
};

export default ChapterPreviewCard;
