from hello import main

def test_hello(capsys):
	main()
	stdout, stderr = capsys.readouterr()
	assert stdout == 'Hello world from dev\n', 'hello.py prints "Hello world from dev\\n"'

