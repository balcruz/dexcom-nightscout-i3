# nightscout-i3

This project retrieves data from [Nightscout](https://nightscout.github.io/) and updates the [i3 status bar](https://i3wm.org/docs/i3status.html) on any
GNU/Linux distribution with `i3wm` installed.
〰️

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/balcruz/nightscout-i3.git
   cd nightscout-i3
   ```

2. Create a virtual environment

```bash
# Navigate to your project directory
cd nightscout-i3

# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On Linux or macOS
source venv/bin/activate

```

3. Environment file

Add your values to the following variables in the `.env` file:

- `NIGHTSCOUT_HOST`
- `NIGHTSCOUT_API_TOKEN`
- `TIMEZONE`

4. Install dependencies:

```bash
  pip install -r requirements.txt
```

## Usage

```bash
  python src/nightscout/main.py
```

## i3 Configuration

### Create a `status.sh` script

Create a script `$HOME/bin/status.sh` with the following content:

```bash
#!/bin/sh

i3status | while :; do
  read line
  data=$(~/bin/nightscout.py)
  echo "${data} | $line" || exit 1
done
```

### Update the `$HOME/.i3/config` file

Update the line

```bash
 status_command i3status
```

with the following:

```bash
 status_command exec $HOME/bin/status.sh
```

## References

- [Nightscout site](https://nightscout.github.io/)
- [i3wm site](https://i3wm.org/)

## License

This project is licensed under the MIT License.
