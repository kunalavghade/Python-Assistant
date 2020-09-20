import win32com.client as voice


class inputOutput:
    @staticmethod
    def input_Vals():
        r =input("Entern")
        return r

    @staticmethod
    def output(out):
        print(out)
        voice.Dispatch("SAPI.SpVoice")
        
