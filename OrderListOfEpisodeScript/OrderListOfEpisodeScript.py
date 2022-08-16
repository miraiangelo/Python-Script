import os

def goToFolder():
    path = input("Folder Path:")
    changing_directory = os.chdir(path)
    return changing_directory

def listOfEpisodeInFolder():
    filepath = goToFolder()
    list_file = [file for file in os.listdir(filepath) if file.endswith(".mkv") or file.endswith(".mp4")] 
    return list_file
def OrderEpisodeInFolder():
    filelist = listOfEpisodeInFolder()
    index = 0
    folderList = []
    while index < len(filelist):
        indexEpisodeNumber = -5
        file_number = filelist[index][indexEpisodeNumber]
        filename = filelist[index]
        if file_number.isdecimal():
            last_string_format = f"episódio {file_number}.mp4"
            folder_names = filename.split(last_string_format)
            for folder_name in folder_names:
                if folder_name != '':
                    folderList.append(folder_name)
        index = index + 1
    return folderList

def makeFolderByName():
    anime_folders = OrderEpisodeInFolder()
    for anime_folder in anime_folders:
        try:
            os.mkdir(anime_folder)
        except Exception:
            continue
    return "folders successfully created"


print(makeFolderByName())