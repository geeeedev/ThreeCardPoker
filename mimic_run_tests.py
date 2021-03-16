# run command: cd M43 <dir>
# run command: python3 ./mimic_run_tests.py "python3 M43Poker.py"   - test for exact output checking
# run command: python3 ./run_tests "python3 M43Poker.py"            - final test for Pass/Fail/Error output

import os
import sys
import subprocess

# print(sorted(os.listdir('tests/'))) #['.DS Store','01','02']
for file_num in sorted(os.listdir('tests/')):
    if not file_num.isnumeric():
        continue
    # print(file_num)       #01
    test_contents = open('tests/' + file_num, 'r').read()
    # print(test_contents)  #hamburger reads
    test_contents = test_contents.split("\n\n")
    # print(test_contents)  #[ , , ] reads
    (name, inp, out) = (test_contents[0], test_contents[1], test_contents[2].strip())
    # print(name,inp,out)
    # print(name)
    # print(inp)
    # print(out)

    # run command: python3 ./mimic_run_tests.py 'python3 M43Poker.py'
    # print(sys.argv)               # ./mimic_run_tests.py 'python3 M43Poker.py' - anything after 'python3'
    # print(sys.argv[1])            # python3 M43Poker.py
    # print(sys.argv[1].split())    # ['python3','M43Poker.py']
    # universal_newlines=T          # taking input as text not byte sequence
    # input=                        # input string passing to sys.stdin for pickup
    # .strip()                      # takes out ending \n
    output = subprocess.check_output(sys.argv[1].split(), universal_newlines=True, input=inp).strip()
    print(output)






# ### <<anotherTestFileContainsMain()>>.py for this testing
# print(__name__)  # __main__
# print(__main__)  #not defined

# import sys
# 
#
# def main(line):
#     print(line)
#
# if __name__ == "__main__":
#     for line in sys.stdin:        # correct syntax to PASS inp to my script!!!
#         print(f'sys.stdin')       # but this is delivering line by line to Game which won't work
#         print(line)
#       # main(line)
#
# test successful
# run python3 ./mimic_run_tests.py 'python3 <<anotherTestFileContainsMain()>>.py'
#
# sys.stdin
# 3
# \n
# sys.stdin
# 0 2c As 4d
# \n
# sys.stdin
# 1 Kd 5h 6c
# \n
# sys.stdin
# 2 Jc Jd 9s