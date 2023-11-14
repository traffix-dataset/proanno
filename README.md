# proAnno: 3D Annotation Tool

# Installation
1. Clone repository: `git clone https://github.com/traffix-dataset/proanno.git`
2. Install npm
   + Linux: `sudo apt-get install npm`
   + Windows: https://nodejs.org/dist/v10.15.0/node-v10.15.0-x86.msi
   + Mac: https://blog.teamtreehouse.com/install-node-js-npm-mac
4. Open folder `proanno` in e.g. WebStorm.
5. Move into directory: `cd proAnno`.
6. Move images and point clouds into the `input/Traffix/drive_42_west_to_east/` folder.
The structure should look like this:
  ![OVERVIEW](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/input_structure.png)
7. Install required python packages: `pip install -r requirements.txt`
8. Run the `resize_images.py` script to resize the images by half.
9. Run the `create_file_name_list.py` script to create a file name list for the images, point clouds and annotations.
10. Open the configuration file config/config.json and set the default sequence for annotation, e.g.
   ```
         "default_sequence": "drive_42_west_to_east",
   ```
   Extend the sequence array inside the config/config.json file with the new sequence that you want to annotate. Add e.g. the following entry to the end of the array:
   ```
   ,{
          "name": "drive_42_west_to_east",
          "num_frames": 100,
          "default_weather_type": "SUNNY"
   }
   ```
   Also set the number of frames, and the default weather type for that sequence.
11. Install required packages: `npm install`
12. Install python and pip. Then run `pip install -r requirements.txt` to install the python dependencies.
13. Start the backend-server with `npm run start-server` and the applications with `npm run start`
14. Open `index.html` with chromium-browser (Linux) or Chrome (Windows) within the IDE. Right click on index.html -> Open in Browser -> Chrome/Chromium

### Load HD map

It is possible to load HD map for visual support.

1. Add a `input/Traffix/hdmap/resources/` folder.
2. Add  `world.obj` and corresponding resources (`world.mtl`, textures, etc.) to the folder
3. To adjust the position or rotation of the hdmap add a `transform.json` file with the following structure:
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

# 3D Bounding Box Labeling Instructions
1. Hold Down the Ctrl key and draw 2D bounding box in the drawing area (below the camera image). A 3D bounding box will be generated automatically with default vehicle size. If the box contains more than 10 points, the rotation, scale and position of the object will be automatically predicted and adjusted.
2. Move/Scale the 3D bounding box using the red, green and blue arrow (drag and drop) or use the blue sliders in the side menu.
3. Choose one of the available classes in the bottom left corner (Car, Pedestrian, Bicycle, Motorcycle, Truck, Van, Bus, Trailer, Special_Vehicle)
4. Repeat steps 1-3 for all objects in the sequence
5. Download 2D and 3D labels, as well as projected 3D labels to your computer (as zip archive)

# Annotation tips & tricks
#### 1. Interpolation of objects (available in sequence mode)
  1. Select object to interpolate by clicking on a bounding box
  2. Activate 'Interpolation Mode' in the menu (checkbox) -> start position will be saved
  3. Move to desired frame by skipping x frames
  4. Translate object to new position
  5. Click on the 'Interpolate' button in the menu

#### 2. Grid view
  1. Activate the grid in the side menu for better orientation

#### 3. 3D View
  1. Switch into 3D view to review your annotations and check for correct orientation

