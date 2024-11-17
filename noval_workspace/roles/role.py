# roles/role.py
class Role:
    def __init__(self, agent, name=None):
        self.agent = agent
        self.name = name  # TODO

    def perform_task(self, task):
        raise NotImplementedError("Subclasses must implement this method")

    def report_status(self, task_id, status):
        """ 展示指定任务的执行状态 """
        # TODO 这个功能，有意义吗？
        message = {
            "task_id": task_id,
            "status": status
        }
        self.agent.environment.communicator.send_message(self.agent.id, self.agent.manager_id, message)        



    def is_manager(self):
        return False

    def is_worker(self):
        return False

    def can_handle_task(self, task):
        return False

    def needs_notification(self, task):
        return False 
        
    def __str__(self):
        return f"Role: {self.name}"