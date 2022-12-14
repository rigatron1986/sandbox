import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(hostname="192.168.101.175", username='pi', password='admin@321')
stdin, stdout, stderr = client.exec_command('screen -ls')
out = stdout.read().decode('utf-8')
err = stderr.read().decode('utf-8')
client.close()
print(out)
