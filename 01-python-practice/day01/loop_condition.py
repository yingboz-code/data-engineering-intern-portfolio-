scores = [72, 85, 59, 93, 68, 77, 90, 55]

# 1. 筛选出及格的分数（>=60）
pass_scores = []
for s in scores:
    if s >= 60:
        pass_scores.append(s)

print("及格分数:", pass_scores)

# 2. 统计及格人数和平均分
pass_count = len(pass_scores)
avg_score = sum(pass_scores) / pass_count
print(f"及格人数: {pass_count}, 平均分: {avg_score:.2f}")

# 3. 多条件筛选：80分以上且为偶数
target_scores = []
for s in scores:
    if s >= 80 and s % 2 == 0:
        target_scores.append(s)

print("80分以上且为偶数:", target_scores)

# 4. 遍历字典列表（模拟表格数据）
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 76},
    {"name": "Charlie", "score": 92}
]

print("\n学生成绩表:")
for stu in students:
    if stu["score"] >= 80:
        print(f"{stu['name']}: 优秀")
    else:
        print(f"{stu['name']}: 良好")