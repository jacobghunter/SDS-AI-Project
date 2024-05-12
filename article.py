import json

class article_obj:
    # constructor for strings
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    @classmethod
    def fromDict(self, dict: dict):
        self.title = dict["title"]
        self.content = dict["content"]
    
    @classmethod
    def fromJSON(self, json_obj: dict):
        self.title= list(json_obj.keys())[0]
        self.content = json_obj[self.title]
    
    def __str__(self):
        return self.title
    
    def toDict(self):
        return json.dumps({"title": self.title, "content": self.content})

    def toJSON(self):
        return {self.title: self.content}