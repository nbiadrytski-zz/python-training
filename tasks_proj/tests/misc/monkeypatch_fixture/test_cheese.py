import copy
from tasks_proj.tests.misc.monkeypatch_fixture import cheese


def test_def_prefs_change_expanduser(tmpdir, monkeypatch):
    """During the test, anything in cheese module that calls os.path.expanduser() gets our lambda expression instead"""
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(cheese.os.path, 'expanduser', (lambda x: x.replace('~', str(fake_home_dir))))
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_defaults(tmpdir, monkeypatch):
    """
    Let’s say we’re worried about what happens if the file already exists.
    We want to be sure it gets overwritten with the defaults when write_default_cheese_preferences() is called
    """
    # write the file once
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(cheese.os.path, 'expanduser', (lambda x: x.replace('~', str(fake_home_dir))))
    cheese.write_default_cheese_preferences()
    defaults_before = copy.deepcopy(cheese._default_prefs)

    # change the defaults
    # Because _default_prefs is a dictionary, we can use monkeypatch.setitem() to change dictionary
    # items just for the duration of the test.
    monkeypatch.setitem(cheese._default_prefs, 'slicing', ['provolone'])
    monkeypatch.setitem(cheese._default_prefs, 'spreadable', ['brie'])
    monkeypatch.setitem(cheese._default_prefs, 'salads', ['pepper jack'])
    defaults_modified = cheese._default_prefs

    # write it again with modified defaults
    cheese.write_default_cheese_preferences()

    # read, and check
    actual = cheese.read_cheese_preferences()
    assert defaults_modified == actual
    assert defaults_modified != defaults_before
