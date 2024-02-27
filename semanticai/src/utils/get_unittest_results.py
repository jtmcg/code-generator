def get_unittest_results(results_string):
    lines = results_string.split('\n')
    total_tests = int(lines[-4].split(' ')[1])
    failed_tests_lines = [line for line in lines if line.startswith('FAIL:')]
    failed_tests = [line.split(' ')[1] for line in failed_tests_lines]
    failed_count = len(failed_tests)
    return {
        'total_count': total_tests,
        'failed_count': failed_count,
        'failed_names': failed_tests,
        'success_count': total_tests - failed_count
    }