import { useState } from 'react';
import './App.css';

function App() {
  const [topic, setTopic] = useState("");
  const [isForging, setIsForging] = useState(false);
  const [result, setResult] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!topic.trim()) {
      alert("Please enter a topic to research.");
      return;
    }
    console.log("Starting research for topic:", topic);
    setIsForging(true);
    setResult("");

    setTimeout(() => {
      setResult(`Here are the synthesized findings for "${topic}". The agent has analyzed multiple sources to provide a comprehensive overview...`);
      setIsForging(false);
    }, 2500);
  };

  return (
    <>
      <main className="wrap" role="main">
        {/* Left: The control panel */}
        <section className="form-pane" aria-labelledby="title">
          <h1 id="title">Castanea</h1>
          <p className="hello">
            Welcome, researcher <span aria-hidden="true">👋</span>!
          </p>
          <p className="description">
            Provide a complex topic, and AI agent will autonomously decompose it, conduct research, and forge a structured thesis for you.
          </p>

          <form onSubmit={handleSubmit}>
            <div className="field">
              <label className="label" htmlFor="topic">
                I want to research…
              </label>
              <textarea
                className="textarea"
                id="topic"
                name="topic"
                placeholder="For example: 'The impact of quantum computing on modern cryptography'"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
                required
              />
            </div>

            <button className="submit" type="submit" disabled={isForging}>
              {isForging ? 'Researching...' : 'Start Research'}
            </button>
          </form>
        </section>

        {/* Right: The results panel */}
        <aside className="media" aria-label="Research results">
          <div className="results-content">
            {isForging && (
              <div className="spinner-container">
                <div className="spinner"></div>
                <p>Agent is thinking...</p>
              </div>
            )}
            {result && (
                <div className="result-text">
                    <h2>Research Synthesis</h2>
                    <p>{result}</p>
                </div>
            )}
            {!isForging && !result && (
                 <div className="placeholder-text">
                    <h2>Your results will appear here</h2>
                    <p>Once you submit a topic, the agent's findings will be displayed in this panel.</p>
                 </div>
            )}
          </div>
        </aside>
      </main>
    </>
  )
}

export default App;