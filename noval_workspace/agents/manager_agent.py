# agents/manager_agent.py
from .base_agent import BaseAgent
from roles.manager_role import ManagerRole
from tasks.task import Task
from tasks.task_manager import TaskManager
from communication.message import Message
from communication.redis_communicator import RedisCommunicator

class ManagerAgent(BaseAgent):
    def __init__(self, role, environment):
        super().__init__(role, environment)
        self.task_manager = TaskManager()
        self.environment.manager_id = self.id

    def assign_task(self, agent_id, task_type, content):
        task = self.task_manager.create_task(task_type, content)
        self.send_message(agent_id, {"task": task.to_dict()})

    def handle_message(self, message):
        content = message["content"]
        if "report" in content:
            report = content["report"]
            self.handle_report(report)

    def handle_report(self, report):
        task_id = report["task_id"]
        status = report["status"]
        result = report.get("result", "")
        self.task_manager.update_task_status(task_id, status)
        print(f"Manager received report: {report}")
        if status == "COMPLETED":
            print(f"Task {task_id} completed: {result}")
        elif status == "FAILED":
            print(f"Task {task_id} failed: {result}")

    def run(self):
        # 初始任务分配
        self.assign_task("Worker1", "IdeaInput", "Submit your ideas for the novel")
        self.assign_task("Worker2", "PlotGeneration", "Generate a basic plot based on the submitted ideas")
        self.assign_task("Worker3", "CharacterDevelopment", "Develop characters for the plot")
        self.assign_task("Worker4", "Writing", "Start writing the story")
        self.assign_task("Worker5", "Editing", "Edit and optimize the final draft")
        self.assign_task("Worker6", "Feedback", "Provide feedback on the quality of the work")

        # 监控进度
        while True:
            for task in self.task_manager.list_tasks():
                if task["status"] == "COMPLETED":
                    print(f"Task {task['task_id']} completed: {task['content']}")
                elif task["status"] == "FAILED":
                    print(f"Task {task['task_id']} failed: {task['content']}")