# agents/base_agent.py
import uuid

class BaseAgent:
    def __init__(self, role, environment):
        self.id = str(uuid.uuid4())
        self.role = role
        self.environment = environment
        self.environment.add_agent(self)

    def send_message(self, recipient_id, content):
        message = {
            "sender_id": self.id,
            "recipient_id": recipient_id,
            "content": content
        }
        self.environment.communicator.send_message(message)

    def receive_message(self, message):
        if message["recipient_id"] == self.id:
            self.handle_message(message)

    def handle_message(self, message):
        raise NotImplementedError("Subclasses must implement this method")

    def run(self):
        raise NotImplementedError("Subclasses must implement this method")