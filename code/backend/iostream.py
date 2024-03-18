#!/usr/bin/env python3

import subprocess
import json
from datetime import datetime
import time
import os
import config

class IOStream:
    def __init__(self):
        if config.sshconfig_hostname:
            self.sftp_command_conf = ['sftp', config.sshconfig_hostname]
        else:
            self.sftp_command_conf = [
                'sftp', '-p', config.sftpserver_port, f'{config.sftpserver_user}@{config.sftpserver_hostname}'
                ]

        # self.sftp_proc = subprocess.Popen(['sftp', 'enigma'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def get(self, need_print: bool=True) -> dict:
        sftp_proc = subprocess.Popen(['sftp', 'enigma'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sftp_proc.stdin.write('get messages.json'.encode())
        sftp_proc.communicate()
        del sftp_proc

        if os.path.exists('./messages.json'):
            with open('messages.json', 'r', encoding='utf-8') as file:
                content = json.load(fp=file)
        else:
            print('Check your server config and is it avaible')
            return

        if not need_print:
            return content
        elif not content:
            print('No messages here.')
            return content

        for message_id, payload in content.items():
            print(f'ID: {message_id}; User: {payload["user"]}; Time: {payload["time"]}. Content:\n{payload["content"]}\n')

        os.remove('messages.json')
        return content
    
    def put(self, message: str) -> None:
        content = self.get(need_print=False)
        
        payload = {
            "user": config.messager_username,
            "time": datetime.now().strftime('%d.%m.%Y %H:%M'),
            "content": message
        }
        
        if not content:
            content['1'] = payload
        else:
            content[str( int(list(content)[-1]) + 1 )] = payload
        with open('messages.json', 'w', encoding='utf-8') as file:
            json.dump(content, file, indent=4)
        
        sftp_proc = subprocess.Popen(['sftp', 'enigma'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sftp_proc.stdin.write('put messages.json'.encode())
        sftp_proc.communicate()
        del sftp_proc