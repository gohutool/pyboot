# PyBoot 框架全面介绍指南

## 第一章：PyBoot 框架概述

### 1.1 框架简介

PyBoot 是一个基于 Python 的现代化全栈 Web 开发框架，其设计理念深受 Java 生态中 Spring Boot 框架的启发。PyBoot 旨在为 Python 开发者提供一个开箱即用、功能完备的企业级应用开发解决方案。通过合理的架构设计和丰富的功能集成，PyBoot 显著降低了构建复杂 Python Web 应用的难度，同时保证了应用的高性能和高可维护性。

PyBoot 框架的核心设计哲学是"约定优于配置"和"开箱即用"。开发者无需花费大量时间进行繁琐的配置，框架已经为大多数常见场景提供了合理的默认配置。同时，PyBoot 保持了高度的灵活性，允许开发者在需要时进行自定义配置，以满足特定的业务需求。

### 1.2 设计理念与架构思想

PyBoot 框架的架构设计遵循了现代软件工程的多个重要原则：

**模块化设计**：PyBoot 采用高度模块化的架构，每个功能模块都相对独立，可以按需引入。这种设计不仅降低了框架的复杂性，还使得开发者能够根据项目需求灵活选择所需功能。

**依赖注入与控制反转**：框架内置了强大的依赖注入容器，实现了控制反转（IoC）的设计模式。这种机制使得组件之间的耦合度大大降低，提高了代码的可测试性和可维护性。

**面向切面编程**：PyBoot 全面支持 AOP（面向切面编程），允许开发者将横切关注点（如日志追踪记录、事务管理、安全控制等）与业务逻辑分离，实现了更好的代码组织和复用。

**配置外部化**：框架支持将配置信息从代码中分离出来，通过外部的 YAML 文件进行管理。同时支持多环境配置，使得应用在不同部署环境下的配置管理变得简单而高效。

### 1.3 核心特性总览

PyBoot 框架提供了一系列强大的核心特性，包括但不限于：

- 内嵌 FastAPI 作为 Web 容器，提供高性能的 Web 服务能力
- 完整的服务容器体系，支持依赖注入和组件生命周期管理
- 强大的定时任务调度系统
- 优化的多线程池管理
- 类似 MyBatis-Plus 的便捷数据库操作
- 完整的消息队列集成（Kafka）
- Redis 缓存和数据存储支持
- 多数据源动态路由
- 基于注解的配置系统
- YAML 配置文件和多环境配置支持
- 可扩展的自定义组件机制
- 灵活的过滤器系统
- 声明式的控制器编程模型
- 完善的数据库事务管理

### 1.4 适用场景

PyBoot 框架适用于各种规模的 Python Web 应用开发，特别适合以下场景：

- 企业级后台管理系统
- 微服务架构中的单个服务
- 高并发的 API 服务
- 需要复杂业务逻辑的数据处理应用
- 需要集成多种数据源和中间件的应用
- 需要良好可维护性和可测试性的长期项目

## 第二章：快速开始

### 2.1 环境要求与安装

在开始使用 PyBoot 之前，需要确保系统满足以下环境要求：

- Python 3.8 或更高版本
- pip 包管理工具
- 可选：虚拟环境工具（如 venv 或 conda）

安装 PyBoot 框架非常简单，可以通过 pip 命令直接安装：

```bash
pip install pyboot-framework
```

或者从源代码安装：

```bash
git clone https://github.com/pyboot/framework.git
cd framework
pip install -e .
```

### 2.2 创建第一个 PyBoot 应用

让我们创建一个简单的 "Hello World" 应用来演示 PyBoot 的基本用法：

**项目结构**：
```
myapp/
├── app.py
├── application.yaml
└── requirements.txt
```

**application.yaml**：
```yaml
app:
  name: my-first-pyboot-app
  version: 1.0.0

server:
  port: 8080
  host: "0.0.0.0"
```

**app.py**：
```python
from pyboot import PyBootApplication
from pyboot.web import controller, GetMapping

@controller
class HelloController:
    
    @GetMapping("/hello")
    def hello(self):
        return {"message": "Hello, PyBoot!"}

if __name__ == "__main__":
    app = PyBootApplication()
    app.run()
```

运行应用：
```bash
python app.py
```

访问 http://localhost:8080/hello 即可看到返回的 JSON 消息。

### 2.3 基本项目结构说明

一个标准的 PyBoot 项目通常具有以下目录结构：

```
project/
├── src/                    # 源代码目录
│   ├── main/              # 主要代码
│   │   ├── python/        # Python 代码
│   │   │   ├── controllers/    # 控制器层
│   │   │   ├── services/       # 服务层
│   │   │   ├── repositories/   # 数据访问层
│   │   │   ├── models/         # 数据模型
│   │   │   ├── config/         # 配置类
│   │   │   └── aspects/        # 切面类
│   │   └── resources/     # 资源文件
│   │       ├── application.yaml    # 主配置文件
│   │       ├── application-dev.yaml # 开发环境配置
│   │       └── application-prod.yaml # 生产环境配置
│   └── test/              # 测试代码
├── static/                # 静态资源
├── templates/             # 模板文件
├── requirements.txt       # 依赖列表
└── README.md             # 项目说明
```

### 2.4 配置文件基础

PyBoot 使用 YAML 格式的配置文件，默认加载 `application.yaml` 文件。基本的配置项包括：

```yaml
app:
  name: "我的应用"
  version: "1.0.0"
  
server:
  port: 8080
  host: "0.0.0.0"
  static:
    path: "/static"
    directory: "./static"
  
logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  
database:
  default:
    url: "postgresql://user:pass@localhost:5432/mydb"
    echo: false
```

## 第三章：Web 容器与 FastAPI 集成

### 3.1 内嵌 FastAPI 的优势

PyBoot 选择内嵌 FastAPI 作为其 Web 容器，主要基于以下考虑：

**高性能**：FastAPI 是基于 Starlette 和 Pydantic 的现代 Web 框架，具有极高的性能，能够与 NodeJS 和 Go 相媲美。

**异步支持**：原生支持异步请求处理，能够更好地处理高并发场景。

**自动 API 文档**：自动生成交互式 API 文档（Swagger UI 和 ReDoc），极大提高了 API 的开发效率和可用性。

**类型提示**：充分利用 Python 的类型提示系统，提供更好的代码补全和错误检查。

**易于学习**：简洁的 API 设计使得开发者能够快速上手。

### 3.2 控制器(Controller)详解

在 PyBoot 中，控制器负责处理 HTTP 请求并返回响应。通过装饰器模式，可以轻松定义路由和请求处理方法。

**基本控制器示例**：

```python
from pyboot.web import controller, GetMapping, PostMapping, RequestBody, PathVariable

@controller
class UserController:
    
    @GetMapping("/users")
    def get_all_users(self):
        # 获取所有用户
        return user_service.get_all_users()
    
    @GetMapping("/users/{user_id}")
    def get_user_by_id(self, user_id: int):
        # 根据ID获取用户
        user = user_service.get_user_by_id(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user
    
    @PostMapping("/users")
    def create_user(self, user_data: RequestBody):
        # 创建新用户
        new_user = user_service.create_user(user_data)
        return new_user, 201
    
    @GetMapping("/users/{user_id}/orders")
    def get_user_orders(self, user_id: int, page: int = 1, size: int = 10):
        # 获取用户的订单，支持分页参数
        orders = order_service.get_orders_by_user(user_id, page, size)
        return {
            "page": page,
            "size": size,
            "total": len(orders),
            "data": orders
        }
```

### 3.3 请求映射与参数处理

PyBoot 支持多种类型的请求参数绑定：

**路径参数**：
```python
@GetMapping("/users/{user_id}/orders/{order_id}")
def get_order(self, user_id: int, order_id: int):
    # 使用路径参数
    return order_service.get_order(user_id, order_id)
```

**查询参数**：
```python
@GetMapping("/users")
def search_users(self, name: str = None, age: int = None, page: int = 1):
    # 使用查询参数，带有默认值
    return user_service.search_users(name, age, page)
```

**请求体参数**：
```python
from pyboot.web import RequestBody
from pydantic import BaseModel

class UserCreateRequest(BaseModel):
    name: str
    email: str
    age: int

@PostMapping("/users")
def create_user(self, user_data: RequestBody[UserCreateRequest]):
    # 使用请求体参数，支持Pydantic模型验证
    return user_service.create_user(user_data)
```

