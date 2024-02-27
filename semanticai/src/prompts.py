def construct_initial_prompt(language, unittest_code):
    return f"""

You're a {language} software developer. You will write code to make the unit tests given in the triple backticks passed. Provide the code to make the tests pass.

Perform the following actions. The only output should be the JSON object specified in the last step:

1. Summarize what the code is intended to do given the tests.
2. List the names of the functions that this test is covering.
3. Provide the code to make this test pass.
4. Output the above steps in a JSON object in the following format: 
{{
    "test_summary": "1", 
    "function_names": "2",
    "code": "3"}}

tests:
```{unittest_code}```

"""

def construct_iteration_prompt(provided_code, unittest_code, test_feedback):
    return f"""

    Some or all of the tests did not pass. 
    
    The provided code is in the first set of triple backticks, the unittest code used to test the provided code is in the second triple backticks, and the test runner feedback is in the third set of triple backticks. Using the test runner feedback, iterate on the provided code to make the failing tests pass while maintaining that the passing tests continue to pass. 
    
    Make sure that any non-test errors are addressed first and remove any unused imports. 
    
    Perform the following actions. The only output should be the JSON object specified in the last step:

    1. List which tests passed.
    2. State what in the code made the passing tests pass.
    3. List which tests failed.
    4. Summarize why each test failed.
    5. Summarize the functionality required for the failing tests to pass. Be sure to check that all positional arguments are used in the code.
    6. Provide the code that contains that functionality.
    7. Output the above steps in a JSON object in the following format: 
    {{
    "passing_tests": "1",
    "passing_tests_summary": "2",
    "failing_tests": "3",
    "failing_tests_summary": "4", 
    "missing_functionality": "5",
    "code": "6"}}

    code:
    ```{provided_code}```
    tests:
    ```{unittest_code}```
    test runner feedback:
    ```{test_feedback}```

    """