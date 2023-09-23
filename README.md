# misc
Dumping ground of scripts and other bits

## Setup
Run `python3 ./setup.py` to configure and move files.

It's also recommended to add `~/.my-scripts` to `PATH`

### buildkite_digitalocean
These are scripts to handle automatic starting and stopping of digitalocean droplets
which have a basic buildkite agent set up.

- `dobk-start` will create droplets for buildkite. These will all have the `buildkite` tag.
- `dobk-stop` will tear down all droplets with the `buildkite` tag.