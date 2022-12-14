import pickle

example_dict = {1: "6", 2: "2", 3: "f"}


class Tester:
    def __int__(self):
        pass

class_obj = Tester
print(class_obj)

pickle_out = open("dict.pickle", "wb")
pickle.dump(class_obj, pickle_out)
pickle_out.close()
