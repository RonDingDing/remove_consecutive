from typing import Tuple


class Solution:
    def _remove_once(self, string: str, mode: int = 0) -> Tuple[str, bool]:
        has = False
        new_string = string + "0"  # 加一个字符集外的元素，就不用处理重复元素结尾的特殊情况了
        list_str = list(string)
        new_length = len(new_string)
        i = 0
        while i < new_length - 1:
            this = new_string[i]
            for j in range(i + 1, new_length):
                if new_string[j] != this:
                    if j - i >= 3:
                        has = True
                        if mode == 0:
                            list_str[i:j] = [""] * (j - i)
                        else:
                            if this == 'a':
                                new = ''
                            else:
                                new = chr(ord(this) - 1)
                            list_str[i:j] = [new] + [""] * (j - i - 1)
                    break
            i = j
        return "".join(list_str), has

    def consecutive(self, string: str, mode: int) -> str:
        has = True
        print("Input: ", string)
        print("Output:")
        while has and string:
            string, has = self._remove_once(string, mode)
            if has:
                print("->", string)
        print()
        return string

    def remove_3_more_consecutive_characters(self, string: str) -> str:
        return self.consecutive(string, 0)

    def change_3_more_consecutive_characters(self, string: str) -> str:
        return self.consecutive(string, 1)


if __name__ == "__main__":
    solution = Solution()
    print("输出中间结果：")
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
