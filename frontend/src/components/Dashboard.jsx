import React, { useEffect, useState } from "react";

export default function Dashboard() {
  const [apiMsg, setApiMsg] = useState("");

  useEffect(() => {
    fetch("/api")
      .then(res => res.json())
      .then(data => setApiMsg(data.message || "API online!"))
      .catch(() => setApiMsg("Backend nicht erreichbar."));
  }, []);

  return (
    <main style={{ maxWidth: 700, margin: '40px auto', background: '#fff', padding: 40, borderRadius: 16, boxShadow: '0 2px 8px #0001' }}>
      <h1 style={{ fontSize: 36 }}>Nick Dashboard</h1>
      <p>Backend Status: <b>{apiMsg}</b></p>
      <section>
        <h2>Willkommen!</h2>
        <p>Dies ist ein moderner Startpunkt für dein Projekt.</p>
      </section>
    </main>
  );
}
