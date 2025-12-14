import os
import re
from datetime import datetime

from utils.driver_factory import create_driver
from utils.config import SCREENSHOTS_DIR

FAIL_STATUSES = {"failed", "error"}

def safe_name(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]+', "_", name)

def before_scenario(context, scenario):
    context.driver = create_driver()

def after_scenario(context, scenario):
    status = scenario.status.name.lower()
    if status in FAIL_STATUSES:
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{ts}_{safe_name(scenario.name)[:120]}.png"
        path = os.path.join(SCREENSHOTS_DIR, filename)
        context.driver.save_screenshot(path)
    context.driver.quit()