# AirBnB_clone - The Console
Player 1 ready

## Welcome to the AirBnB clone project!
_Before starting, please read the AirBnB concept page._

__First step:__ Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: __the AirBnB clone__. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

__Each task is linked and will help you to:__

put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances\
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file\
create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`\
create the first abstracted storage engine of the project: File storage.\
create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
_Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project_:

Create a new object (ex: a new User or a new Place)\
Retrieve an object from a file, a database etc…\
Do operations on objects (count, compute stats, etc…)\
Update attributes of an object\
Destroy an object\

### Resources
Read or watch:

cmd module\
cmd module in depth\
packages concept page\
uuid module\
datetime\
unittest module\
--->args/kwargs\
-->Python test cheatsheet\
->cmd module wiki page\
>python unittest

## The console
create your data model

manage (create, update, destroy, etc) objects via a console / command interpreter

store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
