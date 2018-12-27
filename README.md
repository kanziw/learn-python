# learn-python

## Python version 관리

> using pyenv [link1](https://github.com/pyenv/pyenv) [link2](https://github.com/pyenv/pyenv/issues/1219)

```bash
# Install pyenv
❯ brew install pyenv
❯ pyenv versions
* system (set by /Users/kanziw/.pyenv/version)

# List available versions
❯ pyenv install --list
Available versions:
  2.1.3
  2.2.3
  2.3.7
  2.4
  2.4.1
...

❯ pyenv install 3.7.1
# 실패한다면 아래 명령어 수행 후 다시 시도
❯ xcode-select --install
❯ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /

❯ pyenv versions
* system (set by /Users/kanziw/.pyenv/version)
  3.7.1
```

## Project 별 Python version 관리

> using `.python-version`

```bash
❯ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
# at each project
❯ echo "3.7.1" >> .python-version
```

