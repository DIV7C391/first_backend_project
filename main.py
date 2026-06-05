from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()
notes=[]

class create_note(BaseModel):
    title:str = Field(...,min_length=1)
    content:str = Field(...,min_length=1)

class Note_response(BaseModel):
    title:str
    content:str
    id:int

@app.post("/notes",response_model=Note_response)
def note_create(note: create_note):
    new_note={
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content
    }
    notes.append(new_note)
    return new_note


@app.get("/notes",response_model=List[Note_response])
def get_notes():
    return notes

@app.get("/notes/{note_id}", response_model=Note_response)
def get_one(note_id:int):
    for note in notes:
        if note["id"]==note_id:
            return note
        
class update_note(BaseModel):
    title:str
    content:str

@app.put("/notes/{note_id}", response_model=Note_response)
def update_note(note_id:int, updated_note=update_note):
    for note in notes:
        if note["id"]== note_id:
            note["title"]=updated_note.title
            note["content"]=updated_note.content

        return note
    
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):

    for note in notes:

        if note["id"] == note_id:

            notes.remove(note)

            return {
                "message": "Deleted"
            }


