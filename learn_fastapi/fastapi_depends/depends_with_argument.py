from typing import Optional
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

dummpy_db = {
    '1':"SDE1 at Google",
    '2':"SDE2 at Amazon",
    '3':"Backend Dev. at Spotify",
    '4':"Senior Engineer at Alphabet",
    '5':"Devops Eng. at Microsoft",
}

class GetObjectOrFeatured:
    def __init__(self, featured_job:Optional[str]=None):
        self.featured_job = featured_job
    
    def __call__(self, id:str)-> Optional[str]:
        value = dummpy_db.get(id)
        if not value and self.featured_job:
            value = dummpy_db.get(self.featured_job)
        if not value:
            raise HTTPException(status_code=404, detail='job not found')
        return value

@app.get('/job/{id}')
def get_job_by_id(job_title:str = Depends(GetObjectOrFeatured())):
    return job_title

"""
при вызове endpoint мы передаем параметр id, тем самым вызываем Depends 
c указанныс id что возвращает определенную работу
Если мы передадим id которого не будет в бд работ ты по дефолту вернется
первая работа из списка
"""