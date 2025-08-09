import { useState } from 'react';
import './App.css';
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import BarLoader from "./components/BarLoader.jsx";

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [userQuery, setUserQuery] = useState('');
  const [aiResponse, setAiResponse] = useState('');

  const VITE_REACT_APP_BACKEND_URL = import.meta.env.VITE_REACT_APP_BACKEND_URL;

  const handleQueryChange = (event) => {
    setUserQuery(event.target.value);
  };

  const handleSubmitQuery = async () => {
    event.preventDefault();
    if (!userQuery.trim()) return;

    setIsLoading(true);
    setAiResponse("");

    try {
      const response = await fetch(VITE_REACT_APP_BACKEND_URL + '/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userQuery }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setAiResponse(data.response);
      setUserQuery('');
    } catch (error) {
      console.error("Error sending query to backend:", error);
      setAiResponse("Error: Could not get response from AI. Please try again later.");
    } finally {
      setIsLoading(false);
    }
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

          <form onSubmit={handleSubmitQuery}>
            <div className="field">
              <label className="label" htmlFor="topic">
                I want to research…
              </label>
              <textarea
                className="textarea"
                id="topic"
                name="topic"
                placeholder="For example: 'The impact of quantum computing on modern cryptography'"
                value={userQuery}
                onChange={handleQueryChange}
                required
              />
            </div>

            <button
              className="submit"
              type="submit"
              disabled={isLoading || !userQuery.trim()}
            >
              {isLoading ? 'Researching...' : 'Start Research'}
            </button>
          </form>
        </section>

        {/* Right: The results panel */}
        <aside className="media" aria-label="Research results">
          <div className="results-content">
            {isLoading ? (
                <div className="spinner-container">
                  <BarLoader />
                </div>
            ) : aiResponse ? (
              <div className="ai-response-container">
                <div className="prose max-w-none">
                   <ReactMarkdown remarkPlugins={[remarkGfm]}>
                     {aiResponse}
                   </ReactMarkdown>
                </div>
              </div>
            ) : (
              <div className="placeholder-text">
                <h2>Your results will appear here</h2>
                <p>Fill in the field on the left, the agent's findings will be displayed in this panel.</p>
              </div>
            )}
          </div>
        </aside>
      </main>
    </>
  )
}

export default App;