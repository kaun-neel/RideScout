```text
██████╗ ██╗██████╗ ███████╗    ███████╗ ██████╗ ██████╗ ██╗   ██╗████████╗
██╔══██╗██║██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔═══██╗██║   ██║╚══██╔══╝
██████╔╝██║██║  ██║█████╗      ███████╗██║     ██║   ██║██║   ██║   ██║   
██╔══██╗██║██║  ██║██╔══╝      ╚════██║██║     ██║   ██║██║   ██║   ██║   
██║  ██║██║██████╔╝███████╗    ███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝    ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   
```
# Cab Price Comparison Automation

**Droidrun Hackathon Project** - An automated workflow for comparing cab prices across Uber, Ola, and Rapido using Android emulator automation.

## Overview

This project demonstrates how automated workflows can provide significant value by comparing ride prices across multiple cab services and helping users make informed decisions. The automation runs entirely on an Android emulator using Droidrun's accessibility and vision capabilities.

## Features

- 🚕 **Multi-App Comparison**: Automatically checks prices across Uber, Ola, and Rapido
- 🤖 **LLM-Powered**: Uses z-ai/glm-4.5-air and mistralai/devstral-2512:free model via OpenRouter for intelligent UI interaction
- 🎯 **Reliable**: Handles failures gracefully - continues even if one or two apps fail
- 👀 **Vision-Enabled**: Uses screenshots and accessibility tree for UI understanding
- 🔒 **Safe**: Never auto-books rides - requires user confirmation
- 📊 **Transparent**: Shows all prices and failures clearly

## Impact

This automation saves users:
- **Time**: No need to manually open and check each app
- **Money**: Quickly identifies the cheapest option
- **Effort**: Automated data entry and price extraction

## Prerequisites

### 1. Android Emulator Setup

You need a running Android emulator with:
- Android version 8.0 (API 26) or higher
- Google Play Store installed
- Uber, Ola, and Rapido apps installed
- Apps configured and logged in

**Recommended Emulator Settings:**
- Device: Pixel 4 or similar
- RAM: 4GB minimum
- Storage: 8GB minimum

### 2. Droidrun Portal Setup

