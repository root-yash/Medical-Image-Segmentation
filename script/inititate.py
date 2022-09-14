import os 

class Initiate:
    def __init__(self):
        os.mkdir("Data")
        os.system("!pip install -q kaggle")
        os.system("!mkdir -p ~/.kaggle")
        os.system("!mkdir -p ~/.kaggle")
        os.system("!cp kaggle.json ~/.kaggle/")
        os.system("!chmod 600 kaggle.json")

    def download(self, data = "hubmap-organ-segmentation"):
        os.system(f"!kaggle competitions download -c {data}")
        os.system(f"!unzip {data}.zip -d Data/{data}/")
        os.system(f"!rm -r {data}.zip")

