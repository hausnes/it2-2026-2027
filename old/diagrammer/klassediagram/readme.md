# Online Version of PlatinumUML
[PlantUML Online](http://www.plantuml.com/plantuml/uml/)

# Local Installation (see links in Smidig IT-2)
We will use PlantUML, which can be installed as an extension in VS Code. For it to work, we also need to install Java and Graphviz. We can manage without Graphviz, as it can be a bit tricky to install on Mac. Instead, we can use Smetana, which is built into PlantUML and specified with `!pragma layout smetana` in the code. The links are on the PlantUML page in VS Code. Watch these three videos to get started with PlantUML:
1. [Using PlantUML in VSCode (6 min)](https://youtu.be/xkwJ9GwgZJU)
2. [PlantUML - beautiful quick diagrams to explain your models (16 min)](https://www.youtube.com/watch?v=EM-cvRubP4g)
3. [PlantUML with Domain Models (class diagrams) (10 min)](https://youtu.be/46m3_03uzfw)

More information can be found on the PlantUML website, and here is an [instruction book](https://www.plantuml.com/book) that might be useful.

# From [PlantUML Starting Guide](https://plantuml.com/starting)
## Local Installation Procedure
After trying the online version, if you're considering a more comprehensive local environment, a local installation of PlantUML is suggested. Before installation, ensure the following prerequisites are met:

### Java
PlantUML requires Java to be installed on your machine.
- Check if Java is already installed: `java -version`. The minimum version needed is Java 8.
- If not installed, download and install it from the official [Java website](https://www.java.com) or through package managers like `apt` for Ubuntu, `brew` for macOS, etc.

### Graphviz
Needed only for some diagrams.
- **Linux**: You'll find more information [here](https://graphviz.org/download/) about Graphviz installation.
- **Windows**: A compiled version of Graphviz is embedded within PlantUML, eliminating the need for a separate installation. However, if needed, you can acquire a standalone version [here](https://graphviz.org/download/).

Once ready, download the `plantuml.jar` file and execute it to access PlantUML’s graphical user interface. No further unpacking or installation procedures are needed.

# Note
My experience with the installation was that I had problems with PATH, even though it worked in both terminal and CMD in Windows. To set this in VS Code, I opened `settings.json` and added:

```json
"terminal.integrated.env.windows": {
    "PATH": "C:\\Program Files\\Java\\jre1.8.0_431\\bin;${env:PATH}"
}
```

I did not need the plantuml.jar-file, but it worked for testing (automatically exporting from the watch-folder).