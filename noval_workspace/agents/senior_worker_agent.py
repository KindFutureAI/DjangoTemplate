from .base_agent import BaseAgent
from roles.senior_worker_role import SeniorWorkerRole

class SeniorWorkerAgent(BaseAgent):
    def __init__(self, name):
        super().__init__(name, SeniorWorkerRole())

    def execute_task(self, task):
        # 高级职位员工负责特定业务小组的任务
        print(f"{self.name} is working on the task: {task.description}")
        # 可以与专家沟通
        self.communicate_with_expert(task)

    def communicate_with_expert(self, task):
        # 与专家沟通
        message = f"SeniorWorker {self.name} needs guidance for task: {task.description}"
        self.send_message(message, "ExpertAgent")
        