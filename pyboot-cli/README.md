# PyBoot CLI 创建命令使用文档

## 命令概述

`pyboot create` 命令是 PyBoot CLI 的核心功能之一，用于快速生成标准化的 PyBoot 项目结构和代码文件。

PyBoot CLI 提供以下优势：

- **快速启动**：几秒钟内创建完整的项目结构，无需手动配置
- **标准化**：遵循 PyBoot 最佳实践和项目结构约定
- **模板化**：多种项目模板可选，满足不同应用场景

## 安装方法

PyBoot CLI 可以通过 pip 直接安装：

```bash
pip install pyboot-cli
```

或者从源码安装：

```bash
git clone https://github.com/pyboot/pyboot-cli.git
cd pyboot-cli
pip install -e .
```

## 使用指南

### 创建应用

使用 `pyboot create app` 命令创建新的 PyBoot 应用项目。

**命令语法：**
```bash
pyboot create app NAME [OPTIONS]
```

**选项说明：**

| 选项 | 缩写 | 说明 |
|------|------|------|
| `--directory` | `-d` | 项目输出目录，默认为当前目录 |
| `--template` | `-t` | 项目模板类型：default, web, api, microservice |
| `--package` |  | 基础包名，默认为项目名称 |
| `--description` |  | 项目描述 |
| `--force` | `-f` | 覆盖已存在的目录 |
| `--no-input` |  | 非交互模式，使用默认值 |

**使用示例：**

1. **创建基础应用**
```bash
pyboot create app myapp
```

2. **使用特定模板和包名**
```bash
pyboot create app myapi -t api --package com.example.myapi
```

3. **在指定目录创建项目**
```bash
pyboot create app myproject -d /path/to/projects --description "我的PyBoot项目"
```

### 创建模块

使用 `pyboot create module` 命令在现有项目中创建新模块。

**命令语法：**
```bash
pyboot create module NAME [OPTIONS]
```

**选项说明：**

| 选项 | 说明 |
|------|------|
| `--package` | 模块包名 |

**使用示例：**
```bash
pyboot create module auth --package com.example.auth
```

### 创建组件

使用 `pyboot create component` 命令创建特定类型的组件。

**命令语法：**
```bash
pyboot create component NAME [OPTIONS]
```

**选项说明：**

| 选项 | 缩写 | 说明 |
|------|------|------|
| `--type` |  | 组件类型：service, util, config |

**使用示例：**
```bash
pyboot create component email --type service
```

## 项目模板

PyBoot CLI 提供多种项目模板，满足不同应用场景的需求。

### 默认模板
标准 PyBoot 项目结构，包含基本配置和示例代码。
```bash
pyboot create app myapp -t default
```

### Web 模板
包含前端资源、模板引擎和静态文件服务的完整 Web 应用。
```bash
pyboot create app myweb -t web
```

### API 模板
专注于 RESTful API 开发，包含 OpenAPI 文档和认证中间件。
```bash
pyboot create app myapi -t api
```

### 微服务模板
适用于微服务架构，包含服务发现、配置中心和健康检查。
```bash
pyboot create app myservice -t microservice
```

## 项目结构

PyBoot 创建的标准项目结构遵循最佳实践，确保代码组织和维护性。

```
myproject/
├── src/
│   └── myproject/
│       ├── config/
│       │   ├── __init__.py
│       │   ├── app_config.py
│       │   └── database_config.py
│       ├── controllers/
│       │   ├── __init__.py
│       │   ├── hello_controller.py
│       │   └── health_controller.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── hello_service.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── user.py
│       ├── repositories/
│       │   └── __init__.py
│       ├── aspects/
│       │   └── __init__.py
│       ├── utils/
│       │   ├── __init__.py
│       │   └── response_util.py
│       └── __init__.py
├── tests/
│   ├── test_main.py
│   └── conftest.py
├── static/
├── templates/
├── docs/
├── logs/
├── app.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
└── application.yaml
```

### 关键文件说明

| 文件/目录 | 说明 |
|-----------|------|
| `app.py` | 应用入口文件，包含应用启动逻辑 |
| `pyproject.toml` | 项目配置和依赖管理文件 |
| `application.yaml` | 应用配置文件，包含数据库、服务器等配置 |
| `src/` | 源代码目录，遵循包结构组织 |
| `src/[package]/controllers/` | 控制器层，处理 HTTP 请求和响应 |
| `src/[package]/services/` | 服务层，包含业务逻辑 |
| `src/[package]/models/` | 数据模型定义 |
| `src/[package]/config/` | 配置类定义 |
| `tests/` | 测试代码目录 |
| `static/` | 静态资源文件目录 |
| `templates/` | 模板文件目录 |

## 完整示例

以下是一个完整的 PyBoot 项目创建和使用示例。

### 1. 创建项目
```bash
pyboot create app demo-api -t api --package com.example.demo --description "示例API项目"
```

### 2. 进入项目目录
```bash
cd demo-api
```

### 3. 安装依赖
```bash
pip install -e .
```

### 4. 生成新组件
```bash
pyboot generate controller UserController
pyboot generate service UserService --methods create,read,update,delete
```

### 5. 运行应用
```bash
pyboot run --reload
```

### 6. 访问应用
打开浏览器访问以下地址：
- 应用首页: http://localhost:8080
- API 文档: http://localhost:8080/docs

## 总结

PyBoot CLI 的 `create` 命令为开发者提供了快速创建标准化项目的能力，大大减少了项目初始化时间，确保了代码结构的一致性。通过多种模板选项和灵活的配置参数，可以满足不同场景下的开发需求。

通过遵循本文档的指南，您可以快速开始使用 PyBoot 框架进行项目开发，享受现代化 Python Web 开发带来的便利和高效。

---

*文档版本：1.0.0*  
*最后更新：2024年*  
*PyBoot Team © 2024 保留所有权利*