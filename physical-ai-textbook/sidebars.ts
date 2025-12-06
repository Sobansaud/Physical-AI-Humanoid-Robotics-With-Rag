import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {type: 'doc', id: 'intro', label: 'Home'},
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      collapsible: true,
      collapsed: true,
      items: [
        {type: 'doc', id: 'module-1-overview', label: '📚 Overview'},
        {type: 'doc', id: 'module-1-week-1', label: 'Week 1: Physical AI Foundations'},
        {type: 'doc', id: 'module-1-week-2', label: 'Week 2: ROS 2 Architecture'},
        {type: 'doc', id: 'module-1-week-3', label: 'Week 3: Communication Patterns'},
        {type: 'doc', id: 'module-1-week-4', label: 'Week 4: Services & Actions'},
        {type: 'doc', id: 'module-1-week-5', label: 'Week 5: Package Development'},
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      collapsible: true,
      collapsed: true,
      items: [
        {type: 'doc', id: 'module-2-overview', label: '📚 Overview'},
        {type: 'doc', id: 'module-2-week-6', label: 'Week 6: Gazebo Simulation'},
        {type: 'doc', id: 'module-2-week-7', label: 'Week 7: URDF & SDF Formats'},
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      collapsible: true,
      collapsed: true,
      items: [
        {type: 'doc', id: 'module-3-overview', label: '📚 Overview'},
        {type: 'doc', id: 'module-3-week-8', label: 'Week 8: Isaac SDK & Sim'},
        {type: 'doc', id: 'module-3-week-9', label: 'Week 9: Perception & Manipulation'},
        {type: 'doc', id: 'module-3-week-10', label: 'Week 10: Reinforcement Learning'},
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      collapsible: true,
      collapsed: true,
      items: [
        {type: 'doc', id: 'module-4-overview', label: '📚 Overview'},
        {type: 'doc', id: 'module-4-week-11', label: 'Week 11: Humanoid Development'},
        {type: 'doc', id: 'module-4-week-12', label: 'Week 12: Kinematics & Dynamics'},
        {type: 'doc', id: 'module-4-week-13', label: 'Week 13: Conversational Robotics'},
      ],
    },
    {type: 'doc', id: 'why-physical-ai-matters', label: 'Why Physical AI Matters'},
    {type: 'doc', id: 'learning-outcomes', label: 'Learning Outcomes'},
    {type: 'doc', id: 'weekly-breakdown', label: 'Weekly Breakdown (13 weeks)'},
    {type: 'doc', id: 'assessments', label: 'Assessments'},
    {type: 'doc', id: 'hardware-requirements', label: 'Hardware Requirements'},
  ],
};

export default sidebars;
