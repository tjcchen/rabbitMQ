# RabbitMQ 

## How to install RabbitMQ on macOS

1. Install Homebrew

```bash
# install homebrew if you don't have one
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# add homebrew to your path
echo >> /Users/chen/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/chen/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# check homebrew version
brew --version
```

2. Install RabbitMQ

```bash
# install rabbitmq, this will install erlang required by rabbitmq as well
brew install rabbitmq
```


3. Start RabbitMQ

```bash
# start rabbitmq server manually
rabbitmq-server

# start rabbitmq server as a service (This will make RabbitMQ run in the background and auto-start on boot.)
brew services start rabbitmq

# stop rabbitmq server as a service
brew services stop rabbitmq

# enable rabbitmq management plugin
rabbitmq-plugins enable rabbitmq_management

# check rabbitmq status
http://localhost:15672/#/

# login with default username and password
username: guest
password: guest
```


4. Verify RabbitMQ Installation 

```bash
# check rabbitmq status
brew services list

# or check rabbitmq status
rabbitmqctl status

# check rabbitmq process
brew services start rabbitmq
ps aux | grep rabbit

# stop rabbitmq server as a service
brew services stop rabbitmq
ps aux | grep rabbit
```


