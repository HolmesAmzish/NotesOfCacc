依据虚拟机系统文件不使用图形化进行开关虚拟机

```bash
vmrun -T ws start "/home/cacc/vmware/kampfer-viii/kampfer-viii.vmx" nogui
vmrun -T ws stop "/home/cacc/vmware/kampfer-viii/kampfer-viii.vmx" soft
```

```bash
vmrun -T ws start "/home/cacc/vmware/limbo-vi/limbo-vi.vmx" nogui
vmrun -T ws stop "/home/cacc/vmware/limbo-vi/limbo-vi.vmx" soft
```

也可以通过 alias 进行快捷启动

```bash
alias "limborun"="vmrun -T ws start /home/cacc/vmware/limbo-vi/limbo-vi.vmx nogui"
alias "limbostop"="vmrun -T ws stop /home/cacc/vmware/limbo-vi/limbo-vi.vmx soft"
```



查看当前运行的虚拟机

```bash
vmrun list
```