**请求头参数**：
```python
from pyboot.web import RequestHeader

@GetMapping("/profile")
def get_profile(self, authorization: str = RequestHeader()):
    # 获取请求头
    token = authorization.replace("Bearer ", "")
    return auth_service.get_profile(token)
```

### 3.4 静态文件服务配置

PyBoot 支持静态文件服务，可以轻松托管前端资源：

**配置静态文件**：
```yaml
server:
  static:
    - path: "/static"
      directory: "./static"
    - path: "/uploads"
      directory: "./uploads"
      show_index: true
```

**自定义静态文件处理器**：
```python
from pyboot.web import StaticFileConfig

@Configuration
class WebConfig:
    
    @Bean
    def static_file_config(self) -> StaticFileConfig:
        config = StaticFileConfig()
        config.add_mapping("/web", "./web-resources")
        config.add_mapping("/docs", "./documentation", show_index=True)
        return config
```

### 3.5 代理服务与流式响应

PyBoot 提供了强大的代理服务支持，包括常规代理和流式响应代理：

**普通代理服务**：
```python
from pyboot.web import ProxyService

@Bean
def user_proxy_service(self) -> ProxyService:
    service = ProxyService()
    service.add_route("/api/users", "http://user-service:8080")
    service.add_route("/api/orders", "http://order-service:8080")
    return service
```

**流式响应代理**：
```python
from pyboot.web import StreamingProxyService

@Bean
def streaming_proxy_service(self) -> StreamingProxyService:
    service = StreamingProxyService()
    
    # 代理SSE（Server-Sent Events）端点
    service.add_sse_proxy("/events", "http://event-service:8080/events")
    
    # 代理WebSocket端点
    service.add_websocket_proxy("/ws", "http://websocket-service:8080/ws")
    
    return service
```

**自定义流式处理**：
```python
import asyncio
from pyboot.web import GetMapping, controller

@controller
class StreamController:
    
    @GetMapping("/stream-data")
    async def stream_data(self):
        """流式返回数据示例"""
        async def generate_data():
            for i in range(10):
                yield f"data: Message {i}\n\n"
                await asyncio.sleep(1)
        
        return StreamingResponse(
            generate_data(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
            }
        )
```

## 第四章：服务容器与依赖注入

### 4.1 服务容器核心概念

PyBoot 的服务容器是其核心功能之一，它负责管理应用中所有组件的生命周期和依赖关系。服务容器基于依赖注入模式，实现了控制反转（IoC）原则。

**容器的基本功能**：
- 组件的注册与发现
- 依赖关系的自动解析
- 组件生命周期的管理
- 作用域管理（单例、请求作用域等）

### 4.2 组件注册与生命周期

在 PyBoot 中，有多种方式可以注册组件：

**类装饰器方式**：
```python
from pyboot.core import Component, Service, Repository

@Component
class EmailValidator:
    def validate(self, email: str) -> bool:
        return "@" in email

@Service
class UserService:
    def __init__(self, email_validator: EmailValidator):
        self.email_validator = email_validator
    
    def create_user(self, user_data):
        if not self.email_validator.validate(user_data.email):
            raise ValueError("Invalid email address")
        # 创建用户逻辑
        return new_user

@Repository
class UserRepository:
    def save(self, user):
        # 保存用户到数据库
        return saved_user
```

**配置类方式**：
```python
from pyboot.core import Configuration, Bean

@Configuration
class AppConfig:
    
    @Bean
    def data_source(self) -> DataSource:
        return PostgreSQLDataSource()
    
    @Bean
    def user_service(self, data_source: DataSource) -> UserService:
        return UserService(data_source)
```

**组件生命周期**：
```python
from pyboot.core import Component, PostConstruct, PreDestroy

@Component
class CacheManager:
    
    def __init__(self):
        self.cache = {}
    
    @PostConstruct
    def initialize(self):
        """在组件初始化后调用"""
        print("CacheManager initialized")
        # 加载初始缓存数据
        self.load_initial_data()
    
    @PreDestroy
    def cleanup(self):
        """在组件销毁前调用"""
        print("CacheManager cleaning up")
        self.cache.clear()
    
    def load_initial_data(self):
        # 加载初始数据逻辑
        pass
```

### 4.3 依赖注入的多种方式

PyBoot 支持多种依赖注入方式：

**构造函数注入**：
```python
@Service
class OrderService:
    def __init__(self, user_service: UserService, product_service: ProductService):
        self.user_service = user_service
        self.product_service = product_service
```

**属性注入**：
```python
from pyboot.core import Autowired

@Service
class PaymentService:
    
    @Autowired
    private user_service: UserService
    
    @Autowired
    private order_service: OrderService
    
    def process_payment(self, order_id: int):
        order = self.order_service.get_order(order_id)
        user = self.user_service.get_user(order.user_id)
        # 处理支付逻辑
```

**方法注入**：
```python
@Service
class ReportService:
    
    private database_connection: DatabaseConnection
    
    @Autowired
    def set_database_connection(self, connection: DatabaseConnection):
        self.database_connection = connection
```

### 4.4 条件化组件注册

PyBoot 支持基于条件的组件注册，类似于 Spring Boot 的 `@Conditional` 注解：

```python
from pyboot.core import Configuration, Bean, ConditionalOnProperty, ConditionalOnClass

@Configuration
class ConditionalConfig:
    
    @Bean
    @ConditionalOnProperty(name="cache.enabled", having_value="true")
    def cache_manager(self) -> CacheManager:
        return RedisCacheManager()
    
    @Bean
    @ConditionalOnProperty(name="cache.enabled", having_value="false", match_if_missing=True)
    def cache_manager(self) -> CacheManager:
        return SimpleCacheManager()
    
    @Bean
    @ConditionalOnClass("redis.Redis")
    def redis_template(self) -> RedisTemplate:
        return RedisTemplate()
```

### 4.5 配置属性绑定

PyBoot 支持将配置文件中的属性绑定到组件：

```python
from pyboot.core import Component, ConfigurationProperties

@ConfigurationProperties(prefix="app.database")
class DatabaseProperties:
    url: str
    username: str
    password: str
    pool_size: int = 10
    timeout: int = 30

@Component
class DatabaseConfig:
    
    def __init__(self, properties: DatabaseProperties):
        self.properties = properties
    
    @Bean
    def data_source(self) -> DataSource:
        return create_data_source(
            url=self.properties.url,
            username=self.properties.username,
            password=self.properties.password,
            pool_size=self.properties.pool_size,
            timeout=self.properties.timeout
        )
```

对应的配置文件：
```yaml
app:
  database:
    url: "postgresql://localhost:5432/mydb"
    username: "admin"
    password: "secret"
    pool_size: 20
    timeout: 60
```

## 第五章：面向切面编程(AOP)

### 5.1 AOP 基本概念

面向切面编程（AOP）是一种编程范式，旨在将横切关注点（如日志、事务、安全等）与业务逻辑分离。PyBoot 提供了完整的 AOP 支持，让开发者能够以声明式的方式处理这些横切关注点。

**AOP 核心概念**：
- 切面（Aspect）：横切关注点的模块化
- 连接点（Join Point）：程序执行过程中的特定点
- 通知（Advice）：在连接点执行的动作
- 切点（Pointcut）：匹配连接点的谓词
- 引入（Introduction）：为现有类添加新的方法或属性
- 目标对象（Target Object）：被一个或多个切面通知的对象

### 5.2 切面定义与配置

在 PyBoot 中定义切面：

