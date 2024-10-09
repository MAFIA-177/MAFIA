import os
import subprocess as sub

sub.run(['pkg', 'uninstall', 'python'])
sub.run(['pkg', 'install', 'python'])
os.system('git pull')
os.system('chmod 777 MAFIA')
os.system('./MAFIA')
