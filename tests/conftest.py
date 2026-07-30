from copy import deepcopy

import pytest

import src.app as app_module


BASELINE_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities.clear()
    app_module.activities.update(deepcopy(BASELINE_ACTIVITIES))

    yield

    app_module.activities.clear()
    app_module.activities.update(deepcopy(BASELINE_ACTIVITIES))
