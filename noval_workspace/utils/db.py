# 数据库的保存，在demo阶段，使用yaml文件保存，实际使用中，使用mysql数据库保存
import yaml
from config import nw_config 


class NWDataCenter:
    """ 数据中心：保存应用的数据"""

    def __init__(self):
        self.data_center = {}
        self.config = nw_config

    def _init_config(self):
        self._load_config()

    def _load_config(self):
        with open(self.config.NOVAL_WORKSPACE_CONFIG_PATH, 'r') as f:
            self.data_center = yaml.load(f, Loader=yaml.FullLoader)
    
    def _dump_config(self):
        with open(self.config.NOVAL_WORKSPACE_CONFIG_PATH, 'w') as f:
            yaml.dump(self.data_center, f)

    def _update_data_center(self, data):
        self.data_center = data
        self._dump_config()
    
    def update_data_center(self, data):
        self._update_data_center(data)

    def get_data_center(self):
        return self.data_center
    
def write_demo_data_to_config():
    """
    这个函数是给NOVAL_WORKSPACE_CONFIG添加一些默认的数据，方便调试
    """
    data = {
        "agents": [
            {
                "name": "agent_1",
                "role": "manager",
                "tasks": [
                    {
                        "task_id": "task_1",
                        "task_type": "idea_input",
                        "content": "I want to write a story about a robot who is trying to save the world."
                    },
                    {
                        "task_id": "task_2",
                        "task_type": "plot_generation",
                        "content": "I want to write a story about a robot who is trying to save the world."
                    },
                    {
                        "task_id": "task_3",
                    }
                ]
            }
        ]
    }
    nw_data_center.update_data_center(data)

    print("write demo data to config file")
    print(nw_data_center.get_data_center())


if __name__ == "__main__":
    nw_data_center = NWDataCenter()
    write_demo_data_to_config()