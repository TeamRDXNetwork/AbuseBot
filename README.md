<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Abuse Guardian — README</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg:#0f1724; /* deep navy */
      --card:#0b1220;
      --muted:#93a2bf;
      --accent:#7c3aed; /* violet */
      --accent-2:#06b6d4; /* teal */
      --glass: rgba(255,255,255,0.03);
      --code-bg:#0b1220;
      font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    }
    html,body{height:100%;margin:0;background:linear-gradient(180deg,#071428 0%, #071427 40%, #031021 100%);color:#e6eef8}
    .wrap{max-width:980px;margin:36px auto;padding:28px;border-radius:14px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));box-shadow:0 10px 40px rgba(2,6,23,0.6);border:1px solid rgba(255,255,255,0.03)}
    header{display:flex;gap:18px;align-items:center}
    .logo{width:84px;height:84px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent-2));display:flex;align-items:center;justify-content:center;font-weight:800;color:white;font-size:32px;box-shadow:0 6px 20px rgba(124,58,237,0.18)}
    h1{margin:0;font-size:28px;letter-spacing:-0.4px}
    p.lead{margin:6px 0 0;color:var(--muted)}

    .badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
    .badge{background:var(--glass);padding:6px 10px;border-radius:999px;font-size:13px;color:var(--muted);border:1px solid rgba(255,255,255,0.02)}

    .grid{display:grid;grid-template-columns:1fr 320px;gap:20px;margin-top:22px}
    .card{background:linear-gradient(180deg, rgba(255,255,255,0.015), rgba(255,255,255,0.01));padding:18px;border-radius:12px;border:1px solid rgba(255,255,255,0.02)}

    .hero-features{display:flex;flex-direction:column;gap:10px}
    .feature{display:flex;gap:12px;align-items:flex-start}
    .feature .dot{width:12px;height:12px;border-radius:3px;background:var(--accent);margin-top:6px}
    .feature h4{margin:0;font-size:15px}
    .feature p{margin:4px 0 0;color:var(--muted);font-size:13px}

    pre.code{background:var(--code-bg);padding:12px;border-radius:8px;color:#d6e6ff;overflow:auto;border:1px solid rgba(255,255,255,0.02);font-size:13px}
    code.inline{background:rgba(255,255,255,0.03);padding:2px 6px;border-radius:6px}

    .section{margin-top:18px}
    h2.section-title{display:flex;align-items:center;gap:12px;margin:0;font-size:18px}
    .cmd-list{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-top:10px}
    .cmd{padding:10px;border-radius:8px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.01);font-size:13px}

    footer{margin-top:22px;text-align:center;color:var(--muted);font-size:13px}

    .cta-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
    .btn{background:linear-gradient(90deg,var(--accent),var(--accent-2));padding:10px 14px;border-radius:10px;color:white;text-decoration:none;font-weight:600;box-shadow:0 8px 30px rgba(12,12,40,0.6)}
    .btn.ghost{background:transparent;border:1px solid rgba(255,255,255,0.04);color:var(--muted);box-shadow:none}

    .sidebar .meta p{margin:6px 0 0;color:var(--muted);font-size:13px}
    .kbd{display:inline-block;background:rgba(255,255,255,0.02);padding:6px 8px;border-radius:6px;border:1px solid rgba(255,255,255,0.02);font-weight:600}

    .copy{float:right;background:rgba(255,255,255,0.02);border-radius:6px;padding:6px 8px;border:1px solid rgba(255,255,255,0.03);cursor:pointer}

    @media (max-width:900px){.grid{grid-template-columns:1fr} .logo{width:64px;height:64px}}
  </style>