#### 4. Use keyboard short cuts (WIP)
| Key | Description   |
| --- | ------------- |
|       ![V](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/c.png)  | Toggle view (3D view/Bird's-Eye-View)|
|       ![W](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/w.png)  | Move forward in 3D view|
|       ![A](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/a.png)  | Move left in 3D view|
|       ![S](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/s.png)  | Move backward in 3D view|
|       ![D](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/d.png)  | Move right in 3D view|
|       ![Q](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/q.png)  | Move down in 3D view|
|       ![E](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/e.png)  | Move up in 3D view|
|       ![LEFT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/left.png) | Rotate camera counter-clock-wise |
|       ![RIGHT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/right.png)| Rotate camera clock-wise |
|       ![UP](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/up.png) | Rotate camera up |
|       ![DOWN](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/down.png)| Rotate camera down |
|       ![C](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/c.png)  | Enlarge camera image|
|       ![N](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/n.png)  | Next frame     |
|       ![P](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/p.png)  | Previous frame   |
|       ![I](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/i.png)  | Interpolate    |
|       ![CTRL](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/ctrl.png)![MOUSELEFT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/mouseleft.png) | Snap to grid in 0.5m steps (floor alignment mode)  |
|       ![CTRL](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/ctrl.png)![T](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/t.png)  | Enable/Disable Translation mode|
|       ![W](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/w.png)  | Move selected object forward (Y++)|
|       ![A](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/a.png)  | Move selected object to left (X--)|
|       ![S](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/s.png)  | Move selected object backward (Y--)|
|       ![D](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/d.png)  | Move selected object to right (X++)|
|       ![Q](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/q.png)  | Move selected object down (Z--)|
|       ![E](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/e.png)  | Move selected object up (Z++)|
|       ![CTRL](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/ctrl.png)![R](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/r.png)  | Enable/Disable Rotation mode|
|       ![Q](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/q.png) | Rotate selected object counter-clock-wise|
|       ![E](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/e.png)  | Rotate selected object clock-wise|
|       ![CTRL](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/ctrl.png)![S](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/s.png)  | Enable/Disable Scaling mode |
|      ![W](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/w.png) | Increase length along longitudinal axis (y-axis)  |
|      ![S](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/s.png) | Decrease length along longitudinal axis (y-axis)  |
|      ![A](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/a.png)  | Decrease width along lateral axis (x-axis) |
|      ![D](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/d.png)  | Increase width along lateral axis (x-axis) |
|      ![E](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/e.png)! | Increase height along vertical axis (z-axis) |
|      ![Q](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/q.png)! | Decrease height along vertical axis (z-axis) |
|  ![PLUS](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/plus.png)  | Increase arrow size |
|  ![MINUS](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/minus.png)  | Decrease arrow size |
|  ![X](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/x.png)  | Show/Hide X-axis |
|  ![Y](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/y.png)  | Show/Hide Y-axis |
|  ![Z](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/z.png)  | Show/Hide Z-axis (only in 3D mode)|
|  ![SPACE](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/space.png)  | Switch between different operation modes (translate, rotate, scale) |
|  ![TAB](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/tab.png)  | Select next object |
| ![DEL](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/del.png) OR ![BACKSPACE](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/backspace.png) | Delete selected object |
|  ![M](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/m.png)  | Marking mode (TODO)|
|  ![ONE](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/1.png)  | Select class CAR |
|  ![TWO](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/2.png)  | Select class Truck |
|  ![THREE](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/3.png)  | Select class Trailer |
|  ![FOUR](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/4.png)  | Select class Van |
|  ![FIVE](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/5.png)  | Select class Motorcycle |
|  ![SIX](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/6.png)  | Select class Bus |
|  ![SEVEN](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/7.png)  | Select class Pedestrian |
|  ![EIGHT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/8.png)  | Select class Bicycle |
|  ![NINE](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/9.png)  | Select class Special_Vehicle |
| ![MOUSELEFT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/mouseleft.png) | On a 2D/3D object: Show bounding box|
|            | On a camera image: Enlarge/Shrink camera image (TODO)|
|            | On ego vehicle: Show field-of-view (TODO)|
| ![LEFT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/left.png)![RIGHT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/right.png): | Switch FOV to next channel|
| ![R](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/r.png)| Reset all selected bounding boxes (TODO)|
| ![F11](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/f11.png) | Full Screen Mode|
| ![P](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/p.png) | Play video (TODO)||
| ![K](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/k.png) | Keyboard navigation (only in 3D view) (TODO)|
| ![L](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/l.png) | Toggle Lighting (TODO)|
| ![L](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/l.png)![ONE](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/1.png) | Label random color (TODO)|
| ![L](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/l.png)![TWO](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/2.png) | Label class color (TODO)|
| ![T](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/t.png) | Show/Hide trajectory (TODO)|
| ![SHIFT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/shift.png)![D](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/d.png)| Download annotation file (TODO)|
| ![CTRL](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/ctrl.png)![Z](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/z.png)| Undo operation |
| ![CTRL](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/ctrl.png)![Y](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/y.png)| Redo operation (TODO)|
| ![G](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/g.png) | Show/Hide grid (TODO)|
| ![J](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/j.png) | Hide all labels except selected object (Press again to show all labels) (TODO)|
| ![QUESTIONMARK](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/questionmark.png) | Show keyboard shortcuts|
| ![ESC](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/esc.png) | Unselect box |
| ![CTRL](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/ctrl.png)![W](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/w.png)| Close tab (exit)|
|                                                                                                                               | Quit fullscreen cam image (TODO)|
| ![ALT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/alt.png)![MOUSELEFT](https://github.com/traffix-dataset/proanno/blob/master/assets/textures/keyboard_small/mouseleft.png) | Copy bounding box (by dragging) (TODO)|

Hints:
+ Select `Copy label to next frame` checkbox if you want to keep the label (position, size, class) for next frame
+ Use helper views (available in point cloud mode) to align object along z-axis (no need to switch into 3D view)
+ Label one object from start to end (using interpolation) and then continue with next object (available in sequence mode)
+ **Do not** apply more than one box to a single object. If there is a truck with a trailer, then put two boxes (one box for Truck and another one for Trailer). Both boxes should overlap.
+ The program has been quite stable in my use cases, but there is no guarantee that it won't crash. So please back up (download) your annotated scenes regularly.
+ Download the annotation file into the following folder: `proAnno/input/<DATASET>/<SEQUENCE>/annotations`
+ Please write me an e-mail for questions and bug reports. Thanks!

# Special Rules
+ **Extremities** :
    + **If** an object has extremities (eg. arms and legs of pedestrians), **then** the bounding box should include the extremities.
    + **Exception**: Do not include vehicle side view mirrors. Also, do not include other vehicle extremities (crane arms etc.) that are above 1.5 meters high.
+ **Carried Object** :
    + If a pedestrian is carrying an object (bag, umbrella, tools etc.), such objects will be included in the bounding box for the pedestrian. If two or more pedestrians are carrying the same object, the bounding box of only one of them will include the object.

# Labels
**For every bounding box, include one of the following labels:**
1. **[Car](#car)**: Vehicle designed primarily for personal use, e.g. sedans, hatch-backs, wagons, vans, mini-vans, SUVs, jeeps and pickup trucks (a pickup truck is a light duty truck with an enclosed cab and an open or closed cargo area; a pickup truck can be intended primarily for hauling cargo or for personal use).

![CAR](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/car.png)

2. **[Truck](#truck)**: Vehicles primarily designed to haul cargo including lorrys, trucks.

Delivery Truck:

![TRUCK](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/truck.png)

Pickup Truck:

![PICKUP_TRUCK](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/pickup_truck.png)

3. **[Trailer](#trailer)**: A trailer of type container/box/dump/vehicle_transporter/mixer/tank/flat_bed/other.

Trailer Type: Container

![TRAILER_CONTAINER](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/trailer_container.png)

Trailer Type: Box

![TRAILER_BOX](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/trailer_box.png)

Trailer Type: Dump

![TRAILER_DUMP](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/trailer_dump.png)

Trailer Type: Vehicle Transport

![TRAILER_VEHICLE_TRANSPORT](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/trailer_vehicle_transport.png)

Trailer Type: Mixer

![TRAILER_MIXER](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/trailer_mixer.png)

Trailer Type: Tank

![TRAILER_TANK](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/trailer_tank.png)

Trailer Type: Flatbed

![TRAILER_FLATBED](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/trailer_flatbed.png)

Trailer Type: Other

![TRAILER_OTHER](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/trailer_other.png)

4. **[Van](#van)**: Vans designed primarily for transporting something.

Van - Example 1:

![VAN_1](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/van1.png)

Van - Example 2:

![VAN_2](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/van2.png)

Van - Example 3:

![VAN_3](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/van3.png)

5. **[Motorcycle](#motorcycle)**: Gasoline or electric powered 2-wheeled vehicle designed to move rapidly (at the speed of standard cars) on the road surface. This category includes all motorcycles, vespas and scooters. It also includes light 3-wheel vehicles, often with a light plastic roof and open on the sides, that tend to be common in Asia (rickshaws). If there is a rider and/or passenger, include them in the box and set the attribute "with_rider".

Motorcycle Type: Motorbike

![MOTORCYCLE_MOTORBIKE](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/motorcycle_motorbike.png)

Motorcycle Type: Scooter

![MOTORCYCLE_SCOOTER](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/motorcycle_scooter.png)

6. **[Bus](#bus)**: Vehicles transporting more than 10 people.

Bus Type: Rigid

![BUS_RIGID](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/bus_rigid.png)

Bus Type: Bendy

![BUS_BENDY](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/bus_bendy.png)

7. **[Pedestrian](#pedestrian)**: An adult/child pedestrian moving around the cityscape. Mannequins should also be annotated as `Pedestrian`.

![PEDESTRIAN](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/pedestrian.png)

8. **[Bicycle](#bicycle)**: Human or electric powered 2-wheeled vehicle designed to travel at lower speeds either on road surface, sidewalks or bicycle paths. If there is a rider and/or passenger, include them in the box.

Bicycle - without rider:

![BICYCLE_WITHOUT_RIDER](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/bicycle_without_rider.png)

Bicycle - with rider:

![BICYCLE_WITH_RIDER](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/bicycle_with_rider.png)

9. **[Special_vehicle](#specialvehicle)**: A special vehicle (e.g. police car, ambulance, fire truck or tractor etc).

Special vehicle - Ambulance:

![SPECIAL_VEHICLE_AMBULANCE](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/special_vehicle_ambulance.png)

Special vehicle - Ambulance (with attribute flashing lights:

![SPECIAL_VEHICLE_AMBULANCE_FLASHING_LIGHTS](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/special_vehicle_ambulance_flashing_lights.png)

Special vehicle - Police vehicle:

![SPECIAL_VEHICLE_POLICE_VEHICLE](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/special_vehicle_police_vehicle.png)

Special vehicle - Police vehicle (with attribute flashing lights):

![SPECIAL_VEHICLE_POLICE_VEHICLE_FLASHING_LIGHTS](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/special_vehicle_police_vehicle_flashing_lights.png)

Special vehicle - Firetruck:

![SPECIAL_VEHICLE_FIRETRUCK](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/special_vehicle_firetruck.png)

Special vehicle - Firetruck (with attribute flashing lights):

![SPECIAL_VEHICLE_FIRETRUCK_FLASHING_LIGHTS](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/special_vehicle_firetruck_flashing_lights.png)

Special vehicle - Tractor

![SPECIAL_VEHICLE_TRACTOR](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/special_vehicle_tractor.png)

Special vehicle - Other

![SPECIAL_VEHICLE_OTHER](https://github.com/traffix-dataset/proanno/blob/master/assets/annotation_classes/special_vehicle_other.png)


 # Detailed Instructions and Examples

Bounding Box color convention in example images:
 + **Green**: Objects like this should be annotated


## Car
+ Vehicle designed primarily for personal use, e.g. sedans, hatch-backs, wagons, vans, mini-vans, SUVs and jeeps.

+ If it is primarily designed to haul cargo it is a truck.

![](https://www.nuscenes.org/public/images/taxonomy_imgs/personal_vehicle_2.jpg)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/personal_vehicle_4.jpg)

## Truck
+ Vehicles primarily designed to haul cargo including lorrys, trucks, pickup truck (a pickup truck is a light duty truck with an enclosed cab and an open or closed cargo area; a pickup truck can be intended primarily for hauling cargo or for personal use).

![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_2.png)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_3.png)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_5.png)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_6.png)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_7.png)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_8.png)

+ When a truck has a trailer, then both boxes should overlap a bit so that an enclosed box (truck+trailer) can be calculated in the post-processing step.

+ If you can see a truck from the front side, then only label it as truck with one bounding box and do not set the number of trailers.

![TRUCK_FRONT](https://github.com/traffix-dataset/proanno/blob/master/assets/labeling_examples/truck_front.png)

+ If you can see a truck from the back side, then only label it as trailer with one bounding box and select the corresponding trailer type attribute (e.g. container).

![TRUCK_BACK](https://github.com/traffix-dataset/proanno/blob/master/assets/labeling_examples/truck_back.png)

+ If you can see both (truck and trailer), then put 2 overlapping boxes and set the truck attribute "number_of_trailers" to the amount of trailers.

![TRUCK_FRONT_AND_BACK](https://github.com/traffix-dataset/proanno/blob/master/assets/labeling_examples/truck_front_and_back.png)

Pickup Truck:

![](https://www.nuscenes.org/public/images/taxonomy_imgs/pickup_truck_2.jpg)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/pickup_truck_4.jpg)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/pickup_truck_5.jpg)

 ## Motorcycle
+ Gasoline or electric powered 2-wheeled vehicle designed to move rapidly (at the speed of standard cars) on the road surface. This category includes all motorcycles, vespas and scooters. It also includes light 3-wheel vehicles, often with a light plastic roof and open on the sides, that tend to be common in Asia (rickshaws).
    + If there is a rider, include the rider in the box.
    + If there is a passenger, include the passenger in the box.
    + If there is a pedestrian standing next to the motorcycle, do NOT include in the annotation.

    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/motorcycle_1.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/motorcycle_2.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/motorcycle_3.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/motorcycle_4.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/motorcycle_5.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/motorcycle_6.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/motorcycle_7.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/motorcycle_8.jpg)

## Bicycle
+ Human or electric powered 2-wheeled vehicle designed to travel at lower speeds either on road surface, sidewalks or bicycle paths.
    + If there is a rider, include the rider in the box
    + If there is a passenger, include the passenger in the box
    + If there is a pedestrian standing next to the bicycle, do NOT include in the annotation

    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/bicycle_1.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/bicycle_2.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/bicycle_3.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/bicycle_4.jpg)


## Pedestrian
+ An adult/child pedestrian moving around the cityscape.
    + Mannequins should also be treated as pedestrian.

    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/mannequin_1.png)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/adult_pedestrian_2.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/adult_pedestrian_3.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/adult_pedestrian_4.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/adult_pedestrian_5.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/child_pedestrian_1.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/child_pedestrian_3.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/child_pedestrian_4.jpg)
    ![](https://www.nuscenes.org/public/images/taxonomy_imgs/child_pedestrian_5.jpg)

# License

MIT: https://mit-license.org/
