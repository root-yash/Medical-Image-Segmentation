import os

class Initiate:
    def __init__(self):
        """
        It connects kaggle using api(it contain user id and password)
        """
        os.mkdir("Data")
        os.system("pip install -q kaggle")
        os.system("mkdir -p ~/.kaggle")
        os.system("mkdir -p ~/.kaggle")
        os.system("cp kaggle.json ~/.kaggle/")
        os.system("chmod 600 kaggle.json")

    def download(self, data = "hubmap-organ-segmentation"):
        """
        Input = Name of competitions whose data needs to be downloaded 
        what will happed?
        download the data and save it in "Data" folder
        """
        os.system(f"kaggle competitions download -c {data}")
        os.system(f"unzip {data}.zip -d Data/{data}/")
        os.system(f"rm -r {data}.zip")
        os.system("clear")
        print(f"{data} Downloaded")

