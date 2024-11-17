# roles/character_developer_role.py

from .role import Role

class CharacterDeveloperRole(Role):
    def __init__(self):
        super().__init__("Character Developer")

    def perform_task(self, task):
        # 丰富情节中的人物
        print(f"{self.name} is developing characters for the plot: {task.plot}")
        # 这里可以调用大模型生成人物设定
        # 例如：characters = generate_characters(task.plot)
        # 返回生成的人物设定
        return "Developed Characters"