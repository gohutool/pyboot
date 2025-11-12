# 🚀 PyBoot · 让 Python 开发者也拥有 SpringBoot 般的极致体验！

> 谁说只有 Java 才能“一键启动”？  
> 谁说只有 SpringBoot 才能“约定大于配置”？  
> **PyBoot** 用纯粹的 Python 语法，把 **FastAPI + 自研 ORM + 热加载 + 自动配置 + 依赖注入** 全部装进一个 `pyboot run` 命令里！  
> 写完业务逻辑直接跑，**像 Python 一样优雅，像 SpringBoot 一样强大**！

---

## 1. 一键启动 · 约定大于配置
```bash
pip install pyboot
pyboot create app myapp
cd myapp
pyboot run
```
浏览器打开 `http://localhost:8080/docs`——Swagger 已就绪！  
不用写任何 `@Configuration`、`@EnableAutoConfiguration`，PyBoot 自动扫描 `./app/application` 目录下的 **控制器 / 服务 / 实体**，**零 XML、零装饰器、零样板代码**！

---

## 2. MVC 控制器 · 类型提示即校验
```python
# app/controller/user_controller.py
from pyboot import Controller, Get, Post, Body

class UserController(Controller):
    @Get("/users/{user_id}")
    async def get_user(self, user_id: int) -> UserDTO:
        return self.user_service.find_by_id(user_id)

    @Post("/users")
    async def create_user(self, dto: UserDTO = Body(...)) -> int:
        return self.user_service.create(dto)
```
等价于 Spring 的 `@RestController` + `@RequestMapping` + `@Validated`，但**全程 Python 类型注解**，**IDE 自动补全 + FastAPI 自动生成文档**！

---

## 3. 自动依赖注入 · 像 Spring 一样解耦
```python
# app/service/user_service.py
from pyboot import Service, Inject

class UserService(Service):
    repo: UserRepo = Inject()          # 同 Spring 的 @Autowired
    cache: RedisCache = Inject()

    async def find_by_id(self, uid: int) -> UserDTO:
        if await self.cache.exists(f"user:{uid}"):
            return await self.cache.get(f"user:{uid}")
        return await self.repo.find_by_id(uid)
```
**无需注册 Bean、无需手动 new**——PyBoot 在启动期扫描并构建单例，支持 **循环依赖检测** 与 **懒加载**。

---

## 4. 自研 ORM · 真正的 Pythonic SQLAlchemy
```python
# app/model/user.py
from pyboot import Model, column

class User(Model):
    id: int = column(primary_key=True, auto_increment=True)
    username: str = column(max_length=32, unique=True)
    password: str = column(max_length=128)

# 查询
users = await User.select().where(User.username == "tom").limit(10).fetch()

# 分页
page = await User.page(page_no=1, page_size=20)

# 事务
async with Transaction():
    user = await User.save(username="tom", password=encoded_pwd)
    await Profile.save(user_id=user.id, bio="Hello PyBoot!")
```
支持 **连表懒加载、乐观锁、读写分离、自动建表、迁移脚本**——**SQLAlchemy 的能力，Django ORM 的简洁**！

---

## 5. 配置中心 · 多环境一键切换
```yaml
# config/application.yml
server:
  host: 0.0.0.0
  port: 8000

spring:
  datasource:
    url: ${DB_URL:sqlite+aiosqlite:///./dev.db}
    pool_size: 20

logging:
  level: ${LOG_LEVEL:INFO}
```
用法同 SpringBoot `application.yml`：  
- `${KEY:default}` 占位符自动注入环境变量  
- `pyboot run --profile=prod` 加载 `config/application-prod.yml`  
- **热加载**修改配置后 `CTRL+R` 即时生效，**无需重启**！

---

## 6. 热加载 · 开发效率 MAX
开发模式下 **监测 `./app` 所有 `.py` 文件变动**，**毫秒级重载**，**保持数据库连接不断**！  
写完代码**保存即可刷浏览器**——**比 Spring DevTools 更快**！

---

## 7. 官方插件 · 开箱即用
| 插件 | 一句话描述 |
|---|---|
| `pyboot-security` | JWT + OAuth2 + RBAC，像 Spring Security 一样配置 `security.yml` 即可 |
| `pyboot-admin` | 自动生成 **Web UI 管理后台**（类似 Spring-Boot-Admin） |
| `pyboot-task` | 基于 **Celery** 的分布式任务，一行 `@task` 声明 |
| `pyboot-test` | 提供 `@PyBootTest` + `TestClient`，**单元测试 & 集成测试**一键跑 |

---

## 8. 性能 & 生产部署
- **基于 FastAPI + uvloop**，媲美 **Go** 的吞吐量（见官方 benchmark）  
- **内置 gunicorn + uvicorn worker** 启动脚本：`pyboot deploy --workers 8`  
- **Docker 官方镜像** `pyboot/pyboot:3.11-slim` 仅 **60 MB**，**冷启动 < 1 秒**  
- **Prometheus + Grafana** 模板已集成，**指标端点** `/actuator/metrics` 一键暴露

---

## 9. 三分钟上线 · 完整 CI/CD 模板
```dockerfile
FROM pyboot/pyboot:3.11-slim
COPY . /app
RUN pyboot build
CMD ["pyboot", "run", "--host=0.0.0.0", "--port=8000"]
```
GitHub Actions 文件已内置：`pyboot generate pipeline` 自动生成 `.github/workflows/deploy.yml`，**push 即部署**！

---

## 10. 写在最后 · 这是我们的 Python SpringBoot！

> 我们热爱 Python 的简洁，也羡慕 SpringBoot 的省心。  
> 于是，我们把 **自动配置、依赖注入、热加载、ORM、安全、监控、插件生态** 全部带到了 Python 世界！  

**PyBoot** 不是又一个 Web 框架，  
它是 **“让 Python 开发者也能拥有 SpringBoot 般生产力”** 的答案！

🔥 **现在就试试：**
```bash
pip install pyboot
pyboot create -n my_app && cd my_app && pyboot run
```
欢迎贡献、欢迎 Star，让我们一起 **把 Python 的生产力推向极致！**