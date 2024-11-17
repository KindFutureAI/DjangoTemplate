# roles/idea_inputer_role.py

from .role import Role

class IdeaInputerRole(Role):
    def __init__(self):
        super().__init__("Idea Inputer")

    def perform_task(self, task):
        # 提交创意想法
        print(f"{self.name} is submitting an idea: {task.idea}")
        
        # 这里可以调用大模型生成创意想法
        # 例如：idea = generate_idea(task)
        # 返回生成的想法
        return task.idea