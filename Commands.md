# Annotation commands

<!-- TODO : Insert picture or video -->

## 3D Bounding Box Labeling - Instructions

1. Hold Down the Ctrl key and draw 2D bounding box in the drawing area (below the camera image). A 3D bounding box will be generated automatically with default vehicle size. If the box contains more than 10 points, the rotation, scale and position of the object will be automatically predicted and adjusted.
2. Move/Scale the 3D bounding box using the red, green and blue arrow (drag and drop) or use the blue sliders in the side menu.
3. Choose one of the available classes in the bottom left corner (Car, Pedestrian, Bicycle, Motorcycle, Truck, Van, Bus, Trailer, Special_Vehicle)
4. Repeat steps 1-3 for all objects in the sequence
5. Download 2D and 3D labels, as well as projected 3D labels to your computer (as zip archive)

## Annotation tips & tricks

#### 1. Interpolation of objects (available in sequence mode)
  1. Select object to interpolate by clicking on a bounding box
  2. Activate 'Interpolation Mode' in the menu (checkbox) -> start position will be saved
  3. Move to desired frame by skipping x frames
  4. Translate object to new position
  5. Click on the 'Interpolate' button in the menu

#### 2. Grid view & 3D View
  1. Activate the grid in the side menu for better orientation
  2. Switch into 3D view to review your annotations and check for correct orientation

