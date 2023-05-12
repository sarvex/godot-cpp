import os


def options(opts):
    opts.Add("osxcross_sdk", "OSXCross SDK version", "darwin16")


def exists(env):
    return "OSXCROSS_ROOT" in os.environ


def generate(env):
    root = os.environ.get("OSXCROSS_ROOT", "")
    if env["arch"] == "arm64":
        basecmd = f"{root}/target/bin/arm64-apple-" + env["osxcross_sdk"] + "-"
    else:
        basecmd = f"{root}/target/bin/x86_64-apple-" + env["osxcross_sdk"] + "-"

    env["CC"] = f"{basecmd}clang"
    env["CXX"] = f"{basecmd}clang++"
    env["AR"] = f"{basecmd}ar"
    env["RANLIB"] = f"{basecmd}ranlib"
    env["AS"] = f"{basecmd}as"

    binpath = os.path.join(root, "target", "bin")
    if binpath not in env["ENV"]["PATH"]:
        # Add OSXCROSS bin folder to PATH (required for linking).
        env["ENV"]["PATH"] = f'{binpath}:{env["ENV"]["PATH"]}'
