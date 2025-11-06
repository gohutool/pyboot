"""
创建命令 - 使用 Click 和 Jinja2
"""
import shutil
from pathlib import Path
from typing import Optional
import os
import click
from jinja2 import Environment, PackageLoader, select_autoescape

# 创建 Jinja2 环境
env = Environment(
    loader=PackageLoader("pyboot.cli", "templates"),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True
)


@click.command()
@click.argument("name")
@click.option("-d", "--directory", default=".", 
              help="项目输出目录", show_default=True)
@click.option("-t", "--template", default="default",
              type=click.Choice(["default", "web", "api", "microservice"]),
              help="项目模板", show_default=True)
@click.option("--package", help="基础包名")
@click.option("--description", help="项目描述")
@click.option("-f", "--force", is_flag=True, help="覆盖已存在的目录")
@click.option("--no-input", is_flag=True, help="非交互模式，使用默认值")
def create_app(name: str, directory: str, template: str, package: Optional[str], 
               description: Optional[str], force: bool, no_input: bool):
    """
    创建新的 PyBoot 应用

    NAME: 项目名称
    """
    project_name = name
    output_dir = Path(directory) / project_name
    package_name = package or project_name.replace("-", "_").replace(" ", "_").lower()
    project_description = description or f"A PyBoot application named {project_name}"

    # 显示创建信息
    click.echo(click.style("🚀 创建 PyBoot 应用", fg="green", bold=True))
    click.echo(f"📁 项目名称: {project_name}")
    click.echo(f"📂 输出目录: {output_dir}")
    click.echo(f"🎨 模板类型: {template}")
    click.echo(f"📦 包名: {package_name}")

    # 检查目录是否存在
    if output_dir.exists():
        if not force and not no_input:
            if not click.confirm(f"❓ 目录 {output_dir} 已存在，是否覆盖?"):
                click.echo("❌ 取消创建")
                return
        click.echo("🗑️  清理现有目录...")
        shutil.rmtree(output_dir)

    # 创建项目结构
    try:
        _create_project_structure(project_name, package_name, project_description, 
                                 template, output_dir)
        click.echo(click.style("✅ 项目创建成功!", fg="green", bold=True))
        
        # 显示下一步指引
        _show_next_steps(output_dir, project_name)
        
    except Exception as e:
        click.echo(click.style(f"❌ 创建失败: {e}", fg="red"))
        # 清理部分创建的文件
        if output_dir.exists():
            shutil.rmtree(output_dir)
        raise click.Abort()


@click.command()
@click.argument("name")
@click.option("--package", help="模块包名")
def create_module(name: str, package: Optional[str]):
    """创建新的模块"""
    click.echo(f"创建模块: {name}")
    # TODO: 实现模块创建逻辑


@click.command()
@click.argument("name")
@click.option("--type", "component_type", 
              type=click.Choice(["service", "util", "config"]),
              default="service", help="组件类型")
def create_component(name: str, component_type: str):
    """创建新的组件"""
    click.echo(f"创建 {component_type} 组件: {name}")
    # TODO: 实现组件创建逻辑


def _create_project_structure(project_name: str, package_name: str, 
                             description: str, template: str, output_dir: Path):
    """创建项目目录结构"""
    
    # 模板上下文
    context = {
        "project_name": project_name,
        "package_name": package_name,
        "package_path": package_name.replace(".", "/"),
        "description": description,
        "template": template,
        "current_year": 2025,
        "python_version": "3.12.10"
    }
    
    # 定义目录结构
    directories = [
        # output_dir / "src" / package_name,
        output_dir / "application" / package_name, 
        output_dir / "docs",
        output_dir / "web", 
        output_dir / "conf",
        output_dir / "conf" / "sql",
        output_dir / "logs",
        output_dir / "db",
    ]
    
    # 包结构子目录
    package_dir = output_dir / "application" / package_name
    sub_dirs = [
        "config",
        "controller", 
        "service",
        "dao",
        "model",
        "utils",
    ]
    
    for sub_dir in sub_dirs:
        directories.append(package_dir / sub_dir)
    
    # 创建所有目录
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
    
    # 生成文件
    _generate_project_files(context, output_dir)