```python
from pyboot.aop import Aspect, Pointcut, Before, After, Around, AfterReturning, AfterThrowing

@Aspect
@Component
class LoggingAspect:
    
    @Pointcut("execution(* com.example.service.*.*(..))")
    def service_methods(self):
        """匹配service包下所有类的所有方法"""
        pass
    
    @Before("service_methods()")
    def log_before(self, joinpoint):
        method_name = joinpoint.method.__name__
        class_name = joinpoint.target.__class__.__name__
        print(f"Before executing {class_name}.{method_name}")
    
    @AfterReturning(pointcut="service_methods()", returning="result")
    def log_after_returning(self, joinpoint, result):
        method_name = joinpoint.method.__name__
        print(f"Method {method_name} returned: {result}")
    
    @AfterThrowing(pointcut="service_methods()", throwing="exception")
    def log_after_throwing(self, joinpoint, exception):
        method_name = joinpoint.method.__name__
        print(f"Method {method_name} threw exception: {exception}")
    
    @Around("service_methods()")
    def measure_performance(self, proceeding_joinpoint):
        import time
        start_time = time.time()
        
        try:
            result = proceeding_joinpoint.proceed()
            return result
        finally:
            execution_time = time.time() - start_time
            method_name = proceeding_joinpoint.method.__name__
            print(f"Method {method_name} executed in {execution_time:.3f}s")
```

### 5.3 五种通知类型详解

PyBoot 支持五种标准的通知类型：

**@Before** - 前置通知：
```python
@Before("execution(* UserService.*(..))")
def validate_arguments(self, joinpoint):
    # 在目标方法执行前进行参数验证
    args = joinpoint.args
    for arg in args:
        if arg is None:
            raise ValueError("Arguments cannot be None")
```

**@AfterReturning** - 返回后通知：
```python
@AfterReturning(
    pointcut="execution(* UserService.get_user(..))",
    returning="user"
)
def audit_user_access(self, joinpoint, user):
    # 在成功获取用户信息后记录审计日志
    if user:
        user_id = user.id
        accessed_by = get_current_user()
        audit_service.log_access(user_id, accessed_by)
```

**@AfterThrowing** - 异常通知：
```python
@AfterThrowing(
    pointcut="execution(* OrderService.*(..))",
    throwing="ex"
)
def handle_order_errors(self, joinpoint, ex):
    # 处理订单服务中的异常
    error_msg = f"Error in {joinpoint.method.__name__}: {str(ex)}"
    error_service.report_error(error_msg, severity="HIGH")
```

**@After** - 后置通知：
```python
@After("execution(* DatabaseService.*(..))")
def cleanup_resources(self, joinpoint):
    # 无论方法执行成功与否，都进行资源清理
    database_connection.cleanup_temp_resources()
```

**@Around** - 环绕通知：
```python
@Around("execution(* ExternalService.call_api(..))")
def retry_on_failure(self, proceeding_joinpoint):
    # 在调用外部API时实现重试机制
    max_attempts = 3
    last_exception = None
    
    for attempt in range(max_attempts):
        try:
            result = proceeding_joinpoint.proceed()
            return result
        except TemporaryError as ex:
            last_exception = ex
            if attempt < max_attempts - 1:
                time.sleep(2 ** attempt)  # 指数退避
            continue
    
    # 所有重试都失败了
    raise ServiceUnavailableError("Service unavailable after retries") from last_exception
```

### 5.4 切点表达式语法

PyBoot 使用强大的切点表达式来匹配连接点：

**执行表达式**：
```python
# 匹配特定方法
@Pointcut("execution(public String com.example.UserService.getUserName(int))")

# 匹配包下所有方法
@Pointcut("execution(* com.example.service.*.*(..))")

# 匹配特定类所有方法
@Pointcut("execution(* com.example.UserService.*(..))")

# 匹配所有public方法
@Pointcut("execution(public * *(..))")

# 匹配所有以get开头的方法
@Pointcut("execution(* *.get*(..))")
```

**Within 表达式**：
```python
# 匹配包内所有方法
@Pointcut("within(com.example.service..*)")

# 匹配特定类
@Pointcut("within(com.example.UserService)")

# 匹配注解标注的类
@Pointcut("@within(com.example.Transactional)")
```

**注解表达式**：
```python
# 匹配带有特定注解的方法
@Pointcut("@annotation(com.example.Cacheable)")

# 匹配带有特定注解的参数
@Pointcut("@args(com.example.Validated)")

# 匹配带有特定注解的类的方法
@Pointcut("@within(com.example.Secured)")
```

### 5.5 实际应用场景

**事务管理切面**：
```python
@Aspect
@Component
class TransactionAspect:
    
    @Autowired
    def set_transaction_manager(self, tx_manager: TransactionManager):
        self.tx_manager = tx_manager
    
    @Around("@annotation(transactional)")
    def manage_transaction(self, proceeding_joinpoint, transactional):
        tx = self.tx_manager.begin_transaction(
            isolation=transactional.isolation,
            read_only=transactional.read_only
        )
        
        try:
            result = proceeding_joinpoint.proceed()
            self.tx_manager.commit_transaction(tx)
            return result
        except Exception as ex:
            self.tx_manager.rollback_transaction(tx)
            raise ex
```

**缓存切面**：
```python
@Aspect
@Component
class CacheAspect:
    
    @Autowired
    def set_cache_manager(self, cache_manager: CacheManager):
        self.cache_manager = cache_manager
    
    @Around("@annotation(cacheable)")
    def cache_result(self, proceeding_joinpoint, cacheable):
        # 生成缓存键
        cache_key = self.generate_cache_key(
            proceeding_joinpoint.method,
            proceeding_joinpoint.args
        )
        
        # 尝试从缓存获取
        cached_result = self.cache_manager.get(cache_key)
        if cached_result is not None:
            return cached_result
        
        # 执行方法并缓存结果
        result = proceeding_joinpoint.proceed()
        self.cache_manager.set(
            cache_key, 
            result, 
            ttl=cacheable.ttl
        )
        
        return result
    
    @AfterReturning("@annotation(cache_evict)")
    def evict_cache(self, joinpoint, cache_evict):
        # 根据配置清除缓存
        if cache_evict.all_entries:
            self.cache_manager.clear()
        else:
            cache_key = self.generate_cache_key(
                joinpoint.method,
                joinpoint.args
            )
            self.cache_manager.delete(cache_key)
```

## 第六章：定时任务调度

### 6.1 定时任务基础

PyBoot 提供了强大的定时任务调度功能，支持多种类型的任务调度需求。定时任务系统基于 cron 表达式和简单间隔，可以轻松配置周期性执行的任务。

**启用定时任务**：
```python
from pyboot.scheduling import EnableScheduling

@EnableScheduling
@PyBootApplication
class MyApplication:
    def main(self):
        app = PyBootApplication(MyApplication)
        app.run()
```

### 6.2 多种调度方式

**固定速率调度**：
```python
from pyboot.scheduling import Scheduled, Component

@Component
class FixedRateTasks:
    
    @Scheduled(fixed_rate=5000)  # 每5秒执行一次
    def report_metrics(self):
        """每5秒报告一次系统指标"""
        metrics = system_metrics_collector.collect()
        metrics_reporter.report(metrics)
    
    @Scheduled(fixed_rate=60000, initial_delay=10000)  # 启动后10秒开始，每60秒执行
    def cleanup_temp_files(self):
        """每分钟清理一次临时文件"""
        temp_file_cleaner.cleanup()
```

**固定延迟调度**：
```python
@Component
class FixedDelayTasks:
    
    @Scheduled(fixed_delay=30000)  # 上次执行完成后30秒再执行
    def process_batch_data(self):
        """批处理数据，确保每次执行间隔至少30秒"""
        batch_processor.process_next_batch()
```

**Cron 表达式调度**：
```python
@Component
class CronTasks:
    
    @Scheduled(cron="0 0 * * * *")  # 每小时执行一次
    def hourly_backup(self):
        """每小时执行一次数据备份"""
        backup_service.create_hourly_backup()
    
    @Scheduled(cron="0 0 2 * * *")  # 每天凌晨2点执行
    def daily_report(self):
        """每天生成日报"""
        report_generator.generate_daily_report()
    
    @Scheduled(cron="0 0 0 * * MON")  # 每周一凌晨执行
    def weekly_cleanup(self):
        """每周执行一次大清理"""
        system_cleaner.perform_weekly_cleanup()
```

### 6.3 动态定时任务

PyBoot 支持动态创建和管理定时任务：

