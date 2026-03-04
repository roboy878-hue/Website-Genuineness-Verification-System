# Production Startup Guide

## Start Your Website in Production Mode

### 🚀 Quick Start (Windows)

#### Option 1: Using Batch Script
```bash
cd backend
start_production.bat
```

#### Option 2: Manual Gunicorn (Recommended)
```bash
cd backend
gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 120 wsgi:app
```

#### Option 3: Development Mode (Flask)
```bash
cd backend
python app.py
```

---

### Frontend Server

Open another terminal:
```bash
cd frontend
python -m http.server 8001
```

---

### Access Your Application

| Component | URL | Purpose |
|-----------|-----|---------|
| **Frontend UI** | http://localhost:8001 | Web interface |
| **Backend API** | http://localhost:8000 | API endpoint |
| **Health Check** | http://localhost:8000/ | Server status |
| **Verify API** | http://localhost:8000/verify | JSON API |

---

## 📊 Production Server Details

**Gunicorn Configuration:**
- **Bind**: 0.0.0.0:8000 (all interfaces)
- **Workers**: 4 (increase for more traffic)
- **Timeout**: 120 seconds
- **Max Requests**: 1000 (prevents memory leaks)
- **Logs**: 
  - Access: `logs/access.log`
  - Error: `logs/error.log`
  - Verification: `logs/verification.log`

---

## 🔧 Scaling for High Traffic

Increase workers based on your CPU cores:

```bash
gunicorn \
  --bind 0.0.0.0:8000 \
  --workers 8 \
  --threads 4 \
  --worker-class gthread \
  --max-requests 1000 \
  wsgi:app
```

**Worker Formula**: `(2 × CPU_CORES) + 1`

---

## 📁 Project Structure (Production Ready)

```
website/
├── backend/
│   ├── app.py (Flask application)
│   ├── wsgi.py (Gunicorn entry point)
│   ├── config.py (Configuration management)
│   ├── requirements.txt (All dependencies)
│   ├── start_production.bat (Batch startup)
│   ├── modules/ (7 verification modules)
│   ├── logs/ (Application logs)
│   └── verification.db (SQLite database)
├── frontend/
│   ├── index.html (Web UI)
│   ├── style.css (Styling)
│   └── script.js (Frontend logic)
├── DEPLOYMENT.md (Full deployment guide)
├── PRODUCTION_STARTUP.md (This file)
└── README.md (Project documentation)
```

---

## ✅ Verification Checklist

Before going live:

- [ ] All dependencies installed: `pip install -r requirements.txt`
- [ ] Environment variables set (if using external DB)
- [ ] Logs directory exists: `mkdir logs`
- [ ] Port 8000 is available
- [ ] Port 8001 is available
- [ ] Database initialized
- [ ] SSL/HTTPS configured (for public deployment)
- [ ] Firewall rules configured

---

## 🐛 Troubleshooting

**Error: Port already in use**
```bash
# Find what's using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID)
taskkill /PID <PID> /F
```

**Error: ModuleNotFoundError**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**Error: Database locked**
```bash
# SQLite can have issues. Check file permissions
# Or specify a different database
```

---

## 📈 Monitoring

### Check Server Status
```bash
python -c "import requests; print(requests.get('http://localhost:8000').json())"
```

### View Logs (Real-time)
```bash
# Verification logs
Get-Content logs/verification.log -Wait -Tail 20

# Access logs
Get-Content logs/access.log -Wait -Tail 10
```

### Performance Stats
```bash
# See active Gunicorn processes
tasklist | findstr gunicorn

# See system resource usage
systeminfo
```

---

## 🌐 Deploy to Production Server

See [DEPLOYMENT.md](DEPLOYMENT.md) for:
- Heroku deployment
- Docker containerization
- Cloud platform setup
- Network accessibility

---

## 💡 Tips for Production

1. **Use environment variables** for sensitive data
2. **Monitor logs regularly** for errors
3. **Set up automated backups** for the database
4. **Use a reverse proxy** (Nginx) for SSL/HTTPS
5. **Scale horizontally** with multiple servers if needed
6. **Keep dependencies updated** for security

---

**Your verification system is now production-ready!** 🎉

For more information, see [DEPLOYMENT.md](DEPLOYMENT.md)  
