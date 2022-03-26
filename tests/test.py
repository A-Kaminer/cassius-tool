import general_tests

def tests():
    print("General Tests:")
    print(f"Test 1: {general_tests.test1()}")
    print(f"Test 2: {general_tests.test2()}")

if __name__ == "__main__":
    import sys
    sys.path.append('../')
    input("Note! You need to run this from the actual tests directory for it to work. Otherwise, there will be problems. Ok?")
    print("Starting Analysis tests:")
    tests()
