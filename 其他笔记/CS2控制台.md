# Counter Strike 2 控制台指令

## 跳过热身和重新开始

```c
mp_warmup_end 
mp_restartgame 1 
```



```c
ent_fire weapon_knife changesubclass 508
ent_fire weapon_knife changesubclass 508
ent_fire weapon_knife changesubclass 508
```





## 自定义地图

```c
map de_inferno loopback=0; 
game_type 0;game_mode 2 
```

| mode       | game_type | game_mode |
| ---------- | --------- | --------- |
| wingman    | 0         | 2         |
| deathmatch | 1         | 2         |
| competive  | 0         | 1         |

```c
sv_cheats 1 //开启作弊
sv_grenade_trajectory_prac_pipreview 1 // 道具落点查看
ammo_grenade limit total 6 // 携带道具数量限制
sv_infinite_ammo 1 // [开启]无限子弹、道具
mp_buy_anywhere 1 // [开启]在任意处购买
sv_grenade_trajectory_prac_trailtime 8 // 道具轨迹持续时间(s)
bind j "noclip" // 飞行
bind n "sv_rethrow_last_grenade"// N 重丢上一个道具
mp_warmuptime @ // 热身时间(s)
bot_stop 1 // bot静止
mp_freezetime  // 回合开始前冻结时间(s)
mp_startmoney 16 // 初始金钱
mp_buytime 99999 // 购买时间(s)
mp_restartgame 1 // 重新开始游戏
mp_respawn_on_death_ct 1;mp_respawn_on death_t 1 //无限复活
sv_infinite ammo 1 //弹药道具无限
mp_ignore_round_win_conditions 1 //回合不结束
```

sv_cheats true 

nolicp 

## 视角

niko持枪视角：viewmodel_fov 65; viewmodel_offset_x 2; viewmodel_offset_y 1.5; viewmodel_offset_z -1; viewmodel_presetpos 0; cl_viewmodel_shift_left_amt 1.5; cl_viewmodel_shift_right_amt 0.75; viewmodel_recoil 0; cl_righthand 1 

# Counter Strike Global Offensive
```c
game_type 1;game_mode 1 

game_type 0;game_mode 0 

mp_warmup_end 

mp_maxrounds 

mp_round_restart_delay 

mp_fresszetime 

mp_roundtime_defuse 

mp_damage_headshot_only 

game_type 0;game_mode 0;map de_dust 

game_type 0;game_mode 0;map de_aztec 

mp_round_restart_delay 0.01; mp_freezetime 0.01; mp_roundtime_defuse0.06; mp_maxrounds 200 

mp_maxmoney 16000

mp_roundtime_defuse 60

mp_startmoney 16000

mp_buytime 16000

mp_buy_anywhere 1

mp_autoteambalance 0

mp_freezetime 0

sv_cheats 1

ammo_grenade_limit_total 5

sv_grenade_trajectory "1"

sv_grenade_trajectory_time "40"
sv_showimpacts 1

sv_infinite_ammo 1

GOD; 

mp_restartgame 1

bot_add ct

bot_stop 1

bind "uparrow" "sv_rethrow_last_grenade 1"

bind "downarrow" "noclip"

bind "leftarrow" "bot_place"

bind "rightarrow" "bot_add ct"
```