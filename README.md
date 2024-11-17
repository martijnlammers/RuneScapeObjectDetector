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
| `target_path` | string | Valid relative or absolute path to .png. This image will be attempted to be located. | 
| `confidence` | float | Value between 0.1 and 1. Lower means it will be less strict with finding exact pixels, but this also results in worse accuracy. | 
| `frame_path` | string | Valid relative or absolute path to .png. This image will be attempted to be located. | 
| `confidence` | float | Value between 0.1 and 1. Lower means it will be less strict with finding exact pixels, but this also results in worse accuracy. | 


## Conventions 
Style: https://peps.python.org/pep-0008/