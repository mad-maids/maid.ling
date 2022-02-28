[![Telegram](https://img.shields.io/badge/telegram-%40roomFinderTgBot-blue)](https://t.me/roomFinderTgBot)

# Empty Room Finder

Simple Telegram bot that finds empty rooms at WIUT.
Say goodbye to wasting time on timetable page going through each room on the dropdown menu!
For more info on what this bot does, please check out the [bot](https://t.me/roomFinderTgBot) and run `/help`.

## Installation

Edit the `.env.example` file and then rename it to `.env`. Create your `redis.conf` file in the root folder of the repository (an example is provided, see `redis-example.conf`).

Then just run the following in your terminal:

```sh
docker-compose up -d
```
