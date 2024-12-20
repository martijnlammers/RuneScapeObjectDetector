## Environment: 
* Microsoft Windows 11 Version 24H2 (OS Build 26100.2033)
* Python 3.9.13 (64-bits)
* OpenCV 4.10.0.84


## Target Capture: 
Before making a screenshot in RuneScape we need to standardize the camera view to effectively
locate targets.

* Zoom out camera max.
* Reset the camera by pressing the compass.

    ![image](/res/compass.png)



## Configurations
To configure the app, change values in `detector_config.json` in the root of 
the repository.

| Name | Type | Description |
|---|---|---|
| `frame_path` | string | Path to .png used as searching grounds. | 
| `target_path` | string | Path to target .png. | 
| `confidence` | float | Value between 0.1 and 1. Lower means it will be less strict with finding exact pixels, but this also results in worse accuracy. |
| `debug` | boolean | Used to enable debug functionalities of the app. | 


## Conventions 
Style: https://peps.python.org/pep-0008/