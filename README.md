# Emoncms 20 Second Polling

A custom [Home Assistant](https://www.home-assistant.io/) integration for importing [Emoncms](https://emoncms.org/) feeds as sensor entities. It is based on the standard Emoncms integration, with the polling interval set to **20 seconds**.

## Features

- Configures entirely through the Home Assistant UI.
- Connects to local or hosted Emoncms instances using an API key.
- Imports all available feeds or only the feeds you select.
- Refreshes feed values every 20 seconds.
- Assigns Home Assistant device classes and units to common energy, power, voltage, current, temperature, pressure, flow, and other measurements.
- Allows the selected feeds, server URL, and API key to be updated after setup.

## Installation

### HACS

1. Open HACS in Home Assistant and select **Integrations**.
2. Open the menu, select **Custom repositories**, and add this repository as an **Integration**.
3. Find and download **Emoncms 20 Second Polling**.
4. Restart Home Assistant.

### Manual

Copy `custom_components/emoncms` into the `custom_components` directory in your Home Assistant configuration folder, then restart Home Assistant.

## Configuration

1. In Home Assistant, go to **Settings > Devices & services**.
2. Select **Add integration** and search for **Emoncms**.
3. Enter the full Emoncms server URL, including `http://` or `https://`.
4. Enter your Emoncms API key.
5. Choose whether to synchronize every feed or select feeds manually.

The feed selection can be changed later from the integration's **Configure** dialog. The server URL and API key can be changed with **Reconfigure**.

## Requirements

- A reachable Emoncms server and API key.
- Emoncms 11.5.7 or newer is recommended so the integration can use the server UUID for stable entity IDs.

## Notes

The 20-second polling interval is fixed in this version. Polling more frequently increases traffic and load on both Home Assistant and the Emoncms server.