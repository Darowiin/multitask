import concurrent.futures
import argparse
import random
import os

def monte_carlo_pi(n):
    inside_circle = 0

    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / n) * 4

def main():
    parser = argparse.ArgumentParser(description='Оценка числа Пи методом Монте-Карло')
    parser.add_argument('num_points', type=int, help='Количество случайных точек для оценки')
    args = parser.parse_args()

    num_points = args.num_points
    
    num_processes = os.cpu_count()
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(monte_carlo_pi, [num_points]))

    pi_estimate = sum(results) / len(results)
    print(f'Полученное значение Пи: {pi_estimate}')

if __name__ == "__main__":
    main()