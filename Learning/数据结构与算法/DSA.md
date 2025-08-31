# 数据结构考试大纲

## 线性表

### 顺序表的实现

1. 顺序存储

   顺序表是静态存储分配，实现确定其容量。

2. 链式存储

   链表动态存储分配，运行时分配空间。单链表作为线性表的连接存储结构，用一组任意的存储单元存放线性表的元素。单链表的节点数据结构通常如下。

   ```cpp
   struct Node {
     	int value;
       Node* next; // The pointer to the next node
   };
   ```

### 线性表的基本操作

1. 初始化线性表

2. 销毁线性表

3. 判断线性表是否为空

4. 求线性表的长度

5. 输出线性表

6. 求线性表L中指定位置的某个数据元素

7. 定位查找元素

8. 插入一个数据元素

   假设在线性链表中找到了插入的位置，设为`current_node`，创建新节点并修改`new_node`和`current_node`的指针以完成修改。

   ```cpp
   int listInsert(LinkNode* L, int insert_value) {
       ......
       LinkNode* new_node = new LinkNode(insert_value);
       new_node->next = current_node->next;
       current_node->next = new_node;
   }
   ```

   

9. 删除数据元素

### 循序表和单链表的比较

1. 时间性能比较

   - 按位查找：顺序表的时间为O(1)，是随机存取；单链表的时间为O(n)，是顺序存取。
   - 插入和删除：循序表需要移动表长一半的元素，时间为O(n)；单链表不需要移动元素，在给出的某个元素合适位置的指针后，插入和删除操作所需的时间仅为O(1)。

2. 空间性能比较

   - 结点的存储密度：顺序表: 存储密度为1（只存储数据元素），没有浪费空间；单链表:  存储密度<1（包括数据域和指针域），有指针的结构性开销。
   - 整体结构：顺序表: 需要预分配存储空间，如果预分配得过大，造成浪费，若估计得过小，又将发生上溢；单链表: 不需要预分配空间，只要有内存空间可以分配，单链表中的元素个数就没有限制。 



## 栈、队列和数组

### 多维数组的存储

### 特殊矩阵的压缩存储

## 树与二叉树

### 二叉树

### 树、森林

### 哈夫曼编码

1. 步骤一：统计字符频率
   统计待编码字符集合中每个字符出现的频率，记录在一个频率表中。

2. 步骤二：构建优先队列
   将每个字符及其频率作为一个节点，并将所有节点按照频率大小放入一个优先队列（通常是最小堆）。

3. 步骤三：构建哈夫曼树
   从优先队列中取出两个频率最小的节点作为左右子节点，构建一个新的节点。新节点的频率是其左右子节点频率之和，将这个新节点重新插入优先队列。重复上述过程，直到优先队列中只剩下一个节点，即为哈夫曼树的根节点。
4. 步骤四：生成哈夫曼编码
   从根节点开始，遍历哈夫曼树，生成每个字符的编码：
   遍历左子节点时，向编码中添加 0；
   遍历右子节点时，向编码中添加 1；
   直到到达叶子节点，即得到了该字符的哈夫曼编码。

## 图

### 图的存储和基本操作

1. 邻接矩阵法
2. 邻接表法
3. 邻接多重表、十字链表

### 图的遍历

1. 深度优先遍历
2. 广度优先遍历

### 图的基本应用

1. 最小生成树

2. 最短路径

   **Djisktra**

   其用于求单元最短路问题。每一次选择距离起始节点最近的点，并更新。

   **Prim**

   选择起始节点，判断出其出边最小的边和节点，依次加入点，直至加入了所有节点位置。

   **Kruskal**

   将所有边抽离出图中，从小到大排序。依次将边和两个节点加入到图中，依次加入时判断是否形成回路。

3. 拓朴排序

4. 关键路径

   **AOE网***

   网是带权值的图。从起始节点到目标节点的最长路径为关键路径。先求点再求边。首先利用拓扑排序，每次选入读为0的点，然后不断更新距离。

