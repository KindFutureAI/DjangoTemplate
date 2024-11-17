# roles/reader_simulator_role.py

from .role import Role

class ReaderSimulatorRole(Role):
    def __init__(self):
        super().__init__("Reader Simulator")

    def perform_task(self, task):
        # 提供反馈，帮助评估作品的质量
        print(f"{self.name} is simulating a reader's experience with the story: {task.story}")
        # 这里可以调用大模型生成读者反馈
        # 例如：feedback = generate_feedback(task.story)
        # 返回读者反馈
        return "Reader Feedback"