# roles/role.py
class Role:
    def __init__(self, agent):
        self.agent = agent

    def perform_task(self, task):
        raise NotImplementedError("Subclasses must implement this method")

    def report_status(self, task_id, status):
        message = {
            "task_id": task_id,
            "status": status
        }
        self.agent.environment.communicator.send_message(self.agent.id, self.agent.manager_id, message)        