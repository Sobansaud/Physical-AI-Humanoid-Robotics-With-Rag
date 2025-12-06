import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import Heading from "@theme/Heading";
import styles from "./index.module.css";
import { JSX } from "react";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header
      className={clsx("hero", "heroBanner")}
      style={{
        padding: "10rem 0",
        position: "relative",
        overflow: "hidden",
        minHeight: "100vh", 
        display: "flex",
        alignItems: "center",
        background: "transparent"
      }}
    >
      <div className="animated-hero-bg"></div>

      <div className="hero-grid-overlay"></div>

      <div
        className="container"
        style={{
          position: "relative",
          zIndex: 10,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          textAlign: "center",
        }}
      >
        <Heading as="h1" className="hero__title" style={{ marginBottom: "1.5rem" }}>
          <span
            style={{
              background: "linear-gradient(to right, #00f2ea, #fff, #7000ff)",
              backgroundSize: "200% auto",
              WebkitBackgroundClip: "text",
              WebkitTextFillColor: "transparent",
              fontSize: "clamp(3.5rem, 9vw, 7.5rem)",
              fontWeight: 800,
              filter: "drop-shadow(0 0 40px rgba(112, 0, 255, 0.6))",
              lineHeight: 1.1,
              display: "inline-block",
              animation: "shine 4s linear infinite",
            }}
          >
            {siteConfig.title}
          </span>
        </Heading>

        <p
          className="hero__subtitle"
          style={{
            fontSize: "clamp(1.2rem, 3vw, 2rem)",
            marginTop: "1.5rem",
            color: "#e6f7ff",
            fontWeight: "500",
            letterSpacing: "0.5px",
            maxWidth: "900px",
            lineHeight: "1.4",
            textShadow: "0 2px 10px rgba(0,0,0,0.5)",
          }}
        >
          {siteConfig.tagline}
        </p>

        {/* Buttons */}
        <div
          className={styles.buttons}
          style={{
            display: "flex",
            gap: "2rem",
            justifyContent: "center",
            flexWrap: "wrap",
            marginTop: "3rem",
          }}
        >
          <Link to="/docs/intro" className="premium-button">
            <span>Start Learning</span>
          </Link>

          <Link
            to="https://github.com/Sobansaud"
            className="premium-button secondary"
          >
            <span>GitHub Repo</span>
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout title={`${siteConfig.title}`} description="Physical AI & Humanoid Robotics Textbook">
      <HomepageHeader />

      <main>
        <section style={{ padding: "6rem 0", position: "relative" }}>
          {/* Bento Grid Layout */}
          <div className="container">
            <div className="bento-grid">
              {/* Large Card */}
              <div className="bento-card large">
                <div className="card-icon">🦾</div>
                <h3>Physical AI</h3>
                <p>Bridging the gap between digital algorithms and physical actuation. Control humanoid robots in the real world.</p>
                <div className="card-glow"></div>
              </div>

              {/* Medium Card 1 */}
              <div className="bento-card medium">
                <div className="card-icon">🧠</div>
                <h3>NVIDIA Isaac</h3>
                <p>Photorealistic simulation & synthetic data generation.</p>
                <div className="card-glow"></div>
              </div>

              {/* Medium Card 2 */}
              <div className="bento-card medium delay-1">
                <div className="card-icon">🔗</div>
                <h3>ROS 2</h3>
                <p>The standard middleware for robot control.</p>
                <div className="card-glow"></div>
              </div>

              {/* Wide Card */}
              <div className="bento-card wide">
                <div className="card-icon">🤖</div>
                <h3>Vision-Language-Action (VLA)</h3>
                <p>The convergence of LLMs and Robotics. Build agents that understand natural language and execute complex physical tasks.</p>
                <div className="card-glow"></div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}