# roles/worker_role.py
from .role import Role
import random

class IdeaInputer(Role):
    def perform_task(self, task):
        print(f"IdeaInputer {self.agent.id} is working on task: {task['content']}")
        # Simulate idea input
        ideas = ["A story about a lost treasure", "A mystery in a small town", "A fantasy world with dragons"]
        idea = random.choice(ideas)
        self.report_status(task["task_id"], f"Submitted idea: {idea}")

class PlotGenerator(Role):
    def perform_task(self, task):
        print(f"PlotGenerator {self.agent.id} is working on task: {task['content']}")
        # Simulate plot generation using Qwen API (or any other NLP model)
        plot = "Once upon a time, in a small village, a young hero discovers a map leading to a hidden treasure."
        self.report_status(task["task_id"], f"Generated plot: {plot}")

class CharacterDeveloper(Role):
    def perform_task(self, task):
        print(f"CharacterDeveloper {self.agent.id} is working on task: {task['content']}")
        # Simulate character development
        characters = {
            "Hero": {"name": "Ethan", "background": "A brave and curious young man"},
            "Villain": {"name": "Malcolm", "background": "A cunning and ruthless treasure hunter"}
        }
        self.report_status(task["task_id"], f"Developed characters: {characters}")

class Writer(Role):
    def perform_task(self, task):
        print(f"Writer {self.agent.id} is working on task: {task['content']}")
        # Simulate writing the story
        story = "In a small village, Ethan, a brave and curious young man, discovers a map leading to a hidden treasure. He sets out on an adventure, facing many challenges and encountering a cunning and ruthless treasure hunter named Malcolm."
        self.report_status(task["task_id"], f"Wrote story: {story}")

class Editor(Role):
    def perform_task(self, task):
        print(f"Editor {self.agent.id} is working on task: {task['content']}")
        # Simulate editing the story
        edited_story = "In a quaint village, Ethan, a valiant and inquisitive youth, stumbles upon a cryptic map that promises a hidden treasure. Embarking on a perilous journey, he confronts numerous obstacles and crosses paths with Malcolm, a shrewd and malevolent treasure seeker."
        self.report_status(task["task_id"], f"Edited story: {edited_story}")

class ReaderSimulator(Role):
    def perform_task(self, task):
        print(f"ReaderSimulator {self.agent.id} is working on task: {task['content']}")
        # Simulate reader feedback
        feedback = "The story is engaging and well-written. The characters are well-developed, and the plot is intriguing. However, some parts of the story could be more detailed."
        self.report_status(task["task_id"], f"Provided feedback: {feedback}")