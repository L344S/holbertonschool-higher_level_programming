#!/usr/bin/python3

# can't test locally hidden_4 contains null bytes + wrong version of python
if __name__ == "__main__":  # make sure code does not execute when imported
    import hidden_4  # import hidden_4 module
    for i in dir(hidden_4):  # for loop through the list of names
        print(i)  # print the names
