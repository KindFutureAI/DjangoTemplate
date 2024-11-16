 # environment/base_environment.py
from communication.redis_communicator import RedisCommunicator

class BaseEnvironment:
    def __init__(self):
        self.agents = {}
        self.communicator = RedisCommunicator()

    def add_agent(self, agent_id, agent):
        if agent_id in self.agents:
            raise ValueError(f"Agent with ID {agent_id} already exists")
        self.agents[agent_id] = agent
        agent.environment = self

    def remove_agent(self, agent_id):
        if agent_id not in self.agents:
            raise ValueError(f"Agent with ID {agent_id} does not exist")
        del self.agents[agent_id]

    def get_agent(self, agent_id):
        return self.agents.get(agent_id)

    def list_agents(self):
        return list(self.agents.keys())

    def send_message(self, sender_id, receiver_id, message):
        if receiver_id not in self.agents:
            raise ValueError(f"Receiver with ID {receiver_id} does not exist")
        self.communicator.send_message(sender_id, receiver_id, message)

    def receive_message(self, agent_id):
        return self.communicator.receive_message(agent_id)