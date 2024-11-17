# tasks/idea_inputer_task.py
from .task import Task

class IdeaInputerTask(Task):
    def __init__(self, task_id, content):
        super().__init__(task_id, "idea_inputer", content)

    def generate_ideas(self):
        # 生成创意的具体逻辑
        # 这里可以调用大模型API来生成创意
        ideas = self.call_qwen_api("Generate some creative ideas for a novel.")
        return ideas