import concurrent.futures
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

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(search_keyword_in_file, keyword, file): file for file in files}
        for future in concurrent.futures.as_completed(futures):
            file = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f'Error in file {file}: {e}')

    print("Поиск завершен")

if __name__ == "__main__":
    main()