## 查找

### 顺序查找法

### 分块查找法

### 树形查找

1. 二叉搜索树

   二叉搜索树的平均查找长度公式
   $$
   ASL_{成功}=\frac{1}{节点总数}\sum 每层的节点数\times 所在层数\\
   ASL_{失败}=\frac{1}{外部节点总数}\sum 每层外部节点数\times 所在层数
   $$

2. 平衡二叉树

3. 红黑树

### 散列表（哈希表）

### 字符串模式匹配

1. 暴力破解（Brute Froce）
2. KMP算法



## 排序

### 排序的概念
1. 排序算法的稳定性

   假定在待排序的记录集中，存在多个具有相同键值的记录，若经过排序，这些记录的相对次序仍然保持不变。原序列中：ki=kj且ri在rj之前，排序后：ri仍在rj之前，稳定的；反之，不稳定。 

2. 排序的键值

   排序根据某一个关键码进行排序，如果根据多个关键码则称为多键排序。
   
3. 排序的分类

   - 插入排序：直接插入排序，折半插入排序，**希尔排序**
   - 交换排序：冒泡排序，**快速排序**
   - 选择排序：简单选择排序，**堆排序**
   - 归并排序：**二路归并排序**
### 直接插入排序

将某个数字插入前面的有序数列，使之依然有序。第一趟排序可以将前面单个数字看作一个有序数组。

### 折半插入排序

### 冒泡排序

将每次的最大值循环沉底。

```cpp
for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
        if (array[j] > array[i]) {
            swap(array[j], array[i]);
        }
    }
}
```



### 简单选择排序

首先找到序列中最小的，然后与当前比较序列最小的替换。

### 希尔排序

根据增量，将每一组分开的序列排序。

### 快速排序

### 堆排序

### 二路归并排序

不断将两个有序数组归并。第一趟可以将单个数字看成有序数组。



# 数据结构上机实验

## 迪杰斯特拉算法

【问题描述】

 1. 从键盘输入一串字符，表示若干个顶点的信息

 2. 输入若干个字符对和一个整数，分别表示弧尾、弧头和权值，以#作为输入结束

3.  输入一个顶点信息

4.  求出该顶点到其余各顶点的最短路径。
【输入形式】
```
ABCDEFGH
AB 6
AD 1
AF 50
BC 43
BD 11
BE 6
CH 8
DE 12
EC 38
EG 24
FE 1
FG 12
GH 20
#
A
```
【输出形式】
```
AD 1
AB 6
AE 12
AG 36
AC 49
AF 50
AH 56
```
```cpp
/*
 * Program: dijkstra.cpp
 * Date: 2024.05.25
 * Author: nulla
 * Description: 
 */

#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>
#include <unordered_map>

using namespace std;

const int INFTY = INT_MAX;

typedef unordered_map<char, int> DistanceMap;
typedef unordered_map<char, unordered_map<char, int>> IndexMatrix;

class Graph {
public:
    void addEdge(char from, char to, int weight);
    DistanceMap dijkstra(char start);

private:
    IndexMatrix adj_list;
};

void Graph::addEdge(char from, char to, int weight) {
    adj_list[from][to] = weight;
    if (adj_list.find(to) == adj_list.end()) {
        adj_list[to] = unordered_map<char, int>();
    }
}

DistanceMap Graph::dijkstra(char start) {
    DistanceMap distances;

    // Initial adjancency matrix
    for (auto edge : adj_list) {
        distances[edge.first] = INFTY;
    }
    distances[start] = 0;

    priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        int current_distance = pq.top().first;
        char current_vertex = pq.top().second;
        pq.pop();

        if (current_distance > distances[current_vertex]) {
            continue;
        }

        for (const auto& neighbour : adj_list[current_vertex]) {
            char neighbour_vertex = neighbour.first;
            int weight = neighbour.second;
            int distance = current_distance + weight;

            if (distance < distances[neighbour_vertex]) {
                distances[neighbour_vertex] = distance;
                pq.push({distance, neighbour_vertex});
            }
        }
    }

    return distances;
}

int main() {
    Graph graph;
    string vertices;
    cin >> vertices;

    // Enter edges information
    char from, to;
    int weight;
    while (cin >> from && from != '#') {
        cin >> to >> weight;
        graph.addEdge(from, to, weight);
    }

    // Find min distances
    char start;
    cin >> start;
    DistanceMap distances = graph.dijkstra(start);
    vector<pair<char, int>> sorted_distances(distances.begin(), distances.end());

    // Sort the vector by value
    sort(sorted_distances.begin(), sorted_distances.end(), [](const pair<char, int>& a, const pair<char, int>& b) {
        return a.second < b.second;
    });

    for (const auto& pair : sorted_distances) {
        if (pair.first != start) {
            cout << start << pair.first << ' ' << pair.second << endl;
        }
    }

    return 0;
}
```

