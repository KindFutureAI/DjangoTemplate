# communication/message.py
import json

class Message:
    """A class representing a message."""
    def __init__(self, sender_id, receiver_id, content):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content

    def to_dict(self):
        """ Convert the message to a dictionary. """
        return {
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "content": self.content
        }

    @classmethod
    def from_dict(cls, message_dict):
        """Create a Message object from a dictionary."""
        return cls(
            sender_id=message_dict["sender_id"],
            receiver_id=message_dict["receiver_id"],
            content=message_dict["content"]
        )

    def to_json(self):
        """Convert the message to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str):
        """Create a Message object from a JSON string."""
        message_dict = json.loads(json_str)
        return cls.from_dict(message_dict)