# tasks/writer_task.py
from .task import Task

class WriterTask(Task):
    def __init__(self, task_id, content):
        super().__init__(task_id, "writer", content)

    def write_story(self):
        # 撰写故事的具体逻辑
        # 这里可以调用大模型API来撰写故事
        story = self.call_qwen_api(f"Write a story based on the following plot and characters: {self.content}")
        return story