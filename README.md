# JenkinsCI
Demo of an initial Jenkins setup for continuous development of a simple python library. 

## Linux (Ubuntu)

1. Follow the steps exaplined [here](https://pkg.jenkins.io/debian-stable/) to install Jenkins on Ubuntu
2. I am using the following environment variable setup to avoid premission issues:
* export JENKINS_HOME=$HOME/.jenkins
* export JAVA_OPTS="-Djava.awt.headless=true -Djava.io.tmpdir=$JENKINS_HOME/tmp"
* export TMP=$JENKINS_HOME/tmp
* export TEMP=$JENKINS_HOME/tmp
* export TMPDIR=$JENKINS_HOME/tmp
3. Run jenkins --httpListenAddress=127.0.0.1 --httpPort=9051 --enable-future-java
* Use this URL localhost:9051 in your browser
4. On the initial run you will be prompted with an initial password in the CLI. Paste this one into the required field in your browser and follow additional steps (account setup, plugin-install etc.)
5. You may be required to restart Jenkins
6. Create a new freelance project with some descriptive name
7. In the source code management section add the git-repository of your project (I'm using https://github.com/MMilczynski/JenkinsCI.git).
8. My settings are polling every minute for triggering a new build (* * * * *)
9. I use the following shell script for the build steps:
![image](https://user-images.githubusercontent.com/44039388/159805647-8cce2e5c-cd53-46d2-a917-f57345d48cbb.png)
10. Install the Cobertura plugin in Jenkins
11. Add the following settings to the post-build steps
![image](https://user-images.githubusercontent.com/44039388/159805793-3fcba4f1-1763-44ca-ba65-eb49e8f09f5c.png)
12. Hit save.

