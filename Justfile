
server *ARGS: venv
	@./.venv/bin/python3 src/server.py {{ARGS}}

install: venv
	./.venv/bin/pip install --no-cache-dir -r requirements.txt

venv:
	@[ -d .venv ] || python -m venv .venv

clean:
	rm -rf ./.venv
