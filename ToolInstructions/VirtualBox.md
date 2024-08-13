```bash
vboxmanage list vms
# list all the virtual machines
vboxmanage list vms --long
vboxmanage list runningvms

vboxmanage showvminfo "vm_name"

vboxmanage list hdds
# list all virtual hard disk

vboxmanage list hostonlyifs

vboxmanage startvm "vm_name" --type headless
vboxmanage controlvm "vm_name" acpipowerbutton
vboxmanage controlvm "vm_name" poweroff
```

