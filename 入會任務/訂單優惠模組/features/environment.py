import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def before_scenario(context, scenario):
    if 'skip' in scenario.tags:
        scenario.skip("Marked with @skip")
