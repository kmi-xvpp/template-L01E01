def test_output(script_runner):
    ret = script_runner.run("hello_world.py")
    assert ret.success
    assert ret.stdout == "Hello world!\n"
    assert ret.stderr == ""
