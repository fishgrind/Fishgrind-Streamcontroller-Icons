import os
import sh
import shutil
import codecs
import cairo

if __name__ == "__main__":
    if not os.path.exists("tabler-icons/"):         # Check if the GitHub repo is not there
        print("Downloading GitHub repository...")
        sh.git.clone("https://github.com/tabler/tabler-icons")

    # Delete and create "icons" directory
    if os.path.exists("icons/"):
        shutil.rmtree("icons/")

    os.mkdir("icons")
    os.mkdir("icons/black")
    os.mkdir("icons/white")

    # Find every icon
    for root, dirs, files in os.walk("tabler-icons/icons"):
        for file in files:
            if file.endswith(".svg"):
                icon = os.path.join(root, file)
                newFile = os.path.splitext(file)[0] + "-" + os.path.basename(root) + os.path.splitext(file)[1]

                # Copy icon
                shutil.copyfile(icon, "icons/black/" + newFile)

                # Open icon
                with codecs.open(icon, encoding="utf-8", errors="ignore") as svg:
                    content = svg.read()

                    # Fill with white
                    if os.path.basename(root) == "filled":
                        white_icon_text = content.replace('fill="currentColor"', 'fill="white"')
                    else:
                        white_icon_text = content.replace('stroke="currentColor"', 'stroke="white"')
                    white_icon = open("icons/white/" + newFile, "w")
                    white_icon.write(white_icon_text)
                    white_icon.close()
shutil.rmtree("tabler-icons/")