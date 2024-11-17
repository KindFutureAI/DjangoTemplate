class Task:
    """
    任务类，用于描述一个任务的类型、内容、状态等属性。
    
    :param task_id: 任务ID
    :param task_type: 任务类型, 例如：writing, editing, character_development, plot_generation, idea_input, feedback
    :param content: 任务内容
    :param status: 任务状态, 默认为"WAITING"
    """
    def __init__(self, task_id, task_type, content, status="WAITING"):
        self.task_id = task_id 
        self.task_type = task_type
        self.content = content
        self.status = status  # WAITING, IN_PROGRESS, COMPLETED, FAILED

    def to_dict(self):
        # 将Task对象转换为字典
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "content": self.content,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, task_dict):
        # 从字典中创建一个Task对象
        return cls(
            task_id=task_dict["task_id"],
            task_type=task_dict["task_type"],
            content=task_dict["content"],
            status=task_dict["status"]
        )

    def __str__(self):
        return f"Task ID: {self.task_id}, Type: {self.task_type}, Status: {self.status}, Content: {self.content}"