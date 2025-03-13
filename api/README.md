# Therapy Service backend application

## Setup local environment (MacOS)
### Environment variables:
1. Download `direnv`: `brew install direnv`
   - For direnv to work properly it needs to be hooked into the shell. Each shell has its own extension mechanism.
        - `bash`: Add the following line at the end of the `~/.bashrc` file: `eval "$(direnv hook bash)"`
        - `zsh`: Add the following line at the end of the `~/.zshrc` file: `eval "$(direnv hook zsh)"`
2. Set up your `.env` file using example `cp .env.example .env`
3. Edit `.env` file or leave it as is
4. Allow `direnv` for `app` folder by running `direnv allow`
### Python installation:
1. Install `pyenv`: `brew install pyenv`
2. Install `Python`: `pyenv install`
### Dependency installation:
1. Install `poetry`: `pip install poetry`
2. Install dependencies: `poetry install -with dev,test`

## Run
1. `poetry run api` - to start the web server
   - you can set a port server is running by providing a positional arg like `poetry run api 8082`
