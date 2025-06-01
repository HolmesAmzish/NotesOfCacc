# 无线传感网 LEACH 协议模拟

## 提供代码解读

**全局参数**

```python
AREA_SIZE = 100       # 网络区域大小（100x100单位）
NUM_NODES = 100       # 节点总数
P = 0.1               # 簇头选举概率（10%的节点成为簇头）
ENERGY_INIT = 0.5     # 初始能量（0.5 J）
```

**`P=0.1`**：每轮约10%的节点被随机选为簇头（CH），符合LEACH的动态分簇思想。

**`ENERGY_INIT`**：所有节点初始能量相同，模拟能量受限场景。

**随即生成节点**

```python
nodes = np.random.rand(NUM_NODES, 2) * AREA_SIZE  # 随机生成节点坐标
energies = np.full(NUM_NODES, ENERGY_INIT)        # 初始化能量数组
```

**`nodes`**：生成100个节点的随机坐标（均匀分布在100x100区域内）。

**`energies`**：记录每个节点的剩余能量。

**选举簇头**

```python
def select_cluster_heads():
    num_cluster_heads = int(NUM_NODES * P)  # 计算簇头数量
    return np.random.choice(range(NUM_NODES), num_cluster_heads, replace=False)
```

**随机选择**：每轮从100个节点中随机选10个作为簇头（无重复）。

**能量消耗**

```python
def energy_consumption(node_indices, cluster_head_index):
    d0 = 10                                   # 距离阈值（单位：米）
    E_elec = 50e-9                            # 电路能耗（50 nJ/bit）
    E_fs = 10e-12                             # 自由空间模型系数（pJ/bit/m²）
    E_mp = 0.0013e-12                         # 多径模型系数（pJ/bit/m⁴）
    data_packet_size = 4000                   # 数据包大小（4000 bits）

    for node_index in node_indices:
        distance = np.linalg.norm(nodes[node_index] - nodes[cluster_head_index])
        if distance < d0:
            energy = data_packet_size * (E_elec + E_fs * distance ** 2)
        else:
            energy = data_packet_size * (E_elec + E_mp * distance ** 4)
        energies[node_index] -= energy        # 普通节点能耗

    # 簇头额外能耗（接收和聚合数据）
    cluster_head_energy = data_packet_size * E_elec * len(node_indices)
    energies[cluster_head_index] -= cluster_head_energy
```

**普通节点**：发送数据能耗 = `E_elec * data + E_{fs/mp} * data * distance^n`（n=2或4）。
$$
E_{\text{Tx}}(k, d) = 
\begin{cases}
k \cdot E_{\text{elec}} + k \cdot \epsilon_{\text{fs}} \cdot d^2 & \text{若 } d < d_0 \text{（自由空间模型）} \\
k \cdot E_{\text{elec}} + k \cdot \epsilon_{\text{mp}} \cdot d^4 & \text{若 } d \geq d_0 \text{（多径模型）}
\end{cases}
$$

**簇头节点**：接收能耗 = `E_elec * data * 成员数量`（未模拟数据聚合能耗）。
$$
E_{\text{Rx}}(k, N) = N \cdot k \cdot E_{\text{elec}}
$$


**阈值`d0`**：短距离用自由空间模型（`d²`），长距离用多径模型（`d⁴`）。

**单轮LEACH模拟**

```python
def simulate_leach():
    cluster_head_indices = select_cluster_heads()  # 选举簇头
    cluster_heads = nodes[cluster_head_indices]

    # 分配普通节点到最近的簇头
    clusters = {i: [] for i in range(len(cluster_head_indices))}
    for i, node in enumerate(nodes):
        distances = np.linalg.norm(cluster_heads - node, axis=1)
        cluster_index = np.argmin(distances)
        clusters[cluster_index].append(i)

    # 计算总能耗
    total_energy_used = 0
    for cluster_index, node_indices in clusters.items():
        total_energy_used += energy_consumption(node_indices, cluster_head_indices[cluster_index])
    return cluster_heads, clusters, total_energy_used
```

**分簇逻辑**：每个普通节点加入距离最近的簇头。

**能量统计**：累加所有节点和簇头的能耗。

**Matplotlib 可视化**