</head>
<body>
    <header>
        <h1>🛡️ Abuse Guardian Bot — Powerful AI Anti-Abuse Telegram Bot</h1>
        <p class="subtitle">A next-gen moderation bot with AI contextual filtering, advanced pattern detection, and real-time group protection.</p>
    </header>

    <section>
        <h2>⚡ Introduction</h2>
        <p>Abuse Guardian Bot ek advanced <strong>AI-powered Telegram moderation bot</strong> hai jo abusive, sexual, hateful, ya NSFW content ko automatically detect karke delete karta hai. Ye bot <strong>hybrid moderation system</strong> use karta hai: <strong>Custom Badword Database + AI Context Verification</strong>, jisse false positives almost zero ho jaate hain.</p>
    </section>

    <section>
        <h2>🚀 Features</h2>

        <h3>🔥 AI-Powered Message Filtering</h3>
        <ul>
            <li>GPT-based AI model se contextual message analysis.</li>
            <li>Sirf real abusive messages delete — normal slang ignore.</li>
        </ul>

        <h3>📌 Smart Badword System</h3>
        <ul>
            <li>Custom badword database — add/remove anytime.</li>
            <li>AI Auto-Learning — abusive patterns detect hote hi auto-add.</li>
        </ul>

        <h3>🛑 Advanced Pattern Detection</h3>
        <ul>
            <li>Disguised abusive words detect jaise: <code>m*ch</code>, <code>m.c</code>, <code>m c</code>, <code>m..c</code>.</li>
        </ul>

        <h3>🎨 NSFW Media Detection (Ready Placeholder)</h3>
        <ul>
            <li>Image/Video/Document NSFW scan feature placeholder.</li>
            <li>Easy integration: OpenAI, SightEngine, etc.</li>
        </ul>

        <h3>🤖 Sudo System</h3>
        <ul>
            <li>Unlimited sudo users add/remove.</li>
            <li>Owner & sudo users full control.</li>
        </ul>

        <h3>🗑️ Message Edit Protection</h3>
        <ul>
            <li>User edited message me badword mila → instant delete + log.</li>
        </ul>

        <h3>🔥 Sticker Pack Blocking</h3>
        <ul>
            <li>Pura sticker pack block/unblock.</li>
            <li>Blocked pack ka koi sticker aaya → auto delete.</li>
        </ul>

        <h3>📊 Live Stats Dashboard</h3>
        <ul>
            <li>Total deletions</li>
            <li>AI flags</li>
            <li>DB matches</li>
            <li>Edited violations</li>
            <li>Known chats</li>
        </ul>

        <h3>🔗 Broadcast System</h3>
        <ul>
            <li>All groups/chats me broadcast message.</li>
        </ul>

        <h3>📥 Custom Logging System</h3>
        <ul>
            <li>Har violation ka complete log dedicated log chat me.</li>
        </ul>

        <h3>🛡 Chat Tracker</h3>
        <ul>
            <li>Bot jaha bhi message dekhta hai, wo chat auto-save hoti hai.</li>
        </ul>
    </section>

    <section>
        <h2>⚙️ Commands</h2>

        <h3>👑 Owner / Sudo Commands</h3>
        <table>
            <tr><th>Command</th><th>Description</th></tr>
            <tr><td>/addsudo &lt;id/reply&gt;</td><td>Add sudo user</td></tr>
            <tr><td>/rmsudo &lt;id/reply&gt;</td><td>Remove sudo user</td></tr>
            <tr><td>/sudolist</td><td>Show sudo users</td></tr>
            <tr><td>/setlog &lt;chat_id&gt;</td><td>Set log chat</td></tr>
            <tr><td>/api &lt;key&gt;</td><td>Set OpenRouter API key</td></tr>
            <tr><td>/broadcast &lt;text&gt;</td><td>Send message to all chats</td></tr>
            <tr><td>/blockpack (reply sticker)</td><td>Block sticker pack</td></tr>
            <tr><td>/unblockpack (reply sticker)</td><td>Unblock sticker pack</td></tr>
        </table>

        <h3>📝 Badword Control</h3>
        <table>
            <tr><th>Command</th><th>Description</th></tr>
            <tr><td>/add &lt;word&gt;</td><td>Add badword</td></tr>
            <tr><td>/rm &lt;word&gt;</td><td>Remove badword</td></tr>
            <tr><td>/list</td><td>Show badword list</td></tr>
        </table>

        <h3>ℹ️ General</h3>
        <table>
            <tr><th>Command</th><th>Description</th></tr>
            <tr><td>/start</td><td>Start message</td></tr>
            <tr><td>/help</td><td>Show help menu</td></tr>
            <tr><td>/stats</td><td>Show moderation stats</td></tr>
            <tr><td>/cleanmedia</td><td>Clean old media (placeholder)</td></tr>
        </table>
    </section>

    <section>
        <h2>🛠️ Setup & Installation</h2>

        <h3>1️⃣ Requirements</h3>
        <ul>
            <li>Python 3.9+</li>
            <li>MongoDB Database</li>
            <li>Telegram Bot Token</li>
            <li>API_ID + API_HASH</li>
            <li>Optional: OpenRouter API key</li>
        </ul>

        <h3>2️⃣ Install Libraries</h3>
        <pre><code>pip install -r requirements.txt</code></pre>

        <h3>3️⃣ Fill <code>config.py</code></h3>
        <pre><code>API_ID = 12345
API_HASH = "your_api_hash"
BOT_TOKEN = "12345:ABCDEF"
MONGO_URI = "mongodb+srv://..."
OWNER_ID = 123456
OPENROUTER_KEY = ""
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
WARN_DELETE_DELAY = 7
</code></pre>

        <h3>4️⃣ Run Bot</h3>
        <pre><code>python3 bot.py</code></pre>
    </section>

    <section>
        <h2>🧠 AI Logic (How It Works)</h2>
        <ul>
            <li>User message → bot clean formatting.</li>
            <li>DB match check.</li>
            <li>Match mila → AI verify.</li>
            <li>AI: <strong>BAD</strong> → delete + warn + log.</li>
            <li>AI: <strong>OK</strong> → ignore.</li>
            <li>Edited messages & stickers background me scan hote hain.</li>
        </ul>
    </section>

    <section>
        <h2>📡 Logging System</h2>
        <p>Har delete event ka log send hota hai:</p>
        <ul>
            <li>User</li>
            <li>Chat</li>
            <li>Time</li>
            <li>Reason</li>
            <li>Matched word</li>
            <li>Full message content</li>
        </ul>
    </section>

    <section>
        <h2>🧑‍💻 Developer Notes</h2>
        <ul>
            <li>Media NSFW detection placeholder.</li>
            <li>Auto-learning DB.</li>
            <li>Modular and customizable architecture.</li>
            <li>Real-time group safety.</li>
        </ul>
    </section>

    <section>
        <h2>⭐ Credits</h2>
        <p>Built with ❤️ by <strong>@TrueNakshu</strong></p>
        <p>Support: https://t.me/hellbotsupport<br>Updates: https://t.me/TheAceUpdates</p>
    </section>
</body>
</html>