```python
from pyboot.scheduling import TaskScheduler, Trigger, TaskRegistrar

@Component
class DynamicTaskManager:
    
    def __init__(self, task_scheduler: TaskScheduler):
        self.task_scheduler = task_scheduler
        self.scheduled_tasks = {}
    
    def schedule_task(self, task_id: str, cron_expression: str, task_function):
        """动态调度任务"""
        trigger = Trigger.cron(cron_expression)
        task = self.task_scheduler.schedule_task(task_function, trigger)
        self.scheduled_tasks[task_id] = task
    
    def reschedule_task(self, task_id: str, new_cron_expression: str):
        """重新调度任务"""
        if task_id in self.scheduled_tasks:
            self.cancel_task(task_id)
            # 重新创建任务
            task_function = self.scheduled_tasks[task_id].function
            self.schedule_task(task_id, new_cron_expression, task_function)
    
    def cancel_task(self, task_id: str):
        """取消任务"""
        if task_id in self.scheduled_tasks:
            self.task_scheduler.cancel_scheduled_task(self.scheduled_tasks[task_id])
            del self.scheduled_tasks[task_id]
```

### 6.4 任务执行配置

**配置任务执行器**：
```python
from pyboot.scheduling import SchedulingConfig, TaskExecutor

@Configuration
class SchedulingConfiguration:
    
    @Bean
    def task_executor(self) -> TaskExecutor:
        from concurrent.futures import ThreadPoolExecutor
        return ThreadPoolExecutor(
            max_workers=10,
            thread_name_prefix="scheduled-task-"
        )
```

**任务异常处理**：
```python
@Component
class ScheduledTaskErrorHandler:
    
    @EventListener
    def handle_task_exception(self, event: TaskExecutionExceptionEvent):
        exception = event.exception
        task_method = event.task_method
        logger.error(f"Task {task_method} failed with exception: {exception}")
        
        # 发送告警
        alert_service.send_alert(
            f"Scheduled task failed: {task_method}",
            severity="ERROR"
        )
```

## 第七章：多线程池管理

### 7.1 线程池配置与管理

PyBoot 提供了强大的线程池管理功能，可以轻松配置和管理多种用途的线程池。

**线程池配置类**：
```python
from pyboot.executor import ThreadPoolConfig, EnableThreadPools

@Configuration
@EnableThreadPools
class ExecutorConfig:
    
    @Bean
    def io_thread_pool(self) -> ThreadPoolConfig:
        """I/O密集型任务线程池"""
        return ThreadPoolConfig(
            name="io-executor",
            core_pool_size=20,
            max_pool_size=100,
            queue_capacity=1000,
            keep_alive_seconds=60,
            thread_name_prefix="io-worker-"
        )
    
    @Bean
    def cpu_thread_pool(self) -> ThreadPoolConfig:
        """CPU密集型任务线程池"""
        return ThreadPoolConfig(
            name="cpu-executor",
            core_pool_size=4,  # 通常设置为CPU核心数
            max_pool_size=8,
            queue_capacity=100,
            keep_alive_seconds=30,
            thread_name_prefix="cpu-worker-"
        )
    
    @Bean
    def scheduled_thread_pool(self) -> ThreadPoolConfig:
        """定时任务线程池"""
        return ThreadPoolConfig(
            name="scheduled-executor",
            core_pool_size=5,
            max_pool_size=20,
            queue_capacity=500,
            thread_name_prefix="scheduled-"
        )
```

### 7.2 线程池使用示例

**注入和使用线程池**：
```python
from pyboot.executor import ThreadPoolExecutor, Async

@Service
class DataProcessingService:
    
    def __init__(self, io_executor: ThreadPoolExecutor):
        self.io_executor = io_executor
    
    def process_large_dataset(self, dataset: List[Data]) -> List[ProcessedData]:
        """使用线程池并行处理大数据集"""
        futures = []
        
        # 分批提交任务
        batch_size = 100
        for i in range(0, len(dataset), batch_size):
            batch = dataset[i:i + batch_size]
            future = self.io_executor.submit(self.process_batch, batch)
            futures.append(future)
        
        # 收集结果
        results = []
        for future in futures:
            try:
                batch_result = future.result(timeout=300)  # 5分钟超时
                results.extend(batch_result)
            except TimeoutError:
                logger.error("Batch processing timeout")
        
        return results
    
    def process_batch(self, batch: List[Data]) -> List[ProcessedData]:
        """处理单个数据批次"""
        return [self.process_single_item(item) for item in batch]
```

**异步方法执行**：
```python
@Service
class AsyncService:
    
    @Async("io_executor")  # 指定使用I/O线程池
    def async_process_data(self, data: Data) -> ProcessedData:
        """异步处理数据"""
        # 模拟耗时操作
        time.sleep(2)
        return self.process_data(data)
    
    @Async  # 使用默认线程池
    def async_send_notification(self, user: User, message: str):
        """异步发送通知"""
        notification_service.send(user, message)
    
    def process_multiple_async(self, items: List[Data]) -> List[ProcessedData]:
        """并行处理多个异步任务"""
        futures = [self.async_process_data(item) for item in items]
        
        # 等待所有任务完成
        results = []
        for future in futures:
            try:
                result = future.get(timeout=30)
                results.append(result)
            except Exception as e:
                logger.error(f"Async task failed: {e}")
        
        return results
```

### 7.3 线程池监控与管理

**线程池监控**：
```python
@Component
class ThreadPoolMonitor:
    
    def __init__(self, thread_pool_manager: ThreadPoolManager):
        self.thread_pool_manager = thread_pool_manager
    
    @Scheduled(fixed_rate=30000)  # 每30秒监控一次
    def monitor_thread_pools(self):
        """监控所有线程池状态"""
        pools = self.thread_pool_manager.get_all_pools()
        
        for pool_name, pool in pools.items():
            stats = pool.get_statistics()
            
            # 记录监控指标
            self.record_metrics(pool_name, stats)
            
            # 检查异常情况
            if stats.active_count > stats.max_pool_size * 0.8:
                self.alert_high_usage(pool_name, stats)
            
            if stats.queue_size > stats.queue_capacity * 0.9:
                self.alert_queue_full(pool_name, stats)
    
    def record_metrics(self, pool_name: str, stats: ThreadPoolStats):
        metrics.record_gauge(f"thread_pool.{pool_name}.active_count", stats.active_count)
        metrics.record_gauge(f"thread_pool.{pool_name}.queue_size", stats.queue_size)
        metrics.record_gauge(f"thread_pool.{pool_name}.completed_count", stats.completed_count)
```

**动态线程池调整**：
```python
@Service
class DynamicThreadPoolManager:
    
    def __init__(self, thread_pool_manager: ThreadPoolManager):
        self.thread_pool_manager = thread_pool_manager
    
    def adjust_thread_pool_size(self, pool_name: str, new_core_size: int, new_max_size: int):
        """动态调整线程池大小"""
        pool = self.thread_pool_manager.get_thread_pool(pool_name)
        if pool:
            pool.set_core_pool_size(new_core_size)
            pool.set_maximum_pool_size(new_max_size)
            logger.info(f"Adjusted {pool_name} to core={new_core_size}, max={new_max_size}")
    
    @EventListener
    def handle_high_load_event(self, event: SystemHighLoadEvent):
        """根据系统负载事件自动调整线程池"""
        if event.metric == "cpu_usage" and event.value > 0.8:
            # CPU使用率高，减少CPU密集型线程池
            self.adjust_thread_pool_size("cpu-executor", 2, 4)
        elif event.metric == "io_wait" and event.value > 0.5:
            # I/O等待高，增加I/O线程池
            self.adjust_thread_pool_size("io-executor", 30, 150)
```

## 第八章：数据库操作与 MyBatis-Plus 风格功能

### 8.1 数据访问层配置

PyBoot 提供了类似 MyBatis-Plus 的便捷数据库操作功能，支持多种数据库和灵活的查询方式。

**数据库配置**：
```yaml
database:
  default:
    url: "postgresql://user:pass@localhost:5432/mydb"
    driver: "postgresql"
    host: "localhost"
    port: 5432
    database: "mydb"
    username: "user"
    password: "pass"
    pool:
      max_connections: 20
      min_connections: 5
      max_lifetime: 3600
  read_replica:
    url: "postgresql://user:pass@replica:5432/mydb"
    read_only: true
```

