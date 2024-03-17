#!/usr/bin/env python3

import subprocess
import json
import config

class IOStream:
    def __init__(self):
        if config.sshconfig_hostname:
            self.sftp_command_conf = ['sftp', config.sshconfig_hostname]
        else:
            self.sftp_command_conf = [
                'sftp', '-p', config.sftpserver_port, f'{config.sftpserver_user}@{config.sftpserver_hostname}'
                ]

    def get(self, need_print: bool=True) -> dict:
        subprocess.call(['echo', 'get messages.json', '|'].extend(self.sftp_command_conf))

        with open('messages.json', 'r', encoding='utf-8') as file:
            content = json.load(fp=file)

        for message_id in content: pass
    
    def put(self, content: str) -> None:
        content = self.get(need_print=False)
        