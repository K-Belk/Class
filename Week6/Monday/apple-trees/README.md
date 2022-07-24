# Apple Tree 1 - Just Apples

## Learning Competencies

* Modeling systems with objects.
* Use instance variables and accessing instance variables effectively. 
* Work with objects in Python

## Summary

Rainy Washington grows apples. Fun fact: on average, Washington state grows 125 million boxes of apples per year. At 40 lbs per box, that’s 2.5 million TONS of apples!

Let's create a toy program to model an apple tree growing over the years.  We plant the apple tree, wait for it to bear some fruit, and then pick all the apples as soon as it does.

The tests in `apple_tree_spec.py` show how all this might work together.

## Releases

### Release 0 : Implement the AppleTree and Apple classes

Set up your AppleTree and Apple classes with the appropriate attributes. You'll need to be able to call  `tree.height` and `tree.age` to get a tree's height or age, respectively. What other attributes might your class need? Use the code in the runner file to guide you. Write tests to make sure your class is working the way you expect it to. 

### Release 1 : Implement Aging

As a tree ages, it grows taller.  Eventually it starts bearing fruit and stops growing &mdash; not necessarily at the same time.  Some years later, the tree dies and can bear fruit no more!

Implement an `age_tree()` instance method that will age your tree one year.  Each year the tree should get some amount taller, and then eventually stop growing.  You can decide when the tree stops growing.

Later, it should die.

At this point your `AppleTree` class should:

1. Have a `height` attribute which returns the tree's current height
2. Have an `age` attribute which returns the tree's current age
3. Have an `age_tree()` method which ages the tree one year and grows the tree a little, if it's able to grow
4. Have an `is_dead()` method which returns `True` if the tree has died. Let's say trees die at age 100.

Update your tests to test these methods and their side-effects.

### Release 2 : Implement Apple-picking

After some number of years &mdash; you decide &mdash; the apple tree starts to bear fruit.  Write a method `any_apples()` which returns `True` if there are any apples on the tree and `False` otherwise.

Also write a method `pick_an_apple()` which will return one of the apples on the tree (an instance of the `Apple` class).  If you try to pick an apple when there are no apples left, your code should raise an error.

The `Apple` class needs to be implemented by this point, including `Apple()` and `apple.diameter`.

Write tests for your methods. Make sure you assert their behavior and side-effects.

#### Does the script run?

Now that you've implemented your code and created tests for it, let's try and run it. Fill out `runner.py` to calculate `avg_diameter`, then run the file to see your classes in action.

Does the script at the top of the challenge run and output what you'd expect?  (Hint: you have to be clear about your expectations before you answer that question.)

If not, what are the errors or unexpected behaviors?  Do you understand them? Fix your code and write tests that would have caught your bug(s). You might need to update existing tests if you find you were asserting the wrong thing, or in the wrong way.

## Resources

* [Variable Scopes in Python](https://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html)
* Unittest Documentation: [Python 3 Unittest](https://docs.python.org/3/library/unittest.html)
