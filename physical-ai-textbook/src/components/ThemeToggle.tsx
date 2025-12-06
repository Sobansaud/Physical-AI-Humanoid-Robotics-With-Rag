import React from 'react';
import {useColorMode} from '@docusaurus/theme-common';
import {motion} from 'framer-motion';

export default function ThemeToggle(): JSX.Element {
  const {colorMode, setColorMode} = useColorMode();

  const toggle = () => setColorMode(colorMode === 'dark' ? 'light' : 'dark');

  return (
    <button
      aria-label="Toggle color mode"
      onClick={toggle}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: '8px',
        background: 'transparent',
        border: '1px solid rgba(255,255,255,0.06)',
        padding: '6px 10px',
        borderRadius: 8,
        cursor: 'pointer',
      }}
    >
      <motion.span
        initial={{rotate: 0}}
        animate={{rotate: colorMode === 'dark' ? 40 : 0}}
        transition={{duration: 0.25}}
      >
        {colorMode === 'dark' ? '🌙' : '☀️'}
      </motion.span>
      <span style={{fontFamily: 'Inter, sans-serif'}}>{colorMode === 'dark' ? 'Dark' : 'Light'}</span>
    </button>
  );
}
