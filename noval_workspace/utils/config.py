import os


current_dir = os.path.dirname(__file__)
config_file = os.path.join(current_dir, 'assets', 'config.yaml')

# TODO 等项目demo运行起来之后，就将这个大的配置文件拆分成更小的配置文件，方便管理
 

class NWConfig:
    NOVAL_WORKSPACE_CONFIG = {}
    NOVAL_WORKSPACE_CONFIG_PATH = config_file


nw_config = NWConfig()