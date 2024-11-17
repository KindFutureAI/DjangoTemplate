from .role import Role

class ExpertRole(Role):
    def __init__(self):
        super().__init__("Expert")

    def perform_task(self, task):
        # 与一个初级员工组成一个业务小组
        print(f"{self.name} is working with a junior worker on the task: {task.content}")
        return f"Expert Task: {task.content} - Collaborating with Junior Worker"