import NotePadFileModel
import speech_recognition as s
import NotePadDbModel
class File_Controller:
    def __init__(self):
        self.file_model=NotePadFileModel.File_Model()

    def save_file(self,msg):
        self.file_model.save_file(msg)

    def save_as(self,msg):
        self.file_model.save_as(msg)

    def read_file(self,url=''):
        self.msg,self.base=self.file_model.read_file(url)
        return self.msg,self.base

    def new_file(self):
        self.file_model.new_file()

    def take_query(self):
        sr = s.Recognizer()
        print("Say something")
        with s.Microphone() as m:
            try:
                audio = sr.listen(m)
                text = sr.recognize_google(audio, language='hi-IN')
                return text
            except:
                print("Exception occurred")

