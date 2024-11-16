# main.py
from environment.simple_factory import SimpleFactory
from agents.manager_agent import ManagerAgent
from agents.worker_agent import WorkerAgent
from roles.manager_role import ManagerRole
from roles.worker_role import WorkerRole

def main():
    # 创建工厂环境
    factory = SimpleFactory()
    
    # 创建管理智能体
    manager_role = ManagerRole()
    manager_agent = ManagerAgent(role=manager_role)
    factory.add_agent(manager_agent)
    
    # 创建工人智能体
    for i in range(5):  # 假设有5个工人智能体
        worker_role = WorkerRole()
        worker_agent = WorkerAgent(role=worker_role)
        factory.add_agent(worker_agent)
    
    # 启动环境
    factory.run()

if __name__ == "__main__":
    main()