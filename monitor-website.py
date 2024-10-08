import requests
import paramiko
import smtplib
import os
from dotenv import load_dotenv  # pip install python-dotenv
import linode_api4
import time
import schedule

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
LINODE_TOKEN = os.getenv('LINODE_TOKEN')

def restart_server_and_container():
    # restart linode server
    print('Rebooting the server...')
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instance, 64975557)
    nginx_server.reboot()

    # restart the application
    while True:
        nginx_server = client.load(linode_api4.Instance, 64975557)
        if nginx_server.status == 'running':
            time.sleep(5)
            restart_container()
            break



def send_notification(email_msg):
    print('Sending an email')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

def restart_container():
    print('Restarting the aplication...Application restarted')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoPolicy())
    print("Connecting to server with ssh")
    ssh.connect(hostname='172-105-245-110', username='root', key_filename='/Users/anapedra/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('docker start e3ca13edebef')
    print(stdout.readlines())
    ssh.close()
    
def monitor_application():
    try:
        response = requests.get('http://172-105-245-110.ip.linodeusercontent.com:8080/')

        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            msg = f"Application returned {response.status_code}"
            send_notification(msg)
            restart_container()

    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = "Application not accessible at all."
        send_notification(msg)
        restart_server_and_container()

schedule.every(5).minutes.do(monitor_application)

while True:
    shcedule.run_pending()

    
        

