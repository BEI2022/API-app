# R1 Identification of the problem you are trying to solve by building this particular app

通过构建此特定应用程序确定您尝试解决的问题。  
My app is a real estate management system designed to bring together scattered listings of properties that are interested in selling or buying/renting and unify them for users to browse and select the homes they want.

## R2 Why is it a problem that needs solving?

为什么这是一个需要解决的问题？  
With the diversification of life or some force majeure factors (such as living in another state buyer/seller and during the covid period of lock dowm), resulting in many people do not want to go to the site to see the property like the original, only through the Internet way to learn about the desired property online, plus the original way of distributing paper flyers is too wasteful of resources, so through the online way has become increasingly popular in recent years, my program is to solve this problem of people do not want to go out and want to learn about the relevant properties.

## R3 Why have you chosen this database system. What are the drawbacks compared to others?

为什么选择这个数据库系统。与其他人相比有什么缺点？  
(Pestgrest与NO-SQL的区别)  
The database I chose was PostgreSQL, the reason is that

1. PostgreSQL was a database I had just learned and I could use it directly without spending time and effort to learn a completely new database.  
2. It is an open source database and it is free.  
3. It is the only relational database that is compatible with SQL, which means it has no contradictions in its consistency and legacy features.  
4. It has higher readability and cleaner and tidier code compared to NO-SQL.  
5. It provides procedural language to implement complex procedures via Python.

I think the drawbacks are

1. Postgresql's multi-version concurrency control is not very good,i.e. the database has many versions of data instead of many versions of the database itself, so when you need to process a piece of data, you need to determine which version of data to use before you can process the operation.  This will generate a lot of data and take up a lot of space,which needs to be cleaned up regularly.
2. Postgresql takes a long time to expand its capacity.

## R4 Identify and discuss the key functionalities and benefits of an ORM

识别并讨论 ORM 的关键功能和好处  
(1什么是ORM.2是干嘛的.3使用它的好处是什么)  
ORM is short for Object-Relational-Mapper is a library that allows you to manipulate data in a database using an object-oriented approach.

An ORM library is a library written in the language of your choice that has encapsulated the SQL code needed to manipulate the data, and you can interact directly with the database objects using the language of your choice.

The benefits are  

1. Dry code, easy to update and maintain.
2. Avoid bugs caused by writing SQL.  
3. Simple call method.  
4. Use your own programming language.

## R5 Document all endpoints for your API

记录 API 的所有端点  
https://github.com/acoomans/flask-autodoc

## R6 An ERD for your app

应用的 ERD  
画图并解释

## R7 Detail any third party services that your app will use

详细说明您的应用将使用的任何第三方服务  
pypi package

## R8 Describe your projects models in terms of the relationships they have with each other

根据彼此之间的关系来描述您的项目模型  
讨论SQLAlchemy模型和Marshmallow模式

## R9 Discuss the database relations to be implemented in your application

讨论要在您的应用程序中实现的数据库关系  
讨论DB(表、列、关系、主键/外键)

## R10 Describe the way tasks are allocated and tracked in your project

描述在您的项目中分配和跟踪任务的方式  
解释trello过程
