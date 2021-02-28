# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
import bpy
import bmesh
from mathutils import Vector
from bpy.props import FloatProperty


bl_info = {
    'name': 'Merge UVs By Jointed Vertex',
    'author': 'Masayuki Osaka',
    'version': (1, 0),
    'blender': (2, 80, 0),
    'location': 'Image-Window > UV > Merge > By Jointed Vertex',
    'description': 'Merge UVs if the corresponding vertices are merged',
    'support': 'COMMUNITY',
    'category': 'UV'
}


class MergeUVsJointedByVertex(bpy.types.Operator):

    bl_idname = "uv.merge_uv_jointed_by_vertex"
    bl_label = 'By Jointed Vertex'
    bl_description = 'Merge UVs if the corresponding vertices are merged'
    bl_options = {'REGISTER', 'UNDO'}

    threshold: FloatProperty(
        name = 'Threshold',
        description = 'Maximum distance to search for UVs to be combined',
        default = 0.99
    )

    # merge uv
    def _move_uvs(self, loopuvs):
        uvs = list(loopuvs)
        while True:
            # pick up UVs at distances below a threshold
            uvs_to_merge = {uvs[0], }
            for i in range(1, len(uvs)):
                if (uvs[0].uv - uvs[i].uv).length < self.threshold:
                    uvs_to_merge.add(uvs[i])

            # merge
            total = Vector((0, 0))
            for uv in uvs_to_merge:
                total += uv.uv
            ave_x = total.x / len(uvs_to_merge)
            ave_y = total.y / len(uvs_to_merge)
            average = Vector((ave_x, ave_y))
            for uv in uvs_to_merge:
                uv.uv = average

            # "uvs" is used for recursive processing
            uvs = set(uvs)
            for uv in uvs_to_merge:
                uvs.remove(uv)
            uvs = list(uvs)

            if len(uvs) <= 1:
                return

    # collect uvs per object to merge
    def _execute_per_object(self, obj):
        bm = bmesh.from_edit_mesh(obj.data)
        uv_layer = bm.loops.layers.uv.verify()

        # collect selected UVs per vertex. {(int)vertex_id: (BMLoopUV, )}
        uvs_per_vtx = dict()
        for face_id, face in enumerate(bm.faces):
            for floop, vtx_id in zip(face.loops, face.verts):
                loopuv = floop[uv_layer]
                if not loopuv.select:
                    continue
                if vtx_id not in uvs_per_vtx:
                    uvs_per_vtx[vtx_id] = {loopuv, }
                    continue
                else:
                    uvs_per_vtx[vtx_id].add(loopuv)

        # merge uvs per vertex_id
        for loopuvs in uvs_per_vtx.values():
            self._move_uvs(loopuvs)

        bmesh.update_edit_mesh(obj.data)

    def execute(self, context):
        if bpy.context.mode != 'EDIT_MESH':
            self.report({'ERROR'}, 'Execute in editmode')
            return {'CANCELLED'}
        if bpy.context.scene.tool_settings.use_uv_select_sync:
            self.report({'ERROR'}, 'UV Sync Selection is not supported')
            return {'CANCELLED'}

        objects = context.selected_objects
        for obj in objects:
            if obj.type == 'MESH':
                self._execute_per_object(obj)

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(MergeUVsJointedByVertex.bl_idname)


def register():
    bpy.utils.register_class(MergeUVsJointedByVertex)
    bpy.types.IMAGE_MT_uvs_merge.append(menu_fn)


def unregister():
    bpy.types.IMAGE_MT_uvs_merge.remove(menu_fn)
    bpy.utils.unregister_class(MergeUVsJointedByVertex)
