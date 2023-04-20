from vimeo_downloader import Vimeo, URLNotSupported
import os
import json
from utils import utilsFunctions

COURSES_BASE_PATH = os.path.join(os.getcwd(), 'courses')


def download_video(vimeo_url, directory, filename):
    video = Vimeo(vimeo_url)
    best_stream = video.streams[-1]
    best_stream.download(download_directory=directory, filename=filename)

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def load_json_data(json_file_path):
    data = None
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    return data


def download_course(course_json_file_path):
    json_data = load_json_data(course_json_file_path)
    course_name_unformat = json_data.get('nome_curso')
    course_name = json_data.get('nome_curso').replace('/', '').replace(':', '').replace('*').replace('?', '').replace('<','').replace('>', '')
    course_folder_path = os.path.join(COURSES_BASE_PATH, course_name)
    create_folder(course_folder_path)
    course_modules = json_data.get('modulos')
    for module in course_modules:
        module_number = module.get('index_modulo')
        module_folder_path = os.path.join(course_folder_path, f'{module_number} - {module.get("nome_modulo")}')
        create_folder(module_folder_path)
        module_video_list = module.get('lista_videos')
        for video in module_video_list:
            video_number = video.get('index_video')
            video_name = video.get('nome_video')
            video_file_name = f'{video_number} - {video_name}'
            video_url = video.get('url_video_vimeo')
            try:
                download_video(vimeo_url=video_url, directory=module_folder_path, filename=video_file_name, )
            except URLNotSupported as erro_url:
                print('Não é possível fazer o download. ', erro_url)


caminho_arquivo_json_curso = utilsFunctions.open_file()
download_course(caminho_arquivo_json_curso)


# dir = 'C:\\Users\\Guilherme\\Desktop\\Download Cursos\\download\\courses\Fundamentos em Contratação\\5 - Como selecionar os melhores talentos'
# file_name = '3 - AfterClass'
# download_video(vimeo_url='https://player.vimeo.com/video/542177592?byline=0&portrait=0&title=0&autopause=0', directory=dir , filename=file_name)