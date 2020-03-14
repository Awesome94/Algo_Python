### SOLID PRINCIPLES OF OOP IN PYTHON.

#### Single Responsibility Principle.
A class must and should have only one job to avoid the domino effect. Hence if a class is having more than one job then it is coupled and hence this violates the Single responsibility principle.


#### Open Closed Principle.
A class is closed to modification but open to extension. Hence a class can't be modified in order to add a new functionality but can be extended instead.

#### Liskov's Substitution Principle.
It states that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application. This means that objects of your subclass behave the same way as your superclass hence one can implement restrictive rules in the superclass but not stricter rules in the subclass as that mught lead to an exception when the object is called with the superclass attribs

#### Interface Segreggation Principle.
Many client specific interfaces are better than one general-purpose interface. The interface segregation pricnciple Splits very large interfaces into smaller and more specific ones that clients will only have to know about the methods that are of interest to them. ISP is intended to keep a system decoupled and thus easier to refactor or change.

#### Dependency Inversion Principle.
Entities must depend on abstractions not concretions. It states that high level modules must depend on abstractions and not low level modules

