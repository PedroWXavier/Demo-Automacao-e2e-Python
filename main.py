from behave import __main__ as behave_executable

debug = False


if __name__ == "__main__":
    behave_executable.main('features/login.feature --no-capture --no-capture-stderr')
