# Merge UVs By Jointed Vertex

This add-on merge UVs if the corresponding vertices are merged.

![merge_uvs_by_jointed_vertex](https://user-images.githubusercontent.com/33594299/109412903-0d76d100-79ee-11eb-96b9-2153c49a04dc.gif)

## Support Version

2.90.0 or later

# Install
Copy **merge_uvs_by_jointed_vertex.py** to your addons folder.

e.g. {install_folder}/{version}/scripts/addons

# Useage

1. Select UVs in Image-Editor
2. Image-Editor (Edit Mode) > UV > Merge > By Jointed Vertex *(or Shortcut [M] > By Jointed Vertec)*

## Operator Property
### Threshold
If the distance is greater than this value, merging is not guaranteed.
![image](https://user-images.githubusercontent.com/33594299/109414061-34380600-79f4-11eb-9a8e-9a6301795ff3.png)

# Specifications
This Add-on...
* does not support UV Sync Selection.
* does not merge across multiple objects.
* can be merged across UV islands.
* does not consider the edge seam.

# Author
Masayuki Osaka

![image](https://user-images.githubusercontent.com/33594299/109414691-8d556900-79f7-11eb-93fd-27e9a0079efe.png)![image](https://user-images.githubusercontent.com/33594299/109414698-90505980-79f7-11eb-8b6f-a0abbca0ef7c.png)