**实体类定义**：
```python
from pyboot.data import Entity, Table, Column, Id, GeneratedValue

@Table(name = "users")
class User:
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    def id(self) -> int:
        return self._id
    
    @Column(name = "username", length = 50, unique = True, nullable = False)
    def username(self) -> str:
        return self._username
    
    @Column(name = "email", length = 100, unique = True, nullable = False)
    def email(self) -> str:
        return self._email
    
    @Column(name = "created_at")
    def created_at(self) -> datetime:
        return self._created_at
    
    @Column(name = "updated_at")
    def updated_at(self) -> datetime:
        return self._updated_at
```

### 8.2 通用 Mapper 功能

PyBoot 的通用 Mapper 提供了丰富的 CRUD 操作方法：

**基础 Repository**：
```python
from pyboot.data import Repository, BaseMapper

@Repository
class UserRepository(BaseMapper[User, int]):
    """用户数据访问接口"""
    
    def find_by_username(self, username: str) -> Optional[User]:
        return self.select_one(
            self.table.username == username
        )
    
    def find_by_email(self, email: str) -> Optional[User]:
        return self.select_one(
            self.table.email == email
        )
    
    def find_active_users(self) -> List[User]:
        return self.select_list(
            self.table.status == UserStatus.ACTIVE
        )
    
    def find_by_create_time_range(self, start: datetime, end: datetime) -> List[User]:
        return self.select_list(
            (self.table.created_at >= start) & 
            (self.table.created_at <= end)
        )
```

**复杂查询方法**：
```python
@Repository
class OrderRepository(BaseMapper[Order, int]):
    """订单数据访问接口"""
    
    def find_user_orders(self, user_id: int, page: int = 1, size: int = 10) -> Page[Order]:
        return self.select_page(
            page=page,
            size=size,
            where=self.table.user_id == user_id,
            order_by=[self.table.created_at.desc()]
        )
    
    def find_orders_with_details(self, order_ids: List[int]) -> List[Order]:
        # 使用连接查询获取订单详情
        return self.select_list(
            self.table.id.in_(order_ids)
        ).join(OrderItem).on(
            self.table.id == OrderItem.order_id
        ).fetch_all()
    
    def calculate_user_total_spent(self, user_id: int) -> float:
        result = self.select(
            func.sum(Order.total_amount)
        ).where(
            self.table.user_id == user_id,
            self.table.status == OrderStatus.COMPLETED
        ).scalar()
        
        return result or 0.0
```

### 8.3 查询构造器

PyBoot 提供了强大的查询构造器，支持复杂的查询条件：

**查询构造器示例**：
```python
@Service
class UserService:
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def search_users(self, criteria: UserSearchCriteria) -> Page[User]:
        """复杂用户搜索"""
        query = self.user_repository.query_builder()
        
        # 动态添加查询条件
        if criteria.username:
            query = query.where(self.user_repository.table.username.like(f"%{criteria.username}%"))
        
        if criteria.email:
            query = query.where(self.user_repository.table.email.like(f"%{criteria.email}%"))
        
        if criteria.min_age:
            query = query.where(self.user_repository.table.age >= criteria.min_age)
        
        if criteria.max_age:
            query = query.where(self.user_repository.table.age <= criteria.max_age)
        
        if criteria.roles:
            query = query.where(self.user_repository.table.role.in_(criteria.roles))
        
        # 排序和分页
        return query.order_by(
            self.user_repository.table.created_at.desc()
        ).page(
            page=criteria.page, 
            size=criteria.size
        )
    
    def get_user_statistics(self) -> UserStatistics:
        """用户统计信息"""
        total_users = self.user_repository.select_count()
        active_users = self.user_repository.select_count(
            self.user_repository.table.status == UserStatus.ACTIVE
        )
        new_today = self.user_repository.select_count(
            self.user_repository.table.created_at >= datetime.today().replace(hour=0, minute=0, second=0)
        )
        
        return UserStatistics(
            total_users=total_users,
            active_users=active_users,
            new_today=new_today
        )
```

### 8.4 乐观锁与逻辑删除

**乐观锁实现**：
```python
@Table(name = "products")
class Product:
    
    @Id
    @GeneratedValue
    def id(self) -> int:
        return self._id
    
    @Column(name = "name")
    def name(self) -> str:
        return self._name
    
    @Column(name = "stock")
    def stock(self) -> int:
        return self._stock
    
    @Version
    @Column(name = "version")
    def version(self) -> int:
        return self._version

@Repository
class ProductRepository(BaseMapper[Product, int]):
    
    def decrease_stock(self, product_id: int, quantity: int) -> bool:
        """减少库存，使用乐观锁防止超卖"""
        product = self.select_by_id(product_id)
        if not product or product.stock < quantity:
            return False
        
        product.stock -= quantity
        updated = self.update_by_id(product)
        
        # 如果版本冲突，重试
        if not updated:
            return self.decrease_stock(product_id, quantity)
        
        return True
```

**逻辑删除**：
```python
@Table(name = "articles")
class Article:
    
    @Id
    @GeneratedValue
    def id(self) -> int:
        return self._id
    
    @Column(name = "title")
    def title(self) -> str:
        return self._title
    
    @Column(name = "content")
    def content(self) -> str:
        return self._content
    
    @LogicDelete
    @Column(name = "deleted")
    def deleted(self) -> bool:
        return self._deleted

@Repository
class ArticleRepository(BaseMapper[Article, int]):
    
    def find_all_include_deleted(self) -> List[Article]:
        """查询包括已删除的文章"""
        return self.select_list(ignore_logic_delete=True)
```

## 第九章：消息队列与 Kafka 集成

### 9.1 Kafka 配置与连接

PyBoot 提供了完整的 Kafka 集成支持，包括生产者、消费者和流处理。

**Kafka 配置**：
```yaml
kafka:
  bootstrap-servers: "localhost:9092,localhost:9093"
  producer:
    acks: "all"
    retries: 3
    batch-size: 16384
    linger-ms: 1
    buffer-memory: 33554432
  consumer:
    group-id: "my-application"
    auto-offset-reset: "earliest"
    enable-auto-commit: false
    max-poll-records: 500
  topics:
    user-events: "user-events"
    order-events: "order-events"
    notification-events: "notification-events"
```

**Kafka 配置类**：
```python
from pyboot.kafka import KafkaConfig, EnableKafka

@Configuration
@EnableKafka
class KafkaConfiguration:
    
    @Bean
    def kafka_config(self) -> KafkaConfig:
        config = KafkaConfig()
        config.bootstrap_servers = ["localhost:9092", "localhost:9093"]
        config.producer_config = {
            "acks": "all",
            "retries": 3,
            "batch_size": 16384
        }
        config.consumer_config = {
            "group_id": "my-application",
            "auto_offset_reset": "earliest"
        }
        return config
```

### 9.2 消息生产者

**Kafka 生产者服务**：
```python
from pyboot.kafka import KafkaTemplate, KafkaProducer

@Service
class EventProducerService:
    
    def __init__(self, kafka_template: KafkaTemplate):
        self.kafka_template = kafka_template
    
    def send_user_created_event(self, user: User):
        """发送用户创建事件"""
        event = UserCreatedEvent(
            user_id=user.id,
            username=user.username,
            email=user.email,
            timestamp=datetime.now()
        )
        
        self.kafka_template.send(
            topic="user-events",
            key=str(user.id),
            value=event
        )
    
    def send_order_created_event(self, order: Order):
        """发送订单创建事件"""
        event = OrderCreatedEvent(
            order_id=order.id,
            user_id=order.user_id,
            total_amount=order.total_amount,
            items=[item.to_dict() for item in order.items],
            timestamp=datetime.now()
        )
        
        # 使用事务性发送
        self.kafka_template.execute_in_transaction(
            lambda: self.kafka_template.send(
                topic="order-events",
                key=str(order.id),
                value=event
            )
        )
    
    async def send_async_notification(self, notification: Notification):
        """异步发送通知事件"""
        await self.kafka_template.send_async(
            topic="notification-events",
            key=notification.user_id,
            value=notification
        )
```

### 9.3 消息消费者

