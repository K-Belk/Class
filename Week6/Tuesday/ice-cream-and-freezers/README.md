# Ice Cream And Freezers 
 
## Learning Competencies 

* Create single responsibility classes
* Implement clean and flexible interfaces between objects
* Use composition to give structure to more complex objects

## Summary 

 **I <3 Ice Cream** is a creamery that makes delicious ice cream.  They are growing rapidly, and they need some software to help them manage their kitchen.
  
Your job is to build a program that will help them manage their ice cream freezing.  Here are a few user stories to help get you started:
    
- As a ice cream maker, I want to make different types of ice cream (peanut butter, chocolate chip, etc.).
- As a ice cream maker, I want to place batches of ice cream in an freezer.
- As a ice cream maker, I want to know when a batch of ice cream is ready to be removed from the freezer.

## Releases

### Release 0 :Design the structure

Think about this problem critically before you even begin to write code and describe how you would design the program in plain English.
        
At the very least, consider these questions in your answer:
        
- What are essential classes?
- What attributes will each class have?
- What interface will each class provide?
- How will the classes interact with each other?
- Which classes will inherit from others, if any?


Implement a minimum viable product.

It does not need to track multiple types of ice cream, but you should be able to move ice cream into and out of a freezer.  This would be a great time to write some tests in the spec file that show how you'd _like_ your classes to work, and then get them all to pass!

### Release 1 : Additional Features

Add more features to your program.
      
- Multiple types of ice cream, each with a different freezing time
- Status attribute for ice cream, with at least these possible values: `:watery`, `:almost_ready`, `:ready`, `:freezer_burned`

Don't forget to write more tests for this release.

### Release 2 : Refactor

Take a step back and look at the code you've produced.  Run through a checklist to see if you are following the principles of object-oriented design:
        
- Is it DRY?
- Do your classes follow the [Law of Demeter](http://en.wikipedia.org/wiki/Law_of_Demeter)?
- Are your classes [orthogonal](http://stackoverflow.com/a/1527430)?
- Do you expose only the minimum amount of surface area for each object?

---

The Law of Demeter can be summarized as follows:

*For all classes C. and for all methods M attached to C, all objects to which M sends a message must be instances of classes associated with the following classes:*

1. *The argument classes of M (including C).*
2. *The instance variable classes of C.*

*(Objects created by M, or by functions or methods which M calls, and objects in global variables are considered as arguments of M.)*
      
Read [Avdi Grimm's post](http://devblog.avdi.org/2011/07/05/demeter-its-not-just-a-good-idea-its-the-law/) for a more thorough explanation.

### Release 3 : Get Creative!

Put yourself in the ice cream maker's shoes, and imagine what other features you might like to have.  Then pick the most useful and feasible one and build it out. 
