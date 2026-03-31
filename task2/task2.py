import sys
import math

def read_circle_data(filepath):
    with open(filepath, 'r') as f:
        line = f.readline().strip()
        while line == '':
            line = f.readline().strip()
        x_center, y_center = map(float, line.split())

        line = f.readline().strip()
        while line == '':
            line = f.readline().strip()
        radius = float(line)

    return x_center, y_center, radius

def read_points(filepath):
    points = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Пропускаем пустые строки
                x, y = map(float, line.split())
                points.append((x, y))
    return points

def check_point_position(x_center, y_center, radius, x_point, y_point):
    distance_squared = (x_point - x_center) ** 2 + (y_point - y_center) ** 2
    radius_squared = radius ** 2

    if abs(distance_squared - radius_squared) < 1e-10:
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2

def main():

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    try:

        x_center, y_center, radius = read_circle_data(circle_file)

        points = read_points(points_file)

        for x_point, y_point in points:
            result = check_point_position(x_center, y_center, radius, x_point, y_point)
            print(result)

    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e.filename}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: некорректный формат данных - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
