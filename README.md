# Image Message Encoder/Decoder

This Python program is designed to encode and decode messages within the RGB values of an image. It slightly manipulates the RGB values to encode a message in binary that is not visible to the naked eye. The script can then decode the message from the image. Created in 2022.

## How It Works

- **Encoding**: The script takes a message input and encodes it into the least significant bit of the red channel in the image's pixels.
- **Decoding**: It decodes the message by reading the manipulated pixels and converting the binary data back into text.

## Limitations

Currently, the program does not work as intended due to the automatic rounding of image pixel color values when being saved, aimed at reducing file size. This rounding alters the least significant bits used for encoding the message, making accurate decoding challenging. Any suggestions or solutions to this issue would be greatly appreciated.

## Usage

1. **Encode a Message**: Run the script and select the encode option. You will be prompted to enter a message, which will then be encoded into a predefined image.
2. **Decode a Message**: Run the script again and choose the decode option to extract the message from the encoded image.

### Requirements

- Python 3.x
- PIL library (Pillow)

### Installation

Ensure Python 3 and PIL are installed. You can install PIL using pip:
`pip install Pillow`

### Contributions
Contributions are welcome, especially in addressing the program's current limitations with pixel rounding. If you have any ideas or solutions, please feel free to fork the project and submit a pull request.


