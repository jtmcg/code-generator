def construct_initial_prompt(language, unittest_code):
    return f"""

You're a {language} software developer. You will write code to make the unit tests given in the triple backticks passed. You will use the strategies of test driven development to do this. Provide the code to make the first test pass.

Perform the following actions:

1. Summarize what the code is intended to do given the first test.
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

def construct_iteration_prompt(test_feedback):
    return f"""

    Some or all of the tests did not pass. The feedback from the test runner is in the triple backticks. Using that feedback, iterate on the code you previously provided to make the failing tests pass while maintaining that the passing tests continue to pass. Make sure that any non-test errors are addressed first and remove any unused imports. Perform the following actions:

    1. Summarize what the code is intended to do given the tests.
    2. List the names of the functions that these tests are covering.
    3. Provide the code.
    4. 4. Output the above steps in a JSON object in the following format: 
    {{
    "test_summary": "1", 
    "function_names": "2",
    "code": "3"}}

    test feedback:
    ```{test_feedback}```

    """

