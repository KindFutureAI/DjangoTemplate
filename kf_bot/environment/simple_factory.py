 # environment/simple_factory.py
from .base_environment import BaseEnvironment

class SimpleFactory(BaseEnvironment):
    def __init__(self):
        super().__init__()

    def initialize(self, agents):
        for agent_id, agent in agents.items():
            self.add_agent(agent_id, agent)

    def run(self):
        print("Starting the factory environment...")
        while True:
            for agent_id, agent in self.agents.items():
                # 检查是否有消息需要处理
                messages = self.receive_message(agent_id)
                for message in messages:
                    agent.handle_message(message)

                # 让智能体执行其任务
                agent.run()