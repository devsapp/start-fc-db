# 阿里云函数计算 Python 访问 Lindorm 云数据库

只需几步就可以快速在阿里云函数计算服务上体验 Python 访问 Lindorm 数据库

- 初始化项目：`s init start-fc-lindorm-python -d start-fc-lindorm-python`
- 进入项目：`cd start-fc-lindorm-python`
- 将 s.yaml 中的环境变量和 vpc 配置修改成您自己的值, 并将代码中有关数据库操作改成您自己需要的
- 构建项目：`s build --use-docker`
- 部署项目：`s deploy`
- 触发项目：`s invoke`

即可实现`Python 访问 Lindorm`案例的初始化、部署整个流程。


# Python access to Lindorm cloud database in Function Compute

In just a few steps, you can quickly experience Python on the Function Compute to access the Lindorm database

- Initialize the project: `s init start-fc-lindorm-python -d start-fc-lindorm-python`
- Enter the project: `cd start-fc-lindorm-python`
- Modify the environment variables and vpc configuration in s.yaml to yours, and change the database operations in the code to what you need
- Build the project: `s build --use-docker`
- Deployment project: `s deploy`
- Invoke Function: `s invoke`

The whole process of initializing and deploying the case of `Python access to Lindorm` can be realized.