## 最小生成树Prim算法

1.从键盘输入无向图若干个顶点信息，以！作为结束；

2.输入一组顶点信息，分别表示图中边依附的两个顶点和权值，以-1 作为输入结束；以邻接矩阵作为存储；

3.输入起始顶点

4.利用prim算法求解最小生成树，输出每一步选出的边；

5.输出最小生成树的代价。

【输入样例】
```
ABCDEF!
0 1 9
0 2 10
1 2 7
1 3 5
2 4 6
2 5 7
3 4 11
4 5 8
-1
C
```
【输出样例】
```
CE 6
CB 7
BD 5
CF 7
BA 9
34
```

【示例代码】

```cpp
/*
 * Program: prim-mst.cc
 * Date: 2024.05.19
 * Author: Nulla
 * Repository: Milton-Code
 * Description: Find the minimum spanning tree by Prim's algorithm
 */

#include <iostream>
#include <vector>
#include <climits>
#include <unordered_map>
using namespace std;
const int INF = INT_MAX;

struct Vertex {
    char value;
    bool selected;
    int distance;
    int parent_index;

    Vertex(char x) : value(x), selected(false), distance(INF), parent_index(-1) {}
};

class Graph {
private:
    vector<Vertex> vertices;
    vector<vector<int>> adj_matrix;
    unordered_map<char, int> vertex_map;

public:
    void CreateGraph(const string& sequence) {
        int index = 0;
        for (char v : sequence) {
            if (v != '!') {
                vertices.push_back(Vertex(v));
                vertex_map[v] = index++;
            }
        }
        InitializeAdjMatrix();
    }

    void InitializeAdjMatrix() {
        int n = vertices.size();
        adj_matrix.resize(n, vector<int>(n, INF));
        for (int i = 0; i < n; i++) {
            adj_matrix[i][i] = 0;
        }
    }

    void AddEdge(int x, int y, int weight) {
        adj_matrix[x][y] = weight;
        adj_matrix[y][x] = weight;
    }

    void PrimMst(char start) {
        int n = vertices.size();
        int start_index = vertex_map[start];
        vertices[start_index].distance = 0;
        int total_weight = 0;

        for (int count = 0; count < n; count++) {
            int min_dist = INF, min_node = -1;

            // Find the node who has the min distance
            for (int current_node = 0; current_node < n; current_node++) {
                if (!vertices[current_node].selected
                && vertices[current_node].distance < min_dist) {
                    min_dist = vertices[current_node].distance;
                    min_node = current_node;
                }
            }
            vertices[min_node].selected = true;

            // Print the choosen node
            if(vertices[min_node].parent_index != -1) {
                cout << vertices[vertices[min_node].parent_index].value
                << vertices[min_node].value << " "
                << adj_matrix[min_node][vertices[min_node].parent_index] << endl;
                total_weight += adj_matrix[min_node][vertices[min_node].parent_index];
            }

            // Update information for next scan
            for (int i = 0; i < n; i++) {
                if (adj_matrix[min_node][i] != INF
                && !vertices[i].selected
                && adj_matrix[min_node][i] < vertices[i].distance) {
                    vertices[i].parent_index = min_node;
                    vertices[i].distance = adj_matrix[min_node][i];
                }
            }
        }
    
        cout << total_weight << endl;
    }

};

int main() {
    string sequence;
    cin >> sequence;

    Graph graph;
    graph.CreateGraph(sequence);
    
    int x, y, w;
    while (true) {
        cin >> x;
        if (x == -1) break;
        cin >> y >> w;
        graph.AddEdge(x, y, w);
    }

    char start_vertex;
    cin >> start_vertex;
    
    graph.PrimMst(start_vertex);

    return 0;
}
```



