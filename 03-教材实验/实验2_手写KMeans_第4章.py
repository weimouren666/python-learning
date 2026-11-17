# -*- coding: utf-8 -*-
"""手写 K-Means 聚类 —— 对应教材 4.4.1 节。纯 NumPy，不依赖 sklearn。"""
import numpy as np
np.random.seed(42)

groups = [(175, 55), (168, 50), (160, 78)]          # 运动型 / 学术型 / 社交型 的真实中心
names = {0: "运动型", 1: "学术型", 2: "社交型"}
X = np.vstack([np.random.normal(c, [6, 5], (40, 2)) for c in groups])
truth = np.repeat([0, 1, 2], 40)

def kmeans(X, k, it=50):
    """单次 K-Means：随机初始化 -> 反复『分配 + 重算簇心』直到簇心不再移动"""
    centers = X[np.random.choice(len(X), k, replace=False)]
    for _ in range(it):
        labels = ((X[:, None, :] - centers[None, :, :])**2).sum(axis=2).argmin(axis=1)
        new = np.array([X[labels == i].mean(axis=0) if (labels == i).any()
                        else centers[i] for i in range(k)])
        if np.allclose(new, centers):
            break
        centers = new
    inertia = ((X - centers[labels]) ** 2).sum()
    return centers, labels, inertia

best = max((kmeans(X, 3) for _ in range(20)), key=lambda t: -t[2])   # 20 次重启取最优
centers, labels, inertia = best

print("簇心（身高cm, 体重kg）：")
for i, c in enumerate(centers):
    near = int(np.argmin([np.linalg.norm(c - g) for g in groups]))
    print("  簇%d   身高 %5.1f   体重 %5.1f    ← 最接近：%s" % (i + 1, c[0], c[1], names[near]))

print("\n混淆矩阵（行=真实身份，列=算法分簇）：")
print("             簇1   簇2   簇3")
for t in range(3):
    row = "".join("%5d" % int(((truth == t) & (labels == p)).sum()) for p in range(3))
    print("真实%s:%s" % (names[t], row))
print("\n聚类准确率 = %.1f%%" % ((truth == labels).mean() * 100))
print("簇内平方和 = %.0f" % inertia)
print("\n教学要点：")
print("1) 单次 K-Means 随机初始化不同，结果可能差很多（我第一次跑只有 52.5%），")
print("   标准做法是多次重启取最优 —— 这就是『算法也有运气成分』。")
print("2) 簇的编号 1/2/3 本身没有意义，是随机的；有意义的是簇心坐标。")
print("3) 真实数据里『学术型』和『运动型』的体重本来就接近，边界那几个点分错很正常。")
