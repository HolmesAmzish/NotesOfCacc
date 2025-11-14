import numpy as np
import matplotlib.pyplot as plt

# 参数
Ts = 1.0  # 符号周期
alpha = 1.0  # 滚降因子
sps = 20  # 每符号采样点数
t_duration = 4 * Ts  # 脉冲持续时间（截断范围），中心在 0
t_pulse = np.linspace(-t_duration/2, t_duration/2, int(t_duration/Ts * sps) + 1)

# 升余弦脉冲定义
def raised_cosine(t, Ts, alpha):
    t = np.asarray(t)
    y = np.zeros_like(t)
    # 避免除零
    idx0 = np.abs(t) < 1e-8
    idx1 = np.abs(np.abs(t) - Ts/(2*alpha)) < 1e-8
    idx_other = ~(idx0 | idx1)
    
    # t=0 点
    y[idx0] = 1.0
    # 奇异点 t = ± Ts/(2α)
    if alpha != 0:
        t_special = Ts / (2*alpha)
        y[np.abs(t - t_special) < 1e-8] = (np.pi/4) * np.sinc(1/(2*alpha))
        y[np.abs(t + t_special) < 1e-8] = (np.pi/4) * np.sinc(1/(2*alpha))
    
    # 一般情况
    t_other = t[idx_other]
    y[idx_other] = np.sinc(t_other / Ts) * np.cos(np.pi * alpha * t_other / Ts) \
                   / (1 - (2 * alpha * t_other / Ts)**2)
    return y

# 生成脉冲
pulse = raised_cosine(t_pulse, Ts, alpha)
# 归一化到峰值1
pulse /= np.max(pulse)

# 二进制序列
bits = [1, 0, 1, 0, 0, 1, 1]
n_bits = len(bits)

# 生成基带信号
total_time = n_bits * Ts
t_signal = np.linspace(0, total_time, int(total_time/Ts * sps), endpoint=False)
signal = np.zeros_like(t_signal)

for i, bit in enumerate(bits):
    # 每个符号的幅值: 1 -> +1, 0 -> -1
    amp = 1 if bit == 1 else -1
    # 脉冲中心时间
    center_time = (i + 0.5) * Ts
    # 脉冲时间轴相对于中心
    t_rel = t_signal - center_time
    # 只取在脉冲范围内的点
    valid = np.abs(t_rel) <= t_duration/2
    # 将脉冲加到信号上
    for j in range(len(t_signal)):
        if valid[j]:
            # 找到脉冲中对应的时间索引
            idx_pulse = np.argmin(np.abs(t_pulse - t_rel[j]))
            signal[j] += amp * pulse[idx_pulse]

# 画眼图函数
def plot_eye_diagram(t, s, T0, title):
    T_total = t[-1] + t[1] - t[0]
    n_segments = int(T_total / T0)
    # 每段内的点数
    sps_segment = int(T0 / (t[1]-t[0]))
    plt.figure(figsize=(10, 5))
    for start_idx in range(0, len(t), sps_segment):
        if start_idx + sps_segment > len(t):
            break
        t_seg = t[start_idx:start_idx+sps_segment] - t[start_idx]
        s_seg = s[start_idx:start_idx+sps_segment]
        plt.plot(t_seg, s_seg, 'b-', alpha=0.5, linewidth=0.8)
    plt.xlabel('Time (mod T0)')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, T0)
    # 标记最佳抽样时刻和判决门限
    # 对于双极性信号，最佳采样时刻在 T0/2 附近（对 T0=Ts 来说就是符号中间）
    best_sample_time = T0 / 2
    plt.axvline(best_sample_time, color='red', linestyle='--', alpha=0.7, label='Best sample time')
    # 判决门限是0
    plt.axhline(0, color='green', linestyle='--', alpha=0.7, label='Decision threshold')
    plt.legend()
    plt.show()

# 绘制眼图
plot_eye_diagram(t_signal, signal, T0=Ts, title=f'Eye Diagram ($T_0 = T_s$, α={alpha})')
plot_eye_diagram(t_signal, signal, T0=2*Ts, title=f'Eye Diagram ($T_0 = 2T_s$, α={alpha})')

# 比较两种眼图的最佳抽样时刻、判决门限和噪声容限
print("比较：")
print(f"1. T0 = Ts:")
print("   - 最佳抽样时刻：每个符号周期的中间（T0/2）")
print("   - 判决门限电平：0")
print("   - 噪声容限：眼的垂直张开高度的一半（对于无码间串扰的理想升余弦，峰值=1，噪声容限=1）")

print(f"2. T0 = 2Ts:")
print("   - 显示两个符号周期，可能看到多个眼")
print("   - 最佳抽样时刻：每个符号的中间（但眼图可能重叠，需分开看每个眼）")
print("   - 判决门限电平：0（对双极性信号）")
print("   - 噪声容限：与T0=Ts时相同，因为信号性质未变")