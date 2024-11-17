# main.py
# from environment.simple_factory import SimpleFactory
# from agents.manager_agent import ManagerAgent
# from agents.worker_agent import WorkerAgent
# from roles.manager_role import ManagerRole
# from roles.worker_role import WorkerRole

# def main():
#     # 创建工厂环境
#     factory = SimpleFactory()
    
#     # 创建管理智能体
#     manager_role = ManagerRole()
#     manager_agent = ManagerAgent(role=manager_role)
#     factory.add_agent(manager_agent)
    
#     # 创建工人智能体
#     for i in range(5):  # 假设有5个工人智能体
#         worker_role = WorkerRole()
#         worker_agent = WorkerAgent(role=worker_role)
#         factory.add_agent(worker_agent)
    
#     # 启动环境
#     factory.run()


# main.py

from tasks.task_manager import TaskManager
from agents.base_agent import BaseAgent
from .roles import (IdeaInputerRole, PlotGeneratorRole, WriterRole, EditorRole,
                   CharacterDeveloperRole, ReaderSimulatorRole) 

def main():
    # Initialize TaskManager
    task_manager = TaskManager()

    # Create roles
    idea_inputer_role = IdeaInputerRole()
    plot_generator_role = PlotGeneratorRole()
    character_developer_role = CharacterDeveloperRole()
    writer_role = WriterRole()
    editor_role = EditorRole()
    reader_simulator_role = ReaderSimulatorRole()

    # Create agents with roles
    manager_agent = BaseAgent("Manager", idea_inputer_role)
    expert_agent = BaseAgent("Expert", plot_generator_role)
    senior_worker_agent = BaseAgent("SeniorWorker", character_developer_role)
    junior_worker_1_agent = BaseAgent("JuniorWorker1", writer_role)
    junior_worker_2_agent = BaseAgent("JuniorWorker2", editor_role)

    # Create a task
    task = task_manager.create_task("IDEA_INPUT", "Write a novel about a futuristic world")

    # Assign the task to the appropriate agent
    if manager_agent.role.can_handle_task(task.task_type):
        manager_agent.take_task(task)
    elif expert_agent.role.can_handle_task(task.task_type):
        expert_agent.take_task(task)
    elif senior_worker_agent.role.can_handle_task(task.task_type):
        senior_worker_agent.take_task(task)
    elif junior_worker_1_agent.role.can_handle_task(task.task_type):
        junior_worker_1_agent.take_task(task)
    elif junior_worker_2_agent.role.can_handle_task(task.task_type):
        junior_worker_2_agent.take_task(task)

    # Complete the task
    if manager_agent.current_task:
        manager_agent.complete_task("A detailed outline of the novel")
    elif expert_agent.current_task:
        expert_agent.complete_task("A basic plot for the novel")
    elif senior_worker_agent.current_task:
        senior_worker_agent.complete_task("Detailed character profiles")
    elif junior_worker_1_agent.current_task:
        junior_worker_1_agent.complete_task("First draft of the novel")
    elif junior_worker_2_agent.current_task:
        junior_worker_2_agent.complete_task("Edited and polished version of the novel")

    # Print all tasks
    for t in task_manager.get_all_tasks():
        print(t)

if __name__ == "__main__":
    main()