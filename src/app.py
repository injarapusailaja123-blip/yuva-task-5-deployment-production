from flask import Flask, jsonify
import datetime

app = Flask(__name__)
# Yuva Intern - Task 5 - Deployment and Production
# Name: Injarapu Sailaja

DEPLOY_LOG = [
    {"step": "1. Code Commit", "status": "SUCCESS", "time": "10:00 AM"},
    {"step": "2. Build & Test", "status": "SUCCESS", "time": "10:05 AM"},
    {"step": "3. Deploy to Staging", "status": "SUCCESS", "time": "10:12 AM"},
    {"step": "4. Final Testing in Staging", "status": "SUCCESS", "time": "10:20 AM"},
    {"step": "5. Deploy to Production", "status": "SUCCESS - LIVE", "time": "10:30 AM"},
]

@app.route('/')
def dashboard():
    logs = "".join([f"<tr><td>{l['step']}</td><td>{l['time']}</td><td><b>{l['status']}</b></td></tr>" for l in DEPLOY_LOG])
    return f"""
    <html><head><title>Deployment & Production - Sailaja</title>
    <style>
    body{{font-family:Arial;background:#0f172a;color:white;padding:15px;text-align:center}}
    h1{{color:#4ade80}} .box{{background:#1e293b;padding:15px;border-radius:12px;margin:10px}}
    .live{{background:#14532d;padding:12px;border-radius:10px;font-weight:bold}}
    table{{width:100%;background:#1e293b;border-radius:10px;border-collapse:collapse;margin-top:10px}}
    th,td{{padding:10px;border-bottom:1px solid #334155}}
    </style></head><body>
    <h1>DEPLOYMENT & PRODUCTION</h1>
    <p>Author: Injarapu Sailaja | Python Developer Intern | Yuva Intern</p>
    <div class="live">PRODUCTION IS LIVE - App is Available to Real Users!</div>
    <div class="box"><b>Staging:</b> staging.myapp.com - For Testing | <b>Production:</b> www.myapp.com - For Real Users</div>
    <div class="box"><b>Monitoring:</b> CPU 42% | Memory 55% | Uptime 99.9% | Errors: 0</div>
    <div class="box"><b>Rollback Ready:</b> If any issue, Previous Version v1.0 can be restored in 2 mins</div>
    <table><tr><th>Pipeline Step</th><th>Time</th><th>Status</th></tr>{logs}</table>
    <p>Deployment Date: {datetime.date.today()} | Version: v2.0 | Environment: Production</p>
    </body></html>
    """

@app.route('/api/deployment-status')
def status():
    return jsonify({"environment":"production","version":"v2.0","status":"LIVE","uptime":"99.9%","monitoring":"Active","rollback_available":True,"deployed_by":"Injarapu Sailaja"})

@app.route('/api/logs')
def logs():
    return jsonify({"logs": DEPLOY_LOG, "message": "No errors found in production logs"})

if __name__ == '__main__':
    app.run(debug=True)