from cx_Freeze import setup, Executable
# this is to give cx_Freeze the basic configuration of your app
setup(

    name="CheckFaceRecog",

    version="1.0",

    description="Checking Face Recognition",

    executables=[Executable("checking_face_recog.py")],

)