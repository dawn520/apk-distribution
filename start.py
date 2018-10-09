import sys, os, shutil, zipfile, time

apkVersion = "1.0"
srcFileName = "source.apk"
destDir = os.path.abspath('.')
file = open("channel.txt")


def writeChannelToApk(filename, channel):
    z = zipfile.ZipFile(filename, 'a', zipfile.ZIP_DEFLATED)
    empty_channel_file = "META-INF/channel_{channe}".format(channe=channel)
    target_file = "channel.apk"
    z.write(target_file, empty_channel_file)
    z.close()
    print
    "writeChannelToApkchannel" + channel + "," + filename + "\n"


def cpFile(srcPath, fileName):
    destPath = destDir + os.path.sep + fileName
    if os.path.exists(srcPath) and not os.path.exists(destPath):
        shutil.copy(srcPath, destPath)


if not os.path.exists(srcFileName):
    print
    "sourcefile" + srcFileName + "notexists"
    sys.exit(1)

start = time.clock()

for line in file:
    channel = line.strip('\n').strip()
    targetFileName = "apk_" + channel + "-" + apkVersion + ".apk"
    print
    "copyfile:" + targetFileName
    cpFile(srcFileName, targetFileName)
    writeChannelToApk(targetFileName, channel)
end = time.clock()

print("The function run time is : %.03f seconds" % (end - start))
