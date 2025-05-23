import subprocess
import datetime

Import("env")

def get_firmware_specifier_build_flag():
    try:
        ret = subprocess.run(
            ["git", "describe", "--tags", "--dirty", "--exclude", "nightly"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, # Suppress error output
            text=True,
            check=True # Raise CalledProcessError if git command fails
        )
        build_version = ret.stdout.strip()
    except subprocess.CalledProcessError:
        build_version = "local"
    build_flag = f'-D BUILD_GIT_VERSION=\\"{build_version}\\"'
    print("Build version:", build_version)
    return (build_flag)

def get_time_specifier_build_flag():
    build_timestamp = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    build_flag = "-D BUILD_TIMESTAMP=\\\"" + build_timestamp + "\\\""
    print ("Build date: " + build_timestamp)
    return (build_flag)

env.Append(
    BUILD_FLAGS=[get_firmware_specifier_build_flag(), get_time_specifier_build_flag()]
)
