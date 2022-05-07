# This is a sample Python script.
import flask_app
import data.data_controller as data_controller
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
comment format

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    item_interface = data_controller.get_item_interface()
    item_interface.get_items()
    flask_app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
