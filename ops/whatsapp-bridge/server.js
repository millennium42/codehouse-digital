/*
 * CodeHouse WhatsApp bridge — Baileys (sem Chrome, estavel no Windows).
 * TEST ONLY: usa numero pessoal; viola ToS Meta em producao (usar Cloud API).
 */
const { default: makeWASocket, useMultiFileAuthState, DisconnectReason } = require('@whiskeysockets/baileys');
const qrcode = require('qrcode');
const qrcodeTerminal = require('qrcode-terminal');
const express = require('express');
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const PORT = process.env.BRIDGE_PORT || 3000;
const INGEST_URL = process.env.AGENT_INGEST_URL || 'http://127.0.0.1:8000/inbound';
const CONTACT_ALLOWED = process.env.CONTACT_ALLOWED || '';
const AUTH_DIR = path.join(__dirname, 'baileys_auth');

const app = express();
app.use(express.json());
let sock = null;

function maskPhone(jid) {
  const d = (jid || '').replace('@s.whatsapp.net', '');
  return d.slice(0, 4) + '****' + d.slice(-4);
}

async function start() {
  const { state, saveCreds } = await useMultiFileAuthState(AUTH_DIR);
  sock = makeWASocket({
    auth: state,
    printQRInTerminal: false,
    browser: ['CodeHouse', 'Chrome', '1.0'],
  });

  sock.ev.on('creds.update', saveCreds);

  sock.ev.on('connection.update', async (update) => {
    const { connection, lastDisconnect, qr } = update;
    if (qr) {
      console.log('\n=== ESCANEAR QR ABAIXO (terminal ASCII) ===');
      qrcodeTerminal.generate(qr, { small: true }, (qrStr) => {
        console.log(qrStr);
      });
      console.log('WhatsApp > Dispositivos conectados > Conectar um dispositivo\n');
    }
    if (connection === 'open') console.log('[bridge] PRONTO - conectado');
    if (connection === 'close') {
      const reason = lastDisconnect?.error?.output?.statusCode;
      console.log('[bridge] desconectado:', reason);
      if (reason !== DisconnectReason.loggedOut) setTimeout(start, 3000);
    }
  });

  sock.ev.on('messages.upsert', async ({ messages }) => {
    for (const m of messages) {
      if (!m.message || m.key.fromMe) continue;
      const from = m.key.remoteJid;
      if (!from.endsWith('@s.whatsapp.net')) continue;
      if (CONTACT_ALLOWED && from !== CONTACT_ALLOWED) continue;
      const body = m.message.conversation || m.message.extendedTextMessage?.text || '';
      const lead_id = Math.abs([...from].reduce((h, c) => (h << 5) - h + c.charCodeAt(0) | 0, 0)) % 100000;
      try {
        await axios.post(INGEST_URL, { lead_id, body, from }, { timeout: 10000 });
      } catch (e) { console.log('[bridge] ingest falhou:', e.message); }
    }
  });
}

app.post('/send', async (req, res) => {
  const { to, message } = req.body || {};
  if (!to || !message) return res.status(400).json({ error: 'to/message obrigatorio' });
  if (!sock) return res.status(503).json({ error: 'nao conectado' });
  try {
    const jid = to.includes('@s.whatsapp.net') ? to : `${to}@s.whatsapp.net`;
    await sock.sendMessage(jid, { text: message });
    res.json({ ok: true, to: maskPhone(jid) });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/health', (_q, r) => r.json({ status: sock && sock.user ? 'ready' : 'connecting' }));

app.listen(PORT, async () => {
  console.log(`[bridge] ouvindo :${PORT}`);
  await start();
});
