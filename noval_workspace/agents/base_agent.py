# agents/base_agent.py
import uuid
from ..roles.role import Role
from ..environment.base_environment import BaseEnvironment

class BaseAgent:
    """ 团队成员基类 """
    def __init__(self, name, environment: BaseEnvironment):
        self.id = str(uuid.uuid4())  # ID
        self.roles = []              # 角色
        self.name = name             # 名称
        # self.position_level = 1      # 职位级别 TODO
        self.environment = environment
        self.environment.add_agent(self)

    def add_role(self, role: Role):
        """ 添加角色 """
        self.roles.append(role)
        
    def remove_role(self, role: Role):
        """ 移除角色 """
        self.roles.remove(role)

    def send_message(self, receiver_id, content):
        """ 发送消息 """
        message = {
            "sender_id": self.id,
            "receiver_id": receiver_id,
            "content": content
        }
        self.environment.communicator.send_message(message)

    def receive_message(self, message):
        """ 接收消息 """
        if message["receiver_id"] == self.id:
            self.handle_message(message)

    def handle_message(self, message):
        """ 处理消息 """
        raise NotImplementedError("Subclasses must implement this method")

    def run(self):
        """ 运行 """
        raise NotImplementedError("Subclasses must implement this method")
    

    def set_environment(self, environment):
        """ 指定环境 """
        self.environment = environment

    def can_handle_task(self, task):
        """ 判断是否可以处理任务 """
        return self.role.can_handle_task(task)

    def assign_task(self, task):
        """ 分配任务 """
        self.current_task = task
        print(f"{self.role.name} assigned task: {task}")

    def has_completed_task(self):
        """ 判断是否完成任务 """
        return self.current_task and self.current_task.status == "completed"

    def get_completed_task(self):
        """ 获取已完成的任务 """
        return self.current_task

    def notify(self, task):
        """ 通知 """
        print(f"{self.role.name} notified about task: {task}")

    def needs_notification(self, task):
        """ 是否需要通知 """
        return self.role.needs_notification(task)
    
    def report_status(self, status):
        # 向 ManagerAgent 报告状态
        message = f"{self.name} reports: {status}"
        self.send_message(message, "ManagerAgent")