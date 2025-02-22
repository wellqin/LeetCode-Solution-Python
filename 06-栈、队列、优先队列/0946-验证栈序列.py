# 946. 验证栈序列
# 给定 pushed 和 popped 两个序列，
# 只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，
# 返回 true；否则，返回 false 。

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 特判
        if len(pushed) == 0 and len(popped) == 0:
            return True
        if len(pushed) == 0 or len(popped) == 0 or len(pushed) != len(popped):
            return False

        # 辅助栈
        stack = []
        # 遍历的索引，从 0 开始
        index = 0
        for ele in pushed:
            stack.append(ele)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        # 最后不要忘记判断 stack 为空的情况
        # return len(stack) == 0
        return index == len(pushed)
