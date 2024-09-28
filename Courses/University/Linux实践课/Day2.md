# Linux 实训练习 - Day 2

1. 创建一个新用户（命名随意），修改其密码，请展示/etc/passwd文件中刚刚创建的用户信息，提供截图。

   ```bash
   useradd newuser
   # create new user
   
   passwd newuser
   ```

   ![image-20240626140837384](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240626140837384.png)

2. 创建一个新文件1.txt，对其权限进行修改。将其所有者更改为第一题创建的用户，让所有者拥有所有权限，所属组拥有可读可写权限，其他人拥有可读权限，请提供截图。

   ```bash
   touch 1.txt
   echo "Hello, World!" > 1.txt
   # create a file and write something
   
   chown newuser 1.txt
   # change the owner of file
   
   chmod 764 1.txt
   
   ls -l | grep 1.txt
   ```

   ![image-20240626141256038](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240626141256038.png)

3. 查找系统中的sshd_config文件所在的位置，请提供截图

   ```bash 
   find / -name "sshd_config"
   # find file at root
   ```

   ![image-20240626141332011](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240626141332011.png)

4. 安装并使用cowsay命令，使用cowsay命令，用其他动物打印出一句话

   ```bash
   whereis cowsay
   export PATH=$PATH:/usr/games
   # add to path
   
   cowsay -f dragon "The quieter you become, the more you are able to hear."
   ```

   ![image-20240626141424326](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240626141424326.png)

5. 练习：Linux有一个命令可以在屏幕上跑小火车，请自行研究后，截图完成的成果

   ```bash
   apt install sl -y
   sl -a
   ```

   ![image-20240626141451223](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240626141451223.png)

6. 创建一个新的用户组test，再创建一个新用户testIT，将用户testIT添加进去

   ```bash
   groupadd test
   useradd testIT
   usermod -aG test testIT
   id testIT
   ```

   ![image-20240626141528204](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240626141528204.png)

7. 自行创建所需的文件和用户：将file1.txt的所有者更改为user1，所属组更改为group1（使用chown命令）。使用chmod命令将file1.txt的权限设置为所有者具有读写执行权限，所属组具有读执行权限，其他用户具有读权限（权限码为755）。

   ```bash
   touch file1.txt
   groupadd group1
   useradd -g group1 user1
   chown user1:group1 file1.txt
   chmod 755 file1.txt
   
   ls -l file1.txt
   ```

   ![image-20240626141613100](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240626141613100.png)

