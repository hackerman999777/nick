import React from 'react';
import { FaServer, FaChartLine, FaListUl, FaCog, FaCircle } from 'react-icons/fa';

// Du kannst diese CSS-Regeln mit CSS-in-JS-Lösungen oder in eine eigene CSS-Datei auslagern
const styles = {
  dashboardBg: {
    minHeight: '100vh',
    background: 'linear-gradient(135deg, #241E92 0%, #5432D3 50%, #7B6CF6 100%)',
    padding: '40px',
    boxSizing: 'border-box',
    fontFamily: 'Inter, sans-serif',
  },
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))',
    gap: '2rem',
    marginTop: '30px',
  },
  card: {
    background: 'rgba(255,255,255,0.82)',
    borderRadius: '1.5rem',
    boxShadow: '0 8px 30px rgba(62,33,138,0.16)',
    padding: '30px 28px',
    display: 'flex',
    flexDirection: 'column',
    gap: '10px',
    position: 'relative',
    overflow: 'hidden',
  },
  cardTitle: {
    fontSize: '1.5rem',
    fontWeight: 700,
    color: '#241E92',
    display: 'flex',
    alignItems: 'center',
    gap: '0.6em',
    marginBottom: '0.5rem',
    letterSpacing: '0.04em',
  },
  status: {
    display: 'flex',
    alignItems: 'center',
    fontWeight: 600,
    color: '#4BB543',
  },
  statusCircle: {
    animation: 'pulse 1.2s infinite cubic-bezier(.61,.32,.58,.78)',
    marginRight: '8px',
    fontSize: '0.9em',
  },
  placeholder: {
    color: '#aaa',
    fontStyle: 'italic',
    marginTop: '8px',
  },
  '@keyframes pulse': {
    '0%':   { opacity: 1, transform: 'scale(1)' },
    '60%':  { opacity: 0.5, transform: 'scale(1.17)' },
    '100%': { opacity: 1, transform: 'scale(1)' },
  },
};

function StatusIndicator({ online }) {
  return (
    <span style={styles.status}>
      <FaCircle style={{ ...styles.statusCircle, color: online ? '#4BB543' : '#E53A40', animation: styles.statusCircle.animation }} />
      {online ? 'Online' : 'Offline'}
    </span>
  );
}

const Dashboard = () => {
  // Simulierter Status und Platzhalter
  const backendOnline = true; // Könnte durch Props/State/etc. gesteuert werden

  return (
    <div style={styles.dashboardBg}>
      <h1 style={{ color: 'white', fontWeight: 900, letterSpacing: '0.1em', marginBottom: 0 }}>
        🚀 Dashboard
      </h1>
      <p style={{ color: '#e4e4f5', maxWidth: 530, marginTop: 8, fontSize: '1.15rem' }}>
        Willkommen! Übersichtlich, modern, bereit für Monitoring- und Analysefunktionen.
      </p>
      <div style={styles.grid}>
        {/* Systemstatus Card */}
        <div style={styles.card}>
          <div style={styles.cardTitle}>
            <FaServer /> Systemstatus
          </div>
          <div style={{ marginBottom: 6 }}>
            Backend:&nbsp;
            <StatusIndicator online={backendOnline} />
          </div>
          <div style={styles.placeholder}>Weitere Services werden hier überwacht.</div>
        </div>

        {/* Monitoring-Widgets Panel */}
        <div style={styles.card}>
          <div style={styles.cardTitle}>
            <FaChartLine /> Monitoring & Analytics
          </div>
          <div style={styles.placeholder}>
            Platzhalter: Trenddiagramm, Traffic, KPIs etc.
          </div>
        </div>

        {/* Logs Panel */}
        <div style={styles.card}>
          <div style={styles.cardTitle}>
            <FaListUl /> Logs-Vorschau
          </div>
          <div style={{ fontFamily: 'Fira Mono, monospace', color: '#453593', background: '#f3f2fa', borderRadius: '9px', padding: '8px 10px', fontSize: '0.98em' }}>
            2024-06-10 10:12:21 - Server gestartet<br/>
            2024-06-10 10:13:48 - Auth erfolgreich<br/>
            ...
          </div>
          <div style={styles.placeholder}>Mehr Details & Filter folgen...</div>
        </div>

        {/* Konfiguration Panel */}
        <div style={styles.card}>
          <div style={styles.cardTitle}>
            <FaCog /> Einstellungen
          </div>
          <div style={styles.placeholder}>
            Platzhalter für Nutzer- & Systemoptionen.
          </div>
        </div>

        {/* Weitere Widgets hier einfach ergänzen */}
      </div>
      {/* Animierter Keyframes-Style: */}
      <style>
        {`@keyframes pulse {0%{opacity:1;transform:scale(1);}60%{opacity:.5;transform:scale(1.17);}100%{opacity:1;transform:scale(1);}}`}
      </style>
    </div>
  );
};

export default Dashboard;
