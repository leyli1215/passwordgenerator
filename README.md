# Random Password Generator

## Overview
This Python script generates a random password based on user-defined criteria. The user specifies the number of digits and letters they want in their password, and the script ensures that the total length does not exceed 16 characters. The generated password is a random mix of digits and letters.

## Features
- **Customizable Password Length:** The user can specify how many digits and letters to include in the password.
- **Randomized Output:** The characters in the password are shuffled to ensure randomness.
- **Input Validation:** The script includes checks to ensure that the total number of characters does not exceed 16.

## How to Use
1. Run the script.
2. Enter the number of digits you want in the password.
3. Enter the number of letters you want in the password.
4. The script will generate and print a random password based on your input.

 
## Code Structure
- **get_random_char():** Returns a random letter (uppercase or lowercase).
- **get_random_digit_or_char():** Returns a random letter or digit.
- **get_random_digit():** Returns a random digit.
- **generate(num_numbers, num_letters):** Main function that generates the password by combining the specified number of digits and letters, then shuffles them.

## Installation
1. Clone this repository to your local machine using: https://github.com/leyli1215/passwordgenerator.git
2. Ensure you have Python installed on your system (version 3.x recommended).
3. Run the script using Python

## Future Enhancements
- Add an option to include special characters.
- Implement a command-line interface using argparse to allow users to input parameters directly from the command line.
- Add unit tests to validate the functionality.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

