import os
import sys
import asyncio
from typing import Dict, Optional
from droidrun import DroidAgent, DroidrunConfig
from dotenv import load_dotenv
from colorama import Fore, Style, init

init(autoreset=True)
load_dotenv()

#UI
def banner():
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + r"""
██████╗ ██╗██████╗ ███████╗    ███████╗ ██████╗ ██████╗ ██╗   ██╗████████╗
██╔══██╗██║██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔═══██╗██║   ██║╚══██╔══╝
██████╔╝██║██║  ██║█████╗      ███████╗██║     ██║   ██║██║   ██║   ██║   
██╔══██╗██║██║  ██║██╔══╝      ╚════██║██║     ██║   ██║██║   ██║   ██║   
██║  ██║██║██████╔╝███████╗    ███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝    ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   
"""
    )


def section(title: str):
    print(Fore.MAGENTA + Style.BRIGHT + f"\n━━━━━━ {title.upper()} ━━━━━━\n")


def ok(msg: str):
    print(Fore.GREEN + "✔ " + msg)


def fail(msg: str):
    print(Fore.RED + "✖ " + msg)

#CORE
class CabPriceComparator:
    def __init__(self):
        self.config = self._load_config()
        self.apps = ["Uber", "Ola", "Rapido"]
        self.results: Dict[str, Optional[float]] = {}
        self.pickup = ""
        self.drop = ""

    def _load_config(self):
        if not os.getenv("OPENROUTER_API_KEY"):
            fail("OPENROUTER_API_KEY missing")
            sys.exit(1)

        return DroidrunConfig.from_yaml(
            "C:/Users/Indraneel Bose/Cab_Scout/config.yaml"
        )

    def get_input(self):
        banner()
        section("Input")

        self.pickup = input(Fore.YELLOW + "Pickup location : ").strip()
        self.drop = input(Fore.YELLOW + "Drop location   : ").strip()

        ok(f"Pickup → {self.pickup}")
        ok(f"Drop   → {self.drop}")

    async def check_app(self, app: str) -> Optional[float]:
        section(app)

        goal = f"""
You are controlling an Android emulator.

ABSOLUTE RULES:
- Output ONLY valid Python code
- NO markdown, NO explanations
- Do NOT click random buttons
- Do NOT click time, rider, offers, parcel, schedule, or banners

Allowed functions:
click(index)
type(text, index=None, clear=True)
wait(seconds)
complete(success=True, reason="...")
complete(success=False, reason="...")

CRITICAL CLICK FILTER:
ONLY click elements whose visible text contains:
- pickup
- drop
- location
- where to
- search

NEVER click elements containing:
- pickup now
- for me
- schedule
- parcel
- offer
- promo
- rider

TASK:
1. Open "{app}" or "{app} Lite".
2. Locate pickup input field using the click filter above.
3. Type "{self.pickup}".
4. Choose the MOST RELEVANT suggestion
   (Metro / Station / exact match preferred over distance).
5. Locate drop input field using the same filter.
6. Type "{self.drop}".
7. Choose the MOST RELEVANT suggestion.
8. Wait for ride list.

RIDE FILTER:
VALID:
- Bike
- Cab / Taxi / Mini / Prime / Auto

INVALID (IGNORE COMPLETELY):
- Parcel
- Courier
- Delivery

PRICE RULE:
- If Bike visible → choose Bike
- Else → choose cheapest Cab

Finish with:
complete(success=True, reason="PRICE: <number>")

FAILURE:
If pickup or drop input cannot be found:
complete(success=False, reason="INPUT_FIELD_NOT_FOUND")
"""

        agent = DroidAgent(goal=goal, config=self.config)
        result = await agent.run()

        if not result.success:
            fail(f"{app} failed → {result.reason}")
            return None

        price = self._extract_price(result.reason or "")
        if price is None:
            fail(f"{app} price not extracted")
            return None

        ok(f"{app} price ₹{price}")
        return price

    def _extract_price(self, text: str) -> Optional[float]:
        import re
        m = re.search(r"PRICE:\s*(\d+(?:\.\d+)?)", text)
        return float(m.group(1)) if m else None

    async def run_all(self):
        section("Scanning")
        for app in self.apps:
            self.results[app] = await self.check_app(app)
            await asyncio.sleep(2)

    def show_results(self):
        section("Results")

        valid = {k: v for k, v in self.results.items() if v}
        for app, price in self.results.items():
            if price:
                print(Fore.CYAN + f"{app:10}: ₹{price:.2f}")
            else:
                fail(f"{app:10}: FAILED")

        if not valid:
            fail("No valid rides found")
            return

        cheapest = min(valid, key=valid.get)
        print(
            Fore.GREEN
            + Style.BRIGHT
            + f"\nCHEAPEST → {cheapest} @ ₹{valid[cheapest]:.2f}"
        )

    async def run(self):
        self.get_input()
        await self.run_all()
        self.show_results()
        section("Done")
        ok("Ride Scout completed successfully")


def main():
    asyncio.run(CabPriceComparator().run())


if __name__ == "__main__":
    main()