## 二叉排序树

【问题描述】

以括号形式输入一棵二叉排序树，从键盘输入待查找的元素，并输出元素比较路径。

【输入形式】

从键盘输入一系列数据元素值，以-1作为结束。输入待查找的元素值。

【输出形式】

以括号形式输出每插入一个数据之和的二叉排序树，输出查找路径

【样例输入】

```
4 10 0 1 8 6 3 5 3 7 -1
9
```

【样例输出】

```
 //依次以括号形式输出每插入一个数据之和的二叉排序树
4
4(,10)
4(0,10)
4(0(,1),10)
4(0(,1),10(8,))
4(0(,1),10(8(6,),))
4(0(,1(,3)),10(8(6,),))
4(0(,1(,3)),10(8(6(5,),),))
4(0(,1(,3)),10(8(6(5,),),))
4(0(,1(,3)),10(8(6(5,7),),))
4 10 8  //这一行是查找路径
```

【示例代码】

```cpp
/*
 * Program: binary-search-tree.cpp
 * Date: 2024.06.15
 * Author: Nulla
 * Description: Build a binary search tree by a sequence of numbers
 *              Print the tree by using parentheses
 */

#include <iostream>
#include <vector>
using namespace std;

struct BinaryTreeNode {
    int value;
    BinaryTreeNode *left_child;
    BinaryTreeNode *right_child;

    // Constructor
    BinaryTreeNode(int v) {
        value = v;
        left_child = nullptr;
        right_child = nullptr;
    }
};

void printTree(BinaryTreeNode* root) {
    if (root != nullptr) {
        cout << root->value;
        if (root->left_child != nullptr || root->right_child != nullptr) {
            cout << '(';
            printTree(root->left_child);
            cout << ',';
            printTree(root->right_child);
            cout << ')';
        }
    }
}

BinaryTreeNode* insertNode(BinaryTreeNode* root, int value) {
    // Set the new node if root is null
    if (root == nullptr) {
        return new BinaryTreeNode(value);
    }

    if (value < root->value) {
        root->left_child = insertNode(root->left_child, value);
    } else if (value > root->value) {
        root->right_child = insertNode(root->right_child, value);
    }

    return root;
}

void find(BinaryTreeNode* root, int key) {
    while (root != nullptr) {
        cout << root->value << ' ';
        if (key == root->value) break;
        
        if (key < root->value) {
            root = root->left_child;
        } else {
            root = root->right_child;
        }
    }
}

int main() {
    vector<int> sequence;
    int input, key;
    
    BinaryTreeNode* root = nullptr;
    while (cin >> input && input != -1) {
        root = insertNode(root, input);
        printTree(root);
        cout << endl;
    }

    cin >> key;
    find(root, key);
    
    return 0;
}
```

## 寻找中位数

【问题描述】

请按照如下的算法思想，利用折半查找方法求解两个升序序列A\B的中位数。（中位数的定义见教材P69 2.17）

