# 阿里云函数计算：FC 访问数据库案例

### mysql

只需几步就可以快速在阿里云函数计算服务上体验 Python 访问 mysql 数据库

- 初始化项目：`s init start-fc-mysql-python -d start-fc-mysql-python`
- 进入项目：`cd start-fc-mysql-python`
- 将 s.yaml 中的环境变量修改成您自己的值
- 构建项目：`s build --use-docker`
- 部署项目：`s deploy`
- 触发项目：`s invoke`

即可实现`Python 访问 mysql`案例的初始化、部署整个流程。

## 参考

> - Serverless Devs 项目：https://www.github.com/serverless-devs/serverless-devs
> - Serverless Devs 文档：https://www.github.com/serverless-devs/docs
> - Serverless Devs 钉钉交流群：33947367
