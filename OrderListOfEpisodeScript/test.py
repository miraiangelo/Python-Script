import os

def goToFolder():
    path = input("Folder Path:")
    if os.path.exists(path):
        changing_directory = os.chdir(path)
        return changing_directory
    else:
        return "path reference is invalid"
def listOfEpisodeInFolder():
    filepath = goToFolder()
    if filepath != "path reference is invalid":
        list_file = [file for file in os.listdir(filepath) if file.endswith(".mp4") or file.endswith(".mkv")] 
        return list_file
def OrderEpisodeInFolder():
    filelist = listOfEpisodeInFolder()
    if filelist != None:
        index = 0
        folderList = []
        while index < len(filelist):
            indexEpisodeNumber = -5
            file_number = filelist[index][indexEpisodeNumber]
            filename = filelist[index]
            if file_number.isdecimal():
                last_string_format = "episódio {file_number}.mp4"
                folder_names = filename.split(last_string_format)
                for folder_name in folder_names:
                    if folder_name != '':
                        folderList.append(folder_name)
            index = index + 1
        return folderList
    else:
        return None

def makeFolderByName():
    anime_folders = OrderEpisodeInFolder()
    if anime_folders != None:
        for anime_folder in anime_folders:
            try:
                os.mkdir(anime_folder)
            except Exception:
                continue
        return "folders successfully created"
    else:
        return "There's Neither a validate path nor files in path reference"


print(makeFolderByName())