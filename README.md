# proAnno: Annotation Tool

[![website](https://img.shields.io/badge/Website-Explore%20Now-blueviolet?style=flat&logo=google-chrome)](https://traffix-dataset.github.io/)
<!-- [![paper](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)]() -->
<!-- [![supplement](https://img.shields.io/badge/Supplementary-Material-red)]() -->
<!-- [![video](https://img.shields.io/badge/Video-Presentation-F9D371)]() -->

This is the implementation of the proAnno labeling tool presented in the paper "TraffiX - A V2X Dataset for Multi-Modal Cooperative 3D Object Detection of Traffic Participants Using Onboard and Roadside Sensors".

<!-- TODO : insert image -->

## Overview
- [Features](#features)
- [Data Download](#data-download)
- [Quick Start](#quick-start)

## Features
<!-- TODO -->

## Data Download
Download the Traffix dataset from the following [link](TODO). The data should structured in the following format after downloading:
<!-- ![OVERVIEW](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/input_structure.png) -->
<!-- TODO : Fill in the correct format -->
```shell
├── Traffix
│   ├── drive_42_west_to_east
|      |── images
|      |── point clouds
│   ├── xxx
│   ├── xxx
```
Move the dataset into the `proanno/input` folder.


## Quick Start

### First install the required packages. 

#### 1. Install npm
   + Linux: `sudo apt-get install npm`
   + Windows: https://nodejs.org/dist/v10.15.0/node-v10.15.0-x86.msi
   + Mac: https://blog.teamtreehouse.com/install-node-js-npm-mac

#### 2. Clone repository and open it:
```shell
git clone https://github.com/traffix-dataset/proanno.git & cd proAnno
```
#### 3. Install required python packages: 
```shell
pip install -r requirements.txt
```
#### 4. Install required packages: 
```shell
npm install
```

### Start the labeling tool by running the following commands
#### 1. Run the `resize_images.py` script to resize the images by half.
```shell
python scripts/resize_images.py\
    --input_folder_path_drive ./input/Traffix/drive_42_west_to_east
```
<!-- TODO check if paths are correct -->
#### 2. Run the `create_file_name_list.py` script to create a file name list for the images, point clouds and annotations.
```shell
python scripts/create_file_name_list.py\
    --input_folder_path_drive ./input/Traffix/drive_42_west_to_east
```

#### 3.  Update the configuration file `config/config.json`
1.  set the default sequence for annotation, 
    ```
         "default_sequence": "drive_42_west_to_east",
    ```
2. Extend the sequence array with the new sequence that you want to annotate:
   ```
   {
          "name": "drive_42_west_to_east",
          "num_frames": 100,
          "default_weather_type": "SUNNY"
   }
   ```

#### 4.  Start the backend-server 
```shell
npm run start-server
```
#### 5. Start the applications 
```shell
npm run start
```
#### 6. The `index.html` file should open now. 
If not, open the [index.html](./src/application/index.html) file in the 'src/application' folder with chromium based browser.

### Data annotation

Instruction and commands for data annotation can be found [here](./Commands.md)

<!-- TODO : Insert video -->

### Load HD map

<!-- TODO : Insert picture -->

It is possible to load HD map for visual support.

1. Add a `input/Traffix/hdmap/resources/` folder.
2. Add  `world.obj` and corresponding resources (`world.mtl`, textures, etc.) to the folder
3. To adjust the position or rotation of the HD Map add a `transform.json` file with the following structure:
```
{
  "position": {
    "x": 0,
    "y": 0,
    "z": 0
  },
  "rotation": {
    "x": 0,
    "y": 0,
    "z": 0
  }
}
```

## Traffix annotation

The annotation procedure used for "Traffix - V2X dataset" is described in the paper. Further instructions which were given to the annotators is listed in [this document](./Instructions.md) 
