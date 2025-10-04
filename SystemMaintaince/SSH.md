# OpenSSH

## Basic

### Installation and Config

The config file or sshd is `/etc/ssh/sshd_config`

### Connect to Server

```bash
ssh <username>@<remote_address> (-p <port_number)
```

*example*

```bash
ssh 192.168.0.110
ssh cacc@192.168.0.110
ssh cacc@frp.example.cn -p 6000
```



## Proxy

You can open a proxy with ssh tunnel.

```bash
ssh -L 8080:192.168.0.1:80 user@frp.arorms.com -p 6002
# Open a tunnel from 192.168.0.1:80 of server lan to localhost:8080
```



## SCP

```bash
scp -P 2222 myfile.txt user@192.168.1.100:/home/user/
```



## Security

### Password

The password of ssh is the same with local user password in `/etc/passwd`

### Security key

You can generate public key and private key to login the server, it is recommended and more secure than password authentication.

```bash
ssh-keygen
```

This command will generate key pair like `id_rsa` and `id_rsa.pub`

Then upload public key to the server if you wanna login server with pubkey.

```bash
cat <public_key> >> ~/.ssh/authrized_keys
```

Then you can login remote server without password.
