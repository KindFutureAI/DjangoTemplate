# tasks/character_developer_task.py
from .task import Task

class CharacterDeveloperTask(Task):
    def __init__(self, task_id, content):
        super().__init__(task_id, "character_developer", content)

    def develop_character(self):
        # 开发角色的具体逻辑
        pass