def _generate_project_files(context: dict, output_dir: Path):
    """生成项目文件"""
    base_dir = Path(os.path.dirname(__file__)).parent
    
    
    file_copy_mapping:list[Path, Path] = [        
        ("project/db/etcdv3.db", output_dir / "db/etcdv3.db"),
    ]
    
    for template_name, output_path in file_copy_mapping:
        template_name:Path = Path(f'{base_dir}/templates/{template_name}') 
        output_path:Path = output_path
        bs = template_name.read_bytes()
        output_path.write_bytes(bs)        
        
    # 文件映射：模板文件名 -> 输出路径
    file_mappings = [
        # 根目录文件
        ("project/app.py.j2", output_dir / "app.py"),
        ("project/pyproject.toml.j2", output_dir / "pyproject.toml"),
        ("project/requirements.txt.j2", output_dir / "requirements.txt"),
        ("project/README.md.j2", output_dir / "README.md"),
        ("project/.gitignore.j2", output_dir / ".gitignore"),
        ("project/.env.local.j2", output_dir / ".env.local"),
        
        # 配置文件
        ("project/conf/application.yaml.j2", output_dir / "conf/application.yaml"),
        ("project/conf/logback.yaml.j2", output_dir / "conf/logback.yaml"),
        ("project/conf/sql/sampleMapper.xml.j2", output_dir / "conf/sql/sampleMapper.xml"),
        
        # index.html
        ("project/index.html.j2", output_dir / "web/index.html"),
        
        # 包文件# 包文件
        ("project/__init__.py.j2", output_dir / "application" / "__init__.py"),
        ("project/__init__.py.j2", output_dir / "application" / context["package_name"] / "__init__.py"),
        
        # 配置类
        ("project/__init__.py.j2", output_dir / "application" / context["package_name"] / "config" / "__init__.py"),
        ("project/app_config.py.j2", output_dir / "application" / context["package_name"] / "config" / "config.py"),
        
        
        # 控制器
        ("project/__init__.py.j2", output_dir / "application" / context["package_name"] / "controller" / "__init__.py"),
        ("project/hello.controller.py.j2", output_dir / "application" / context["package_name"] / "controller" / "hello.py"),
        
        # 服务
        ("project/__init__.py.j2", output_dir / "application" / context["package_name"] / "service" / "__init__.py"),
        ("project/hello.service.py.j2", output_dir / "application" / context["package_name"] / "service" / "hello.py"),
        
        # MAPPER服务
        ("project/__init__.py.j2", output_dir / "application" / context["package_name"] / "dao" / "__init__.py"),
        ("project/hello.dao.py.j2", output_dir / "application" / context["package_name"] / "dao" / "hello.py"),
        
        # 模型
        # ("project/__init__.py.j2", output_dir / "application" / context["package_name"] / "model" / "__init__.py"),
        # ("project/user.py.j2", output_dir / "application" / context["package_name"] / "model" / "user.py"),
        
        # 工具类
        # ("project/utils/__init__.py.j2", output_dir / "src" / context["package_name"] / "utils" / "__init__.py"),
        # ("project/utils/response_util.py.j2", output_dir / "src" / context["package_name"] / "utils" / "response_util.py"),
        
    ]
    
    # 渲染并写入所有文件
    for template_name, output_path in file_mappings:
        try:
            template = env.get_template(template_name)
            rendered_content = template.render(**context)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(rendered_content, encoding='utf-8')
            click.echo(f"📄 创建文件: {output_path.relative_to(output_dir)}")
        except Exception as e:
            click.echo(f"⚠️  生成文件失败 {template_name}: {e}")


def _show_next_steps(output_dir: Path, project_name: str):
    """显示下一步指引"""
