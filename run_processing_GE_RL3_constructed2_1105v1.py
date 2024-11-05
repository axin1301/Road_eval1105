import os
import requests
import zipfile
import subprocess
import argparse
import shutil

def download_zip_from_url(url, save_path):
    """
    从给定的 URL 下载 ZIP 文件。

    :param url: ZIP 文件的 URL
    :param save_path: 保存 ZIP 文件的本地路径
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        print(f"下载完成: {save_path}")
    else:
        print(f"下载失败，HTTP状态码: {response.status_code}")

def unzip_file(zip_path, extract_to):
    """
    解压 ZIP 文件到指定目录。

    :param zip_path: ZIP 文件的路径
    :param extract_to: 解压到的目标目录
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"解压完成: {extract_to}")

# def run_python_file(file_path):
#     """
#     运行指定的Python文件。
    
#     :param file_path: 需要运行的Python文件路径
#     """
#     # os.system('cd '+extract_path)
#     result = subprocess.run(['python', file_path], capture_output=True, text=True)
#     print(f"运行结果:\n{result.stdout}")
#     if result.stderr:
#         print(f"运行时出现错误:\n{result.stderr}")


def main(task):
    # # 下载链接 (你可以通过手动获取页面的 ZIP 下载链接)
    # # download_url = "https://anonymous.4open.science/api/repo/Road_eval_new-4010/zip"  # 需要根据页面的具体情况调整
    download_url = "https://anonymous.4open.science/api/repo/Road_eval1105-ED25/zip"

    if not os.path.exists("folder1105"):
        # 本地保存 ZIP 文件的路径
        zip_save_path = "folder1105.zip"
        extract_path = "folder1105"  # 解压到的文件夹

        if task == 'test':
            # 下载 ZIP 文件
            download_zip_from_url(download_url, zip_save_path)

            # 解压 ZIP 文件
            unzip_file(zip_save_path, extract_path)

    source_folder = "folder1105/GraphSamplingToolkit-main_improve_GE_directly_add_RL3_constructed2_1105v1"

    # 指定目标文件夹路径
    destination_folder = "./GraphSamplingToolkit-main_improve_GE_directly_add_RL3_constructed2_1105v1"

    # 将整个文件夹移动到目标位置
    if not os.path.exists(destination_folder):
        shutil.move(source_folder, destination_folder)


    source_folder = "folder1105/GraphSamplingToolkit-main_improve_GE_directly_add_RL3_constructed2_1105v2"

    # 指定目标文件夹路径
    destination_folder = "./GraphSamplingToolkit-main_improve_GE_directly_add_RL3_constructed2_1105v2"

    # 将整个文件夹移动到目标位置
    if not os.path.exists(destination_folder):
        shutil.move(source_folder, destination_folder)


    py_file_list = ['average_statistics_GE_RL3_constructed2_1105v1.py','main_pipeline_GE_RL3_constructed2_1105v1.py','main_pipeline_GE_RL3_constructed2_1105v1_single_test.py', \
                    'mapcompare_GE_RL3_constructed2_1105v1.py','mapcompare_GE_RL3_constructed2_1105v1_single_test.py']
    for py_file in py_file_list:
        shutil.copy('folder1105/'+py_file,'code1013/'+py_file)
    # python_file_path = "main_pipeline2.py" #os.path.join(extract_path, "main_pipeline2.py")  # 替换为你要运行的文件路径
    # run_python_file(python_file_path,extract_path)

    # 第二步：切换到某个文件夹
    target_directory = 'code1013'  # 替换为你想要切换的文件夹路径
    print(f"切换到目录: {target_directory}")
    os.chdir(target_directory)
    
    ##https://anonymous.4open.science/api/repo/Road-eval-new-Oct-F7C9/zip
    if task == 'test':
        python_script = "main_pipeline_GE_RL3_constructed2_1105v1_single_test.py"  # 替换为你要运行的 Python 脚本名
        print(f"运行 Python 脚本: {python_script}")
        subprocess.run(["python", python_script], check=True)

    else:
        # 第三步：运行指定的 Python 脚本
        python_script = "main_pipeline_GE_RL3_constructed2_1105v1.py"  # 替换为你要运行的 Python 脚本名
        print(f"运行 Python 脚本: {python_script}")
        subprocess.run(["python", python_script], check=True)

if __name__ == "__main__":
    # 创建一个解析器对象
    parser = argparse.ArgumentParser(description="一个简单的命令行参数示例")

    # 添加参数
    parser.add_argument('--task', default='train', type=str, help="输入任务类型")
    # parser.add_argument('--age', type=int, help="输入你的年龄")

    # 解析命令行参数
    args = parser.parse_args()
    main(args.task)