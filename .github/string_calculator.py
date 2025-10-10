class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        delimiters = [',', '\n']
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            custom_delimiter = parts[0][2:]
            numbers = parts[1]
            delimiters.append(custom_delimiter)
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ',')
        num_list = [int(num) for num in numbers.split(',') if num]
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
        return sum(num for num in num_list if num <= 1000)