算法思想：分别求出A，B的中位数a，b。若a=b,则a或者b就是所求；否则，舍弃a，b中较小者所在序列之较小一半，同时，舍弃较大者所在序列之较大的一半，且要求两次舍弃的元素个数相同。在保留的两个升序序列里重复这个过程，直到两个序列均只含有一个元素为止，此时，较小者即为所求。

提示：定义search(Rectype A[],Rectype B[],int n); 函数求出A、B的中位数。

测试数据用例Rectype 为int。

【输入形式】

从键盘输入一个整数表示表长-> 输入升序序列A和B->依次输出A、B舍弃部分元素后的序列->输出中位数

【输出形式】

 每次A、B舍弃部分元素之后的序列最终的中位数

【样例输入】

```
6
1 3 5 7 9 11
10 12 14 16 18 19
```

【样例输出】
```
7 9 11
10 12 14
9 11
10 12
11
10
mid=10
```

【示例代码】

```cpp
/*
 * Program: find-median.cpp
 * Date: 2024.06.02
 * Author: Nulla
 * Description: Find the median of two sorted arrays of equal length.
 */

#include <iostream>
#include <vector>
using namespace std;

void printArray(const vector<int>& array) {
    for (int i : array) {
        cout << i << ' ';
    }
    cout << endl;
}

int findMedian(vector<int> array[2], int number) {
    if (number == 1) {
        return min(array[0][0], array[1][0]);
    }

    int median[2];
    median[0] = array[0][(number % 2 == 1) ? number / 2 : (number - 1) / 2];
    median[1] = array[1][(number % 2 == 1) ? number / 2 : (number - 1) / 2];

    if (median[0] == median[1]) {
        return median[0];
    } else {
        if (median[0] < median[1]) {
            array[0].erase(array[0].begin(), array[0].begin() + number / 2);
            array[1].erase(array[1].begin() + (number + 1) / 2, array[1].end());
        } else {
            array[1].erase(array[1].begin(), array[1].begin() + number / 2);
            array[0].erase(array[0].begin() + (number + 1) / 2, array[0].end());
        }
        printArray(array[0]);
        printArray(array[1]);

        number = (number + 1) / 2; 
        return findMedian(array, number);
    }
}

int main() {
    int number, input;
    cin >> number;
    vector<int> array[2];
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < number; ++j) {
            cin >> input;
            array[i].push_back(input);
        }
    }

    int result = findMedian(array, number);
    cout << "mid=" << result << endl;

    return 0;
}
```

## 深度优先遍历

【问题描述】

采用邻接矩阵作为存储结构，利用深度优先搜索，判断有向图中，是否存在从顶点i到顶点j的路径；要求：从键盘输入若干个字符(表示顶点自带的信息),直到！结束->再输入若干对顶点编号（从0开始，表示两个顶点之间存在一条边），直到输入-1 -1结束-->输出对应的邻接矩阵 -->输入查询的顶点-->输出T 或者F

【输入形式】

```
ABCDE!
0 1
0 2
1 3
1 2
2 3
3 4
-1 -1
BE
```
【输出形式】
```
0 1 1 0 0
0 0 1 1 0
0 0 0 1 0
0 0 0 0 1
0 0 0 0 0
T
```
【示例代码】

