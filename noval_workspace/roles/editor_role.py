# roles/editor_role.py

from .role import Role

class EditorRole(Role):
    def __init__(self):
        super().__init__("Editor")

    def perform_task(self, task):
        # 检查并优化最终稿
        print(f"{self.name} is editing the story: {task.story}")
        # 这里可以调用大模型进行校对和优化
        # 例如：edited_story = edit_story(task.story)
        # 返回优化后的最终稿
        return "Edited Story"