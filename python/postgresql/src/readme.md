# 阿里云函数计算 Python 访问 postgresql 数据库

只需几步就可以快速在阿里云函数计算服务上体验 Python 访问 postgresql 数据库

- 初始化项目：`s init start-fc-postgresql-python -d start-fc-postgresql-python`
- 进入项目：`cd start-fc-postgresql-python`
- 将 s.yaml 中的环境变量和 vpc 配置修改成您自己的值, 并将代码中有关数据库操作改成您自己需要的
- 构建项目：`s build --use-docker`
- 部署项目：`s deploy`
- 触发项目：`s invoke`

即可实现`Python 访问 postgresql`案例的初始化、部署整个流程。

# Python access postgresql database in Function Compute

You can quickly experience Python access to postgresql database on Function Compute in just a few steps

- Initialize the project: `s init start-fc-postgresql-python -d start-fc-postgresql-python`
- Enter the project: `cd start-fc-postgresql-python`
- Modify the environment variables and vpc configuration in s.yaml to yours, and change the database operations in the code to what you need
- Build the project: `s build --use-docker`
- Deployment project: `s deploy`
- Invoke Function: `s invoke`

The whole process of initialization and deployment of the case of `Python access postgresql` can be realized.
