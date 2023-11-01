import schedule
import time
import subprocess

def run_script():
    subprocess.run(["python", "/workspaces/WebScraping/cron.py", "-o", "/workspaces/WebScraping/result.log"])

schedule.every(3).seconds.do(run_script)
Continuar = True
while Continuar:
    schedule.run_pending()
    time.sleep(1)
