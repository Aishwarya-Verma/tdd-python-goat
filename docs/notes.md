# Chapter: 1
- Python command to run the test:
``` sh
python functional_tests.py
```
- The first step in getting Django up and running is to create a project, which will be the main container for our site.
- Django provides a little command-line tool for this:
```sh
django-admin startproject superlists .
```
- Don’t forget that "`.`" at the end; it’s important!
- That will create a file called manage.py in your current folder, and a subfolder called superlists, with more stuff inside it:
```sh
.
├── functional_tests.py
├── manage.py
└── superlists
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
- The superlists folder is intended for stuff that applies to the whole project—​like settings.py, for example, which is used to store global configuration information for the site.
- But the main thing is `manage.py`. That’s Django’s Swiss Army knife, and one of the things it can do is run a development server.
- Let’s try that now:
```sh
python manage.py runserver
```
- That’s Django’s development server now up and running on our machine.

---
# Chapter: 2
### Using a Functional Test (FT) to Scope Out a Minimum Viable App
- Tests that use Selenium let us drive a real web browser, so they really let us see how the application functions from the user’s point of view.
- That’s why they’re called functional tests (FT).
- This means that an FT can be a sort of specification for your application.
- It tends to track what you might call a User Story, and follows how the user might work with a particular feature and how the app should respond to them.
- FTs should have a human-readable story that we can follow. We make it explicit using comments that accompany the test code.
- When creating a new FT, we can write the comments first, to capture the key points of the User Story.
- Being human-readable, you could even share them with nonprogrammers, as a way of discussing the requirements and features of your app.
- TDD and agile or lean software development methodologies often go together, and one of the things we often talk about is the minimum viable app, which we have just started to work on!

### The Python Standard Library’s `unittest` Module
- There are some ready-made solutions for us in the standard library’s unittest module. Ref: `tdd_tests/functional_tests.py`
- Tests are organised into classes, which inherit from `unittest.TestCase`.
- The main body of the test is in a method called ex: `test_can_start_a_todo_list`.
- Any method whose name starts with `test_` is a test method, and will be run by the test runner.
- You can have more than one test_ method per class. Nice descriptive names for our test methods are a good idea too.
- `setUp` and `tearDown` are special methods which get run before and after each test.
- `browser`, which was previously a global variable, becomes `self.browser`, an attribute of the test class. This lets us pass it between setUp, tearDown, and the test method itself.
- We use `self.assertIn` instead of just assert to make our test assertions.
- `unittest` provides lots of helper functions like this to make test assertions, like `assertEqual`, `assertTrue`, `assertFalse`, and so on. You can find more in the unittest documentation.
- `self.fail` just fails no matter what, producing the error message given. I’m using it as a reminder to finish the test.
- Finally, we have the `if __name__ == '__main__'` clause 
    - that’s how a Python script checks if it’s been executed from the command line, rather than just imported by another script.
- We call `unittest.main()`, which launches the unittest test runner, which will automatically find test classes and methods in the file and run them.

### Useful TDD Concepts
- **User Story**:
    - A description of how the application will work from the point of view of the user.
    - Used to structure a functional test.
- **Expected failure**:
    - When a test fails in the way that we expected it to.

---
# Chapter: 3
### Testing a Simple Home Page with Unit Tests
- Start an app for our `to-do lists`:
    - That will create a folder called lists, next to manage.py and the existing superlists folder, and within it a number of placeholder files for things like models, views, and tests.
    ```sh
    python manage.py startapp lists
    ```
- Functional tests versus unit tests:
    |Functional tests|Unit tests|
    |---|---|
    |One test per feature/user story | Many tests per feature|
    |Tests from the user’s point of view | Tests the code (i.e., the programmer’s point of view)|
    |Can test that the UI "really" works | Tests the internals—individual functions or classes|
    |Provides confidence that everything is wired together correctly and works end-to-end | Can exhaustively check permutations, details, and edge cases|
    |Can warn about problems without telling you exactly what’s wrong | Can point at exactly where the problem is|
    |Slow | Fast|
- Functional tests should help you build an application that actually works, and guarantee you never accidentally break it. Unit tests should help you to write code that’s clean and bug free.
- Django is structured along a classic model-view-controller (`MVC`) pattern—well, broadly.
    - It definitely does have models, but what Django calls "views" are really controllers, and the view part is actually provided by the templates.
- Django’s workflow goes like:
  1. An HTTP request comes in for a particular URL.
  2. Django uses some rules to decide which view function should deal with the request (this is referred to as resolving the URL).
  3. The view function processes the request and returns an HTTP response.
- Django uses a file called `urls.py` to map URLs to view functions. This mapping is also called `routing`.
    - There’s a main `urls.py` for the whole site in the `superlists` folder.

### Useful Commands and Concepts
- Running the Django dev server
    ```sh
    python manage.py runserver
    ```
- Running the functional tests
    ```sh
    python functional_tests.py
    ```
- Running the unit tests
    ```sh
    python manage.py test
    ```
- The unit-test/code cycle:
    - Run the unit tests in the terminal.
    - Make a minimal code change in the editor.
    - Repeat!

---
# Chapter: 4