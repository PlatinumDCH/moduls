from typing import Optional

Image = list[list[int]]

def flatten_image(image: Image)-> list:
    float_list = []
    for sublist in image:
        for item in sublist:
            float_list.append(item)
    return float_list

class Job:
    def __init__(self, title:str, description:Optional[str])->None:
        self.title = title
        self.description = description
    
    def __repr__(self):
        return self.title

