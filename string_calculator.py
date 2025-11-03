import re

class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        if numbers.startswith("//"):
            delimiter = re.search(r"//\[(.*?)\]\n", numbers).group(1)
            numbers = numbers.split("\n", 1)[1].replace(delimiter, ",")
        numbers = numbers.replace("\n", ",")
        num_list = numbers.split(",")
        negatives = [int(num) for num in num_list if int(num) < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
        return sum(int(num) for num in num_list if int(num) <= 1000)