```python
def visualize_clusters(cluster_heads, clusters):
    plt.scatter(nodes[:, 0], nodes[:, 1], c='blue', label='普通节点')
    plt.scatter(cluster_heads[:, 0], cluster_heads[:, 1], c='red', marker='x', s=100, label='簇头')
    for cluster_index, node_indices in clusters.items():
        cluster_head = cluster_heads[cluster_index]
        for node_index in node_indices:
            plt.plot([cluster_head[0], nodes[node_index, 0]], 
                     [cluster_head[1], nodes[node_index, 1]], 
                     linestyle='--', color='gray', linewidth=0.5)
```

**输出效果**：红色`x`表示簇头，蓝色点表示普通节点，灰色虚线表示簇内通信链路。



## 错误修改

出现了字体错误，导致无法显示中文。

三种方法：1. 在本文件中修改字体。2. 在本环境（系统、venv 或 conda）的扩展库中设置 matplotllib 的全局默认字体，这会直接解决这个环境的所有问题。3. 直接使用英语

## 功能拓展

添加了能量显示和死亡节点报告。能量显示将每个节点绘制时根据当前的能量来绘制颜色，体现出不同能量的分布。死亡节点报告将避免将死亡节点作为通讯节点，并在控制台中报告。为了更好的显示结果，将轮数提升并更改了一些量纲来保证显示比较明显。

