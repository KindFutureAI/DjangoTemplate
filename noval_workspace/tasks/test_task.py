from task import Task
from task_manager import TaskManager

# 创建任务管理器
task_manager = TaskManager()

# 创建任务
task1 = task_manager.create_task("IdeaInput", "Submit your ideas for the novel")
task2 = task_manager.create_task("PlotGeneration", "Generate a basic plot based on the submitted ideas")

# 打印所有任务
print(task_manager)

# 更新任务状态
task_manager.update_task_status(task1.task_id, "COMPLETED")
task_manager.update_task_status(task2.task_id, "IN_PROGRESS")

# 再次打印所有任务
print(task_manager)

# 获取特定任务
specific_task = task_manager.get_task(task1.task_id)
print(specific_task)