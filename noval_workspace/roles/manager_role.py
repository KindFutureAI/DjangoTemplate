# roles/manager_role.py
from .role import Role

class ManagerRole(Role):
    def handle_report(self, message):
        print(f"Manager received report: {message}")
        task_id = message["task_id"]
        status = message["status"]
        self.agent.task_manager.update_task_status(task_id, "COMPLETED")
        print(f"Task {task_id} completed: {status}")

    def run(self):
        # Initial task assignment
        self.agent.assign_task("Worker1", "IdeaInput", "Submit your ideas for the novel")
        self.agent.assign_task("Worker2", "PlotGeneration", "Generate a basic plot based on the submitted ideas")
        self.agent.assign_task("Worker3", "CharacterDevelopment", "Develop characters for the plot")
        self.agent.assign_task("Worker4", "Writing", "Start writing the story")
        self.agent.assign_task("Worker5", "Editing", "Edit and optimize the final draft")
        self.agent.assign_task("Worker6", "Feedback", "Provide feedback on the quality of the work")

        # Monitor progress
        while True:
            for task in self.agent.task_manager.list_tasks():
                if task["status"] == "COMPLETED":
                    print(f"Task {task['task_id']} completed: {task['content']}")
                elif task["status"] == "FAILED":
                    print(f"Task {task['task_id']} failed: {task['content']}")