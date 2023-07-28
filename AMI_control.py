import sys
import subprocess
import telnetlib
import time
import mysql.connector


def login (action_id, username = 'admin', password = 'amp111'):
    ami_resp = b'Asterisk Call Manager/'
    output = telnetObj.read_until(ami_resp)
    command_login = 'Login'
    action_id += 1



