import multiprocessing
import argparse

def search_keyword_in_file(keyword, filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if keyword in line:
                    print(f'Found keyword "{keyword}" in file: {filename}')
                    break
    except Exception as e:
        print(f'Error while searching in file {filename}: {e}')

def main():
    parser = argparse.ArgumentParser(description='Параллельный поиск по ключевым словам в текстовых файлах')
    parser.add_argument('keyword', help='Ключевое слово для поиска')
    parser.add_argument('files', nargs='+', help='Список файлов для поиска')
    args = parser.parse_args()

    keyword = args.keyword
    files = args.files

    processes = []
    for file in files:
        process = multiprocessing.Process(target=search_keyword_in_file, args=(keyword, file))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Поиск завершен")

if __name__ == "__main__":
    main()