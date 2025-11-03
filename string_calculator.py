import re

class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        numbers = self._normalize_delimiters(numbers)
        num_list = self._split_numbers(numbers)
        self._check_for_negatives(num_list)
        return sum(int(num) for num in num_list if int(num) <= 1000)

    def _normalize_delimiters(self, numbers):
        if numbers.startswith("//"):
            delimiter = re.search(r"//\[(.*?)\]\n", numbers).group(1)
            numbers = numbers.split("\n", 1)[1].replace(delimiter, ",")
        return numbers.replace("\n", ",")

    def _split_numbers(self, numbers):
        return numbers.split(",")

    def _check_for_negatives(self, num_list):
        negatives = [int(num) for num in num_list if int(num) < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