8. 在根目录下查找所有以.txt结尾的文件。

   ```bash
   find / -type f -name "*.txt"
   ```

   输出：

   ```bash
   root@3230611081:~# find / -type f -name "*.txt"
   /usr/share/doc/python3-debianbts/THANKS.txt
   /usr/share/doc/util-linux/howto-debug.txt
   /usr/share/doc/util-linux/getopt.txt
   /usr/share/doc/util-linux/deprecated.txt
   /usr/share/doc/util-linux/PAM-configuration.txt
   /usr/share/doc/util-linux/hwclock.txt
   /usr/share/doc/util-linux/pg.txt
   /usr/share/doc/util-linux/getopt_changelog.txt
   /usr/share/doc/util-linux/howto-compilation.txt
   /usr/share/doc/util-linux/00-about-docs.txt
   /usr/share/doc/util-linux/howto-man-page.txt
   /usr/share/doc/util-linux/howto-tests.txt
   /usr/share/doc/util-linux/blkid.txt
   /usr/share/doc/util-linux/howto-build-sys.txt
   /usr/share/doc/util-linux/mount.txt
   /usr/share/doc/util-linux/modems-with-agetty.txt
   /usr/share/doc/util-linux/release-schedule.txt
   /usr/share/doc/util-linux/cal.txt
   /usr/share/doc/util-linux/col.txt
   /usr/share/doc/reportbug/HowToReportGoodBugs.txt
   /usr/share/doc/libdb5.3/build_signature_amd64.txt
   /usr/share/doc/nmap/leet-nmap-ascii-art.txt
   /usr/share/doc/busybox/syslog.conf.txt
   /usr/share/doc/mount/mount.txt
   /usr/share/doc/debian/source-unpack.txt
   /usr/share/doc/debian/bug-mailserver-refcard.txt
   /usr/share/doc/debian/bug-log-access.txt
   /usr/share/doc/publicsuffix/examples/test_psl.txt
   /usr/share/doc/openssl/HOWTO/keys.txt
   /usr/share/doc/openssl/fingerprints.txt
   /usr/share/vim/vim90/doc/os_qnx.txt
   /usr/share/vim/vim90/doc/ft_sql.txt
   /usr/share/vim/vim90/doc/quickfix.txt
   /usr/share/vim/vim90/doc/ft_context.txt
   /usr/share/vim/vim90/doc/usr_30.txt
   /usr/share/vim/vim90/doc/pattern.txt
   /usr/share/vim/vim90/doc/usr_12.txt
   /usr/share/vim/vim90/doc/usr_02.txt
   /usr/share/vim/vim90/doc/digraph.txt
   /usr/share/vim/vim90/doc/pi_zip.txt
   /usr/share/vim/vim90/doc/usr_toc.txt
   /usr/share/vim/vim90/doc/options.txt
   /usr/share/vim/vim90/doc/testing.txt
   /usr/share/vim/vim90/doc/pi_paren.txt
   /usr/share/vim/vim90/doc/usr_11.txt
   /usr/share/vim/vim90/doc/usr_50.txt
   /usr/share/vim/vim90/doc/netbeans.txt
   /usr/share/vim/vim90/doc/ft_ps1.txt
   /usr/share/vim/vim90/doc/version8.txt
   /usr/share/vim/vim90/doc/os_dos.txt
   /usr/share/vim/vim90/doc/undo.txt
   /usr/share/vim/vim90/doc/userfunc.txt
   /usr/share/vim/vim90/doc/version4.txt
   /usr/share/vim/vim90/doc/usr_08.txt
   /usr/share/vim/vim90/doc/sponsor.txt
   /usr/share/vim/vim90/doc/usr_04.txt
   /usr/share/vim/vim90/doc/cmdline.txt
   /usr/share/vim/vim90/doc/os_risc.txt
   /usr/share/vim/vim90/doc/ft_mp.txt
   /usr/share/vim/vim90/doc/usr_90.txt
   /usr/share/vim/vim90/doc/insert.txt
   /usr/share/vim/vim90/doc/usr_41.txt
   /usr/share/vim/vim90/doc/starting.txt
   /usr/share/vim/vim90/doc/os_win32.txt
   /usr/share/vim/vim90/doc/fold.txt
   /usr/share/vim/vim90/doc/os_beos.txt
   /usr/share/vim/vim90/doc/os_mac.txt
   /usr/share/vim/vim90/doc/eval.txt
   /usr/share/vim/vim90/doc/debug.txt
   /usr/share/vim/vim90/doc/helphelp.txt
   /usr/share/vim/vim90/doc/editing.txt
   /usr/share/vim/vim90/doc/windows.txt
   /usr/share/vim/vim90/doc/farsi.txt
   /usr/share/vim/vim90/doc/if_tcl.txt
   /usr/share/vim/vim90/doc/howto.txt
   /usr/share/vim/vim90/doc/usr_21.txt
   /usr/share/vim/vim90/doc/sign.txt
   /usr/share/vim/vim90/doc/version9.txt
   /usr/share/vim/vim90/doc/russian.txt
   /usr/share/vim/vim90/doc/syntax.txt
   /usr/share/vim/vim90/doc/ft_rust.txt
   /usr/share/vim/vim90/doc/intro.txt
   /usr/share/vim/vim90/doc/rileft.txt
   /usr/share/vim/vim90/doc/filetype.txt
   /usr/share/vim/vim90/doc/usr_07.txt
   /usr/share/vim/vim90/doc/autocmd.txt
   /usr/share/vim/vim90/doc/if_mzsch.txt
   /usr/share/vim/vim90/doc/vi_diff.txt
   /usr/share/vim/vim90/doc/os_haiku.txt
   /usr/share/vim/vim90/doc/mlang.txt
   /usr/share/vim/vim90/doc/usr_20.txt
   /usr/share/vim/vim90/doc/usr_09.txt
   /usr/share/vim/vim90/doc/channel.txt
   /usr/share/vim/vim90/doc/if_cscop.txt
   /usr/share/vim/vim90/doc/if_lua.txt
   /usr/share/vim/vim90/doc/os_vms.txt
   /usr/share/vim/vim90/doc/repeat.txt
   /usr/share/vim/vim90/doc/spell.txt
   /usr/share/vim/vim90/doc/usr_40.txt
   /usr/share/vim/vim90/doc/if_perl.txt
   /usr/share/vim/vim90/doc/os_os2.txt
   /usr/share/vim/vim90/doc/pi_netrw.txt
   /usr/share/vim/vim90/doc/usr_32.txt
   /usr/share/vim/vim90/doc/visual.txt
   /usr/share/vim/vim90/doc/usr_10.txt
   /usr/share/vim/vim90/doc/usr_29.txt
   /usr/share/vim/vim90/doc/message.txt
   /usr/share/vim/vim90/doc/various.txt
   /usr/share/vim/vim90/doc/version7.txt
   /usr/share/vim/vim90/doc/motion.txt
   /usr/share/vim/vim90/doc/quickref.txt
   /usr/share/vim/vim90/doc/gui_w32.txt
   /usr/share/vim/vim90/doc/os_390.txt
   /usr/share/vim/vim90/doc/change.txt
   /usr/share/vim/vim90/doc/usr_51.txt
   /usr/share/vim/vim90/doc/usr_26.txt
   /usr/share/vim/vim90/doc/usr_31.txt
   /usr/share/vim/vim90/doc/usr_24.txt
   /usr/share/vim/vim90/doc/version6.txt
   /usr/share/vim/vim90/doc/usr_28.txt
   /usr/share/vim/vim90/doc/ft_ada.txt
   /usr/share/vim/vim90/doc/os_unix.txt
   /usr/share/vim/vim90/doc/if_ruby.txt
   /usr/share/vim/vim90/doc/usr_05.txt
   /usr/share/vim/vim90/doc/gui.txt
   /usr/share/vim/vim90/doc/usr_06.txt
   /usr/share/vim/vim90/doc/os_msdos.txt
   /usr/share/vim/vim90/doc/tagsrch.txt
   /usr/share/vim/vim90/doc/usr_44.txt
   /usr/share/vim/vim90/doc/usr_03.txt
   /usr/share/vim/vim90/doc/pi_gzip.txt
   /usr/share/vim/vim90/doc/textprop.txt
   /usr/share/vim/vim90/doc/todo.txt
   /usr/share/vim/vim90/doc/vim9.txt
   /usr/share/vim/vim90/doc/usr_43.txt
   /usr/share/vim/vim90/doc/tabpage.txt
   /usr/share/vim/vim90/doc/usr_23.txt
   /usr/share/vim/vim90/doc/hangulin.txt
   /usr/share/vim/vim90/doc/usr_45.txt
   /usr/share/vim/vim90/doc/mbyte.txt
   /usr/share/vim/vim90/doc/usr_25.txt
   /usr/share/vim/vim90/doc/usr_01.txt
   /usr/share/vim/vim90/doc/tips.txt
   /usr/share/vim/vim90/doc/terminal.txt
   /usr/share/vim/vim90/doc/arabic.txt
   /usr/share/vim/vim90/doc/recover.txt
   /usr/share/vim/vim90/doc/uganda.txt
   /usr/share/vim/vim90/doc/pi_vimball.txt
   /usr/share/vim/vim90/doc/vim9class.txt
   /usr/share/vim/vim90/doc/version5.txt
   /usr/share/vim/vim90/doc/usr_27.txt
   /usr/share/vim/vim90/doc/os_mint.txt
   /usr/share/vim/vim90/doc/quotes.txt
   /usr/share/vim/vim90/doc/popup.txt
   /usr/share/vim/vim90/doc/help.txt
   /usr/share/vim/vim90/doc/term.txt
   /usr/share/vim/vim90/doc/ft_raku.txt
   /usr/share/vim/vim90/doc/if_pyth.txt
   /usr/share/vim/vim90/doc/pi_getscript.txt
   /usr/share/vim/vim90/doc/gui_x11.txt
   /usr/share/vim/vim90/doc/builtin.txt
   /usr/share/vim/vim90/doc/print.txt
   /usr/share/vim/vim90/doc/map.txt
   /usr/share/vim/vim90/doc/debugger.txt
   /usr/share/vim/vim90/doc/index.txt
   /usr/share/vim/vim90/doc/scroll.txt
   /usr/share/vim/vim90/doc/workshop.txt
   /usr/share/vim/vim90/doc/diff.txt
   /usr/share/vim/vim90/doc/usr_52.txt
   /usr/share/vim/vim90/doc/if_sniff.txt
   /usr/share/vim/vim90/doc/if_ole.txt
   /usr/share/vim/vim90/doc/indent.txt
   /usr/share/vim/vim90/doc/pi_tar.txt
   /usr/share/vim/vim90/doc/usr_42.txt
   /usr/share/vim/vim90/doc/hebrew.txt
   /usr/share/vim/vim90/doc/usr_22.txt
   /usr/share/vim/vim90/doc/pi_logipat.txt
   /usr/share/vim/vim90/doc/os_amiga.txt
   /usr/share/vim/vim90/doc/pi_spec.txt
   /usr/share/vim/vim90/doc/develop.txt
   /usr/share/vim/vim90/doc/remote.txt
   /usr/share/vim/vim90/pack/dist/opt/matchit/doc/matchit.txt
   /usr/share/perl/5.36.0/Unicode/Collate/allkeys.txt
   /usr/share/perl/5.36.0/Unicode/Collate/keys.txt
   /usr/share/perl/5.36.0/unicore/Blocks.txt
   /usr/share/perl/5.36.0/unicore/SpecialCasing.txt
   /usr/share/perl/5.36.0/unicore/NamedSequences.txt
   /usr/share/nmap/nselib/data/http-folders.txt
   /usr/share/nmap/nselib/data/rtsp-urls.txt
   /usr/share/nmap/nselib/data/tftplist.txt
   /usr/share/nmap/nselib/data/enterprise_numbers.txt
   /usr/share/nmap/nselib/data/jdwp-class/README.txt
   /usr/share/netpbm/rgb.txt
   /usr/share/libcaca/caca.txt
   /usr/share/sqlmap/data/txt/user-agents.txt
   /usr/share/sqlmap/data/txt/common-columns.txt
   /usr/share/sqlmap/data/txt/common-files.txt
   /usr/share/sqlmap/data/txt/common-tables.txt
   /usr/share/sqlmap/data/txt/common-outputs.txt
   /usr/share/sqlmap/data/txt/keywords.txt
   /usr/share/sqlmap/data/txt/smalldict.txt
   /usr/lib/python3.11/LICENSE.txt
   /usr/lib/python3/dist-packages/certifi-2022.9.24.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/certifi-2022.9.24.egg-info/dependency_links.txt
   /usr/lib/python3/dist-packages/charset_normalizer-3.0.1.dist-info/entry_points.txt
   /usr/lib/python3/dist-packages/charset_normalizer-3.0.1.dist-info/top_level.txt
   /usr/lib/python3/dist-packages/python_magic-0.4.26.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/python_magic-0.4.26.egg-info/dependency_links.txt
   /usr/lib/python3/dist-packages/chardet-5.1.0.dist-info/entry_points.txt
   /usr/lib/python3/dist-packages/chardet-5.1.0.dist-info/top_level.txt
   /usr/lib/python3/dist-packages/idna-3.3.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/idna-3.3.egg-info/dependency_links.txt
   /usr/lib/python3/dist-packages/python_debianbts-4.0.1.dist-info/entry_points.txt
   /usr/lib/python3/dist-packages/python_debianbts-4.0.1.dist-info/top_level.txt
   /usr/lib/python3/dist-packages/python_apt-2.6.0.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/python_apt-2.6.0.egg-info/dependency_links.txt
   /usr/lib/python3/dist-packages/pycurl-7.45.2.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/pycurl-7.45.2.egg-info/dependency_links.txt
   /usr/lib/python3/dist-packages/requests-2.28.1.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/requests-2.28.1.egg-info/requires.txt
   /usr/lib/python3/dist-packages/requests-2.28.1.egg-info/dependency_links.txt
   /usr/lib/python3/dist-packages/httplib2-0.20.4.dist-info/top_level.txt
   /usr/lib/python3/dist-packages/urllib3-1.26.12.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/urllib3-1.26.12.egg-info/requires.txt
   /usr/lib/python3/dist-packages/urllib3-1.26.12.egg-info/dependency_links.txt
   /usr/lib/python3/dist-packages/reportbug-12.0.0.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/reportbug-12.0.0.egg-info/dependency_links.txt
   /usr/lib/python3/dist-packages/python_debian-0.1.49.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/python_debian-0.1.49.egg-info/requires.txt
   /usr/lib/python3/dist-packages/python_debian-0.1.49.egg-info/dependency_links.txt
   /usr/lib/python3/dist-packages/six-1.16.0.egg-info/top_level.txt
   /usr/lib/python3/dist-packages/six-1.16.0.egg-info/dependency_links.txt
   /var/cache/dictionaries-common/ispell-dicts-list.txt
   /etc/X11/rgb.txt
   /root/file1.txt
   /root/1.txt
   /root/butt.txt
   /root/freebsd_logo.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/node_modules/@xterm/addon-image/lib/addon-image.js.LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/node_modules/vscode-oniguruma/NOTICES.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/node_modules/vscode-oniguruma/LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/node_modules/@vscode/vscode-languagedetection/dist/lib/index.js.LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/node_modules/@vscode/deviceid/owners.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/node_modules/@vscode/deviceid/LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/git/dist/main.js.LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/ms-vscode.js-debug-companion/LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/ms-vscode.js-debug-companion/ThirdPartyNotices.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/ms-vscode.vscode-js-profile-table/ThirdPartyNotices.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/markdown-language-features/server/dist/node/workerMain.js.LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/ms-vscode.js-debug/LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/ms-vscode.js-debug/ThirdPartyNotices.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/npm/dist/npmMain.js.LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/configuration-editing/dist/configurationEditingMain.js.LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/github/testWorkspace/x.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/github/testWorkspace/docs/PULL_REQUEST_TEMPLATE/x.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/github/testWorkspace/.github/PULL_REQUEST_TEMPLATE/x.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/github/testWorkspace/PULL_REQUEST_TEMPLATE/x.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/server/extensions/github/dist/extension.js.LICENSE.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/log.txt
   /root/.vscode-server/cli/servers/Stable-5437499feb04f7a586f677b155b039bc2b3669eb/pid.txt
   /root/.vscode-server/data/User/History/2e6c2d8a/jbHL.txt
   /root/.vscode-server/data/User/History/2e6c2d8a/5DVh.txt
   /root/.vscode-server/data/User/History/2e6c2d8a/5Eem.txt
   /root/.vscode-server/data/User/History/2e6c2d8a/Q9Jb.txt
   /root/.vscode-server/data/User/History/-61d7d606/EfNA.txt
   /root/.vscode-server/extensions/ms-ceintl.vscode-language-pack-zh-hans-1.90.2024061209/ThirdPartyNotices.txt
   ```

9. 复制/etc/passwd文件到当前用户的家目录，并重命名为my_passwd.txt。将my_passwd.txt移动到/tmp目录下。

   ```bash
   cp /etc/passwd ~
   mv passwd my_passwd.txt
   mv ~/my_passwd.txt /tmp
   ```

   ![image-20240626141911880](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240626141911880.png)

10. 使用echo命令将“This line was added using echo.”追加到example.txt文件的末尾。使用sed命令将example.txt文件中所有的“old”替换为“new”。

    ```bash
    touch example.txt
    echo "This line was added using echo." > example.txt
    sed 's/old/new/g' example.txt
    ```
    
    ![image-20240626143531515](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240626143531515.png)

