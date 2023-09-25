**<p style="text-align: center;">Short manual how to setup Appium test environment</p>**

1. [OpenJDK](https://aka.ms/download-jdk/microsoft-jdk-17.0.7-windows-x64.msi)  in C:\Program%20Files\Microsoft\jdk-17.0.7.7-hotspot directory<br/><br/>
2. Install [NodeJS](https://nodejs.org/dist/v18.16.0/node-v18.16.0-x64.msi) 
   - Appium: npm i -g appium@next
   - appium driver install uiautomator2<br/><br/>
3. Android Studio (!!! note the C:\[AndroidSDK] installation path])<br/><br/>
4. to create PATH:
   - 'environment variables' in 'Search' -> Advanced tab -> Environment Variables<br/><br/>
5. System Variables -> New:
   - JAVA_HOME (C:\Program Files\Microsoft\jdk-17.0.7.7-hotspot)
   - ANDROID_HOME (C:\[AndroidSDK] installation path])<br/><br/>
6. System Variables -> Path -> Edit -> New:
   - %ANDROID_HOME%\emulator
   - %ANDROID_HOME%\platform-tools
   - %ANDROID_HOME%\tools
   - %ANDROID_HOME%\tools\bin<br/><br/>
7. Pycharm:
   - create new project - menu File -> Settings -> Project: \<name\> 
   - install packages: Appium-Python-Client, uiautomator2<br/><br/>

**[Appium documentation](https://appium.io/docs/en/2.1/quickstart/)**

*Will be useful after installing the basic elements:*
1. [appium-doctor](https://www.npmjs.com/package/appium-doctor)<br/>using command: npm install appium-doctor -g
2. [appium-inspector](https://github.com/appium/appium-inspector/releases) 
