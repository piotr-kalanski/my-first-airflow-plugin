from airflow.plugins_manager import AirflowPlugin
from my_first_airflow_plugin.operators.my_custom_operator import MyCustomOperator


class MyCustomPlugin(AirflowPlugin):
    name = "MyCustomPlugin"
    operators = [MyCustomOperator]
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
