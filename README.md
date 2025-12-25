# Projekt: Nick

Ein modernes, modulares Fullstack-Projekt für Server- & Agenten-Überwachung mit schickem Dashboard und eigener TikTok-Präsenz.

## Komponenten

- **Backend**: Node.js + Express (`backend/`)
- **Frontend**: React (Vite) mit modernem Dashboard (`frontend/`)
- **Agent**: Python Script (`agent/`)

## Features

- Moderne UI mit animierten Cards, Icons, Farbverlauf und persönlichem TikTok-Profil-Widget
- Einfacher Start per Docker Compose **oder** lokal (npm & Python)
- Erweiterbar für echtes Monitoring (CPU, RAM, Netzwerk etc.), Container-Steuerung, automatische Updates u.v.m.

## Dein TikTok-Profil

<div align="center">
  <a href="https://www.tiktok.com/@hackerman.nick" target="_blank" rel="noopener noreferrer">
    <img src="https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-avt-0068c001-no/dbecedef29cc1201642fad6342cb51da~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=10399&refresh_token=e53618e9&x-expires=1766858400&x-signature=rmbZztdaX96KoTmiBsks0bvmKOs%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=no1a"
    alt="TikTok Profilbild hackerman.nick" width="120" style="border-radius: 50%;border:2px solid #ff0050;">
    <br>
    <b>@hackerman.nick auf TikTok</b>
  </a>
</div>

---

## Quickstart (mit Docker Compose)

```sh
git clone https://github.com/hackerman999777/nick.git
cd nick
docker-compose up --build
```

- Dashboard: [http://localhost:5173](http://localhost:5173)
- Backend-API: [http://localhost:5000](http://localhost:5000)
- Agent läuft automatisch im Container

---

## Lokale Entwicklung

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
### Agent
```sh
cd agent
python agent.py
```

---

## Ordnerstruktur

```
/
├── agent/             # Python-Agent
│   └── agent.py
├── backend/           # Node.js Backend
│   ├── package.json
│   └── src/
│        └── index.js
├── frontend/          # React Frontend
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│        ├── App.jsx
│        ├── main.jsx
│        └── components/
│            └── Dashboard.jsx
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## Hinweise

- Das Frontend kann einfach um Widgets für Realtime-Serverdaten, automatische Updater und vieles mehr erweitert werden!
- Zeig dein Projekt gern auf TikTok: **[@hackerman.nick](https://www.tiktok.com/@hackerman.nick)**
