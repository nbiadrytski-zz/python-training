from learning_p_lutz.oop_stuff.class_coding_details import manynames


X = 66  # global var in otherfile_manynames
print(X)  # 66

# BUT
print(manynames.X)  # 11; global var in manynames

manynames.f()  # 11; manynames X global var from line 1
manynames.g()  # 22; printing manynames' function g() local var defined in line 9

print(manynames.C.X)  # 33; class C attribute in manynames module

I = manynames.C()
print(I.X)  # 33; still class C attribute in manynames module
I.m()  # I is an instance of class C
print(I.X)  # 55; Instance attribute in class C from manynames from line 18

