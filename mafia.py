import os
import subprocess as sub
import time
print('If there is an error in any tool other than Mafia, then run this commands.')
print('pkg uninstall python && pkg install python')
time.sleep(1.5)
sub.run(['pkg', 'uninstall', 'python'])
sub.run(['pkg', 'install', 'python'])
os.system('git pull')
os.system('chmod 777 MAFIA')
os.system('./MAFIA')
