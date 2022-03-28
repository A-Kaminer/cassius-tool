import analysis_tests
import rot_tests

def tests():
    print("Analysis Module Tests:")
    print(f"Test 1: {analysis_tests.test1()}") # import of analysis
    print(f"Test 2: {analysis_tests.test2()}") # creating an object
    
    print("Rot Module Tests:")
    print(f"Test 1: {rot_tests.test1()}") # importing rotciphers and rot13 thinking about capitals
    print(f"Test 2: {rot_tests.test2()}") # same as above but ignoring capitals

if __name__ == "__main__":
    import sys
    sys.path.append('../../')
    input("Note! You need to run this from the actual tests directory for it to work. Otherwise, there will be problems. Ok?")
    print("Starting Analysis tests:")
    tests()