**Kafka 消费者服务**：
```python
from pyboot.kafka import KafkaListener, ConsumerRecord

@Service
class EventConsumerService:
    
    @KafkaListener(topics = ["user-events"])
    def handle_user_events(self, record: ConsumerRecord):
        """处理用户事件"""
        try:
            event_data = json.loads(record.value)
            event_type = event_data.get("event_type")
            
            if event_type == "USER_CREATED":
                self.handle_user_created(event_data)
            elif event_type == "USER_UPDATED":
                self.handle_user_updated(event_data)
            elif event_type == "USER_DELETED":
                self.handle_user_deleted(event_data)
                
        except Exception as e:
            logger.error(f"Error processing user event: {e}")
            # 可以将失败的消息发送到死信队列
    
    @KafkaListener(
        topics = ["order-events"],
        group_id = "order-processor",
        concurrency = 3
    )
    def handle_order_events(self, record: ConsumerRecord):
        """处理订单事件，支持并发处理"""
        order_data = json.loads(record.value)
        self.order_processor.process_order(order_data)
    
    def handle_user_created(self, event_data: dict):
        """处理用户创建事件"""
        user_id = event_data["user_id"]
        username = event_data["username"]
        
        # 创建用户档案
        profile_service.create_default_profile(user_id, username)
        
        # 发送欢迎邮件
        email_service.send_welcome_email(event_data["email"])
        
        # 初始化用户积分
        points_service.initialize_user_points(user_id)
        
        logger.info(f"Processed user creation for {username}")

    @KafkaListener(
        topics = ["notification-events"],
        container_factory = "batch_factory"
    )
    def handle_notification_batch(self, records: List[ConsumerRecord]):
        """批量处理通知事件"""
        notifications = []
        
        for record in records:
            try:
                notification = json.loads(record.value)
                notifications.append(notification)
            except Exception as e:
                logger.error(f"Error parsing notification: {e}")
        
        if notifications:
            notification_service.process_batch(notifications)
```

### 9.4 消息监听器高级特性

**手动提交偏移量**：
```python
from pyboot.kafka import Acknowledgment

@Service
class ManualCommitConsumer:
    
    @KafkaListener(
        topics = ["important-events"],
        ack_mode = "MANUAL"
    )
    def handle_important_events(self, record: ConsumerRecord, ack: Acknowledgment):
        """手动提交偏移量的消费者"""
        try:
            # 处理消息
            self.process_important_event(record.value)
            
            # 处理成功后手动提交
            ack.acknowledge()
            
        except Exception as e:
            logger.error(f"Failed to process event: {e}")
            # 不提交偏移量，让消息重新投递
```

**条件化监听器**：
```python
@Service
class ConditionalEventListener:
    
    @KafkaListener(
        topics = ["system-events"],
        condition = "headers['event-type'] == 'ALERT'"
    )
    def handle_alert_events(self, record: ConsumerRecord):
        """只处理告警类型的事件"""
        alert_service.process_alert(record.value)
    
    @KafkaListener(
        topics = ["data-events"],
        condition = "value.size() > 1000"
    )
    def handle_large_data_events(self, record: ConsumerRecord):
        """只处理大数据量的事件"""
        large_data_processor.process(record.value)
```

## 第十章：Redis 集成与缓存管理

### 10.1 Redis 配置

PyBoot 提供了完整的 Redis 集成，包括连接池管理、序列化配置和模板操作。

**Redis 配置**：
```yaml
redis:
  host: "localhost"
  port: 6379
  password: "your_password"
  database: 0
  timeout: 3000
  pool:
    max-active: 20
    max-idle: 10
    min-idle: 5
    max-wait: 3000
  cluster:
    nodes: "redis1:6379,redis2:6379,redis3:6379"
    max-redirects: 3
  sentinel:
    master: "mymaster"
    nodes: "sentinel1:26379,sentinel2:26379,sentinel3:26379"
```

**Redis 配置类**：
```python
from pyboot.redis import RedisConfig, EnableRedis

@Configuration
@EnableRedis
class RedisConfiguration:
    
    @Bean
    def redis_config(self) -> RedisConfig:
        config = RedisConfig()
        config.host = "localhost"
        config.port = 6379
        config.database = 0
        config.password = "your_password"
        config.pool_config.max_active = 20
        config.pool_config.max_idle = 10
        return config
    
    @Bean
    def redis_template(self) -> RedisTemplate:
        template = RedisTemplate()
        template.key_serializer = StringRedisSerializer()
        template.value_serializer = Jackson2JsonRedisSerializer()
        template.hash_key_serializer = StringRedisSerializer()
        template.hash_value_serializer = Jackson2JsonRedisSerializer()
        return template
```

### 10.2 Redis 模板操作

**基本 Redis 操作**：
```python
@Service
class RedisOperationService:
    
    def __init__(self, redis_template: RedisTemplate):
        self.redis_template = redis_template
    
    def cache_user_session(self, user: User, session_data: dict):
        """缓存用户会话"""
        key = f"user:session:{user.id}"
        self.redis_template.ops_for_value().set(
            key, 
            session_data, 
            timeout=3600  # 1小时过期
        )
    
    def get_user_session(self, user_id: int) -> Optional[dict]:
        """获取用户会话"""
        key = f"user:session:{user_id}"
        return self.redis_template.ops_for_value().get(key)
    
    def cache_user_profile(self, user: User):
        """缓存用户档案"""
        key = f"user:profile:{user.id}"
        self.redis_template.ops_for_hash().put_all(key, {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at.isoformat()
        })
        self.redis_template.expire(key, 1800)  # 30分钟过期
    
    def increment_user_activity(self, user_id: int):
        """增加用户活动计数"""
        key = f"user:activity:{user_id}"
        self.redis_template.ops_for_value().increment(key)
        self.redis_template.expire(key, 86400)  # 24小时过期
```

**高级 Redis 操作**：
```python
@Service
class AdvancedRedisService:
    
    def __init__(self, redis_template: RedisTemplate):
        self.redis_template = redis_template
    
    def leaderboard_operations(self):
        """排行榜操作示例"""
        leaderboard_key = "global:leaderboard"
        
        # 添加分数
        self.redis_template.ops_for_zset().add(
            leaderboard_key, 
            "user:123", 
            1000
        )
        self.redis_template.ops_for_zset().add(
            leaderboard_key, 
            "user:456", 
            1500
        )
        
        # 获取排名
        rank = self.redis_template.ops_for_zset().reverse_rank(
            leaderboard_key, 
            "user:123"
        )
        
        # 获取前10名
        top_10 = self.redis_template.ops_for_zset().reverse_range(
            leaderboard_key, 0, 9
        )
        
        return top_10
    
    def pub_sub_operations(self):
        """发布订阅操作"""
        # 发布消息
        self.redis_template.convert_and_send(
            "user:notifications", 
            {"message": "Hello, World!"}
        )
    
    def lua_script_operations(self):
        """Lua脚本操作"""
        script = """
        local current = redis.call('GET', KEYS[1])
        if current then
            redis.call('SET', KEYS[1], current + ARGV[1])
        else
            redis.call('SET', KEYS[1], ARGV[1])
        end
        return redis.call('GET', KEYS[1])
        """
        
        result = self.redis_template.execute(
            script, 
            keys=["counter"], 
            args=[1]
        )
        return result
```

### 10.3 缓存注解

PyBoot 提供了声明式的缓存注解，类似于 Spring Cache：

**缓存使用示例**：
```python
@Service
class CachedUserService:
    
    @Cacheable(cache_names = "users", key = "#userId")
    def get_user_by_id(self, user_id: int) -> User:
        """根据ID获取用户，结果会被缓存"""
        logger.info(f"Fetching user {user_id} from database")
        return self.user_repository.select_by_id(user_id)
    
    @Cacheable(
        cache_names = "users", 
        key = "#username",
        unless = "#result == null"
    )
    def get_user_by_username(self, username: str) -> Optional[User]:
        """根据用户名获取用户，结果会被缓存"""
        return self.user_repository.find_by_username(username)
    
    @CacheEvict(cache_names = "users", key = "#user.id")
    def update_user(self, user: User) -> User:
        """更新用户信息，并清除缓存"""
        updated_user = self.user_repository.update_by_id(user)
        return updated_user
    
    @CacheEvict(cache_names = "users", all_entries = True)
    def clear_user_cache(self):
        """清除所有用户缓存"""
        logger.info("Cleared all user caches")
    
    @CachePut(cache_names = "users", key = "#user.id")
    def create_user(self, user: User) -> User:
        """创建用户，并更新缓存"""
        new_user = self.user_repository.insert(user)
        return new_user
    
    @Caching(
        evict = {
            @CacheEvict(cache_names = "users", key = "#user.id"),
            @CacheEvict(cache_names = "user_profiles", key = "#user.id")
        }
    )
    def delete_user(self, user: User):
        """删除用户，并清除相关缓存"""
        self.user_repository.delete_by_id(user.id)
```

