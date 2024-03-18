#!/usr/bin/env python3

# Set up below items
# Lines started with # will be ignored

### SERVER LOGIN CREDITALS ###
# if your SSH config exists - write hostname from it here. or set it to None or '' to use creditals below
sshconfig_hostname = None

# SFTP server name. Must be string
sftpserver_hostname = 'localhost'
# SFTP server username. Must be string
sftpserver_user = 'nobody'
# SFTP server port (same for SSH). Must be intiger from 1 to 65535
sftpserver_port = 22



### MESSAGER CREDITALS ###
# Your username. Must be string
messager_username = 'Mama-ama-criminal'



### ----- Don't touch! It check is config valid ----- ###
if sshconfig_hostname:
    assert isinstance(sshconfig_hostname, str|None), 'SSH config hostname'
else:
    assert isinstance(sftpserver_hostname, str), f'SFTP Hostname. Must be str, but get {type(sftpserver_hostname)}'
    assert isinstance(sftpserver_user, str), f'SFTP User. Must be str, but get {type(sftpserver_user)}'
    assert isinstance(sftpserver_port, int), f'SFTP Port. Must be int from 1 to 65535, but get {type(sftpserver_port)}'

    assert sftpserver_port >= 1, 'SFTP Port. Must be int from 1 to 65535'
    assert sftpserver_port <= 65535, 'SFTP Port. Must be int from 1 to 65535'

    sftpserver_port = str(sftpserver_port)

assert isinstance(messager_username, str), f'Messager username must be str, but get {type(messager_username)}'


if __name__ == '__main__':
    print('Config is valid.')
