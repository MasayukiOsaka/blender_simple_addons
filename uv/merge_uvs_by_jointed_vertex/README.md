# Merge UVs By Jointed Vertex

This add-on merge UVs if the corresponding vertices are merged.

![merge_uvs_by_jointed_vertex](https://user-images.githubusercontent.com/33594299/109412903-0d76d100-79ee-11eb-96b9-2153c49a04dc.gif)

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
