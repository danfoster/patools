import pulsectl
import subprocess

DMENU_BIN = '/usr/bin/dmenu'

def main():
    pulse = pulsectl.Pulse('patools')
    sink_list = pulse.sink_list()
    sinks = {}

    for sink in sink_list:
        sinks[sink.description] = sink

    p = subprocess.run(
        [DMENU_BIN, "-i", "-p", "Select Output Device"],
        input = '\n'.join(sinks.keys()),
        encoding='ascii',
        stdout=subprocess.PIPE
    )

    if (p.returncode != 0):
        return p.returncode

    sink_name = p.stdout.rstrip()

    pulse.default_set(sinks[sink_name])

    sink_inputs = pulse.sink_input_list()
    for si in sink_inputs:
        pulse.sink_input_move(si.index,sinks[sink_name].index)

if __name__ == "__main__":
    main()