**缓存配置**：
```python
@Configuration
@EnableCaching
class CacheConfiguration:
    
    @Bean
    def cache_manager(self) -> CacheManager:
        """配置缓存管理器"""
        redis_cache_manager = RedisCacheManager(self.redis_template)
        
        # 配置缓存过期时间
        config = RedisCacheConfiguration.default_cache_config()
        config = config.entry_ttl(Duration.of_minutes(30))
        config = config.prefix_keys_with("myapp:")
        
        redis_cache_manager.set_cache_defaults(config)
        
        return redis_cache_manager
    
    @Bean
    def user_cache_config(self) -> CacheConfiguration:
        """用户缓存特定配置"""
        return RedisCacheConfiguration.default_cache_config()
            .entry_ttl(Duration.of_hours(1))
            .prefix_keys_with("users:")
```

## 第十一章：多数据源与动态路由

### 11.1 多数据源配置

PyBoot 支持多数据源配置和动态数据源路由，适用于读写分离、分库分库等场景。

**多数据源配置**：
```yaml
database:
  primary:
    url: "postgresql://user:pass@master:5432/mydb"
    driver: "postgresql"
    username: "user"
    password: "pass"
    pool:
      max_connections: 20
  replica:
    url: "postgresql://user:pass@replica:5432/mydb"
    read_only: true
    pool:
      max_connections: 10
  reporting:
    url: "postgresql://user:pass@reporting:5432/reports"
    pool:
      max_connections: 5
```

**数据源配置类**：
```python
from pyboot.data import DataSource, DataSourceConfig

@Configuration
class MultiDataSourceConfig:
    
    @Bean
    @Primary
    def primary_data_source(self) -> DataSource:
        config = DataSourceConfig()
        config.url = "postgresql://user:pass@master:5432/mydb"
        config.username = "user"
        config.password = "pass"
        config.pool_size = 20
        return PostgreSQLDataSource(config)
    
    @Bean
    def replica_data_source(self) -> DataSource:
        config = DataSourceConfig()
        config.url = "postgresql://user:pass@replica:5432/mydb"
        config.username = "user"
        config.password = "pass"
        config.pool_size = 10
        config.read_only = True
        return PostgreSQLDataSource(config)
    
    @Bean
    def reporting_data_source(self) -> DataSource:
        config = DataSourceConfig()
        config.url = "postgresql://user:pass@reporting:5432/reports"
        config.username = "report_user"
        config.password = "report_pass"
        config.pool_size = 5
        return PostgreSQLDataSource(config)
```

### 11.2 动态数据源路由

**动态数据源路由器**：
```python
from pyboot.data import AbstractRoutingDataSource

@Component
class DynamicDataSourceRouter(AbstractRoutingDataSource):
    
    def __init__(self):
        super().__init__()
        self._target_data_sources = {}
        self._default_target_data_source = None
    
    def determine_current_lookup_key(self) -> str:
        """确定当前数据源键"""
        return DataSourceContextHolder.get_data_source() or "primary"
    
    def add_data_source(self, key: str, data_source: DataSource):
        """添加数据源"""
        self._target_data_sources[key] = data_source
    
    def set_default_data_source(self, data_source: DataSource):
        """设置默认数据源"""
        self._default_target_data_source = data_source

@Component
class DataSourceContextHolder:
    """数据源上下文持有者"""
    
    _context = threading.local()
    
    @classmethod
    def set_data_source(cls, data_source: str):
        cls._context.data_source = data_source
    
    @classmethod
    def get_data_source(cls) -> Optional[str]:
        return getattr(cls._context, 'data_source', None)
    
    @classmethod
    def clear_data_source(cls):
        if hasattr(cls._context, 'data_source'):
            del cls._context.data_source
```

**数据源切换切面**：
```python
@Aspect
@Component
class DataSourceAspect:
    
    @Around("@annotation(read_only)")
    def switch_to_replica(self, proceeding_joinpoint, read_only):
        """切换到只读数据源"""
        previous_data_source = DataSourceContextHolder.get_data_source()
        
        try:
            DataSourceContextHolder.set_data_source("replica")
            return proceeding_joinpoint.proceed()
        finally:
            if previous_data_source:
                DataSourceContextHolder.set_data_source(previous_data_source)
            else:
                DataSourceContextHolder.clear_data_source()
    
    @Before("@annotation(use_reporting_db)")
    def switch_to_reporting(self, joinpoint, use_reporting_db):
        """切换到报表数据库"""
        DataSourceContextHolder.set_data_source("reporting")
```

**数据源使用注解**：
```python
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface ReadOnly:
    pass

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface UseReportingDB:
    pass

@Service
class UserServiceWithDynamicDS:
    
    @ReadOnly
    def find_users(self, criteria: UserCriteria) -> List[User]:
        """查询用户，自动使用只读副本"""
        return self.user_repository.find_by_criteria(criteria)
    
    def update_user(self, user: User) -> User:
        """更新用户，使用主数据库"""
        return self.user_repository.update(user)
    
    @UseReportingDB
    def generate_user_report(self) -> UserReport:
        """生成用户报表，使用报表数据库"""
        return self.reporting_service.generate_user_report()
```

### 11.3 分库分表支持

**分库分表路由器**：
```python
@Component
class ShardingDataSourceRouter(AbstractRoutingDataSource):
    
    def determine_current_lookup_key(self) -> str:
        """根据分片键确定数据源"""
        shard_key = ShardingContextHolder.get_shard_key()
        if shard_key:
            return self.calculate_shard(shard_key)
        return "default"
    
    def calculate_shard(self, shard_key: int) -> str:
        """计算分片"""
        shard_count = len(self._target_data_sources)
        shard_index = shard_key % shard_count
        return f"shard_{shard_index}"

@Component
class ShardingContextHolder:
    """分片上下文持有者"""
    
    _context = threading.local()
    
    @classmethod
    def set_shard_key(cls, shard_key: int):
        cls._context.shard_key = shard_key
    
    @classmethod
    def get_shard_key(cls) -> Optional[int]:
        return getattr(cls._context, 'shard_key', None)
    
    @classmethod
    def clear_shard_key(cls):
        if hasattr(cls._context, 'shard_key'):
            del cls._context.shard_key

@Aspect
@Component
class ShardingAspect:
    
    @Before("execution(* *.*(..)) && @annotation(sharded)")
    def set_shard_key(self, joinpoint, sharded):
        """设置分片键"""
        # 从参数中提取分片键
        args = joinpoint.args
        shard_key = self.extract_shard_key(args, sharded.key_parameter())
        if shard_key:
            ShardingContextHolder.set_shard_key(shard_key)
```

## 第十二章：配置系统与多环境支持

### 12.1 YAML 配置支持

PyBoot 使用 YAML 作为默认的配置文件格式，支持复杂的配置结构和类型安全的配置绑定。

**主配置文件 (application.yaml)**：
```yaml
app:
  name: "My Application"
  version: "1.0.0"
  description: "A sample PyBoot application"
  
server:
  port: 8080
  host: "0.0.0.0"
  context-path: "/api"
  compression:
    enabled: true
    min-size: 1024
  
database:
  primary:
    url: "jdbc:postgresql://localhost:5432/mydb"
    username: "app_user"
    password: "app_pass"
    pool:
      max-size: 20
      min-size: 5
      connection-timeout: 30000
  
redis:
  host: "localhost"
  port: 6379
  password: "redis_pass"
  database: 0
  
kafka:
  bootstrap-servers: "localhost:9092"
  producer:
    acks: "all"
  consumer:
    group-id: "myapp-group"
  
logging:
  level:
    root: "INFO"
    com.example: "DEBUG"
  file:
    path: "./logs/app.log"
    max-size: "10MB"
    max-history: 7
```

