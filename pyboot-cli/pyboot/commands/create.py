import os
import shutil
from pathlib import Path
import click
from colorama import Fore, Style, init

# 初始化 colorama 用于彩色输出
init(autoreset=True)

def get_template_path(template_name):
    """获取模板路径"""
    template_dir = Path(__file__).parent.parent / "templates"
    template_path = template_dir / template_name
    
    if not template_path.exists():
        raise click.ClickException(f"Template '{template_name}' not found")
    
    return template_path

def create_project_structure(directory, template, project_name):
    """创建项目结构"""
    template_source = get_template_path(template)
    
    # 复制模板文件
    shutil.copytree(template_source, directory, dirs_exist_ok=True)
    
    # 处理模板文件（替换占位符）
    process_template_files(directory, project_name)
    
    # 创建标准文件
    create_standard_files(directory, project_name)

def process_template_files(directory, project_name):
    """替换模板文件中的占位符"""
    for file_path in directory.rglob("*"):
        if file_path.is_file() and file_path.suffix in ('.py', '.md', '.txt', '.html'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 替换占位符
                content = content.replace("{{project_name}}", project_name)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            except (UnicodeDecodeError, IOError) as e:
                click.echo(f"Warning: Could not process {file_path}: {e}")

def create_standard_files(directory, project_name):
    """创建额外的标准项目文件"""
    
    # 创建 .gitignore
    gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environment
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
"""
    gitignore_path = directory / ".gitignore"
    with open(gitignore_path, "w") as f:
        f.write(gitignore_content)
    
    # 创建 setup.py（如果不存在）
    setup_py_path = directory / "setup.py"
    if not setup_py_path.exists():
        setup_py_content = f"""from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={{
        'console_scripts': [
            '{project_name}=app:main',
        ],
    }},
)
"""
        with open(setup_py_path, "w") as f:
            f.write(setup_py_content)

@click.command()
@click.option('-n', '--name', required=True, help='Project name')
@click.option('-t', '--template', default='basic', 
              type=click.Choice(['basic', 'web'], case_sensitive=False),
              help='Project template')
@click.option('-d', '--directory', default='.', 
              help='Directory to create project in')
@click.option('--force', is_flag=True, help='Overwrite existing directory')
def create(name, template, directory, force):
    """Create a new Python project"""
    
    project_dir = Path(directory) / name
    
    click.echo(f"{Fore.CYAN}🚀 Creating new Python project: {Fore.GREEN}{name}{Style.RESET_ALL}")
    click.echo(f"{Fore.CYAN}📋 Template: {Fore.YELLOW}{template}{Style.RESET_ALL}")
    click.echo(f"{Fore.CYAN}📁 Location: {Fore.YELLOW}{project_dir.absolute()}{Style.RESET_ALL}")
    
    # 检查目录是否已存在
    if project_dir.exists():
        if not force:
            if not click.confirm(f"📂 Directory {project_dir} already exists. Overwrite?"):
                click.echo(f"{Fore.YELLOW}Operation cancelled.{Style.RESET_ALL}")
                return
        else:
            click.echo(f"{Fore.YELLOW}⚠️  Overwriting existing directory...{Style.RESET_ALL}")
    
    try:
        # 创建项目结构
        create_project_structure(project_dir, template, name)
        
        click.echo(f"{Fore.GREEN}✅ Project '{name}' created successfully!{Style.RESET_ALL}")
        
        # 显示下一步指引
        click.echo(f"\n{Fore.CYAN}🎯 Next steps:{Style.RESET_ALL}")
        click.echo(f"  {Fore.WHITE}cd {name}{Style.RESET_ALL}")
        
        if template == "web":
            click.echo(f"  {Fore.WHITE}pip install -r requirements.txt{Style.RESET_ALL}")
            click.echo(f"  {Fore.WHITE}python app.py{Style.RESET_ALL}")
            click.echo(f"\n{Fore.CYAN}🌐 Then open: {Fore.WHITE}http://localhost:5000{Style.RESET_ALL}")
        else:
            click.echo(f"  {Fore.WHITE}python app.py{Style.RESET_ALL}")
            
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error creating project: {e}{Style.RESET_ALL}")
        raise click.Abort()