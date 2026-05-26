import os

def get_files_info(dirname):
    files = {}

    with os.scandir(dirname) as entries:
        for entry in entries:
            if entry.is_file():
                stat = entry.stat()
                files[entry.name] = {
                    "size": stat.st_size,
                    "path": entry.path
                }

    return files


def same_content(path1, path2):
    with open(path1, "rb") as f1, open(path2, "rb") as f2:
        return f1.read() == f2.read()


def compare_dirs(dir1, dir2):
    files1 = get_files_info(dir1)
    files2 = get_files_info(dir2)

    names1 = set(files1.keys())
    names2 = set(files2.keys())

    if len(files1) != len(files2):
        print("파일 개수가 다릅니다.")
        return False

    if names1 != names2:
        print("파일 이름 목록이 다릅니다.")
        print("첫 번째 디렉토리에만 있는 파일:", names1 - names2)
        print("두 번째 디렉토리에만 있는 파일:", names2 - names1)
        return False

    for name in names1:
        if files1[name]["size"] != files2[name]["size"]:
            print(name, "파일의 크기가 다릅니다.")
            return False

        if not same_content(files1[name]["path"], files2[name]["path"]):
            print(name, "파일의 내용이 다릅니다.")
            return False

    print("두 디렉토리는 같은 파일들을 가지고 있습니다.")
    return True


dir1 = input("첫 번째 디렉토리 이름: ")
dir2 = input("두 번째 디렉토리 이름: ")

compare_dirs(dir1, dir2)
