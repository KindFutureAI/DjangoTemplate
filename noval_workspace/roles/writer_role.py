# roles/writer_role.py

from .role import Role

class WriterRole(Role):
    def __init__(self):
        super().__init__("Writer")

    def perform_task(self, task):
        # 编写故事
        print(f"{self.name} is writing the story based on the plot and characters: {task.plot}, {task.characters}")
        # 这里可以调用大模型生成故事文本
        # 例如：story = generate_story(task.plot, task.characters)
        # 返回生成的故事文本
        return "Written Story"