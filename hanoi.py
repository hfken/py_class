def hanoi(n, source, target, auxiliary):
    """
    递归解决汉诺塔问题的函数

    参数:
    - n: 需要移动的盘子的数量
    - source: 初始柱子的名字(字符串)
    - target: 目标柱子的名字(字符串)
    - auxiliary: 辅助柱子的名字(字符串)
    """
    if n == 1:
        # 如果只有一个盘子,直接从 source 移动到 target
        print(f"将盘子从 {source} 移到 {target}")
        return
    # 递归地将 n-1 个盘子从 source 移动到 auxiliary,以 target 为辅助柱
    hanoi(n - 1, source, auxiliary, target)
    # 将第 n 个盘子从 source 移动到 target
    print(f"将盘子从 {source} 移到 {target}")
    # 递归地将 n-1 个盘子从 auxiliary 移动到 target,以 source 为辅助柱
    hanoi(n - 1, auxiliary, target, source)

# 示例:移动3个盘子,从柱子A移到柱子C,柱子B作为辅助柱
hanoi(3, "A", "C", "B")
