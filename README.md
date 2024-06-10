# OBS Scenes Export Script

## Description

I wanted a one-click way to export an OBS scene collection with all its dependencies. Not finding a solution online, I asked ChatGPT to create a script for me. Here is the result.

## Features

Automatically extracts media file paths from an OBS configuration JSON file and copies them to a designated folder along with the JSON file.

## Requirements

- [Python 3.x](https://www.python.org/)

## Usage

1. Open a command line or terminal.
2. Run the script with the following command:

   ```bash
   python export.py <path_to_your_json_file>
   ```

   Replace `<path_to_your_json_file>` with the path to your OBS configuration JSON file.

### Example

```bash
python export.py my_profile.json
```

## Project Structure

```
├── export.py
├── README.md
├── example
│   └── my_profile.json
└── output
    └── my_profile
        ├── media
        │   ├── media_file1.mp4
        │   ├── media_file2.png
        │   └── ...
        └── my_profile.json
```

## Notes

- Ensure that the media file paths in your OBS configuration are correct and accessible.
- The script will display a message if a media file is not found.

## Contributions

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
