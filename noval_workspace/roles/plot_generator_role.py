# roles/plot_generator_role.py

from .role import Role

class PlotGeneratorRole(Role):
    def __init__(self):
        super().__init__("Plot Generator")

    def perform_task(self, task):
        # 基于提交的想法生成基本情节
        print(f"{self.name} is generating a plot based on the idea: {task.idea}")
        
        # 这里可以调用大模型生成情节
        # 例如：plot = generate_plot(task.idea)
        # 返回生成的情节
        return "Generated Plot"