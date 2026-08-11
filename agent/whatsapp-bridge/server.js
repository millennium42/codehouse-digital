/**
 * WhatsApp Web bridge para o agente CodeHouse (teste inicial).
 *
 * - Gera QR code no terminal (escaneie com seu numero pessoal).
 * - Mensagens recebidas de CHATS INDIVIDUAIS sao enviadas ao agente ingest (/inbound).
 * - POST /send {to, message} envia mensagem via WhatsApp (usado pelo agente).
 *
 * AVISO: WhatsApp Web automatizado viola os Termos da Meta e pode banir a conta.
 * Use apenas para teste com seu numero. Nao use em producao.
 */
const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const qrcodeImg = require('qrcode');
const express = require('express');
const axios = require('axios');
const path = require('path');

const PORT = process.env.BRIDGE_PORT || 3000;
const INGEST_URL = process.env.AGENT_INGEST_URL || 'http://127.0.0.1:8000/inbound';
// Numero autorizado a ser tratado como "cliente" (sua namorada).
// Formato: example@example.com (sem +, com @c.us). Deixe vazio para aceitar qualquer individual.
const CONTACT_ALLOWED = process.env.CONTACT_ALLOWED || '';

const app = express();
app.use(express.json());

const client = new Client({
  authStrategy: new LocalAuth({ dataPath: './.wwebjs_auth' }),
  puppeteer: { headless: true, args: ['--no-sandbox', '--disable-setuid-sandbox'] },
});

client.on('qr', (qr) => {
  console.log('\n=== ESCANEIE ESTE QR NO SEU WHATSAPP (numero pessoal) ===\n');
  qrcode.generate(qr, { small: true });
  console.log('\n===========================================================\n');
  const out = path.join(__dirname, 'qr.png');
  qrcodeImg.toFile(out, qr, { width: 400, margin: 2 }, (err) => {
    if (!err) console.log(`[bridge] QR salvo em ${out}`);
  });
});

client.on('ready', () => console.log('[bridge] WhatsApp conectado e pronto.'));
client.on('authenticated', () => console.log('[bridge] autenticado'));
client.on('auth_failure', (e) => console.error('[bridge] auth failure', e));
client.on('disconnected', (r) => console.log('[bridge] desconectado', r));

// Mensagem recebida -> encaminha ao agente (apenas chats individuais)
client.on('message', async (msg) => {
  try {
    const from = msg.from;
    // grupos (@g.us) e broadcasts (@broadcast) ignorados
    if (from.endsWith('@g.us') || from.endsWith('@broadcast')) {
      return;
    }
    if (CONTACT_ALLOWED && from !== CONTACT_ALLOWED) {
      console.log(`[bridge] ignorando ${from} (nao autorizado)`);
      return;
    }
    const lead_id = Math.abs(hashString(from)) % 100000;
    console.log(`[bridge] msg de ${from}: ${msg.body}`);
    await axios.post(INGEST_URL, { lead_id, body: msg.body, from }, { timeout: 10000 });
    console.log(`[bridge] encaminhado ao agente (lead_id=${lead_id})`);
  } catch (e) {
    console.error('[bridge] erro ao encaminhar:', e.message);
  }
});

// Agente envia mensagem (resolve ID correto via getNumberId)
app.post('/send', async (req, res) => {
  const { to, message } = req.body || {};
  if (!to || !message) return res.status(400).json({ error: 'to/message obrigatorio' });
  try {
    const number = to.replace('@c.us', '').replace('+', '');
    const id = await client.getNumberId(number);
    if (!id) return res.status(404).json({ error: 'numero nao encontrado no WhatsApp' });
    await client.sendMessage(id._serialized, message);
    res.json({ ok: true, to: id._serialized });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/health', (_req, res) => res.json({ status: client.info ? 'ready' : 'connecting' }));

function hashString(s) {
  let h = 0;
  for (let i = 0; i < s.length; i++) h = (h << 5) - h + s.charCodeAt(i) | 0;
  return h;
}

app.listen(PORT, () => {
  console.log(`[bridge] ouvindo em http://localhost:${PORT} (POST /send, GET /health)`);
  client.initialize();
});
