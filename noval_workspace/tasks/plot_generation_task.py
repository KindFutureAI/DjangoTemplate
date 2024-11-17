# tasks/plot_generator_task.py
from .task import Task

class PlotGeneratorTask(Task):
    def __init__(self, task_id, content):
        super().__init__(task_id, "plot_generator", content)

    def generate_plot(self):
        # 生成情节的具体逻辑
        # 这里可以调用大模型API来生成情节
        plot = self.call_qwen_api(f"Generate a plot for the novel with the following idea: {self.content}")
        return plot