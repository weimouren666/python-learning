# -*- coding: utf-8 -*-
"""模拟《大数据导论》第3章「数据处理」的完整流程：采集→清洗→变换→集成→归约"""
import pandas as pd, numpy as np
pd.set_option("display.width", 120)

raw = """学号,姓名,性别,年龄,入学年份,专业,高数,英语,备注
20210101,张三,男,19,2021,大数据,88,78,
20210102,李四,女,20,2021,大数据,92,80,
20210103,王五,男,19,2021,"大数据 ",75,92,
20210104,赵六,女,20,2021,大数据,61,75,
20210105,钱七,男,,2021,大数据,95,88,竞赛获奖
20210106,孙八,男,19,2021,大数据,70,,
20210101,张三,男,19,2021,大数据,88,78,
20210108,吴十,男,250,2021,大数据,66,71,年龄录入错误
"""
open("raw_students.csv", "w", encoding="utf-8").write(raw)
df = pd.read_csv("raw_students.csv")
n_raw = len(df)

print("="*66)
print("【1 数据采集】read_csv —— 教材 3.1 节")
print("="*66)
print(f"读入 {df.shape[0]} 行 × {df.shape[1]} 列")
print("脏数据清单：")
print("  残缺 -> 钱七年龄缺失、孙八英语缺考")
print("  噪声 -> 吴十年龄 250（录入错误）")
print("  冗余 -> 张三被重复登记两次")
print('  格式 -> 王五的专业字段是 "大数据 "（尾部有空格）')

print("\n" + "="*66)
print("【2 数据清洗】残缺/噪声/冗余 —— 教材 3.2 节")
print("="*66)
df["年龄"] = df["年龄"].fillna(df["年龄"].median())          # 残缺：中位数填充
df.loc[df["年龄"] > 30, "年龄"] = np.nan                    # 噪声：识别异常值
df["年龄"] = df["年龄"].fillna(df["年龄"].median()).astype(int)
before = len(df)
df = df.drop_duplicates()                                   # 冗余：整行重复
df["专业"] = df["专业"].str.strip()                          # 格式：去空格
print(f"重复记录：{before} 行 -> {len(df)} 行（删掉 1 条重复登记）")
print(f"缺失值：{int(df.isnull().sum().sum())} 个（英语缺考 1 + 备注本来就空 5）")
print(df[["学号","姓名","年龄","专业"]].to_string(index=False))

print("\n" + "="*66)
print("【3 数据变换】属性类型/属性值变换 —— 教材 3.3 节")
print("="*66)
df["高数等级"] = pd.cut(df["高数"], [0,60,70,80,90,100],
                        labels=["不及格","及格","中","良好","优秀"])   # 属性值变换
for c in ["高数","英语"]:
    df[c+"_z"] = ((df[c]-df[c].mean())/df[c].std()).round(2)           # 标准化
df["总分"] = df["高数"] + df["英语"]
print(df[["姓名","高数","高数等级","高数_z","英语_z","总分"]].to_string(index=False))

print("\n" + "="*66)
print("【4 数据集成】模式匹配与冲突 —— 教材 3.4 节")
print("="*66)
dorm = pd.DataFrame({"学号":[20210101,20210102,20210103,20210104,20210105],
                     "宿舍":["A101","A101","A102","B201","B201"],"床位数":[4,4,4,6,6]})
merged = df.merge(dorm, on="学号", how="left")
print(merged[["学号","姓名","宿舍","床位数"]].to_string(index=False))
print("-> 孙八/吴十无宿舍信息，合并后为空：这就是『值缺失导致的信息不完整』")

print("\n" + "="*66)
print("【5 数据归约】维归约 + 数值归约 —— 教材 3.5 节")
print("="*66)
reduced = merged.drop(columns=["学号","备注","英语_z","性别","入学年份"])   # 维归约
summary = reduced.groupby("专业").agg(人数=("姓名","count"),
    平均高数=("高数","mean"), 平均英语=("英语","mean"), 平均总分=("总分","mean")).round(1)
print(summary.to_string())
print(f"\n从 {n_raw} 行原始脏数据 -> {len(summary)} 行分析结论")
summary.to_csv("专业成绩汇总.csv", encoding="utf-8-sig")
print("已导出：专业成绩汇总.csv")
