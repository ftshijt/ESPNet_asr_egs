import pandas as pd


class ASREgs:
    def __init__(self):
        self.data_frame = pd.read_csv("egs.csv")
    
    def get_path_text(self, lang):
        output = []
        for eg in self.data_frame:
            if eg["lang"] == lang:
                output.append((eg["path"], eg["text"]))
        return output
