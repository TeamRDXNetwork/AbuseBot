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
  <div class="wrap">
    <header>
      <div class="logo">AG</div>
      <div>
        <h1>Abuse Guardian — AI Moderation Bot</h1>
        <p class="lead">A hybrid moderation system (DB + AI) for Telegram that aggressively minimizes false positives while removing abusive, hateful, or NSFW content.</p>
        <div class="badges">
          <span class="badge">AI-powered</span>
          <span class="badge">MongoDB</span>
          <span class="badge">Pyrogram</span>
          <span class="badge">Auto-learning</span>
          <span class="badge">Sticker blocking</span>
        </div>
      </div>
    </header>

    <div class="grid">
      <main>
        <div class="card hero-features">
          <div class="feature">
            <div class="dot"></div>
            <div>
              <h4>Context-aware AI verification</h4>
              <p>Before deleting, the message is verified by an AI model (OpenRouter/OpenAI style) to avoid accidental removals of legitimate chat — e.g., local slang, usernames, or coincidental substrings.</p>
            </div>
          </div>

          <div class="feature">
            <div class="dot" style="background:var(--accent-2)"></div>
            <div>
              <h4>Smart badword detection</h4>
              <p>Database-driven badwords + pattern matching detect disguised words like <span class="inline"><code class="inline">m*c</code></span>, <span class="inline"><code class="inline">m.c</code></span>, <span class="inline"><code class="inline">m/c</code></span> and other obfuscations.</p>
            </div>
          </div>

          <div class="feature">
            <div class="dot"></div>
            <div>
              <h4>Sticker pack blocking & media checks</h4>
              <p>Block entire sticker packs; placeholder for image/video NSFW scanning that can be integrated with any moderation API.</p>
            </div>
          </div>

          <div class="feature">
            <div class="dot"></div>
            <div>
              <h4>Edit detection & soft warnings</h4>
              <p>Edited messages are rescanned, users receive temporary inline warnings (auto-deleting) and events are logged to the configured log chat.</p>
            </div>
          </div>
        </div>

        <section class="section">
          <h2 class="section-title">Quick Start</h2>
          <p class="muted">Clone, configure <span class="kbd">config.py</span>, and run.</p>
          <pre class="code">git clone &lt;repo&gt;
cd repo
pip install -r requirements.txt
# Edit config.py then
python3 bot.py</pre>

          <div class="section">
            <h2 class="section-title">Config Example</h2>
            <pre class="code"># config.py
API_ID = 12345
API_HASH = "your_api_hash"
BOT_TOKEN = "12345:ABCDEF"
MONGO_URI = "mongodb+srv://..."
OWNER_ID = 123456
OPENROUTER_KEY = ""
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
WARN_DELETE_DELAY = 7</pre>
          </div>

          <div class="section">
            <h2 class="section-title">Commands (Owner / Sudo)</h2>
            <div class="cmd-list">
              <div class="cmd"><strong>/addsudo</strong> &lt;id/reply&gt; — Add sudo user</div>
              <div class="cmd"><strong>/rmsudo</strong> &lt;id/reply&gt; — Remove sudo</div>
              <div class="cmd"><strong>/sudolist</strong> — Show sudo users</div>
              <div class="cmd"><strong>/setlog</strong> &lt;chat_id&gt; — Set log chat</div>
              <div class="cmd"><strong>/api</strong> &lt;key&gt; — Set AI key</div>
              <div class="cmd"><strong>/broadcast</strong> &lt;text/reply&gt; — Broadcast to saved chats</div>
              <div class="cmd"><strong>/blockpack</strong> (reply) — Block pack</div>
              <div class="cmd"><strong>/unblockpack</strong> (reply) — Unblock pack</div>
            </div>
          </div>

          <div class="section">
            <h2 class="section-title">Badword Commands</h2>
            <div class="cmd-list">
              <div class="cmd"><strong>/add &lt;word&gt;</strong> — Add badword</div>
              <div class="cmd"><strong>/rm &lt;word&gt;</strong> — Remove badword</div>
              <div class="cmd"><strong>/list</strong> — Show badwords</div>
            </div>
          </div>

          <div class="section">
            <h2 class="section-title">How detection works (summary)</h2>
            <ol style="color:var(--muted);">
              <li>Incoming message gets normalized (usernames/names stripped).</li>
              <li>DB-based fuzzy & pattern matching checks for badwords.</li>
              <li>If found, AI is queried for final judgment.</li>
              <li>On BAD: message deleted, user warned, event logged, stats incremented.</li>
            </ol>
          </div>
        </section>

      </main>

      <aside class="card sidebar">
        <div class="meta">
          <h3 style="margin:0">Setup & Notes</h3>
          <p>Designed for reliability and low false-positives. Replace the <span class="kbd">ai_media_check</span> stub with your preferred moderation API to enable image/video scanning.</p>
        </div>

        <div style="margin-top:12px">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <strong>Owner</strong>
            <span class="kbd">OWNER_ID</span>
          </div>
          <p style="margin-top:8px;color:var(--muted);">Update the <span class="kbd">OWNER_ID</span> &amp; <span class="kbd">OPENROUTER_KEY</span> in config before running.</p>
        </div>

        <div style="margin-top:14px">
          <strong>Logging</strong>
          <p class="muted">Set your log chat with <span class="kbd">/setlog &lt;chat_id&gt;</span>. Deletion events include timestamp, user, chat, matched word, and content.</p>
        </div>

        <div style="margin-top:14px">
          <strong>Safety</strong>
          <p class="muted">AI key is optional but recommended to reduce false positives. Keep the bot admin in groups to enable message deletion.</p>
        </div>

        <div style="margin-top:12px" class="cta-row">
          <a class="btn" href="#" onclick="copyConfig()">Copy Config Snippet</a>
          <a class="btn ghost" href="#" onclick="window.scrollTo({top:0,behavior:'smooth'})">Back to top</a>
        </div>

        <hr style="margin:14px 0;border:none;border-top:1px solid rgba(255,255,255,0.02)">
        <div>
          <strong>Stats</strong>
          <p class="muted">Stored in MongoDB. See /stats for live counts.</p>
        </div>

        <script>
          function copyConfig(){
            const txt = `API_ID = 12345\nAPI_HASH = "your_api_hash"\nBOT_TOKEN = "12345:ABCDEF"\nMONGO_URI = "mongodb+srv://..."\nOWNER_ID = 123456\nOPENROUTER_KEY = ""\nOPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"\nWARN_DELETE_DELAY = 7`;
            navigator.clipboard.writeText(txt).then(()=>{
              alert('Config copied to clipboard!');
            }).catch(()=>alert('Could not copy — use manual copy.'));
          }
        </script>
      </aside>
    </div>

    <footer>
      <div>Built with ❤️ by <a href="https://t.me/TrueNakshu" style="color:var(--accent)">@TrueNakshu</a> — Support: <a href="https://t.me/hellbotsupport" style="color:var(--accent-2)">@hellbotsupport</a></div>
      <div style="margin-top:8px;color:var(--muted)">License: MIT • Customize freely for your projects</div>
    </footer>
  </div>
</body>
</html>
