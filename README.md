# yancy

Yancy is a machine learning product that eliminates spam with 1 API call.

The product has multiple interfaces and is explained below.

We use the following for deployment.

Route53
ELB
ECS
PostgreSQL
Redis
Docker
Python2.7

The routes you may access are:

/usage = requires your api_key in the arguments and returns your usage
/spam = requires your api_key and spam in the body of the request (in json) and returns a T/F for spam or ham
/brain/rq = shows our internal redis interface
/results/<jobid> = returns whether a job has completed yet

For the project to run it must have access to a redis server and have a worker.py slave running as well

Worker does not run automatically 
