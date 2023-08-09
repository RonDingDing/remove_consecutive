from typing import Dict, List, Tuple


class Solution:
    def consecutive(self, string: str, mode: int) -> str:
        has = True
        changed = {}
        print("Input: ", string)
        print("Output:")
        list_str = list(string)
        while has and list_str:
            changed, list_str, has = self._remove_once(list_str, mode)
            if changed:
                list_str = [
                    changed.get(list_str[i], list_str[i]) for i in range(len(list_str))
                ]
                changed = {}
            if has:
                print("->", "".join(list_str))

        print()
        return "".join(list_str)

    def _remove_once(
        self,
        list_str: List[str],
        mode: int,
    ) -> Tuple[Dict[str, str], List[str], bool]:
        stack = []
        pre = ""
        er = 1
        has = False
        changed = {}
        for this in list_str + ["0"]:
            if stack and stack[-1] != this:
                buf = []
                while stack and stack[-1] == pre:
                    c = stack.pop()
                    buf.append(c)
                if len(buf) >= 3:
                    has = True
                    if mode == 1:
                        if pre == 'a':
                            new = ''
                        else:
                            new = chr(ord(pre) - 1)
                        changed[er] = new
                        if new:
                            stack.append(er)
                        er += 1
                else:
                    stack.extend(buf)
            stack.append(this)
            pre = this
        stack.pop()
        return changed, stack, has

    def remove_3_more_consecutive_characters(self, string: str) -> str:
        return self.consecutive(string, 0)

    def change_3_more_consecutive_characters(self, string: str) -> str:
        return self.consecutive(string, 1)


if __name__ == "__main__":
    solution = Solution()
    print("第一题不输出中间结果：")
    print("第一题")
    solution.remove_3_more_consecutive_characters("aabcccbbad")
    solution.remove_3_more_consecutive_characters("acesveee")
    solution.remove_3_more_consecutive_characters("oooooacesv")
    solution.remove_3_more_consecutive_characters("ddccoooaaabbbocd")
    print("第二题")
    solution.change_3_more_consecutive_characters("aabeeedddcccbad")
    solution.change_3_more_consecutive_characters("aabcccdddcccbbad")
    solution.change_3_more_consecutive_characters("aancccmbbamadd")
    solution.change_3_more_consecutive_characters("acesveee")
    solution.change_3_more_consecutive_characters("oooooacesv")
    solution.change_3_more_consecutive_characters("ddccooaaabbbocd")
    solution.change_3_more_consecutive_characters("abcccbad")