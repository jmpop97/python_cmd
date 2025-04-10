import subprocess
import logging
result = subprocess.run(['ls'], capture_output=True, text=True)
# print(result.stdout)
# logging.basicConfig(filename='./log/main.log',level=logging.DEBUG)
# logging.error(result.stdout)
cmdLine="cat sample.json"
file_path = 'sample.json'
class JsonFile():
    def __init__(self,file_path,cmdLine):
        self.file_path=file_path
        self.cmdLine=cmdLine.split(" ")
        with open(file_path, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()  # 각 줄이 리스트의 요소가 됨
    def changeFile(self):
        for lineI,line in enumerate(self.lines):
            if "#siteLoginInfo" in line:
                self.lines[lineI]=line.replace("#siteLoginInfo","siteLoginInfo")
                self.saveFile()
                self.cmd()
                self.lines[lineI]=line
    def saveFile(self):
        with open(self.file_path,"w",encoding="utf-8") as f:
            f.write("".join(self.lines))
    def cmd(self):
        result = subprocess.run(self.cmdLine, capture_output=True, text=True)
        print(result.stdout)
JsonFile(file_path,cmdLine).changeFile()