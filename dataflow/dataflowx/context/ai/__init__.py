import importlib.util
from dataflow.utils.log import Logger

_logger = Logger('dataflowx.context.ai')

__ignore__ = []

if not importlib.util.find_spec("langchain_community"):
    _logger.WARN('没有langchain_community环境，不加载langchain_community模块，或者pip install langchain_community')
    __ignore__.append('milvus')