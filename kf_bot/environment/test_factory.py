# main.py
from environment.simple_factory import SimpleFactory
from agents.manager_agent import ManagerAgent
from agents.worker_agent import WorkerAgent
from roles.manager_role import ManagerRole
from roles.worker_role import WorkerRole

if __name__ == "__main__":
    # 创建环境
    factory = SimpleFactory()

    # 创建智能体
    manager_role = ManagerRole()
    manager_agent = ManagerAgent(manager_role)

    worker_roles = [WorkerRole() for _ in range(6)]
    worker_agents = [WorkerAgent(role) for role in worker_roles]

    # 初始化环境
    agents = {
        "Manager": manager_agent,
        "Worker1": worker_agents[0],
        "Worker2": worker_agents[1],
        "Worker3": worker_agents[2],
        "Worker4": worker_agents[3],
        "Worker5": worker_agents[4],
        "Worker6": worker_agents[5]
    }
    factory.initialize(agents)

    # 运行环境
    factory.run()