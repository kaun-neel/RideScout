# Quick Start Guide

Get the cab price comparison automation running in 5 minutes!

## Prerequisites Checklist

- [ ] Android emulator running
- [ ] Uber, Ola, and Rapido apps installed and logged in
- [ ] Droidrun Portal accessibility service enabled
- [ ] Python 3.8+ installed
- [ ] OpenRouter API key (get free at [openrouter.ai/keys](https://openrouter.ai/keys))

## Installation (3 steps)

### Option A: Automated Setup (Recommended)

**Linux/Mac:**
```bash
./setup.sh
```

**Windows:**
```bash
setup.bat
```

Then edit `.env` and add your OpenRouter API key.

### Option B: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API key
cp .env.example .env
# Edit .env and add your OpenRouter API key
```

## Run It!

```bash
python cab_price_comparison.py
```

## What Happens

1. You enter pickup and drop locations
2. Script opens each cab app
3. Enters your locations automatically
4. Extracts prices from UI
5. Shows comparison results
6. Asks if you want to open the cheapest app

## Example Output

```
CAB PRICE COMPARISON AUTOMATION
==========================================================

Enter pickup location: Koramangala
Enter drop location: MG Road

✓ Pickup: Koramangala
✓ Drop: MG Road

Processing Uber...
✓ Uber Price: ₹250

Processing Ola...
✓ Ola Price: ₹235

Processing Rapido...
✓ Rapido Price: ₹210

PRICE COMPARISON RESULTS
==========================================================

  Uber       : ₹250.00
  Ola        : ₹235.00
  Rapido     : ₹210.00

----------------------------------------------------------
🎯 CHEAPEST OPTION: Rapido at ₹210.00
----------------------------------------------------------

Do you want me to open Rapido for you? (yes/no):
```

## Troubleshooting

### "OPENROUTER_API_KEY not found"
→ Create `.env` file and add your API key

### "Apps not launching"
→ Check if Droidrun Portal is enabled in Accessibility settings

### "All apps failed"
→ Ensure apps are logged in and emulator has internet

### Need more help?
See full [README.md](README.md) for detailed instructions.

## Important Notes

- Script NEVER auto-books rides
- You maintain full control
- Works only on emulator (not physical device)
- Requires stable internet connection
- Free tier model (z-ai/glm-4.5-air:free) used

## Next Steps

Once it works:
- Try different locations
- Check execution logs
- Experiment with different scenarios
- Read [README.md](README.md) for advanced configuration

---

**Need Help?** Check [Droidrun Documentation](https://droidrun.ai/docs)
