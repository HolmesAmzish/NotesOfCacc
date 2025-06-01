---
title: Java 集合类
date: 2025-05-27
author: Cacc
---

| 接口       | 常用实现类                            | 特性                       |
| ---------- | ------------------------------------- | -------------------------- |
| `List<E>`  | `ArrayList`, `LinkedList`, `Vector`   | 有序、可重复元素           |
| `Set<E>`   | `HashSet`, `LinkedHashSet`, `TreeSet` | 无重复元素，`TreeSet` 有序 |
| `Map<K,V>` | `HashMap`, `LinkedHashMap`, `TreeMap` | 键值对，键唯一             |

## List

```java
List<Integer> list = List.of(1, 2, 5);
```

```java
List<Integer> list = new ArrayList<>(); // LinkedList
list.add(1);
list.add(3);
Integer second = list.get(1);
```

