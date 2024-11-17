import uuid
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task_type, content):
        """ 创建新的任务 """
        task_id = str(uuid.uuid4())
        task = Task(task_id, task_type, content)
        self.tasks[task_id] = task
        return task

    def get_task(self, task_id):
        """ 获取任务详情 """
        return self.tasks.get(task_id)

    def update_task_status(self, task_id, status):
        """ 更新任务的状态 """
        if task_id in self.tasks:
            self.tasks[task_id].status = status
        else:
            raise ValueError(f"Task with ID {task_id} not found")

    def list_tasks(self):
        """ 列出所有任务 """
        return [task.to_dict() for task in self.tasks.values()]

    def __str__(self):
        """ 返回所有任务的字符串表示 """
        if not self.tasks:
            return "No tasks available"
        
        task_strings = [str(task) for task in self.tasks.values()]
        return "\n\n".join(task_strings)  # 使用两个换行符分隔每个任务，使输出更易读