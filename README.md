# Castanea

## Features

Castanea operates through a team of specialized AI agents, each designed for a specific academic task:

-   ### 🧠 ResearcherAgent
    
    Performs in-depth research on complex topics. It leverages the **Perplexity** search engine to gather real-time, factual data and then uses the power of **Gemini Pro** to analyze, synthesize, and structure this information into a comprehensive and coherent report. This Retrieval-Augmented Generation (RAG) approach ensures answers are both accurate and well-written.
    
-   ### ⚡ AnalystAgent
    
    Provides quick and efficient analysis of existing text. Built on the **Gemini Flash** model for maximum speed, this agent can instantly summarize articles, extract key points from lecture notes, or identify the main arguments in a difficult text, helping students grasp core concepts faster.
    
-   ### ✍️ WriterAgent
    
    Acts as a versatile writing assistant. It can generate original content like essays, reports, and formal emails based on a user's prompt. Additionally, it is equipped with a tool to save its output directly to a file (e.g., social_media_essay.txt), making it easy to store and edit the work.

## Technologies

- Vite, React, JavaScript
- Python
- Agent Development Kit (ADK)
- Gemini Pro/Flash
- Perplexity’s Sonar API

## Installation

1. Clone the repository:

	```bash
	git clone https://github.com/vero-code/castanea.git
	cd castanea
	```
2. Configure the `.env` file:

	- Create `.env` in the root of the project.
	- See an example in `.env.example`.

3. Run the services:

	```bash
	# Frontend
	cd frontend
	npm install
	npm run dev
	```
 
	```bash
	# Backend
	cd backend
	python -m venv .venv
	.venv\Scripts\Activate.ps1
	pip install -r requirements.txt
	```

## Testing

### Test for ResearcherAgent  

The CRISPR and GMO problem is a complex, topical issue that requires gathering information from different fields (ethics, biology, law).
It is an ideal stress test for perplexity_search and the agent's ability to synthesize a complex answer.

```
Write a detailed report comparing the ethical implications of CRISPR gene editing with traditional GMO technology.
```

### Test for AnalystAgent

Analyzing a scientific abstract is something that students encounter all the time. 
The task checks whether the agent (Flash model) can quickly and accurately extract the essence from a scientific, "dry" text.

```
Summarize the key finding of this scientific abstract in a single, clear sentence:

This study investigates the correlation between bilingualism and delayed onset of dementia. 
A longitudinal study was conducted over 10 years with a cohort of 500 monolingual and 500 bilingual participants. 
Cognitive decline was measured using the Mini-Mental State Examination (MMSE) annually. 
Results indicated that the bilingual cohort exhibited first symptoms of dementia on average 4.5 years later 
than the monolingual cohort, suggesting that the constant cognitive effort of managing two languages 
builds cognitive reserve, thereby providing a protective effect against neurodegeneration.
```

### Test for WriterAgent  

Writing an argumentative essay is not just text generation, but a demonstration of the ability to build a logical structure (thesis, arguments, conclusion). 
Using the save_report tool here is absolutely logical - the student will want to save his work.

```
Write a 5-paragraph argumentative essay on whether social media has a net positive or negative impact on teenage mental health.
Save the output to 'social_media_essay.txt'.
```

## 📜 License

This project is licensed under the [MIT License](LICENSE).