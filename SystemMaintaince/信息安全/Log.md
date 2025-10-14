dmesg

`/var/log` is the central log storage directory on Linux. Every service, kernal component, and system process writes its messages here.

| File     | Description                                                                      |
| -------- | -------------------------------------------------------------------------------- |
| syslog   | The main system log -- general system messages, daemon logs, boot messages, etc. |
| auth.log | Authntication logs (logins, sudo, SSH attempts).                                 |
| kern.log | Messages from Linux kernal (hardware, drivers, etc.).                            |
|          |                                                                                  |

```bash
tail <file_name>    # Check the last 10 lines of the file
tail -n <number_of_lines> <file_name>    # Check specific lines
tail -n <number_of_lines> -f <file_name>    # Check last lines with scroll
```

dmesg

```bash
dmesg
```

journalctl s

```bash
journalctl    # Check systemctl logs
journalctl -f    # Check with auto scroll
journalctl --since <start time> (--until <end_time>)
```

```bash
journalctl --sincce "30 min ago"
journalctl --since "2025-10-13 06:55:00" --until "2025-10-13 07:25:00"
```
