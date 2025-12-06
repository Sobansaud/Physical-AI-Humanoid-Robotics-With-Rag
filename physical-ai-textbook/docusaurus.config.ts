import remarkCodeTitle from 'remark-code-title';
import remarkPrism from 'remark-prism';
import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Bridging the gap between the digital brain and the physical body.',
  favicon: 'img/favicon.ico',

  url: 'https://Sobansaud.github.io',
  baseUrl: '/',

  organizationName: 'Sobansaud',
  projectName: 'Physical-AI-Humanoid-Robotics-With-Rag',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          remarkPlugins: [remarkCodeTitle, remarkPrism],
          rehypePlugins: [],
          editUrl: 'https://github.com/Sobansaud',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themes: ['@docusaurus/theme-live-codeblock'],

  themeConfig: {
    image: 'img/physical-ai-logo.png',
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI Textbook',
      logo: {
        alt: 'Physical AI Logo',
        src: 'img/physical-ai-logo.png',
      },
      items: [
        {
          to: '/docs/intro',
          label: 'Start Reading',
          position: 'left',
          className: 'navbar-start-reading',
        },
        {
          href: 'https://github.com/Sobansaud',
          label: 'GitHub',
          position: 'right',
          className: 'github-button-nav',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Curriculum',
          items: [
            { label: 'Module 1: ROS 2', to: '/docs/module-1-overview' },
            { label: 'Module 2: Simulation', to: '/docs/module-2-overview' },
            { label: 'Module 3: Isaac Sim', to: '/docs/module-3-overview' },
            { label: 'Module 4: VLA Models', to: '/docs/module-4-overview' },
          ],
        },
        {
          title: 'Socials',
          items: [
            { label: 'YouTube', href: 'https://www.youtube.com/@CodeVerseSoban' },
            { label: 'Twitter (X)', href: 'https://x.com/Sobansaud12345' },
            { label: 'LinkedIn', href: 'https://www.linkedin.com/in/muhammad-soban-saud-235a6b2ba/' },
            { label: 'CodeFusion.AI', href: 'https://codefusion.site' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'GitHub', href: 'https://github.com/Sobansaud' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics. <br/> Built with Docusaurus & ❤️ by Soban Saud.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } as Preset.ThemeConfig,
};

export default config;
