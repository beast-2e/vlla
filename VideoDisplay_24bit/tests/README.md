# Display scripts for the VLLA

In order to set up a script to run at startup, invoke crontab:
```
$ crontab -e
```
Then insert the line:
```
@reboot python3 /path/to/script
```

_TODO_: Write documentation for the scripts that have been written and for the vlla python module.
