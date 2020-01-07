import os

# 크롤링한 웹사이트마다 각각의 폴더를 생성
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

create_project_dir('gomyo')

# 큐 생성, 크롤링 (없는 자료일 경우)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# 새 파일 생성
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# 데이터 입력
def append_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')

# 데이터 삭제
def delete_file_contents(path):
    with open(path,'w'):
        pass

# 파일을 세트로
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# 세트를 파일로
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)