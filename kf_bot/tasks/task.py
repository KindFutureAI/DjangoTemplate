class Task:
    def __init__(self, task_id, task_type, content, status="PENDING"):
        self.task_id = task_id
        self.task_type = task_type
        self.content = content
        self.status = status  # PENDING, IN_PROGRESS, COMPLETED, FAILED

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "content": self.content,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            task_id=task_dict["task_id"],
            task_type=task_dict["task_type"],
            content=task_dict["content"],
            status=task_dict["status"]
        )

    def __str__(self):
        return f"Task ID: {self.task_id}, Type: {self.task_type}, Status: {self.status}, Content: {self.content}"