```cpp
/*
 * Program: deep-first-search.cpp
 * Date: 2024.05.12
 * Author: Nulla
 * Description: store the information of graph in to a adj matrix
 *              find wheather these is a path from A to B
 */

#include <iostream>
#include <vector>

using namespace std;

struct Vertex {
    char value;
    bool visited;
    Vertex(char v) : value(v), visited(false) {}
};

class Graph {
    private:
    vector<Vertex> vertices;
    vector<vector<bool>> matrix;

    public:
    void CreateGraph(string sequence) {
        for(char v : sequence) {
            if (v == '!') break;
            Vertex vertex(v);
            vertices.push_back(vertex);
        }
        int size = vertices.size();
        matrix.resize(size, vector<bool>(size, false));
    }

    void CreateMap(int i, int j) {
        matrix[i][j] = true;
    }

    void DisplayMap() {
        for (int i = 0; i < vertices.size(); i++) {
            for (int j = 0; j < vertices.size(); j++) {
                cout << (matrix[i][j] ? 1 : 0) << ' ';
            }
            cout << '\n';
        }
    }

    void DeepFirstSearch(int i) {
        vertices[i].visited = true;
        for (int j = 0; j < vertices.size(); j++) {
            if (matrix[i][j] == true && vertices[j].visited == false) {
                DeepFirstSearch(j);
            }
        }
    }

    bool hasPath(char start, char target) {
        int start_index = -1;
        for (int index = 0; index < vertices.size(); index++) {
            if (vertices[index].value == start) {
                start_index = index;
                break;
            }
        }

        // Return false if there is no vertx match the input
        if (start_index == -1)
            return false;

        DeepFirstSearch(start_index);

        for (Vertex& vertex : vertices) {
            if (vertex.value == target && vertex.visited == true) {
                return true;
            }
        }
        return false;
    }
};

int main() {
    string sequence;
    cin >> sequence;
    Graph graph;
    graph.CreateGraph(sequence);

    while(true) {
        int vertex_1, vertex_2;
        cin >> vertex_1 >> vertex_2;
        if (vertex_1 == -1 || vertex_2 == -1)
            break;
        graph.CreateMap(vertex_1, vertex_2);
    }

    char start, target;
    cin >> start >> target;
    graph.DisplayMap();
    cout << (graph.hasPath(start, target) ? 'T' : 'F') << endl;

    return 0;
}
```



## 联通分量

【问题描述】

1. 从键盘输入无向图的顶点信息，以！作为结束；
2. 输入一组顶点信息,以-1 -1 作为结束
3. 输出连通分量的个数。

【样例输入】
```
ABCDEF!
0 1
0 3
1 2
2 3
4 5
-1 -1
```
【样例输出】
```
2
```
【示例代码】

```cpp
/*
 * Program: connected-components.cpp
 * Date: 2024.05.13
 * Author: Nulla
 * Description: 
 */

#include <iostream>
#include <vector>

using namespace std;

struct Vertex {
    char value;
    bool visited;
    Vertex(char v) : value(v), visited(false) {}
};

class Graph {
    private:
    vector<Vertex> vertices;
    vector<vector<bool>> matrix;

    public:
    void CreateGraph(string sequence) {
        for(char v : sequence) {
            if (v == '!') break;
            Vertex vertex(v);
            vertices.push_back(vertex);
        }
        int size = vertices.size();
        matrix.resize(size, vector<bool>(size, false));
    }

    void CreateMap(int i, int j) {
        matrix[i][j] = true;
        matrix[j][i] = true;
    }

    void DeepFirstSearch(int i) {
        vertices[i].visited = true;
        for (int j = 0; j < vertices.size(); j++) {
            if (matrix[i][j] == true && vertices[j].visited == false) {
                DeepFirstSearch(j);
            }
        }
    }

    int CountComponents() {
        for (Vertex vertex : vertices) {
            vertex.visited = false;
        }

        int count = 0;
        for (int i = 0; i < vertices.size(); i++) {
            if (vertices[i].visited == false) {
                DeepFirstSearch(i);
                count++;
            }
        }
        return count;
    }
};

int main() {
    string sequence;
    cin >> sequence;
    Graph graph;
    graph.CreateGraph(sequence);

    while(true) {
        int vertex_1, vertex_2;
        cin >> vertex_1 >> vertex_2;
        if (vertex_1 == -1 || vertex_2 == -1)
            break;
        graph.CreateMap(vertex_1, vertex_2);
    }

    cout << graph.CountComponents() << endl;

    return 0;
}
```

