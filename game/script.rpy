init python:
    import enviroment

    # user_info = renpy.fetch("https://itch.io/api/1/me/me", result="text")
    # user_id = user_info#.get("id")



define e = Character("Eileen")
define user_name = enviroment.user_id


# The game starts here.

label start:

    scene bg road
    show eileen happy


    e "You've created a new Ren'Py game."

    # e "user: [user_name]; id: [user_id]; info: [user_info]"

    e "Once you add a story, pictures, and music, you can release it to the world!"


    return
