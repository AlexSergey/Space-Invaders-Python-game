import cx_Freeze
import _paths

GAME_PATH = "./"
BUILD_PATH = "../build"

executables = [cx_Freeze.Executable(
    script="{}/main.py".format(GAME_PATH),
    targetName="SpaceInvaders.exe",
    targetDir = BUILD_PATH,
    copyDependentFiles = True,
    icon = None
)]

included = [
    '{}/images/'.format(GAME_PATH),
    '{}/audio/'.format(GAME_PATH),
]

cx_Freeze.setup(
    name="my game",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": included,
            "build_exe": BUILD_PATH
        }
    },
    executables=executables
)