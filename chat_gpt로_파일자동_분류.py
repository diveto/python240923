import os
import shutil

# 다운로드 폴더 경로 설정
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로 설정
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 이동할 폴더가 존재하지 않으면 생성
os.makedirs(image_folder, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# 파일 확장자별 이동 대상 폴더 설정
file_destinations = {
    ('.jpg', '.jpeg'): image_folder,
    ('.csv', '.xlsx'): data_folder,
    ('.txt', '.doc', '.pdf'): docs_folder,
    ('.zip',): archive_folder,
}

# 다운로드 폴더 내 모든 파일 순회
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)

    # 파일이 아닌 경우 건너뜀
    if not os.path.isfile(file_path):
        continue

    # 파일의 확장자 추출
    _, file_extension = os.path.splitext(filename)

    # 파일 확장자에 따라 적절한 폴더로 이동
    for extensions, destination_folder in file_destinations.items():
        if file_extension.lower() in extensions:
            print(f"Moving {filename} to {destination_folder}")
            shutil.move(file_path, destination_folder)
            break
