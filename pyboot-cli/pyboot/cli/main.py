#!/usr/bin/env python3
"""
PyBoot CLI 主入口 - 使用 Click
"""

import sys
import pathlib
from pathlib import Path

import click

# 添加当前目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from .commands.create import create_app, create_module, create_component
# from .commands.run import run_app


@click.group()
@click.version_option(version="1.0.0", prog_name="PyBoot CLI")
@click.pass_context
def cli(ctx):
    """
    🚀 PyBoot CLI - Python Spring Boot 风格框架命令行工具
    
    快速创建、运行和管理 PyBoot 应用。
    
    示例:
    
    \b
    $ pyboot create app my-project
    $ cd my-project
    $ pyboot run
    """
    ctx.ensure_object(dict)
    
    # 设置项目根目录
    current_dir = Path.cwd()
    pyboot_files = ["app.py", "pyproject.toml", "requirements.txt"]
    
    if any((current_dir / f).exists() for f in pyboot_files):
        ctx.obj["project_root"] = current_dir
        ctx.obj["is_pyboot_project"] = True
    else:
        ctx.obj["project_root"] = None
        ctx.obj["is_pyboot_project"] = False


# 创建命令组
@cli.group()
def create():
    """创建新的项目、模块或组件"""
    pass

create.add_command(create_app, name="app")
create.add_command(create_module, name="module")
create.add_command(create_component, name="component")

# # 其他命令
# cli.add_command(run_app, name="run")


@cli.command()
@click.pass_context
def info(ctx):
    """显示 PyBoot 环境信息"""
    from rich.console import Console
    from rich.table import Table
    from rich import box
    
    console = Console()
    
    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("项目", style="cyan", width=20)
    table.add_column("值", style="green")
    
    table.add_row("Python 版本", sys.version.split()[0])
    table.add_row("工作目录", str(Path.cwd()))
    table.add_row("PyBoot 项目", "✅ 是" if ctx.obj["is_pyboot_project"] else "❌ 否")
    
    console.print(table)


@cli.command()
@click.argument("package_name")
def install(package_name):
    """安装 PyBoot 插件或扩展"""
    import subprocess
    
    click.echo(f"📦 安装包: {package_name}")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package_name],
            check=True,
            capture_output=True,
            text=True
        )
        click.echo(f"✅ 成功安装 {package_name}")
        if result.stdout:
            click.echo(result.stdout)
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ 安装失败: {e}")
        if e.stderr:
            click.echo(e.stderr)
        sys.exit(1)

@cli.command(context_settings={"ignore_unknown_options": True, "allow_extra_args": True})
def run():
    # from dataflow.boot import ApplicationBoot
    # proj_root = pathlib.Path.cwd()          # 假设 cli 就在项目根
    # sys.path.insert(0, str(proj_root)) 
    # ApplicationBoot.Start()
    import runpy
    # 1. 保证模块能被发现
    proj_root = pathlib.Path.cwd()          # 假设 cli 就在项目根
    if proj_root not in sys.path:
        sys.path.insert(0, str(proj_root)) 
    # 2. 把 argv[0] 换成模块入口，保持后续所有参数    
    sys.argv = ["-m dataflow.main", *sys.argv[1:]]
    # 3. 以“python -m dataflow.main <args...>”方式执行
    runpy.run_module("dataflow.main", run_name="__main__")
        
    

@cli.command()
def doctor():
    """检查 PyBoot 环境健康状况"""
    from rich.console import Console
    from rich.table import Table
    
    console = Console()
    console.print("[bold blue]🔧 PyBoot 环境诊断[/bold blue]")
    
    table = Table(show_header=True, header_style="bold green")
    table.add_column("检查项", style="cyan")
    table.add_column("状态", style="white")
    table.add_column("说明", style="yellow")
    
    # 检查 Python 版本
    python_ok = sys.version_info >= (3, 8)
    table.add_row(
        "Python 版本 (>=3.8)",
        "✅" if python_ok else "❌",
        f"当前: {sys.version.split()[0]}"
    )
    
    # 检查必要包
    packages = ["click", "jinja2", "rich"]
    for package in packages:
        try:
            __import__(package)
            table.add_row(f"{package} 包", "✅", "已安装")
        except ImportError:
            table.add_row(f"{package} 包", "❌", "未安装")
    
    # 检查当前目录
    current_dir = Path.cwd()
    has_pyboot_files = any((current_dir / f).exists() for f in ["app.py", "pyproject.toml"])
    table.add_row(
        "PyBoot 项目目录",
        "✅" if has_pyboot_files else "⚠️",
        "当前目录包含 PyBoot 项目文件" if has_pyboot_files else "当前目录不是 PyBoot 项目"
    )
    
    console.print(table)


def main():
    """CLI 主入口"""
    cli(obj={})


if __name__ == "__main__":
    main()