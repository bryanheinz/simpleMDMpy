# Tests

This is my first foray into unit tests. If you see any issues or have any recommendations, please open a [Github issue](https://github.com/macadmins/simpleMDMpy/issues) or reach out to me on the [Mac Admins](https://www.macadmins.org) Slack @bheinz - @bryanheinz

Because our testing currently has to be done on our own SimpleMDM instances, please be extra cautious and review all code before running. This is also why the tests largely don't test for specific data.

## Testing Steps
- Duplicate `settings-sample.py` as `settings.py` and fill in the variables
- Create virtual environments folder if it doesn't already exist `mkdir ~/.env`
- Create the virtual env `python3 -m venv ~/.env/smdm-tests`
- Activate the environment `source ~/.env/smdm-tests/bin/activate`
- Install the simpleMDMpy module version that you'd like to test `pip install -e /path/to/cloned/simpleMDMpy` (requires pyproject.toml and setup.cfg files, and pip v22+)
- Run the tests `python3 -m unittest discover -s /path/to/cloned/simpleMDMpy/tests`
- Uninstall the test module `pip uninstall SimpleMDMpy`
- Deactivate the Python virtual environment `deactivate`