**配置属性类**：
```python
from pyboot.config import ConfigurationProperties

@ConfigurationProperties(prefix = "app")
class AppProperties:
    
    def __init__(self):
        self.name = None
        self.version = None
        self.description = None
    
    # getter 和 setter 方法
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_version(self) -> str:
        return self.version
    
    def set_version(self, version: str):
        self.version = version

@ConfigurationProperties(prefix = "server")
class ServerProperties:
    
    def __init__(self):
        self.port = 8080
        self.host = "0.0.0.0"
        self.context_path = "/"
        self.compression = CompressionProperties()
    
    def get_port(self) -> int:
        return self.port
    
    def set_port(self, port: int):
        self.port = port

class CompressionProperties:
    
    def __init__(self):
        self.enabled = False
        self.min_size = 0
    
    def is_enabled(self) -> bool:
        return self.enabled
    
    def set_enabled(self, enabled: bool):
        self.enabled = enabled

# 注册配置属性
@Configuration
@EnableConfigurationProperties([AppProperties, ServerProperties])
class AppConfig:
    pass
```

### 12.2 多环境配置

PyBoot 支持多环境配置，可以根据不同的运行环境加载不同的配置文件。

**环境特定配置文件**：

- `application.yaml` - 主配置文件
- `application-dev.yaml` - 开发环境配置
- `application-test.yaml` - 测试环境配置  
- `application-prod.yaml` - 生产环境配置

**开发环境配置 (application-dev.yaml)**：
```yaml
app:
  environment: "dev"
  
server:
  port: 8081
  
database:
  primary:
    url: "jdbc:postgresql://localhost:5432/mydb_dev"
    username: "dev_user"
    password: "dev_pass"
  
logging:
  level:
    root: "DEBUG"
    com.example: "TRACE"
```

**生产环境配置 (application-prod.yaml)**：
```yaml
app:
  environment: "prod"
  
server:
  port: 80
  compression:
    enabled: true
  
database:
  primary:
    url: "jdbc:postgresql://prod-db:5432/mydb_prod"
    username: "prod_user"
    password: "${DB_PASSWORD}"
    pool:
      max-size: 50
      min-size: 10
  
logging:
  level:
    root: "WARN"
    com.example: "INFO"
  file:
    path: "/var/log/myapp/app.log"
```

**激活环境配置**：
```bash
# 通过环境变量激活环境
export PYBOOT_PROFILES_ACTIVE=prod

# 或者通过命令行参数
python app.py --pyboot.profiles.active=prod,metrics

# 或者在代码中设置
app = PyBootApplication()
app.set_additional_profiles("prod", "metrics")
app.run()
```

### 12.3 配置覆盖与外部化

**配置覆盖顺序**：
PyBoot 按照以下顺序加载配置，后加载的配置会覆盖前面的配置：

1. 框架默认配置
2. 应用 JAR 包内的 `application.yaml`
3. 应用 JAR 包内的 profile-specific 配置（如 `application-{profile}.yaml`）
4. 文件系统上的外部配置文件（`./config/application.yaml`）
5. 文件系统上的外部 profile-specific 配置（`./config/application-{profile}.yaml`）
6. 环境变量
7. 命令行参数

**外部化配置**：
```bash
# 使用外部配置文件
python app.py --pyboot.config.location=file:/etc/myapp/

# 使用环境变量覆盖特定配置
export SERVER_PORT=8090
export DATABASE_PRIMARY_URL=jdbc:postgresql://external-db:5432/mydb

# 使用命令行参数覆盖配置
python app.py --server.port=8090 --database.primary.url=jdbc:postgresql://external-db:5432/mydb
```

**安全的配置管理**：
```python
@Configuration
class SecureConfig:
    
    @Bean
    @ConfigurationProperties(prefix = "sensitive")
    def sensitive_properties(self) -> SensitiveProperties:
        return SensitiveProperties()
    
    @Bean
    def config_encryptor(self) -> ConfigEncryptor:
        """配置加密器，用于解密加密的配置值"""
        key = os.getenv("CONFIG_ENCRYPTION_KEY")
        return AesConfigEncryptor(key)

@Component
class SensitiveProperties:
    
    def __init__(self):
        self.encrypted_db_password = None
        self.api_key = None
    
    @Value("${sensitive.encrypted-db-password}")
    def set_encrypted_db_password(self, encrypted_value: str):
        # 解密加密的密码
        self.encrypted_db_password = self.config_encryptor.decrypt(encrypted_value)
```

## 第十三章：自定义组件与扩展

### 13.1 自定义组件开发

PyBoot 提供了灵活的扩展机制，允许开发者创建自定义组件来满足特定需求。

**自定义组件示例**：
```python
from pyboot.core import Component, ComponentDefinition, ComponentFactory

@Component
class CustomValidator:
    """自定义验证器组件"""
    
    def validate_email(self, email: str) -> bool:
        """验证邮箱格式"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_phone(self, phone: str) -> bool:
        """验证手机号格式"""
        import re
        pattern = r'^1[3-9]\d{9}$'
        return re.match(pattern, phone) is not None

@Component
class FileStorageService:
    """文件存储服务组件"""
    
    def __init__(self, storage_config: StorageConfig):
        self.config = storage_config
        self.setup_storage()
    
    def setup_storage(self):
        """设置存储后端"""
        if self.config.type == "local":
            self.backend = LocalFileStorage(self.config.local.path)
        elif self.config.type == "s3":
            self.backend = S3Storage(
                self.config.s3.bucket,
                self.config.s3.region
            )
        elif self.config.type == "azure":
            self.backend = AzureStorage(
                self.config.azure.container,
                self.config.azure.connection_string
            )
    
    def store_file(self, file_path: str, content: bytes) -> str:
        """存储文件"""
        return self.backend.store(file_path, content)
    
    def retrieve_file(self, file_path: str) -> bytes:
        """检索文件"""
        return self.backend.retrieve(file_path)
    
    def delete_file(self, file_path: str) -> bool:
        """删除文件"""
        return self.backend.delete(file_path)
```

### 13.2 自定义注解

**创建自定义注解**：
```python
from pyboot.core import Annotation, AnnotationMetadata

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
class RateLimited(Annotation):
    """限流注解"""
    
    def __init__(self, permits_per_second: float = 1.0):
        self.permits_per_second = permits_per_second

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
class ApiVersion(Annotation):
    """API版本注解"""
    
    def __init__(self, version: str):
        self.version = version

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
class AuditLog(Annotation):
    """审计日志注解"""
    
    def __init__(self, action: str, resource: str = ""):
        self.action = action
        self.resource = resource
```

**处理自定义注解的切面**：
```python
@Aspect
@Component
class RateLimitAspect:
    
    def __init__(self):
        self.limiters = {}
    
    @Around("@annotation(rate_limited)")
    def apply_rate_limit(self, proceeding_joinpoint, rate_limited):
        """应用限流逻辑"""
        method_name = f"{proceeding_joinpoint.target.__class__.__name__}.{proceeding_joinpoint.method.__name__}"
        
        # 获取或创建限流器
        limiter = self.limiters.get(method_name)
        if limiter is None:
            limiter = RateLimiter.create(rate_limited.permits_per_second)
            self.limiters[method_name] = limiter
        
        # 申请许可
        if not limiter.try_acquire():
            raise RateLimitExceededException("Rate limit exceeded")
        
        # 执行原方法
        return proceeding_joinpoint.proceed()

@Aspect
@Component
class AuditLogAspect:
    
    @Autowired
    def set_audit_service(self, audit_service: AuditService):
        self.audit_service = audit_service
    
    @AfterReturning("@annotation(audit_log)")
    def log_audit_event(self, joinpoint, audit_log):
        """记录审计日志"""
        user = SecurityContext.get_current_user()
        method_name = joinpoint.method.__name__
        resource = audit_log.resource or f"{joinpoint.target.__class__.__name__}.{method_name}"
        
        audit_event = AuditEvent(
            user_id=user.id if user else "anonymous",
            action=audit_log.action,
            resource=resource,
            timestamp=datetime.now(),
            success=True
        )
        
        self.audit_service.log_event(audit_event)
```

### 13.3 自定义 Starter

**创建自定义 Starter**：

**项目结构**：
```
my-custom-starter/
├── src/
│   └── main/
│       └── python/
│           ├── __init__.py
│           ├── autoconfigure.py
│           ├── properties.py
│           └── service.py
├── setup.py
└── README.md
```

**自动配置类**：
```python
from pyboot.core import Configuration, Condition