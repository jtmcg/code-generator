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

def construct_iteration_prompt(provided_code, unittest_code, test_feedback, test_summary):
    return f"""

    {test_summary["failed_count"]} of the {test_summary["total_count"]} tests failed. The tests that failed were {test_summary["failed_names"]}. 
    
    The provided code is in the first set of triple backticks, the unittest code used to test the provided code is in the second triple backticks, and the test runner feedback is in the third set of triple backticks. Using the test runner feedback, iterate on the provided code to make the failing tests pass while maintaining that the passing tests continue to pass. 
    
    Make sure that any non-test errors are addressed first and remove any unused imports. 
    
    Perform the following actions. The only output should be the JSON object specified in the last step:

    1. Summarize why each failing test failed.
    2. Summarize the functionality required for the failing tests to pass. Be sure to check that all positional arguments are used in the code.
    3. Provide the code that contains that functionality.
    4. Output the above steps in a JSON object in the following format: 
    {{
    "failing_tests_summary": "1", 
    "missing_functionality": "2",
    "code": "3"}}

    code:
    ```{provided_code}```
    tests:
    ```{unittest_code}```
    test runner feedback:
    ```{test_feedback}```

    """

def construct_iterative_success_prompt(provided_code, unittest_code, test_feedback, test_summary, difference, new_passing_tests):
    return f"""

    The provided code improved! {test_summary["success_count"]} of the {test_summary["total_count"]} tests passed, {difference} more than last attempt. The tests that failed were {test_summary["failed_names"]}, and the new passing tests were {new_passing_tests}.

    Iterate on the code, using the test runner feedback, to maintain that the passing tests continue to pass while making the failing tests pass. 
    
    The provided code is in the first set of triple backticks, the unittest code used to test the provided code is in the second triple backticks, and the test runner feedback is in the third set of triple backticks.
    
    Make sure that any non-test errors are addressed first and remove any unused imports. 
    
    Perform the following actions. The only output should be the JSON object specified in the last step:

    1. State what in the code made the new passing tests pass.
    2. Summarize why each failing test failed.
    3. Summarize the functionality required for the failing tests to pass. Be sure to check that all positional arguments are used in the code.
    4. Provide the code that contains that functionality.
    5. Output the above steps in a JSON object in the following format: 
    {{
    "passing_tests_summary": "1",
    "failing_tests_summary": "2", 
    "missing_functionality": "3",
    "code": "4"}}

    code:
    ```{provided_code}```
    tests:
    ```{unittest_code}```
    test runner feedback:
    ```{test_feedback}```

    """

def construct_regression_prompt(unittest_code, test_feedback, most_successful_code, new_failing_tests):
    return f"""

    The provided code has regressed! The tests that were previously passing and are now failing are {new_failing_tests}.

    Iterate on the non-regressed code, using the test runner feedback, to maintain that {new_failing_tests} continue to pass while making the failing tests pass. 
    
    The non-regressed code is in the first set of triple backticks, the unittest code used to test the non-regressed code is in the second triple backticks, and the test runner feedback is in the third set of triple backticks.
    
    Make sure that any non-test errors are addressed first and remove any unused imports. 
    
    Perform the following actions. The only output should be the JSON object specified in the last step:

    1. State what in the code made the new passing tests pass.
    2. Summarize why each failing test failed.
    3. Summarize the functionality required for the failing tests to pass. Be sure to check that all positional arguments are used in the code.
    4. Provide the code that contains that functionality.
    5. Output the above steps in a JSON object in the following format: 
    {{
    "passing_tests_summary": "1",
    "failing_tests_summary": "2", 
    "missing_functionality": "3",
    "code": "4"}}

    code:
    ```{most_successful_code}```
    tests:
    ```{unittest_code}```
    test runner feedback:
    ```{test_feedback}```

    """