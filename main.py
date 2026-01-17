from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    status: str

todos: List[Todo] = []

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message":"Todo created successfully", "todo":todo}

@app.get("/todos")
def get_all_todos():
    return todos

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo:Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated successfully", "todo":updated_todo}
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted = todos.pop(index)
            return {"message": "Todo deleted successfully", "todo":deleted}
    raise HTTPException(status_code=404, detail="Todo not found")
