# Projekt: Nick

Ein modernes, modulares Fullstack-Projekt mit folgenden Komponenten:
- **Backend**: Node.js + Express
- **Frontend**: React (Vite-basiert), modernes Dashboard
- **Agent**: Python Script

## Architektur

- `frontend/` – React UI (Vite-basiert)
- `backend/` – Node.js/Express REST-API
- `agent/` – Separater Python-Agent

## Quickstart (mit Docker Compose)

```sh
git clone https://github.com/hackerman999777/nick.git
cd nick
docker-compose up --build
```

Frontend auf [http://localhost:5173](http://localhost:5173)  
Backend-API auf [http://localhost:5000](http://localhost:5000)  
Agent läuft im eigenen Container

## Entwicklung lokal (Optional)

### Backend
```sh
cd backend
npm install
npm run dev
```
### Frontend
```sh
cd frontend
npm install
npm run dev
```

---

🛠️ Viel Erfolg beim Ausprobieren und Erweitern!