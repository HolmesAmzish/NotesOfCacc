import matplotlib.pyplot as plt
import numpy as np

# Binary sequence
data = [1, 0, 0, 1, 0, 1]
n_bits = len(data)
bit_duration = 1  # Duration of each bit
samples_per_bit = 100  # Samples per bit

# Create time axis
total_time = n_bits * bit_duration
t = np.linspace(0, total_time, n_bits * samples_per_bit, endpoint=False)

# 1. Clock signal
clock_signal = []
for i in range(n_bits):
    for j in range(samples_per_bit):
        # Clock: high in first half, low in second half of each bit period
        if j < samples_per_bit / 2:
            clock_signal.append(1)
        else:
            clock_signal.append(0)

# 2. Data signal (for reference)
data_signal = []
for bit in data:
    data_signal.extend([bit] * samples_per_bit)

# 3. Unipolar NRZ
unipolar_nrz = []
for bit in data:
    if bit == 1:
        unipolar_nrz.extend([1] * samples_per_bit)
    else:
        unipolar_nrz.extend([0] * samples_per_bit)

# 4. Bipolar NRZ
bipolar_nrz = []
for bit in data:
    if bit == 1:
        bipolar_nrz.extend([1] * samples_per_bit)
    else:
        bipolar_nrz.extend([-1] * samples_per_bit)

# 5. Unipolar RZ
unipolar_rz = []
for bit in data:
    for j in range(samples_per_bit):
        if bit == 1 and j < samples_per_bit / 2:
            unipolar_rz.append(1)
        else:
            unipolar_rz.append(0)

# 6. Bipolar RZ
bipolar_rz = []
for bit in data:
    for j in range(samples_per_bit):
        if bit == 1 and j < samples_per_bit / 2:
            bipolar_rz.append(1)
        elif bit == 0 and j < samples_per_bit / 2:
            bipolar_rz.append(-1)
        else:
            bipolar_rz.append(0)

# 7. Manchester code (IEEE standard: 1=high-to-low, 0=low-to-high)
manchester = []
for bit in data:
    for j in range(samples_per_bit):
        if j < samples_per_bit / 2:
            if bit == 1:
                manchester.append(1)
            else:
                manchester.append(0)
        else:
            if bit == 1:
                manchester.append(0)
            else:
                manchester.append(1)

# Create figure
fig, axes = plt.subplots(7, 1, figsize=(6, 10))
fig.suptitle('Line Coding Schemes for Binary Sequence: 100101', fontsize=16, fontweight='bold')

# Plot clock signal
axes[0].plot(t, clock_signal, 'r-', linewidth=2)
axes[0].set_ylabel('Clock', fontsize=12)
axes[0].set_ylim(-0.5, 1.5)
axes[0].grid(True, alpha=0.3)

# Plot data signal
axes[1].step(t, data_signal, 'b-', where='post', linewidth=2)
axes[1].set_ylabel('Data', fontsize=12)
axes[1].set_ylim(-0.5, 1.5)
axes[1].grid(True, alpha=0.3)
axes[1].set_title('Original Data', fontsize=12)

# Plot Unipolar NRZ
axes[2].step(t, unipolar_nrz, 'g-', where='post', linewidth=2)
axes[2].set_ylabel('Amplitude', fontsize=12)
axes[2].set_ylim(-0.5, 1.5)
axes[2].grid(True, alpha=0.3)
axes[2].set_title('Unipolar NRZ: 1=High, 0=Low', fontsize=12)

# Plot Bipolar NRZ
axes[3].step(t, bipolar_nrz, 'purple', where='post', linewidth=2)
axes[3].set_ylabel('Amplitude', fontsize=12)
axes[3].set_ylim(-1.5, 1.5)
axes[3].grid(True, alpha=0.3)
axes[3].set_title('Bipolar NRZ: 1=+V, 0=-V', fontsize=12)

# Plot Unipolar RZ
axes[4].step(t, unipolar_rz, 'orange', where='post', linewidth=2)
axes[4].set_ylabel('Amplitude', fontsize=12)
axes[4].set_ylim(-0.5, 1.5)
axes[4].grid(True, alpha=0.3)
axes[4].set_title('Unipolar RZ: 1=Half-width pulse, 0=Zero', fontsize=12)

# Plot Bipolar RZ
axes[5].step(t, bipolar_rz, 'brown', where='post', linewidth=2)
axes[5].set_ylabel('Amplitude', fontsize=12)
axes[5].set_ylim(-1.5, 1.5)
axes[5].grid(True, alpha=0.3)
axes[5].set_title('Bipolar RZ: 1=+V half-pulse, 0=-V half-pulse', fontsize=12)

# Plot Manchester code
axes[6].step(t, manchester, 'red', where='post', linewidth=2)
axes[6].set_ylabel('Amplitude', fontsize=12)
axes[6].set_xlabel('Time (Bit Periods)', fontsize=12)
axes[6].set_ylim(-0.5, 1.5)
axes[6].grid(True, alpha=0.3)
axes[6].set_title('Manchester: 1=High→Low, 0=Low→High', fontsize=12)

# Add bit separation lines for all subplots
for ax in axes:
    for i in range(n_bits + 1):
        ax.axvline(x=i, color='gray', linestyle='--', alpha=0.5)

# Add bit labels only to the data signal plot (axes[1])
for i in range(n_bits):
    axes[1].text(i + 0.5, axes[1].get_ylim()[1] + 0.1, str(data[i]), 
                 ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.show()

# Detailed explanations
print("=" * 70)
print("DETAILED EXPLANATION OF LINE CODING SCHEMES")
print("=" * 70)
print("1. Unipolar Non-Return-to-Zero (NRZ):")
print("   - Bit 1: High level (+V)")
print("   - Bit 0: Zero level (0V)")
print("   - Feature: Level remains constant throughout bit period")

print("\n2. Bipolar Non-Return-to-Zero (NRZ):")
print("   - Bit 1: Positive level (+V)")
print("   - Bit 0: Negative level (-V)")
print("   - Feature: Level remains constant throughout bit period")

print("\n3. Unipolar Return-to-Zero (RZ):")
print("   - Bit 1: High in first half, returns to zero in second half")
print("   - Bit 0: Zero level for entire bit period")
print("   - Feature: Signal returns to zero in each bit period")

print("\n4. Bipolar Return-to-Zero (RZ):")
print("   - Bit 1: Positive pulse in first half, zero in second half")
print("   - Bit 0: Negative pulse in first half, zero in second half")
print("   - Feature: Signal returns to zero in each bit period")

print("\n5. Manchester Coding:")
print("   - Bit 1: High-to-low transition at bit center")
print("   - Bit 0: Low-to-high transition at bit center")
print("   - Feature: Always has transition at bit center for clock recovery")
print("=" * 70)

# Wikipedia references
print("\nWikipedia References:")
print("- Line coding: https://en.wikipedia.org/wiki/Line_code")
print("- NRZ: https://en.wikipedia.org/wiki/Non-return-to-zero")
print("- RZ: https://en.wikipedia.org/wiki/Return-to-zero")
print("- Manchester code: https://en.wikipedia.org/wiki/Manchester_code")
print("- Bipolar encoding: https://en.wikipedia.org/wiki/Bipolar_encoding")
