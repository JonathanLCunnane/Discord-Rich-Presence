from pypresence import Presence


# Before using this script, make sure to read the README.md file. 
# For each of the presets, type the number for which preset you want when running the script


def preset_1(controller: Presence):
    controller.update(
        state="", # This will be displayed on the third line underneath your application name. The user's current status.
        details="", # This will be displayed on the second line underneath your application name. What the user is currently doing.
        large_image="", # Pretty self-explanatory. This is the asset ID for the large image you want on your profile message
        large_text="", # The tooltip for the large image.
        small_image="", # The asset ID for the small image on the bottom right of the large image.
        small_text="", # The tooltip for the small image.
        buttons=[
            {
                "label": "", # first button label here
                "url": "", # the url redirect for the button
                "disabled": "", # bool "true" or "false"
            },
            {
                "label": "", # first button label here
                "url": "", # the url redirect for the button
                "disabled": "", # bool "true" or "false"
            }
        ]
    )


def preset_2(controller: Presence):
    controller.update(
        state="", # This will be displayed on the third line underneath your application name. The user's current status.
        details="", # This will be displayed on the second line underneath your application name. What the user is currently doing.
        large_image="", # Pretty self-explanatory. This is the asset ID for the large image you want on your profile message
        large_text="", # The tooltip for the large image.
        small_image="", # The asset ID for the small image on the bottom right of the large image.
        small_text="", # The tooltip for the small image.
        buttons=[
            {
                "label": "", # first button label here
                "url": "", # the url redirect for the button
                "disabled": "", # bool "true" or "false"
            },
            {
                "label": "", # first button label here
                "url": "", # the url redirect for the button
                "disabled": "", # bool "true" or "false"
            }
        ]
    )


def preset_3(controller: Presence):
    controller.update(
        state="", # This will be displayed on the third line underneath your application name. The user's current status.
        details="", # This will be displayed on the second line underneath your application name. What the user is currently doing.
        large_image="", # Pretty self-explanatory. This is the asset ID for the large image you want on your profile message
        large_text="", # The tooltip for the large image.
        small_image="", # The asset ID for the small image on the bottom right of the large image.
        small_text="", # The tooltip for the small image.
        buttons=[
            {
                "label": "", # first button label here
                "url": "", # the url redirect for the button
                "disabled": "", # bool "true" or "false"
            },
            {
                "label": "", # first button label here
                "url": "", # the url redirect for the button
                "disabled": "", # bool "true" or "false"
            }
        ]
    )


controller = Presence("0123456789012345678") # <- PASTE CLIENT ID HERE
controller.connect()
while True:
    try:
        try:
            preset_num = int(input("Enter the preset number between 1 and 3: "))
            if preset_num == 1:
                preset_1(controller)
            elif preset_num == 2:
                preset_2(controller)
            elif preset_num == 3:
                preset_3(controller)
            else:
                print("Make sure to enter an integer between 1 and 3!")
        except ValueError:
            print("Make sure to enter an integer!")
    except KeyboardInterrupt:
        print("\nQuitting...")
        quit()
