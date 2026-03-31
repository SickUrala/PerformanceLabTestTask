import sys

def min_moves_to_equal(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)

    median = sorted_nums[n // 2]

    moves = sum(abs(num - median) for num in nums)

    return moves

def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:

                line = line.strip()
                if line:
                    numbers.append(int(line))
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        sys.exit(1)
    except ValueError:
        print(f"Ошибка: файл содержит некорректные данные.")
        sys.exit(1)

    return numbers

def main():
    filename = sys.argv[1]

    nums = read_numbers_from_file(filename)

    result = min_moves_to_equal(nums)

    print(result)

if __name__ == "__main__":
    main()
