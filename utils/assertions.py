import allure


def assert_data_is_equal(expected: any, actual: any, name=' '):
    with allure.step(f"Assert: {name}."):
        with allure.step(f'Ожидаемый результат: "{expected}"'):
            assert expected == actual, f'Фактический результат: "{actual}".'


def assert_lists_equal(actual, expected, name):
    with allure.step(f"Assert: {name}:"):
        with allure.step(f'Ожидаемый результат: {expected}'):
            if len(actual) != len(expected):
                raise AssertionError(f"Lists have different lengths: actual {len(actual)}, expected {len(expected)}")

            for i, (a, e) in enumerate(zip(actual, expected)):
                if a != e:
                    raise AssertionError(f"Lists do not match: Element at index {i} is {a}, expected {e}.")
