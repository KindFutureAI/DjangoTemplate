# communication/message.py
import json

class Message:
    def __init__(self, sender_id, receiver_id, content):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content

    def to_dict(self):
        return {
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "content": self.content
        }

    @classmethod
    def from_dict(cls, message_dict):
        return cls(
            sender_id=message_dict["sender_id"],
            receiver_id=message_dict["receiver_id"],
            content=message_dict["content"]
        )

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str):
        message_dict = json.loads(json_str)
        return cls.from_dict(message_dict)