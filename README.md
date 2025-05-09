# stapp-api-workflow
Try to create a workflow to issue API requests in [streamlit](https://streamlit.io/) apps.

## Usage
- [poetry cli](https://python-poetry.org/docs/)を利用する

### Setup
```sh
poetry install

# start poetry virtual env.
# poetry shell # for poetry 1.x version
eval $(poetry env activate) # for poetry 2.x version

# when finish poetry virtual env.
deactivate
```

### Task Commands
- task commands is set at `[tool.taskipy.tasks]` in [pyproject.toml](./pyproject.toml):
```sh
$ task --list
run                 streamlit run src/main.py
test                pytest tests
test-cov            pytest tests --cov --cov-branch -svx
test-report         pytest tests --cov --cov-report=html
format              black --line-length 79 src
lint                flake8 src
check-format        run lint check after format
export-requirements export requirements.txt file
export-req-with-dev export requirements-dev.txt file
rm-dist             remove build and dist directory
make-dist           make distribution package
```

### Start as local service
```sh
# on poetry env.
# streamlit hello
task run
# streamlit run src/main.py
# Local URL: http://localhost:8501
```


### format and lint check
```sh
# task format
# task lint
task check-format
```


### Test with `pytest`
- Refer to [streamlitのテスト手法](https://docs.streamlit.io/develop/concepts/app-testing/get-started)
```sh
# on poetry env
# pytest tests/test_main.py
task test
```

### Test coverage

#### show c1 coverage
```sh
# on poetry env
task test-cov
```

#### output HTML coverage report
```sh
# on poetry env
task test-report
```

### Export `requirements.txt` file

- export `requirements.txt` file of only `[tool.poetry.dependencies]` packages
```sh
# on poetry env
task export-requirements
```

- export `requirements.txt` file of `[tool.poetry.dependencies]` and `[tool.poetry.group.dev.dependencies]` packages
```sh
# on poetry env
task export-req-with-dev
```

### Build Docker image and run
```sh
# Build Docker image
sudo task docker-build

# run docker container
sudo task docker-run
```

#### priviredge setting:
- to execute docker command without sudo, set following:
```sh
sudo usermod -aG docker $USER
newgrp docker
```

### make packages
- make package file under dist for run stapp without Python
```sh
# make distribution package on poetry env
task make-dist
```

- clear package
```sh
# remove distribution package on poetry env
task rm-dist
```

- run package
```sh
# run package without poetry env
./dist/run_stapp/run_stapp
```

## Used Library

This project use following Open Source Library:

- [Streamlit](https://streamlit.io/) - Apache License 2.0

  Copyright © 2019-2025 Streamlit Inc.

  Streamlit is an open source library for easily creating data applications.


## License
MIT License

This project is released under the MIT License. See the [LICENSE](. /LICENSE) file for details.

However, this project uses Streamlit, which is licensed under the Apache License 2.0.
The full Streamlit license can be found [here](https://github.com/streamlit/streamlit/blob/develop/LICENSE).
