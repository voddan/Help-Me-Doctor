init python:
    import enviroment



define e = Character("Eileen")
define user_name = enviroment.user_id


# The game starts here.

label start:

    scene bg road
    show eileen happy


    e "You've created a new Ren'Py game."

    e "user: [user_name]"

    e "Once you add a story, pictures, and music, you can release it to the world!"


    return
