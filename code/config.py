#!/usr/bin/env python3

# Set up below items
# Lines started with # will be ignored

### SERVER LOGIN CREDITALS ###
# if your SSH config exists - write hostname from it here. or set it to None or '' to use creditals below
sshconfig_hostname = None

# SFTP server name
sftpserver_hostname = 'localhost'   # str (string)
# SFTP server username
sftpserver_user = 'nobody'          # str 
# SFTP server port (same for SSH)
sftpserver_port = 22                # int (intiger)



### MESSAGER CREDITALS ###
messager_username = 'Mama-ama-criminal'   # str




### ----- don't touch! it check is config valid ----- ###
if hostname:
    assert isinstance(sshconfig_hostname, (str, None))
else:
    assert isinstance(sftpserver_hostname, str)
    assert isinstance(sftpserver_user, str)
    assert isinstance(sftpserver_port, int)

    assert sftpserver_port > 1
    assert sftpserver_port < 65535

assert isinstance(messager_username, str)