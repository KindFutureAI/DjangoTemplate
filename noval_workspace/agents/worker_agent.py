# agents/worker_agent.py
from .base_agent import BaseAgent
from roles.worker_role import WorkerRole
from tasks.task import Task
from tasks.task_manager import TaskManager
from communication.message import Message
from communication.redis_communicator import RedisCommunicator

class WorkerAgent(BaseAgent):
    def __init__(self, role, environment):
        super().__init__(role, environment)
        self.task_manager = TaskManager()

    def handle_message(self, message):
        content = message["content"]
        if "task" in content:
            task_dict = content["task"]
            task = Task.from_dict(task_dict)
            self.execute_task(task)
        elif "report" in content:
            report = content["report"]
            self.report_status(report)

    def execute_task(self, task):
        print(f"Worker {self.id} is executing task: {task.to_dict()}")
        # 根据任务类型执行具体操作
        if task.task_type == "IdeaInput":
            self.idea_input(task)
        elif task.task_type == "PlotGeneration":
            self.plot_generation(task)
        elif task.task_type == "CharacterDevelopment":
            self.character_development(task)
        elif task.task_type == "Writing":
            self.writing(task)
        elif task.task_type == "Editing":
            self.editing(task)
        elif task.task_type == "Feedback":
            self.feedback(task)
        else:
            print(f"Unknown task type: {task.task_type}")

    def idea_input(self, task):
        # 提交创意想法
        ideas = self.role.generate_ideas()
        self.report_status({"task_id": task.task_id, "status": "COMPLETED", "result": ideas})

    def plot_generation(self, task):
        # 生成基本情节
        plot = self.role.generate_plot(task.content)
        self.report_status({"task_id": task.task_id, "status": "COMPLETED", "result": plot})

    def character_development(self, task):
        # 丰富人物设定
        characters = self.role.develop_characters(task.content)
        self.report_status({"task_id": task.task_id, "status": "COMPLETED", "result": characters})

    def writing(self, task):
        # 编写故事
        story = self.role.write_story(task.content)
        self.report_status({"task_id": task.task_id, "status": "COMPLETED", "result": story})

    def editing(self, task):
        # 校对和优化
        edited_story = self.role.edit_story(task.content)
        self.report_status({"task_id": task.task_id, "status": "COMPLETED", "result": edited_story})

    def feedback(self, task):
        # 提供反馈
        feedback = self.role.provide_feedback(task.content)
        self.report_status({"task_id": task.task_id, "status": "COMPLETED", "result": feedback})

    def report_status(self, report):
        self.send_message(self.environment.manager_id, {"report": report})

    def run(self):
        while True:
            # 监听消息并处理
            message = self.environment.communicator.receive_message(self.id)
            if message:
                self.receive_message(message)