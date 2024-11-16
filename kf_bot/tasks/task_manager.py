import uuid
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task_type, content):
        task_id = str(uuid.uuid4())
        task = Task(task_id, task_type, content)
        self.tasks[task_id] = task
        return task

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def update_task_status(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id].status = status
        else:
            raise ValueError(f"Task with ID {task_id} not found")

    def list_tasks(self):
        return [task.to_dict() for task in self.tasks.values()]

    def __str__(self):
        return "\n".join([str(task) for task in self.tasks.values()])