# Airtel USSD Simulation Program

This Python script simulates an Airtel mobile network's USSD menu, allowing users to interact with a menu system similar to what might be available on a mobile device. The script provides a structured navigation system for selecting Airtel services, including data packs, voice bundles, international calling, and balance checks. 

# Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Functions Overview](#functions-overview)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Payment Processing:** Supports payment via Airtel Money and Main Account options.
- **Data and Voice Bundles:** Includes various options such as daily, weekly, monthly packs, and roaming bundles.
- **International Services:** Provides bundles for international calling, roaming, and tourist packs.
- **Error Handling:** Displays error messages for invalid inputs, promoting a smooth user experience.
- **Console Clear:** Each menu refreshes with a cleared console for easy navigation.

## Getting Started

### Prerequisites

- Python 3.x
- OS Terminal (tested on Windows and Linux)

### Installation

1. Clone the repository or download the script file.
2. Ensure all dependencies are installed (Python `os` and `re` modules are standard).

```bash
git clone <repository-link>
```

## Usage

Run the script using:

```bash
python Main_program.py
```

You’ll be prompted to enter a USSD code to begin. Enter `*117#` to access the main menu.

### Menu Options
Once the main menu loads, navigate by entering the option numbers displayed. For example:

1. **Ikali-Data and Voice:** Displays options for Airtel data and voice bundles.
2. **Soche Pack:** Access daily, weekly, and monthly packs.
3. **All Networks Soche:** Provides bundled packs for all networks.
4. **Data Packs:** Purchase specific data bundles.
5. **Buy for Other:** Gift packs to other Airtel users.
6. **Balance Check:** Check your bundle balance.
7. **Airtime Loan:** Check eligibility and borrow airtime.
8. **Airtel App Download:** Get a link to download the Airtel app.

Enter `n` to view additional international roaming and calling options.

### Functions Overview

The program uses a series of functions, organized to manage various menu paths and services:

- **Main Functions:** Handles navigation, such as `home_menu()`, which provides the main options, and `ussd()`, which checks if the correct USSD is entered.
- **Payment Functions:** `payment_method()`, `pm_main_account()`, and `pm_airtel_money()` manage payment steps.
- **Sub-menu Functions:** Each service has associated functions, like `home_menu_opt1()`, which navigates the Ikali-Data and Voice options.
- **Input Validation:** For phone numbers, uses regular expressions to validate format and identify Airtel numbers.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
Distributed under the GNU License. 

