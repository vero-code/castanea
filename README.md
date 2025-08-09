# Castanea

## Technologies

- Vite, React, JavaScript
- Python
- Agent Development Kit (ADK)
- Gemini Pro/Flash

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

### ResearcherAgent  
```
Explain the main differences between nuclear fission and nuclear fusion.
```
  
### AnalystAgent
```
Summarize the following text in one sentence:
The chestnut, or Castanea, often symbolizes strength, longevity, and stability.
In various cultures, it is also associated with protection, fertility, and energy restoration.
In addition, the chestnut can be a symbol of professionalism and competence.
The powerful trunk and spreading crown of the chestnut symbolize stability and the ability to withstand trials.
The chestnut is considered a talisman against evil spirits and negative energy.
The fruits of the chestnut can symbolize fertility, as well as the restoration of internal resources and harmony.
```

### WriterAgent  
```
Write a short, three-paragraph essay on the importance of bees for the ecosystem.
```

## 📜 License

This project is licensed under the [MIT License](LICENSE).