Install and configure Droidrun Portal accessibility service on the emulator:
1. Follow [Droidrun Documentation](https://droidrun.ai/docs) for Portal setup
2. Ensure Portal accessibility service is enabled
3. Grant all necessary permissions

### 3. Python Environment

- Python 3.8 or higher
- pip package manager

### 4. OpenRouter API Key

1. Sign up at [OpenRouter](https://openrouter.ai)
2. Get your API key from [API Keys page](https://openrouter.ai/keys)
3. The script uses the free `z-ai/glm-4.5-air:free` model

## Installation

### Step 1: Clone or Download This Project

```bash
cd cab_price_comparison
```

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your OpenRouter API key
# Replace 'your_openrouter_api_key_here' with your actual key
```

Your `.env` file should look like:
```
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxx
```

## Usage

### Step 1: Start Android Emulator

Make sure your Android emulator is running with Uber, Ola, and Rapido apps installed.

### Step 2: Ensure Droidrun Portal is Active

Verify that Droidrun Portal accessibility service is enabled and running.

### Step 3: Run the Script

```bash
python main.py
```

### Step 4: Follow the Prompts

The script will ask you for:
1. **Pickup location**: Enter your starting point (e.g., "Koramangala, Bangalore")
2. **Drop location**: Enter your destination (e.g., "MG Road, Bangalore")

### Step 5: Wait for Processing

The automation will:
- Launch each app sequentially (Uber → Ola → Rapido)
- Enter your locations
- Extract fare prices
- Display results

### Step 6: Review Results

You'll see a summary like:
```
PRICE COMPARISON RESULTS
==========================================================

  Uber       : ₹250.00
  Ola        : ₹235.00
  Rapido     : ₹248.00

----------------------------------------------------------
🎯 CHEAPEST OPTION: Ola at ₹235.00
----------------------------------------------------------
```

### Step 7: Confirm to Open

When prompted:
```
Do you want me to open Ola for you? (yes/no):
```

- Type `yes` to open the cheapest app
- Type `no` to exit

**IMPORTANT**: The script will NOT auto-book the ride. You maintain full control.

## How It Works

### Architecture

```
User Input
    ↓
[Droidrun Agent]
    ↓
┌─────────────────────────────────┐
│ For each app (Uber/Ola/Rapido) │
│  1. Launch app                  │
│  2. Enter pickup location       │
│  3. Enter drop location         │
│  4. Wait for fare display       │
│  5. Extract prices via OCR      │
│  6. Store minimum price         │
└─────────────────────────────────┘
    ↓
[Price Comparison]
    ↓
[User Confirmation]
    ↓
[Open Cheapest App]
```

### Key Components

1. **DroidAgent**: Main automation agent that interacts with Android UI
2. **Vision Mode**: Analyzes screenshots to understand UI elements
3. **Reasoning Mode**: Makes intelligent decisions based on UI state
4. **Accessibility Tree**: Navigates UI elements programmatically

### Failure Handling

The script is designed to be resilient:
- If one app fails to load → continues with others
- If prices aren't visible → marks app as failed
- If all apps fail → informs user and exits gracefully
- Never guesses or assumes data

## Configuration

### Adjusting Timeouts

Edit `cab_price_comparison.py` if you need longer wait times:

```python
config = DroidrunConfig(
    max_steps=50,      # Increase if automation times out
    timeout=300        # Total timeout in seconds
)
```

### Changing LLM Model

To use a different model, update the config:

```python
config = DroidrunConfig(
    llm_model="your-preferred-model",
    llm_api_key=api_key,
    llm_base_url="https://openrouter.ai/api/v1"
)
```

## Troubleshooting

### Issue: "OPENROUTER_API_KEY not found"

**Solution**: Ensure you've created `.env` file with your API key.

### Issue: Apps not launching

**Possible causes**:
- Apps not installed on emulator
- Portal accessibility service not enabled
- Emulator not connected

**Solution**: Verify all prerequisites are met.

### Issue: Prices not detected

**Possible causes**:
- UI loaded too slowly
- Price elements have different labels
- Network connectivity issues

**Solution**:
- Increase wait times in the script
- Check app versions match expected UI
- Ensure stable internet connection

### Issue: All apps failing

**Possible causes**:
- Emulator performance issues
- Portal service crashed
- API rate limits

**Solution**:
- Restart emulator
- Restart Portal service
- Check OpenRouter API status

## Best Practices

1. **Clean State**: Close all cab apps before running the script
2. **Stable Connection**: Ensure emulator has stable internet
3. **Sufficient Resources**: Give emulator adequate CPU/RAM
4. **Test Locations**: Use well-known locations for better accuracy
5. **Monitor Execution**: Watch the emulator screen during execution

## Limitations

- Requires apps to be pre-installed and logged in
- UI changes in apps may break automation
- Network speed affects execution time
- Some app features may be region-specific
- Does not handle app-specific promotions or discounts

## Future Enhancements

- Support for more cab apps (Lyft, InDrive, etc.)
- Price history tracking
- Scheduled price checks
- Push notifications for price changes
- Multi-location batch processing
- Integration with calendar for trip planning

## Project Structure

```
cab_price_comparison/
├── cab_price_comparison.py   # Main automation script
├── requirements.txt           # Python dependencies
├── .env.example              # Environment configuration template
├── .env                      # Your API keys (not in git)
├── README.md                 # This file
└── logs/                     # Execution logs (created automatically)
```

## Contributing

This is a hackathon project, but contributions are welcome:
1. Fork the repository
2. Create your feature branch
3. Test thoroughly on emulator
4. Submit a pull request

## License

This project is created for the Droidrun Hackathon. Use it freely for learning and demonstration purposes.

## Acknowledgments

- **Droidrun**: For providing the powerful automation framework
- **OpenRouter**: For API access to LLM models
- **Hackathon Organizers**: For the opportunity to build this

## Support

For questions or issues:
- Check [Droidrun Documentation](https://droidrun.ai/docs)
- Review troubleshooting section above
- Open an issue on the project repository

## Demo Video

[Add link to demo video showing the automation in action]

---

**Built with ❤️ for Droidrun Hackathon**
