 # environment/simple_factory.py
from .base_environment import BaseEnvironment
from ..agents.base_agent import BaseAgent
from ..roles.role import Role
from ..tasks.task_manager import TaskManager

class SimpleFactory(BaseEnvironment):
    def __init__(self):
        super().__init__()
        self.task_manager = TaskManager()

    def initialize(self, agents):
        for agent_id, agent in agents.items():
            self.add_agent(agent_id, agent)


    def add_agent(self, agent: BaseAgent):
        super().add_agent(agent)
        # 根据角色类型进行初始化
        if isinstance(agent.role, Role):
            if agent.role.is_manager():
                self._initialize_manager(agent)
            elif agent.role.is_worker():
                self._initialize_worker(agent)


    def _initialize_manager(self, manager: BaseAgent):
        # 初始化经理级别的智能体
        pass  # 这里可以添加一些初始化逻辑

    def _initialize_worker(self, worker: BaseAgent):
        # 初始化工人级别的智能体
        pass  # 这里可以添加一些初始化逻辑


    def _assign_task(self, task):
        # 根据任务类型和智能体的能力分配任务
        for agent in self.get_agents():
            if agent.can_handle_task(task):
                agent.assign_task(task)
                break

    def _check_task_status(self):
        # 检查所有智能体的任务状态
        for agent in self.get_agents():
            if agent.has_completed_task():
                completed_task = agent.get_completed_task()
                self.task_manager.complete_task(completed_task)
                # 通知其他智能体或进行下一步操作
                self._notify_completion(completed_task)

    def _notify_completion(self, task):
        # 通知其他智能体任务完成
        for agent in self.get_agents():
            if agent.needs_notification(task):
                agent.notify(task)

    def _simulate_time_passing(self):
        # 模拟时间流逝
        import time
        time.sleep(1)  # 每秒检查一次


    def run(self):
        print("Starting the factory environment...")
        while True:

            # 生成新的任务
            new_task = self.task_manager.generate_new_task()
            if new_task:
                # 分配任务
                self._assign_task(new_task)
            # 检查任务状态
            self._check_task_status()
            # 模拟时间流逝
            self._simulate_time_passing()

            # for agent_id, agent in self.agents.items():
            #     # 检查是否有消息需要处理
            #     messages = self.receive_message(agent_id)
            #     for message in messages:
            #         agent.handle_message(message)

            #     # 让智能体执行其任务
            #     agent.run()