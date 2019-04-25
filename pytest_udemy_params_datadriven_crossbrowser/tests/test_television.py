from pytest import mark


# @mark.parametrize('tv_brand', [
#         'Samsung',
#         'Sony',
#         'Vizio'
#     ]
# )
# def test_television_turns_on(tv_brand):
#     print(f'{tv_brand} turns on as expected')


def test_television_turns_on(tv_brand):
    print(f'{tv_brand} turns on as expected')


@mark.skip
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://techstepacademy.com/training-ground')
