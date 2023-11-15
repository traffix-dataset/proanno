# Labeling instructions

1. Either start from a single object and label the entire sequence (with interpolation) **OR** label all objects in a scene and move onto the next timestamp (while copying annotations) 
2. **Do not** apply more than one box to a single object. If there is a truck with a trailer, then put two boxes (one box for Truck and another one for Trailer). Both boxes should overlap.
3. Download the annotation file into the following folder: `proAnno/input/dataset/<CAMERA_CHANNEL>/<SEQUENCE>/annotations`
4. For every bounding box, include one of the following labels 9 :
   - Car
   - Truck
   - Trailer
   - Van
   - Motorcycle
   - Bus
   - Pedestrian
   - Bicycle
   - Special vehicle


The specific details of the classes are below. Detailed instruction on labeling each class can be found at the end of the document.

[<h2>1. Car</h2>](#car)

These include vehicles designed primarily for personal use, e.g. sedans, hatch-backs, wagons, vans, mini-vans, SUVs, jeeps and pickup trucks (a pickup truck is a light duty truck with an enclosed cab and an open or closed cargo area; a pickup truck can be intended primarily for hauling cargo or for personal use).

![CAR](./assets/annotation_classes/car.png)

[<h2>2. Truck</h2>](#truck)

These are vehicles primarily designed to haul cargo including lorrys, trucks.

|Truck type | Example |
| -------- | ------- |
|Delivery Truck |![TRUCK](./assets/annotation_classes/truck.png) |
|Pickup Truck | ![PICKUP_TRUCK](./assets/annotation_classes/pickup_truck.png) |

[<h2>3. Trailer</h2>](#trailer)

A trailer of type container/box/dump/vehicle_transporter/mixer/tank/flat_bed/other.

| Trailer Type    | Example |
| -------- | ------- |
| Container| ![TRAILER_CONTAINER](./assets/annotation_classes/trailer_container.png) |
| Box | ![TRAILER_BOX](./assets/annotation_classes/trailer_box.png)|
| Dump|![TRAILER_DUMP](./assets/annotation_classes/trailer_dump.png)|
|Vehicle Transport|![TRAILER_VEHICLE_TRANSPORT](./assets/annotation_classes/trailer_vehicle_transport.png)|
|Mixer|![TRAILER_MIXER](./assets/annotation_classes/trailer_mixer.png)|
|Tank|![TRAILER_TANK](./assets/annotation_classes/trailer_tank.png)|
|Flatbed|![TRAILER_FLATBED](./assets/annotation_classes/trailer_flatbed.png)|
|Other|![TRAILER_OTHER](./assets/annotation_classes/trailer_other.png)|


[<h2>4. Van </h2>](#van)

Vans designed primarily for transporting something.

Examples :

![VAN_1](./assets/annotation_classes/van1.png)

![VAN_2](./assets/annotation_classes/van2.png)

![VAN_3](./assets/annotation_classes/van3.png)

[<h2>5. Motorcycle </h2>](#motorcycle)

Gasoline or electric powered 2-wheeled vehicle designed to move rapidly (at the speed of standard cars) on the road surface. This category includes all motorcycles, vespas and scooters. It also includes light 3-wheel vehicles, often with a light plastic roof and open on the sides, that tend to be common in Asia (rickshaws). If there is a rider and/or passenger, include them in the box and set the attribute "with_rider".

|Motorcycle Type | Example |
|----------------|---------|
|Motorbike|![MOTORCYCLE_MOTORBIKE](./assets/annotation_classes/motorcycle_motorbike.png)|
|Scooter|![MOTORCYCLE_SCOOTER](./assets/annotation_classes/motorcycle_scooter.png)|

[<h2>6. Bus </h2>](#bus)

Vehicles transporting more than 10 people.

|Bus Type | Example |
|----------------|---------|
|Rigid |![BUS_RIGID](./assets/annotation_classes/bus_rigid.png) |
| Bendy |![BUS_BENDY](./assets/annotation_classes/bus_bendy.png) |

[<h2>7. Pedestrian </h2>](#pedestrian)
 <!-- TODO -->
An adult/child pedestrian moving around the cityscape. Mannequins should also be annotated as `Pedestrian`.

![PEDESTRIAN](./assets/annotation_classes/pedestrian.png)

[<h2>8. Bicycle </h2>](#bicycle)

Human or electric powered 2-wheeled vehicle designed to travel at lower speeds either on road surface, sidewalks or bicycle paths. If there is a rider and/or passenger, include them in the box.

|Bicycle Type | Example |
|----------------|---------|
|without rider | ![BICYCLE_WITHOUT_RIDER](./assets/annotation_classes/bicycle_without_rider.png) |
|with rider | ![BICYCLE_WITH_RIDER](./assets/annotation_classes/bicycle_with_rider.png) |

[<h2>9. Special vehicle </h2>](#specialvehicle)

A special vehicle (e.g. police car, ambulance, fire truck or tractor etc).

|Special vehicle Type | Example |
|----------------|---------|
|Ambulance | ![SPECIAL_VEHICLE_AMBULANCE](./assets/annotation_classes/special_vehicle_ambulance.png) |
| Ambulance (with attribute flashing lights)| ![SPECIAL_VEHICLE_AMBULANCE_FLASHING_LIGHTS](./assets/annotation_classes/special_vehicle_ambulance_flashing_lights.png) |
|Police vehicle | ![SPECIAL_VEHICLE_POLICE_VEHICLE](./assets/annotation_classes/special_vehicle_police_vehicle.png) |
|Police vehicle (with attribute flashing lights) | ![SPECIAL_VEHICLE_POLICE_VEHICLE_FLASHING_LIGHTS](./assets/annotation_classes/special_vehicle_police_vehicle_flashing_lights.png) |
| Firetruck | ![SPECIAL_VEHICLE_FIRETRUCK](./assets/annotation_classes/special_vehicle_firetruck.png) |
| Firetruck (with attribute flashing lights) | ![SPECIAL_VEHICLE_FIRETRUCK_FLASHING_LIGHTS](./assets/annotation_classes/special_vehicle_firetruck_flashing_lights.png) |
| Tractor | ![SPECIAL_VEHICLE_TRACTOR](./assets/annotation_classes/special_vehicle_tractor.png) |
| Other | ![SPECIAL_VEHICLE_OTHER](./assets/annotation_classes/special_vehicle_other.png) |


 # Detailed Instructions and Examples

Follow these instruction when labeling each class to avoid ambiguity.
<!-- Bounding Box color convention in example images:
 + **Green**: Objects like this should be annotated -->

## Car
+ Vehicle designed primarily for personal use, e.g. sedans, hatch-backs, wagons, vans, mini-vans, SUVs and jeeps.

+ If it is primarily designed to haul cargo it is a truck.

![](https://www.nuscenes.org/public/images/taxonomy_imgs/personal_vehicle_2.jpg)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/personal_vehicle_4.jpg)

## Truck
+ Vehicles primarily designed to haul cargo including lorrys, trucks, pickup truck (a pickup truck is a light duty truck with an enclosed cab and an open or closed cargo area; a pickup truck can be intended primarily for hauling cargo or for personal use).

![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_2.png)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_3.png)
<!-- ![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_5.png) -->
<!-- ![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_6.png) -->
![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_7.png)
![](https://www.nuscenes.org/public/images/taxonomy_imgs/front_of_semi_truck_8.png)

+ When a truck has a trailer, then both boxes should overlap a bit so that an enclosed box (truck+trailer) can be calculated in the post-processing step.

+ If you can see a truck from the front side, then only label it as truck with one bounding box and do not set the number of trailers.

![TRUCK_FRONT](./assets/labeling_examples/truck_front.png)

+ If you can see a truck from the back side, then only label it as trailer with one bounding box and select the corresponding trailer type attribute (e.g. container).

![TRUCK_BACK](./assets/labeling_examples/truck_back.png)

+ If you can see both (truck and trailer), then put 2 overlapping boxes and set the truck attribute "number_of_trailers" to the amount of trailers.

![TRUCK_FRONT_AND_BACK](./assets/labeling_examples/truck_front_and_back.png)

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
