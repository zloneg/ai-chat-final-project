function About() {
  return (
    <section className="about-page">
      <div className="about-card">
        <h2>About This Project</h2>

        <p>
          AI Chat Project is a full stack web application that allows users to
          start and continue conversations with an AI assistant.
        </p>

        <p>
          The system uses a React single-page application on the client side,
          a Python FastAPI REST API on the server side, MySQL for storing
          conversations and messages, and OpenAI API for generating answers.
        </p>

        <h3>Main Features</h3>

        <ul>
          <li>Start a new AI conversation</li>
          <li>Continue the same conversation in context</li>
          <li>Display user and assistant messages on opposite sides</li>
          <li>Store conversations and messages in MySQL</li>
          <li>Navigate between Home and About pages</li>
        </ul>

        <h3>Developer</h3>

        <p>Sofia Kaplan</p>
      </div>
    </section>
  );
}

export default About;