```python
import numpy as np
import matplotlib.pyplot as plt

# Network area and node parameters
AREA_SIZE = 100  # Area size (m)
NUM_NODES = 100  # Number of nodes
P = 0.1          # Probability of becoming cluster head
ENERGY_INIT = 0.05  # Reduced initial energy to see changes faster

# Initialize nodes
nodes = np.random.rand(NUM_NODES, 2) * AREA_SIZE  # Random node positions
energies = np.full(NUM_NODES, ENERGY_INIT)  # Initialize all nodes with same energy
dead_nodes = np.zeros(NUM_NODES, dtype=bool)  # Track dead nodes

# Select cluster heads randomly based on probability P (skip dead nodes)
def select_cluster_heads():
    alive_nodes = [i for i in range(NUM_NODES) if not dead_nodes[i]]
    num_cluster_heads = min(int(len(alive_nodes) * P), len(alive_nodes))
    return np.random.choice(alive_nodes, num_cluster_heads, replace=False)

# Calculate energy consumption for nodes communicating with cluster head
def energy_consumption(node_indices, cluster_head_index):
    d0 = 10  # Distance threshold (m)
    E_elec = 50e-9  # Energy per bit (J/bit)
    E_fs = 10e-12  # Free space model coefficient
    E_mp = 0.0013e-12  # Multipath model coefficient
    data_packet_size = 20000  # Further increased for faster energy depletion

    total_energy = 0
    for node_index in node_indices:
        distance = np.linalg.norm(nodes[node_index] - nodes[cluster_head_index])
        if distance < d0:
            energy = data_packet_size * E_elec + data_packet_size * E_fs * (distance ** 2)
        else:
            energy = data_packet_size * E_elec + data_packet_size * E_mp * (distance ** 4)
        total_energy += energy
        energies[node_index] -= energy

    # Additional energy consumption for cluster head
    cluster_head_energy = data_packet_size * E_elec * len(node_indices)
    energies[cluster_head_index] -= cluster_head_energy
    total_energy += cluster_head_energy

    return total_energy

# Simulate one round of LEACH protocol
def simulate_leach():
    cluster_head_indices = select_cluster_heads()
    cluster_heads = nodes[cluster_head_indices]

    # Assign cluster heads to each alive node
    clusters = {i: [] for i in range(len(cluster_head_indices))}
    for i, node in enumerate(nodes):
        if not dead_nodes[i]:  # Skip dead nodes
            distances = np.linalg.norm(cluster_heads - node, axis=1)
            cluster_index = np.argmin(distances)  # Assign to nearest cluster head
            clusters[cluster_index].append(i)

    # Calculate total energy consumption
    total_energy_used = 0
    for cluster_index, node_indices in clusters.items():
        total_energy_used += energy_consumption(node_indices, cluster_head_indices[cluster_index])

    return cluster_heads, clusters, total_energy_used

# Visualization with dead nodes
def visualize_clusters(cluster_heads, clusters):
    plt.figure(figsize=(8, 8))
    
    # Plot all nodes with energy-based colors (dead nodes will show as 0 energy)
    sc = plt.scatter(nodes[:, 0], nodes[:, 1], 
                    c=np.where(dead_nodes, 0, energies),
                    cmap='viridis', vmin=0, vmax=ENERGY_INIT,
                    label='Nodes by energy')
    plt.colorbar(sc, label='Remaining Energy (J)')
    
    # Plot cluster heads (red x)
    plt.scatter(cluster_heads[:, 0], cluster_heads[:, 1], 
               c='red', marker='x', s=100, label='Cluster heads')

    # Draw cluster connections (skip dead nodes)
    for cluster_index, node_indices in clusters.items():
        cluster_head = cluster_heads[cluster_index]
        for node_index in node_indices:
            if not dead_nodes[node_index]:  # Only draw connections for alive nodes
                plt.plot([cluster_head[0], nodes[node_index, 0]],
                         [cluster_head[1], nodes[node_index, 1]],
                         linestyle='--', color='gray', linewidth=0.5)

    plt.title(f'LEACH Protocol - Round {main.round_counter}')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
def main():
    rounds = 10  # Reduced to 10 rounds
    plt.figure(figsize=(15, 10))  # Create figure for subplots
    
    for r in range(rounds):
        print(f"\n--- Round {r + 1} ---")
        cluster_heads, clusters, total_energy_used = simulate_leach()
        print(f"Total energy consumed: {total_energy_used:.6f} J")

        # Check node energy levels and mark dead nodes
        for i, energy in enumerate(energies):
            if energy <= 0:
                if not dead_nodes[i]:
                    dead_nodes[i] = True
                    print(f"Node {i} has died with energy {energy:.6f} J!")
                energies[i] = 0  # Ensure energy doesn't go negative

        # Create subplot for current round with cluster connections
        plt.subplot(2, 5, r + 1)
        sc = plt.scatter(nodes[:, 0], nodes[:, 1], 
                        c=np.where(dead_nodes, 0, energies),
                        cmap='viridis', vmin=0, vmax=ENERGY_INIT)
        plt.scatter(cluster_heads[:, 0], cluster_heads[:, 1], 
                   c='red', marker='x', s=50)
        
        # Draw cluster connections (skip dead nodes)
        for cluster_index, node_indices in clusters.items():
            cluster_head = cluster_heads[cluster_index]
            for node_index in node_indices:
                if not dead_nodes[node_index]:  # Only draw connections for alive nodes
                    plt.plot([cluster_head[0], nodes[node_index, 0]],
                             [cluster_head[1], nodes[node_index, 1]],
                             linestyle='--', color='gray', linewidth=0.3)
        
        plt.title(f'Round {r + 1}')
        plt.grid(True)
    
    plt.tight_layout()
    plt.show()
        

if __name__ == "__main__":
    main()

```

<img src="../img/leach.png">

<center>图1 10 轮簇分布</center>

```
--- Round 1 ---
Total energy consumed: 0.201265 J

--- Round 2 ---
Total energy consumed: 0.200597 J

--- Round 3 ---
Total energy consumed: 0.200709 J

--- Round 4 ---
Total energy consumed: 0.200990 J

--- Round 5 ---
Total energy consumed: 0.200724 J

--- Round 6 ---
Total energy consumed: 0.201065 J

--- Round 7 ---
Total energy consumed: 0.200795 J

--- Round 8 ---
Total energy consumed: 0.202267 J

--- Round 9 ---
Total energy consumed: 0.200714 J

--- Round 10 ---
Total energy consumed: 0.200656 J
Node 3 has died with energy -0.004015 J!
Node 43 has died with energy -0.000036 J!
Node 59 has died with energy -0.004033 J!
```



## 参考文献

[1] Heinzelman, W. R., Chandrakasan, A., & Balakrishnan, H. (2000, January). Energy-efficient communication protocol for wireless microsensor networks. In *Proceedings of the 33rd annual Hawaii international conference on system sciences* (pp. 10-pp). IEEE.