#### 3. Use keyboard short cuts (WIP)
| Key | Description   |
| --- | ------------- |
|       ![V](./assets/textures/keyboard_small/c.png)  | Toggle view (3D view/Bird's-Eye-View)|
|       ![W](./assets/textures/keyboard_small/w.png)  | Move forward in 3D view|
|       ![A](./assets/textures/keyboard_small/a.png)  | Move left in 3D view|
|       ![S](./assets/textures/keyboard_small/s.png)  | Move backward in 3D view|
|       ![D](./assets/textures/keyboard_small/d.png)  | Move right in 3D view|
|       ![Q](./assets/textures/keyboard_small/q.png)  | Move down in 3D view|
|       ![E](./assets/textures/keyboard_small/e.png)  | Move up in 3D view|
|       ![LEFT](./assets/textures/keyboard_small/left.png) | Rotate camera counter-clock-wise |
|       ![RIGHT](./assets/textures/keyboard_small/right.png)| Rotate camera clock-wise |
|       ![UP](./assets/textures/keyboard_small/up.png) | Rotate camera up |
|       ![DOWN](./assets/textures/keyboard_small/down.png)| Rotate camera down |
|       ![C](./assets/textures/keyboard_small/c.png)  | Enlarge camera image|
|       ![N](./assets/textures/keyboard_small/n.png)  | Next frame     |
|       ![P](./assets/textures/keyboard_small/p.png)  | Previous frame   |
|       ![I](./assets/textures/keyboard_small/i.png)  | Interpolate    |
|       ![CTRL](./assets/textures/keyboard_small/ctrl.png)![MOUSELEFT](./assets/textures/keyboard_small/mouseleft.png) | Snap to grid in 0.5m steps (floor alignment mode)  |
|       ![CTRL](./assets/textures/keyboard_small/ctrl.png)![T](./assets/textures/keyboard_small/t.png)  | Enable/Disable Translation mode|
|       ![W](./assets/textures/keyboard_small/w.png)  | Move selected object forward (Y++)|
|       ![A](./assets/textures/keyboard_small/a.png)  | Move selected object to left (X--)|
|       ![S](./assets/textures/keyboard_small/s.png)  | Move selected object backward (Y--)|
|       ![D](./assets/textures/keyboard_small/d.png)  | Move selected object to right (X++)|
|       ![Q](./assets/textures/keyboard_small/q.png)  | Move selected object down (Z--)|
|       ![E](./assets/textures/keyboard_small/e.png)  | Move selected object up (Z++)|
|       ![CTRL](./assets/textures/keyboard_small/ctrl.png)![R](./assets/textures/keyboard_small/r.png)  | Enable/Disable Rotation mode|
|       ![Q](./assets/textures/keyboard_small/q.png) | Rotate selected object counter-clock-wise|
|       ![E](./assets/textures/keyboard_small/e.png)  | Rotate selected object clock-wise|
|       ![CTRL](./assets/textures/keyboard_small/ctrl.png)![S](./assets/textures/keyboard_small/s.png)  | Enable/Disable Scaling mode |
|      ![W](./assets/textures/keyboard_small/w.png) | Increase length along longitudinal axis (y-axis)  |
|      ![S](./assets/textures/keyboard_small/s.png) | Decrease length along longitudinal axis (y-axis)  |
|      ![A](./assets/textures/keyboard_small/a.png)  | Decrease width along lateral axis (x-axis) |
|      ![D](./assets/textures/keyboard_small/d.png)  | Increase width along lateral axis (x-axis) |
|      ![E](./assets/textures/keyboard_small/e.png)! | Increase height along vertical axis (z-axis) |
|      ![Q](./assets/textures/keyboard_small/q.png)! | Decrease height along vertical axis (z-axis) |
|  ![PLUS](./assets/textures/keyboard_small/plus.png)  | Increase arrow size |
|  ![MINUS](./assets/textures/keyboard_small/minus.png)  | Decrease arrow size |
|  ![X](./assets/textures/keyboard_small/x.png)  | Show/Hide X-axis |
|  ![Y](./assets/textures/keyboard_small/y.png)  | Show/Hide Y-axis |
|  ![Z](./assets/textures/keyboard_small/z.png)  | Show/Hide Z-axis (only in 3D mode)|
|  ![SPACE](./assets/textures/keyboard_small/space.png)  | Switch between different operation modes (translate, rotate, scale) |
|  ![TAB](./assets/textures/keyboard_small/tab.png)  | Select next object |
| ![DEL](./assets/textures/keyboard_small/del.png) OR ![BACKSPACE](./assets/textures/keyboard_small/backspace.png) | Delete selected object |
|  ![M](./assets/textures/keyboard_small/m.png)  | Marking mode (TODO)|
|  ![ONE](./assets/textures/keyboard_small/1.png)  | Select class CAR |
|  ![TWO](./assets/textures/keyboard_small/2.png)  | Select class Truck |
|  ![THREE](./assets/textures/keyboard_small/3.png)  | Select class Trailer |
|  ![FOUR](./assets/textures/keyboard_small/4.png)  | Select class Van |
|  ![FIVE](./assets/textures/keyboard_small/5.png)  | Select class Motorcycle |
|  ![SIX](./assets/textures/keyboard_small/6.png)  | Select class Bus |
|  ![SEVEN](./assets/textures/keyboard_small/7.png)  | Select class Pedestrian |
|  ![EIGHT](./assets/textures/keyboard_small/8.png)  | Select class Bicycle |
|  ![NINE](./assets/textures/keyboard_small/9.png)  | Select class Special_Vehicle |
| ![MOUSELEFT](./assets/textures/keyboard_small/mouseleft.png) | On a 2D/3D object: Show bounding box|
|            | On a camera image: Enlarge/Shrink camera image (TODO)|
|            | On ego vehicle: Show field-of-view (TODO)|
| ![LEFT](./assets/textures/keyboard_small/left.png)![RIGHT](./assets/textures/keyboard_small/right.png): | Switch FOV to next channel|
| ![R](./assets/textures/keyboard_small/r.png)| Reset all selected bounding boxes (TODO)|
| ![F11](./assets/textures/keyboard_small/f11.png) | Full Screen Mode|
| ![P](./assets/textures/keyboard_small/p.png) | Play video (TODO)||
| ![K](./assets/textures/keyboard_small/k.png) | Keyboard navigation (only in 3D view) (TODO)|
| ![L](./assets/textures/keyboard_small/l.png) | Toggle Lighting (TODO)|
| ![L](./assets/textures/keyboard_small/l.png)![ONE](./assets/textures/keyboard_small/1.png) | Label random color (TODO)|
| ![L](./assets/textures/keyboard_small/l.png)![TWO](./assets/textures/keyboard_small/2.png) | Label class color (TODO)|
| ![T](./assets/textures/keyboard_small/t.png) | Show/Hide trajectory (TODO)|
| ![SHIFT](./assets/textures/keyboard_small/shift.png)![D](./assets/textures/keyboard_small/d.png)| Download annotation file (TODO)|
| ![CTRL](./assets/textures/keyboard_small/ctrl.png)![Z](./assets/textures/keyboard_small/z.png)| Undo operation |
| ![CTRL](./assets/textures/keyboard_small/ctrl.png)![Y](./assets/textures/keyboard_small/y.png)| Redo operation (TODO)|
| ![G](./assets/textures/keyboard_small/g.png) | Show/Hide grid (TODO)|
| ![J](./assets/textures/keyboard_small/j.png) | Hide all labels except selected object (Press again to show all labels) (TODO)|
| ![QUESTIONMARK](./assets/textures/keyboard_small/questionmark.png) | Show keyboard shortcuts|
| ![ESC](./assets/textures/keyboard_small/esc.png) | Unselect box |
| ![CTRL](./assets/textures/keyboard_small/ctrl.png)![W](./assets/textures/keyboard_small/w.png)| Close tab (exit)|
|                                                                                                                               | Quit fullscreen cam image (TODO)|
| ![ALT](./assets/textures/keyboard_small/alt.png)![MOUSELEFT](./assets/textures/keyboard_small/mouseleft.png) | Copy bounding box (by dragging) (TODO)|

#### Hints:
+ Select `Copy label to next frame` checkbox if you want to keep the label (position, size, class) for next frame
+ Use helper views (available in point cloud mode) to align object along z-axis (no need to switch into 3D view)
+ Label one object from start to end (using interpolation) and then continue with next object (available in sequence mode)
+ Backup (download annotations) regularly to avoid loss of data in case of program crashes.
