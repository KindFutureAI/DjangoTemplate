from .base_agent import BaseAgent
from roles.junior_worker_role_1 import JuniorWorkerRole1

class JuniorWorkerAgent1(BaseAgent):
    def __init__(self, name):
        super().__init__(name, JuniorWorkerRole1())

    def execute_task(self, task):

        # 初级职位员工1负责特定业务小组的任务
        print(f"{self.name} is working on the task: {task.description}")
        
        # 完成任务后报告状态
        self.report_status(f"Task {task.id} completed by {self.name}")