# tasks/editor_task.py
from .task import Task

class EditorTask(Task):
    def __init__(self, task_id, content):
        super().__init__(task_id, "editor", content)

    def edit_text(self):
        # 编辑和校对的具体逻辑
        # 这里可以调用大模型API来进行编辑和校对
        edited_text = self.call_qwen_api(f"Edit and proofread the following text: {self.content}")
        return edited_text