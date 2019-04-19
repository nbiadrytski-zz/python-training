def test_tmpdir(tmpdir):  # tmpdir is of type py.path.local
    # tmpdir already has a path name associated with it
    # join() extends the path to include a filename
    # the file is created when it's written to
    a_file = tmpdir.join('something.txt')

    # you can create directories
    a_sub_dir = tmpdir.mkdir('anything')

    # you can create files in directories (created when written)
    another_file = a_sub_dir.join('something_else.txt')

    # this write creates 'something.txt'
    a_file.write('contents may settle during shipping')

    # this write creates 'anything/something_else.txt'
    another_file.write('something different')

    # you can read the files as well
    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'


def test_tmpdir_factory(tmpdir_factory):
    # you should start with making a directory
    # a_dir acts like the object returned from the tmpdir fixture
    a_dir = tmpdir_factory.mktemp('mydir')
    print(f'directory: {a_dir}')

    # base_temp will be the parent dir of 'mydir'
    # you don't have to use getbasetemp()
    # using it here just to show that it's available
    base_temp = tmpdir_factory.getbasetemp()
    print(f'base directory: {base_temp}')

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    print(f'subdirectory: {a_sub_dir}')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'
# .directory: /private/var/folders/zv/0_bnnz2d5gqfzmq9p6hfdv2dzc19fp/T/pytest-of-mikalai_biadrytski/pytest-37/mydir0
# base directory: /private/var/folders/zv/0_bnnz2d5gqfzmq9p6hfdv2dzc19fp/T/pytest-of-mikalai_biadrytski/pytest-37
# subdirectory: /private/var/folders/zv/0_bnnz2d5gqfzmq9p6hfdv2dzc19fp/T/pytest-of-mikalai_biadrytski/pytest-37/mydir0/anything
