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
# app/application/myapp/controller/hello.py
from dataflow.module.context.web import RequestBind, Controller
@Controller(prefix='/sample/api', tags=["Sample接口"])
class SampleController():
    userService:UerService = Context.Autowired()
    
    @RequestBind.GetMapping('/test/{id}')    
    async def test(self, id):
        _logger.DEBUG(f'id={id}')
        return {'id':id}

    @RequestBind.GetMapping('/user/{id}')   
    async def getuser(self, id):        
        _logger.DEBUG(f'id={id}')
        user = self.userService.getUserByName(id)
        return user
```
等价于 Spring 的 `@RestController` + `@RequestMapping` + `@Validated`，但**全程 Python 类型注解**，**IDE 自动补全 + FastAPI 自动生成文档**！

---

## 3. 自动依赖注入 · 像 Spring 一样解耦
```python
# app/application/myapp/service/hello.py
from dataflow.module import Context

class UserService(Service):    
    pydbc:PydbcTools=Context.Autowired() # 同 Spring 的 @Autowired
    userMapper:UserMapper = Context.Autowired()   # 同 Spring 的 @Autowired

    def getUserByName(self, username):
        return self.userMapper.selectUserByUserName(username)

```
**无需注册 Bean、无需手动 new**——PyBoot 在启动期扫描并构建单例，支持 **循环依赖检测** 与 **懒加载**。

---

## 4. 自研 ORM · 真正的 Pythonic SQLAlchemy
```python
# app/application/myapp/dao/hello.py
from dataflow.module.context.pybatisplus import Mapper

@Mapper(table='sys_user', id_col='user_id')
class UserMapper:
    def selectUserByUserName(self, userName:str)->dict:
        pass

# 查询
    class UserService(Service):    
        pydbc:PydbcTools=Context.Autowired() # 同 Spring 的 @Autowired
        userMapper:UserMapper = Context.Autowired()   # 同 Spring 的 @Autowired

        def getUserByName(self, username):
            return self.userMapper.selectUserByUserName(username)

# 分页
    page_result = self.userMapper.select_list(page_no=1, page_size=20)

# 事务

    @TX(propagation=Propagation.REQUIRES_NEW)
    def test_tx_3(self):
        _logger.DEBUG("BEGIN TX3 ========================")
        sample = '''
            {"id":435177,"tradedate":"2025-09-30","code":"920819","name":"颖泰生物","price":"4.25","changepct":"-0.47","change":"-0.02","volume":"56537","turnover":"24137761.32","amp":"1.17","high":"4.3","low":"4.25","topen":"4.3","lclose":"4.27","qrr":"0.62","turnoverpct":"0.47","pe_fwd":"170.35","pb":"1.02","mc":"5209650000","fmc":"5131906875","roc":"-0.23","roc_5min":"-0.23","changepct_60day":"1.67","changepct_currentyear":"19.72","hot_rank_em":5116,"market":"SZ","createtime":"2025-09-30 09:32:17","updatetime":"2025-09-30 17:06:09","enable":1}
            '''
        sample:dict = str_to_json(sample)
        sample['low']=NULL    
        sample['tradedate']='2025-01-05'
        sample['code']=f'3_{current_millsecond()}'        
        rtn = self.pydbc.insertT('dataflow_test.sa_security_realtime_daily', sample)        
        _logger.DEBUG(f"END TX3 Result={rtn}  {sample}")
        time.sleep(30)

```
支持 **连表懒加载、乐观锁、读写分离、自动建表、迁移脚本**——**SQLAlchemy 的能力，Django ORM 的简洁**！

---

## 5. 配置中心 · 多环境一键切换
```yaml
# app/myapp/conf/application.yaml
application:
  name: {{ project_name }}
  version: 1.0.1-beta
  profiles:
  server:
    port: ${SERVER_PORT:8080}
    host: ${SERVER_HOST:0.0.0.0}
    workers: 1

logging:
  level: ${LOG_LEVEL:INFO}
  config: conf/logback.yaml

context:
  database:
    ds01:
      url: ${MYSQLDS.url:mysql+pymysql://u:p@localhost:61306/dataflow_test?charset%20utf8mb4}
      # url: ${MYSQLDS.url:mysql+pymysql://u:p@localhost:61306/stock_agent?charset=utf8mb4}
      username: ${env:MYSQLDS.user:stock_agent}
      password: ${env:MYSQLDS.password:stock_agent}
      test: select 1

```
用法同 SpringBoot `application.yml`：  
- `${KEY:default}` 占位符自动注入环境变量  
- `pyboot run --profile=dev` 加载 `conf/application-dev.yml`  
- **热加载**修改配置后 `CTRL+R` 即时生效，**无需重启**！

---

## 6. 热加载 · 开发效率 MAX
开发模式下 **监测 `./app` 所有 `.py` 文件变动**，**毫秒级重载**，**保持数据库连接不断**！  
写完代码**保存即可刷浏览器**——**比 Spring DevTools 更快**！

---

## 7. 官方插件 · 开箱即用
| 插件 | 一句话描述 |
|---|---|
| `pyboot-langfuse` | 一键接入 LangFuse 可观测性平台，自动记录、追踪与分析 PyBoot 应用中的每一次请求与模型调用，让 AI 研发链路“白盒化”，一行 `@langfuse` 声明 。 |
| `pyboot-milvus` | 把 PyBoot 的向量数据直接扔进 Milvus，秒变“语义搜索引擎” |
| `pyboot-kafka` | 一键发布订阅 Kafka，让 PyBoot 服务秒变流式事件驱动架构。 提供 `@ON_Consumer` |
| `pyboot-redis` | 为PyBoot提供高速缓存、分布式锁与队列能力，显著提升数据读写性能，轻松构建高并发、低延迟的分布式应用。 |
| `pyboot-etcd` | 为PyBoot提供开箱即用的分布式键值存储与健康检查能力，让服务发现、配置共享和集群协调一键完成，无需额外编码即可构建高可用分布式系统。 |

pyboot组件扩展实现自由扩展自己的插件，自动扫描加载，不需要重写init、run方法完成自定义命令与模板，支持参数注入与生命周期钩子， 集成自定义扩展组件到系统context容器里。

---

## 8. 性能 & 生产部署
- **基于 FastAPI + uvloop**，媲美 **Go** 的吞吐量（见官方 benchmark）  
- **内置 gunicorn + uvicorn worker** 启动脚本：`pyboot run --workers 8`  
- **Docker 官方镜像** `registry.cn-shenzhen.aliyuncs.com/joinsunsoft/pyboot:1.0.0-slim` ，**冷启动 < 5 秒**  
- **Prometheus + Grafana** 模板已集成，**指标端点** `/metrics` 一键暴露

---

## 9. 三分钟上线 · 完整 CI/CD 模板
```dockerfile
FROM registry.cn-shenzhen.aliyuncs.com/joinsunsoft/pyboot:1.0.0-slim
COPY . /data/myapp/
WORKDIR /data/myapp/
CMD ["pyboot", "run", "--host=0.0.0.0", "--port=8000", "--workers=8"]
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
pip install pyboot-cli pyboot-dataflow
pyboot create app my_app && cd myapp && pyboot run
```
欢迎贡献、欢迎 Star，让我们一起 **把 Python 的生产力推向极致！**