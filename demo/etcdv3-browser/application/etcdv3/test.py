from dataflow.utils.utils import parse_long_args_plus

print(parse_long_args_plus(['--port=9090']))
print(parse_long_args_plus(['--port','9090']))