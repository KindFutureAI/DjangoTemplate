import pymysql

"""
这行代码将 pymysql 安装为 MySQLdb 的替代品。
MySQLdb 是一个常用的 Python MySQL 客户端库，但在某些环境中可能无法安装或使用。
通过调用 install_as_MySQLdb() 方法，可以使得 pymysql 在代码中以 MySQLdb 的形式被引用，从而兼容那些依赖于 MySQLdb 的代码。
"""

# pymysql.version_info = (1, 4, 3, "final", 0)
pymysql.version_info = (1, 4, 6, 'final', 1)
pymysql.install_as_MySQLdb()

