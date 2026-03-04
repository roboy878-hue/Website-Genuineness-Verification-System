# Production Deployment Guide

## Website Genuineness Verification System - Deployment Instructions

---

## 📋 Table of Contents
1. [Local Production Setup](#local-production-setup)
2. [Cloud Deployment (Heroku)](#cloud-deployment-heroku)
3. [Docker Deployment](#docker-deployment)
4. [Network Accessibility](#network-accessibility)
5. [Monitoring & Logs](#monitoring--logs)
6. [Troubleshooting](#troubleshooting)

---

## Local Production Setup

### Step 1: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

All dependencies including Gunicorn are now installed.

### Step 2: Start Production Server (Gunicorn)

**Option A: Using batch script (Windows)**
```bash
cd backend
start_production.bat
```

**Option B: Manual command**
```bash
gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 120 wsgi:app
```

**Option C: For development**
```bash
python app.py
```

### Step 3: Serve Frontend

Open another terminal:
```bash
cd frontend
python -m http.server 8001
```

### Configuration

Production server details:
- **Backend Port**: 8000 (Gunicorn)
- **Frontend Port**: 8001 (HTTP Server)
- **Workers**: 4 (can adjust based on CPU cores)
- **Threads**: 2 per worker
- **Timeout**: 120 seconds

---

## Cloud Deployment (Heroku)

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed
- Git installed

### Step 1: Create Heroku App

```bash
heroku create your-app-name
```

### Step 2: Configure Environment Variables

```bash
heroku config:set FLASK_ENV=production
heroku config:set FLASK_SECRET_KEY=your-secret-key-here
```

### Step 3: Deploy

```bash
git push heroku main
```

### Step 4: Scale Dyros

```bash
heroku ps:scale web=1
```

### Access Your App
```
https://your-app-name.herokuapp.com
```

---

## Docker Deployment

### Step 1: Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .
COPY frontend/ ../frontend

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "wsgi:app"]
```

### Step 2: Build Image

```bash
docker build -t website-verification:latest .
```

### Step 3: Run Container

```bash
docker run -p 5000:5000 -p 8000:8000 website-verification:latest
```

---

## Network Accessibility

### Make accessible from other devices on your network

1. Find your local IP:
```bash
ipconfig
```

2. Update frontend to use your IP instead of localhost:
   - Edit `frontend/script.js`
   - Change `http://localhost:5000` to `http://YOUR_IP:5000`

3. Access from other device:
```
http://YOUR_IP:8000
```

---

## Monitoring & Logs

### View Logs

**Backend logs:**
```bash
tail -f backend/logs/verification.log
```

**Access logs:**
```bash
tail -f backend/logs/access.log
```

### Monitor Performance

Check active workers:
```bash
ps aux | grep gunicorn
```

---

## Troubleshooting

### Port Already in Use

Find process using port:
```bash
netstat -ano | findstr :8000
```

Kill process:
```bash
taskkill /PID <PID> /F
```

### Permission Denied

Run terminal as Administrator (Windows)

### Module Not Found

Ensure you're in the correct directory and virtual environment is activated:
```bash
cd backend
pip install -r requirements.txt
```

### Connection Refused

Ensure backend is running:
```bash
python -c "import requests; print(requests.get('http://localhost:5000').json())"
```

---

## Performance Tuning

### For high traffic:

```bash
gunicorn \
  --bind 0.0.0.0:8000 \
  --workers 8 \
  --threads 4 \
  --worker-class gthread \
  --max-requests 1000 \
  --max-requests-jitter 100 \
  --timeout 180 \
  wsgi:app
```

### Environment Variables

Create `.env` file in backend:
```
FLASK_ENV=production
FLASK_DEBUG=False
DATABASE_URL=sqlite:///verification.db
WORKERS=4
THREADS=2
```

---

## Security Checklist

- [ ] Change default SECRET_KEY
- [ ] Update Flask app configuration for production
- [ ] Enable SSL/HTTPS
- [ ] Configure firewall rules
- [ ] Regular backups of database
- [ ] Monitor logs for suspicious activity
- [ ] Update dependencies regularly

---

## Support

For issues or questions:
1. Check logs: `backend/logs/verification.log`
2. Test health endpoint: `http://localhost:8000/`
3. Verify all dependencies are installed

