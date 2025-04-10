
run *ARGS: venv
	@./.venv/bin/python3 {{ARGS}}

install: venv
	./.venv/bin/pip install -r server_requirements.txt

venv:
	@[ -d .venv ] || python -m venv .venv

clean:
	rm -rf ./.venv
