import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==================== 1. Define Word Vectors (3D) ====================
king   = np.array([4, 5, 2])
queen  = np.array([4, 1, 3])
man    = np.array([-2, -1, 1])
woman  = np.array([-2, -5, 2])

# Verify arithmetic relationships
print("queen - king =", queen - king)        # [ 0 -4  0]
print("woman - man =", woman - man)          # [ 0 -4  0]
print("Equal?", np.allclose(queen - king, woman - man))

# ==================== 2. Plot Setup ====================
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Coordinate axis range
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)
ax.set_zlim(-1, 3)
ax.set_xlabel('X (Dimension 1)')
ax.set_ylabel('Y (Dimension 2)')
ax.set_zlabel('Z (Dimension 3)')
ax.set_title('Word Embedding Vectors from Origin', fontsize=16)

# ==================== 3. Plot Vectors from Origin ====================
words = {'king': king, 'queen': queen, 'man': man, 'woman': woman}
colors = {'king': 'blue', 'queen': 'purple', 'man': 'red', 'woman': 'green'}

# Origin point
origin = np.array([0, 0, 0])

# Plot vectors from origin
for word, vec in words.items():
    # Draw vector from origin to word vector
    ax.quiver(
        origin[0], origin[1], origin[2],
        vec[0], vec[1], vec[2],
        color=colors[word], arrow_length_ratio=0.1, linewidth=3, 
        label=f'{word} vector'
    )
    # Mark the endpoint of the vector
    ax.scatter(vec[0], vec[1], vec[2], c=colors[word], s=100, alpha=0.7)
    # Label the word at the endpoint
    ax.text(vec[0]+0.1, vec[1]+0.1, vec[2]+0.1, word, fontsize=12, color=colors[word])

# ==================== 4. Plot Difference Vectors ====================
def plot_difference_vector(ax, vec1, vec2, color, label=None):
    """Plot the difference vector between two word vectors"""
    diff = vec2 - vec1
    ax.quiver(
        vec1[0], vec1[1], vec1[2],
        diff[0], diff[1], diff[2],
        color=color, arrow_length_ratio=0.1, linewidth=2, 
        linestyle='--', alpha=0.7, label=label
    )

# Plot difference vectors
plot_difference_vector(ax, king, queen, 'gray', 'queen − king')
plot_difference_vector(ax, man, woman, 'gray', 'woman − man')

# Verify the arithmetic relationship
predicted_queen = king + (woman - man)
plot_difference_vector(ax, king, predicted_queen, 'orange', 'king + (woman − man)')

# ==================== 5. Legend and Styling ====================
ax.legend(loc='upper left', bbox_to_anchor=(0, 1))
ax.grid(True, alpha=0.3)
ax.view_init(elev=20, azim=45)  # Adjust viewing angle

# Mark the origin
ax.scatter(0, 0, 0, c='black', s=50, label='Origin')
ax.text(0.1, 0.1, 0.1, 'Origin', fontsize=10, color='black')

# ==================== 6. Save High-Quality Images ====================
plt.tight_layout()
plt.savefig('word_embedding_vectors_3d.png', dpi=300, bbox_inches='tight')
plt.savefig('word_embedding_vectors_3d.pdf', bbox_inches='tight')  # Vector graphics
plt.show()
