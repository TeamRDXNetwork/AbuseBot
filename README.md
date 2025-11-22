# 🛡️ **Abuse Guardian Bot**
### **AI-Powered Telegram Moderation Bot for Real-Time Abuse Protection**

A next-gen AI moderation bot jo Telegram groups ko **abusive, hateful, sexual, toxic** messages se real-time protect karta hai —  
Hybrid system: **Badword DB + AI Context Analyzer = Almost Zero False Positives ⚡**

---

## 🚀 **Key Features**

### 🔥 **AI-Powered Message Filtering**
- GPT-based contextual analysis  
- Real abusive message → auto delete  
- Normal slang → ignored

### 📌 **Smart Badword Engine**
- Custom badword DB (add/remove anytime)  
- Pattern detection like: `m*ch`, `m.c`, `m..c`, `m c`  
- Auto-learning mode (optional)

### 🛑 **Advanced Protection**
- Edited message scanning  
- Sticker pack blocking  
- Media NSFW placeholder (ready for integration)

### 📊 **Live Stats Dashboard**
- Total deletions  
- AI flags  
- DB matches  
- Edited viols  
- Known chats

### 🤖 **Full Sudo System**
- Unlimited sudo users  
- Owner & sudo have full power

---

## ⚙️ **Commands Overview**

### 👑 **Owner / Sudo Commands**
| Command | Description |
|--------|-------------|
| `/addsudo <id/reply>` | Add sudo user |
| `/rmsudo <id/reply>` | Remove sudo user |
| `/sudolist` | Show sudo list |
| `/setlog <chat_id>` | Set log channel |
| `/api <key>` | Set OpenRouter API key |
| `/broadcast <text>` | Send message to all chats |
| `/blockpack` | Block sticker pack |
| `/unblockpack` | Unblock sticker pack |

### 📝 **Badword Control**
| Command | Description |
|--------|-------------|
| `/add <word>` | Add badword |
| `/rm <word>` | Remove badword |
| `/list` | Show all badwords |

### ℹ️ **General**
| Command | Description |
|--------|-------------|
| `/start` | Start message |
| `/help` | Help menu |
| `/stats` | Moderation stats |
| `/cleanmedia` | Clean old media (placeholder) |

---

## 🛠️ **Setup & Installation**

### 1️⃣ Install Requirements
```bash
pip install -r requirements.txt
