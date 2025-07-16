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


class Labels:

    MAIN_PROP_SETS_ENABLE_NAME='Enable Option Sets'
    MAIN_PROP_SETS_ENABLE_DESC='Use option sets to manage options in the blend file. Option sets allow one to maintain multiple option presets within a single blend file and switch quickly between them. Press the Help button to learn more'

    FEATURE_NOT_SUPPORTED_MSG = '(Not supported in this edition)'
    FEATURE_NOT_SUPPORTED_ICON = 'ERROR'

    FEATURE_NOT_SUPPORTED_BY_PACKING_MODE_MSG = '(Not supported by the packing mode)'

    PACKING_DEVICE_WARNING="If you don't see your Cuda GPU in the list, make sure you have latest GPU drivers installed"

    # Property labels

    THREAD_COUNT_NAME='Thread Count'
    THREAD_COUNT_DESC="Choose the maximal number of CPU cores which will be used by the plugin. By default this parameter is set to the number of cores in the system"

    PRECISION_NAME='Precision'
    PRECISION_DESC='Number describing how exact the algorithm will be when searching for island placement. Too low value may cause islands to overlap'

    MARGIN_NAME='Margin'
    MARGIN_DESC='Margin to apply during packing'

    PIXEL_MARGIN_ENABLE_NAME='Enable Pixel Margin '
    PIXEL_MARGIN_ENABLE_DESC="Enable the pixel margin functionality. If this parameter is enabled, then the usual 'Margin' option will be ignored and the packer will determine the exact pixel margin"

    PIXEL_MARGIN_NAME='Margin (px)'
    PIXEL_MARGIN_DESC="Distance between distinct UV islands in pixels to apply during packing"

    PIXEL_BORDER_MARGIN_NAME='Border Margin (px)'
    PIXEL_BORDER_MARGIN_DESC="Distance in pixels between UV islands and the UV target box border. This option is disabled and ignored if set to '0' - in such case the distance will be determined by the island margin"

    EXTRA_PIXEL_MARGIN_TO_OTHERS_NAME='Extra Margin To Others'
    EXTRA_PIXEL_MARGIN_TO_OTHERS_DESC="Specifies an additional pixel margin between islands being packed and the other islands (unselected islands when using the 'Pack To Others' mode). In result the final margin between these islands will be calculated using the formula: 'Pixel Margin' + 'Extra Margin To Others'.\n\nWhen using the 'Groups To Tiles' mode and packing two groups into the same UV space, the islands from the other group are also treated as 'Others'. It means that the 'Extra Margin To Others' parameter will also be taken into account when calculating the margin between islands belonging to different groups"

    PIXEL_MARGIN_TEX_SIZE_NAME='Texture Size'
    PIXEL_MARGIN_TEX_SIZE_DESC="Texture size in pixels used for pixel margin calculation. If the 'Use Texture Ratio' option is enabled, then this property is ignored and the dimensions of the active texture are used to calculate pixel margin"

    PIXEL_PERFECT_ALIGN_NAME='Pixel Perfect Alignment'
    PIXEL_PERFECT_ALIGN_DESC='Align bounding boxes of the islands being packed to the nearest pixel coordinates. WARNING: certain restrictions apply for this mode, press the Help button on the right to learn more'

    ROTATION_ENABLE_NAME='Rotation Enable'
    ROTATION_ENABLE_DESC='Allow the packer to rotate islands in order to achieve a better result'

    PRE_ROTATION_DISABLE_NAME='Pre-Rotation Disable'
    PRE_ROTATION_DISABLE_DESC='Disable the initial rotation of islands before generating other orientations. The pre-rotation operation usually optimizes packing, use this option only if you have a good reason'

    FLIPPING_ENABLE_NAME='Flipping Enable'
    FLIPPING_ENABLE_DESC='Allow the packer to flip islands when performing the operation'

    NORMALIZE_SCALE_NAME='Normalize Scale'
    NORMALIZE_SCALE_DESC='Automatically scale selected islands before packing so that the average texel density is the same for every island.\n\nWARNING: if lock overlapping is enabled, then normalization takes place AFTER overlapping islands are locked.\n\nWARNING 2: islands packed with fixed scale will not be normalized'

    NORMALIZE_SPACE_NAME='Normalize Space'
    NORMALIZE_SPACE_DESC='3D space to use when normalizing islands'

    ISLAND_NORMALIZE_MULTIPLIER_ENABLE_NAME='Island Scale Multiplier'
    ISLAND_NORMALIZE_MULTIPLIER_ENABLE_DESC="Specify scale multiplier to be applied after normalization is done on a per-island basis. The multiplier is specified in percentages, for example: multiplier 100% (the default value for all islands) means scaling by 1 i.e. an island scale won't change after normalization; multiplier 200% means an island will be scaled by 2 after normalization, multiplier 50% means an island will be scaled by 0.5 after normalization etc"

    ISLAND_NORMALIZE_MULTIPLIER_NAME='Scale Multiplier (%)'
    ISLAND_NORMALIZE_MULTIPLIER_DESC='Scale multiplier to be set for the selected islands'

    SCALE_MODE_NAME='Scale Mode'
    SCALE_MODE_DESC="Determines how island scaling is performed during packing"

    ARRANGE_NON_PACKED_NAME='Arrange Non-Packed Islands'
    ARRANGE_NON_PACKED_DESC="When packing with fixed scale, arrange the islands that cannot be packed due to a lack of space in a line above the target UV area. The arrangement will be done after the operation is complete"

    TEXEL_DENSITY_VALUE_NAME='Texel Density (px/m)'
    TEXEL_DENSITY_VALUE_DESC="If set to a value greater than 0, the packer will scale the islands before packing to set the requested texel density (unit to use: px/m). After setting texel density, the given islands will be packed with fixed scale (they won't be scaled during packing in order to maintain the requested texel density).\n\nTexel density is calculated using the 'Texture Size' property from the Pixel Margin panel.\n\nIf the 'Texel Density' value is set to 0, texel density won't be set - islands will be packed in the usual manner.\n\nNote that both options: 'Texel Density' as well as 'Texture Size' can be overridden on a per-group basis when using a group-based packing mode.\n\nIf '{}' is enabled, islands with texel density set that cannot be packed (due to lack of space), will be arranged in a line above the target UV area after the operation is complete".format(ARRANGE_NON_PACKED_NAME)

    TEXEL_DENSITY_ENABLE_NAME='Texel Density Enable'
    TEXEL_DENSITY_ENABLE_DESC='Enable automatic texel density setting for the input islands before packing'

    SCALE_MODE_MAX_SCALE_DESC = 'The packer will scale islands up in order to cover the target UV area as much as possible'
    SCALE_MODE_FIXED_SCALE_DESC = "The packer will not scale islands during packing (island size is fixed). If islands don't fit into the target UV area, the packer will pack as many islands as possible and return a No-space warning from the operation"
    SCALE_MODE_FIXED_SCALE_MAX_MARGIN_DESC = 'The packer will not scale islands during packing (island size is fixed). At same the packer will look for the maximum possible margin with which the given islands can be packed into the target UV space. WARNING: by the definition, the Margin options will be ignored for islands packed using this mode'

    PACK_STRATEGY_NAME='Pack Strategy'
    PACK_STRATEGY_DESC=""

    PACK_STRATEGY_START_CORNER_NAME='Start Corner'
    PACK_STRATEGY_START_CORNER_DESC=""

    ROTATION_STEP_NAME='Rotation Step (deg)'
    ROTATION_STEP_DESC="Rotation step (in degrees) to use when generating island orientations which will be considered during packing"

    ISLAND_ROT_STEP_ENABLE_NAME='Enable Island Rotation Step'
    ISLAND_ROT_STEP_ENABLE_DESC="Enable per-island rotation step"

    ISLAND_ROT_STEP_NAME='Rotation Step Value (deg)'
    ISLAND_ROT_STEP_DESC="Rotation step value (in degrees) to be set for the selected islands"

    PACKING_DEPTH_NAME='Packing Depth'

    TEX_RATIO_NAME='Use Texture Ratio'
    TEX_RATIO_DESC='Take into consideration the ratio of the active texture dimensions during packing'

    PACK_TO_OTHERS_NAME='Pack To Others'
    PACK_TO_OTHERS_DESC='Pack selected islands so they do not overlap with unselected islands. Using this mode you can add new islands into a packed UV map'

    PACK_MODE_NAME='Packing Mode'
    PACK_MODE_DESC="Determines how the packer processes the UV map"

    PACK_MODE_SINGLE_TILE_NAME='Single Tile'
    PACK_MODE_SINGLE_TILE_DESC='Standard packing to a single tile'

    PACK_MODE_TILES_NAME='Tiles'
    PACK_MODE_TILES_DESC='Pack islands to tiles'

    PACK_MODE_GROUPS_TOGETHER_NAME='Groups Together'
    PACK_MODE_GROUPS_TOGETHER_DESC="Group islands using the 'Grouping Method' parameter. Pack all groups into a single tile, islands belonging to the same group will be neighbors after packing. For some UV layouts it is required to use the 'Heuristic Search' option in order to obtain a decent result in this mode"

    PACK_MODE_GROUPS_TO_TILES_NAME='Groups To Tiles'
    PACK_MODE_GROUPS_TO_TILES_DESC="Group islands using the 'Grouping Method' parameter. Pack every group into a separate tile"

    TILE_COUNT_NAME="Tile Count"
    TILE_COUNT_DESC="Determines the number of tiles the given group will be packed into"

    PIXEL_PERFECT_VERT_ALIGN_MODE_NAME = 'Vertex Align Mode'
    PIXEL_PERFECT_VERT_ALIGN_MODE_DESC = 'Determines which vertices will be pixel aligned after packing. WARNING: be careful when setting this option as pixel aligning too many vertices may introduce degenerated faces in the UV map'

    PIXEL_PERFECT_VERT_ALIGN_MODE_NONE_DESC = 'None of the vertices will be pixel aligned'
    PIXEL_PERFECT_VERT_ALIGN_MODE_BOUNDING_BOX_CORNERS_DESC = 'Only vertices located in corners of island bounding boxes will be pixel aligned'
    PIXEL_PERFECT_VERT_ALIGN_MODE_BOUNDING_BOX_DESC = 'Only vertices located on island bounding box edges will be pixel aligned'
    PIXEL_PERFECT_VERT_ALIGN_MODE_BORDER_EDGES_DESC = 'Only vertices belonging to island border edges will be pixel aligned. Note it also includes border vertices on inner island holes'
    PIXEL_PERFECT_VERT_ALIGN_MODE_ALL_DESC = 'All vertices will be pixel aligned'

    GROUP_METHOD_NAME="Grouping Method"
    GROUP_METHOD_DESC="Grouping method to use"

    GROUP_METHOD_MATERIAL_DESC = 'Islands sharing the same material will belong to the same group'
    GROUP_METHOD_SIMILARITY_DESC = 'Islands of a similar shape will belong to the same group'
    GROUP_METHOD_MESH_DESC = 'Islands being part of adjacent geometry will belong to the same group'
    GROUP_METHOD_OBJECT_DESC = 'Islands being part of the same object will belong to the same group'
    GROUP_METHOD_MANUAL_DESC = "Grouping is determined manually by the user using a grouping scheme"
    GROUP_METHOD_TILE_DESC = 'Islands placed in the same UDIM tile will belong to the same group'

    GROUP_LAYOUT_MODE_NAME = 'Group Layout Mode'
    GROUP_LAYOUT_MODE_DESC = 'Determines where in the UV space the particular groups will be packed'

    TILES_IN_ROW_NAME="Tiles In Row"
    TILES_IN_ROW_DESC="Determines the maximum number of tiles in a single tile row. After all tiles in the given row are used, further UV islands will be packed into the tiles from the next row"

    GROUP_LAYOUT_MODE_AUTOMATIC_DESC="Groups will be automatically packed one after another. The number of tiles for each group is determined by the '{}' parameter. The maximum number of tiles in a single row is determined by the '{}' parameter".format(TILE_COUNT_NAME, TILES_IN_ROW_NAME)
    GROUP_LAYOUT_MODE_MANUAL_DESC="Determine target boxes for each group manually"
    GROUP_LAYOUT_MODE_AUTOMATIC_HORI_DESC="Every group will be automatically packed into the distinct tile row (first group into the first row, second group into the second row etc). The number of tiles for each group is determined by the '{}' parameter".format(TILE_COUNT_NAME)
    GROUP_LAYOUT_MODE_AUTOMATIC_VERT_DESC="Every group will be automatically packed into the distinct tile column (first group into the first column, second group into the second column etc). The number of tiles for each group is determined by the '{}' parameter".format(TILE_COUNT_NAME)
    GROUP_LAYOUT_MODE_TILE_GRID_DESC='All groups will be packed into a tile grid of the given dimensions'
    
    TEXEL_DENSITY_GROUP_POLICY_NAME = 'Texel Density Policy'
    TEXEL_DENSITY_GROUP_POLICY_DESC = 'Determines how relative texel density of particular groups is processed'

    TEXEL_DENSITY_GROUP_POLICY_INDEPENDENT_NAME = 'Independent'
    TEXEL_DENSITY_GROUP_POLICY_UNIFORM_NAME = 'Uniform'
    TEXEL_DENSITY_GROUP_POLICY_CUSTOM_NAME = 'Custom'
    TEXEL_DENSITY_GROUP_POLICY_AUTOMATIC_NAME = 'Automatic'

    TEXEL_DENSITY_CLUSTER_NAME='Texel Density Cluster'
    TEXEL_DENSITY_CLUSTER_DESC="If given groups have the same value of this parameter set, then uniform scaling will be applied to them during packing (their relative texel density will be maintained). This per-group parameter is only used if '{}' is set to '{}'".format(TEXEL_DENSITY_GROUP_POLICY_NAME, TEXEL_DENSITY_GROUP_POLICY_CUSTOM_NAME)

    TEXEL_DENSITY_GROUP_POLICY_INDEPENDENT_DESC = 'Relative texel density of the groups will NOT be maintained (all groups are scaled independently during packing)'
    TEXEL_DENSITY_GROUP_POLICY_UNIFORM_DESC = 'Relative texel density of the groups will be maintained (uniform scale will be applied to all groups during packing)'
    TEXEL_DENSITY_GROUP_POLICY_CUSTOM_DESC = "Determine manually which groups will have relative texel density maintained. Given groups will have relative texel density maintained during packing (the same scale will be applied to them) if they share the same value of the '{}' per-group parameter".format(TEXEL_DENSITY_CLUSTER_NAME)
    TEXEL_DENSITY_GROUP_POLICY_AUTOMATIC_DESC = "Handle relative texel density automatically: two groups will have relative texel density maintained if and only if their target boxes intersect"

    GROUP_COMPACTNESS_NAME="Grouping Compactness"
    GROUP_COMPACTNESS_DESC="A value from 0 to 1 specifying how much the packer should prefer solutions providing more compact grouping, when packing groups together. A lower value means the packer will strive less to achieve compact grouping, at the same time it will prioritize achieving better coverage of the overall packing. With a greater value of the parameter, groups will be packed more compactly, but the coverage of the entire solution might be worse.\n\nWARNING: use this parameter with care - a small increase of its value might considerably change the result you will get"

    GROUPS_TOGETHER_NAME='Groups Together'
    GROUPS_TOGETHER_DESC='When enabled, islands belonging to the same group will be packed into a single box so that they are neighbors in the resulting layout. The option can be overridden on a per-group basis.\n\nWARNING: enabling this option forces islands from a single group always being packed into a single target box - one of the boxes configured for the group, where the packer sees fit'

    PACK_TO_SINGLE_BOX_NAME="Pack To Single Box"
    PACK_TO_SINGLE_BOX_DESC="Force every group to be packed into a single target box (one of the target boxes configured for the group). Note that different groups may still be packed into different boxes, also different groups may be packed into the same box"

    MANUAL_GROUP_NUM_NAME="Group Number"
    MANUAL_GROUP_NUM_DESC="Manual group number to be assigned to the selected islands"

    GROUPS_ENABLE_NAME='Enable The Group Functionality'
    GROUPS_ENABLE_DESC="Enable the given group functionality. Press the help button next to the group number field for more details"

    GROUP_NUM_NAME="Group Number"
    GROUP_NUM_DESC="Group number to be assigned to the selected islands"

    TRACK_GROUPS_REQUIRE_MATCH_FOR_ALL_NAME="Require Match For All (Recommended)"
    TRACK_GROUPS_REQUIRE_MATCH_FOR_ALL_DESC=''

    TRACK_GROUPS_MATCHING_MODE_NAME='Matching Mode'
    TRACK_GROUPS_MATCHING_MODE_DESC=''

    USE_BLENDER_TILE_GRID_NAME="Use Blender UDIM Grid"
    USE_BLENDER_TILE_GRID_DESC="If enabled, the tile grid shape is determined by the Blender UV editor settings (N-panel / View tab). Otherwise, the shape is configured using the properties below"

    TILE_COUNT_PER_GROUP_NAME="Tile Count Per Group"
    TILE_COUNT_PER_GROUP_DESC="Determines the number of tiles every group will be packed into"

    LOCK_OVERLAPPING_ENABLE_NAME='Lock Overlapping Enable'
    LOCK_OVERLAPPING_ENABLE_DESC='Treat overlapping islands as a single island'

    LOCK_OVERLAPPING_MODE_NAME='Lock Overlapping Mode'
    LOCK_OVERLAPPING_MODE_DESC='Determines when the packer considers two islands as overlapping each other (when checking if two islands should be locked together)'

    TILE_FILLING_METHOD_SIMULTANEOUSLY_NAME='Simultaneously'
    TILE_FILLING_METHOD_ONE_BY_ONE_NAME='One By One'

    TILE_FILLING_METHOD_NAME='Tile Filling Method'
    TILE_FILLING_METHOD_DESC="The '{}' method is much faster, when packing a huge number of islands (thousands of islands) to many tiles. When packing a moderate number of islands, performance of both methods is similar".format(TILE_FILLING_METHOD_SIMULTANEOUSLY_NAME)

    OVERLAP_DETECTION_MODE_ANY_PART_DESC="Two islands will be considered as overlapping if only they overlap by any part"
    OVERLAP_DETECTION_MODE_EXACT_DESC="Two islands will be considered as overlapping only if they have the same bounding boxes in the UV space and have identical area"

    PRE_VALIDATE_NAME='Automatic UV Pre-Validation'
    PRE_VALIDATE_DESC='Automatically validate the UV map before packing. If any invalid UV face is found during validation, packing will be aborted and the given UV faces will be selected. WARNING: enabling this option may increase the packing initialization time for UV maps with the huge number of faces, use it with care'

    HEURISTIC_ENABLE_NAME='Enable Heuristic'
    HEURISTIC_ENABLE_DESC="Perform multiple packing iterations in order to find the optimal result"

    HEURISTIC_SEARCH_TIME_NAME='Search Time (s)'
    HEURISTIC_SEARCH_TIME_DESC='Specify a time in seconds for the heuristic search. After timeout is reached the packer will stop and the best result will be applied to the UV map. If the time is set to 0 the packer will perform the search continuously, until the user manually applies the result by pressing ESC'

    HEURISTIC_MAX_WAIT_TIME_NAME='Max Wait Time (s)'
    HEURISTIC_MAX_WAIT_TIME_DESC="Maximum time the packer will wait for a better result. If the heuristic algorithm is not able to find a tighter packing during that time, the operation will be automatically finished and the best result found so far will be applied to the UV map. If set to 0, then the functionality will be disabled"

    HEURISTIC_ALLOW_MIXED_SCALES_NAME='Allow Mixed Scales'
    HEURISTIC_ALLOW_MIXED_SCALES_DESC="Allow the packer to apply inconsistent scaling to islands during the search in order to improve UV space coverage.\n\nFor example, when a single island in the UV map is much bigger than all other islands, such an island may limit final UV space coverage: the big island results in an upper limit for scale (because it has to be fit into the target box) and that limit also applies for all other islands when uniform scaling is used.\n\nWhen the '{}' option is enabled, the packer is allowed to scale the big island down relatively to other islands - meaning the upper limit for scale no longer applies to the smaller islands. In result the smaller islands may be scaled up resulting in better overall UV space coverage.\n\nWARNING: when the option is enabled, the packer may scale islands independently. It means the relative texel density of islands may be changed after packing".format(HEURISTIC_ALLOW_MIXED_SCALES_NAME)

    ADVANCED_HEURISTIC_NAME='Advanced Heuristic'
    ADVANCED_HEURISTIC_DESC="Use an advanced method during a heuristic search. With this option enabled add-on will examine a broader set of solutions when searching for the optimal one. This method is most useful when packing a limited number of islands - in such case it allows to find a better solution than if using the simple method. Enabling this option is not recommended when packing a UV map containing a greater number of islands"

    SIMI_VERTEX_THRESHOLD_NAME='Vertex Threshold'
    SIMI_VERTEX_THRESHOLD_DESC='Maximum distance below which two vertices are considered as matching'

    SIMI_MODE_NAME='Similarity Mode'
    SIMI_MODE_DESC='Defines the way in which the packer determines whether two UV islands are similar'

    SIMI_MODE_BORDER_SHAPE_NAME='Border Shape'
    SIMI_MODE_BORDER_SHAPE_DESC='Two islands are considered similar, if shapes of their borders are similar. In this mode only the position of vertices which determine the island border are taken into consideration - the internal vertices and redundant border vertices are ignored'

    SIMI_MODE_VERTEX_POSITION_NAME='Vertex Position'
    SIMI_MODE_VERTEX_POSITION_DESC='Two islands are considered similar, if the number of vertices and their relative position match. In this mode the position of all island vertices are taken into account, but the island topology (how the vertices are connected to each other) is ignored'

    SIMI_MODE_TOPOLOGY_NAME='Topology'
    SIMI_MODE_TOPOLOGY_DESC="Two islands are considered similar, if the number of vertices and their relative position match and also island topologies are the same.\n\nIn this mode not only the position of all island vertices are taken into account, but also the island topology (how vertices are connected to each other).\n\nWARNING: the '{0}' mode is the most expensive mode from the computing and memory perspective, that is why it is not recommend to use it with UV islands with a huge number of vertices (10000 vertices or more). If you require aligning with vertex correction for such islands, use the '{1}' mode first and switch to the '{0}' mode only if you didn't receive desired results. If you have to use the '{0}' mode for heavy UV islands, make sure the '{2}' parameter is set to the lowest value which gives you the expected outcome".format(SIMI_MODE_TOPOLOGY_NAME, SIMI_MODE_VERTEX_POSITION_NAME, SIMI_VERTEX_THRESHOLD_NAME)

    SIMI_THRESHOLD_NAME='Similarity Threshold'
    SIMI_THRESHOLD_DESC="A greater value of this parameter means island borders will be more likely recognized as a similar in shape. A lower value means more accurate distinction. For more info regarding similarity detection click the help button"

    SIMI_CHECK_HOLES_NAME='Check Holes'
    SIMI_CHECK_HOLES_DESC="When enabled, the '{}' mode will also take into account shapes of inner holes when determining if two islands are similar. Note that enabling this option will result in increasing the time needed to perform the operation".format(SIMI_MODE_BORDER_SHAPE_NAME)

    SIMI_ADJUST_SCALE_NAME='Adjust Scale'
    SIMI_ADJUST_SCALE_DESC='Allow the packer to scale islands to the same size before determining whether they are similar'

    SIMI_NON_UNIFORM_SCALING_TOLERANCE_NAME='Non-Uniform Scaling Tolerance'
    SIMI_NON_UNIFORM_SCALING_TOLERANCE_DESC='Determines to what extent the packer will be allowed to apply non-uniform scaling when determining if two islands are similar.\n\nIf set to 0, non-uniform scaling will not be allowed at all.\n\nIf the value is between 0 and 1, the packer will consider matches resulting from non-uniform scaling, but it will add a penalty for such matches when comparing them with uniformly scaled matches.\n\nA general rule is: the more non-uniformly a match is scaled, the greater the penalty which will be applied for the match during comparison. On the other hand the greater the value this option, the more tolerance the packer will have for non-uniform scaling i.e. overall penalties for non-uniformly scaled matches will be lower.\n\nIf the option is set to the maximum tolerance (value 1), the packer will not distinguish non-uniform scaling from uniform scaling (both cases will be preferred equally)'

    SIMI_MATCH_3D_ORIENTATION_NAME = 'Match 3D Orientation'
    SIMI_MATCH_3D_ORIENTATION_DESC = 'Consider islands as similar, only if they orient geometry in the 3D space in the same way'

    SIMI_MATCH_3D_AXIS_NAME = 'Match 3D Axis'
    SIMI_MATCH_3D_AXIS_DESC = "When performing the similarity check, accept only those UV island orientations which result in the same mapping (texture) direction along the given axis in the 3D space. If set to 'NONE' then the  functionality is disabled. WARNING: make sure you don't choose an axis which is perpendicular to the 3D geometry being considered - in such a case the UV island corresponding to the given geometry will be excluded from the operation"

    SIMI_MATCH_3D_AXIS_SPACE_NAME = '3D Axis Space'
    SIMI_MATCH_3D_AXIS_SPACE_DESC = "The 3D space to consider when the '{}' functionality is enabled".format(SIMI_MATCH_3D_AXIS_NAME)
    

    SIMI_CORRECT_VERTICES_NAME='Correct Vertices'
    SIMI_CORRECT_VERTICES_DESC="Correct position of matching UV vertices of similar islands so they are placed on the top of each other after aligning"

    ALIGN_PRIORITY_ENABLE_NAME='Enable Align Priority'
    ALIGN_PRIORITY_ENABLE_DESC='Control which island is aligned (moved) onto another when two islands are considered similar by the packer (check the mode documentation for more details)'

    ALIGN_PRIORITY_NAME='Align Priority'
    ALIGN_PRIORITY_DESC='Align priority value to assign'

    SPLIT_OVERLAP_DETECTION_MODE_NAME='Overlap Detection Mode'
    SPLIT_OVERLAP_DETECTION_MODE_DESC='Determines when the packer considers two islands as overlapping each other'

    SPLIT_OVERLAP_MAX_TILE_X_NAME='Max Tile (X)'
    SPLIT_OVERLAP_MAX_TILE_X_DESC='Maximum tile (in the X coord direction), overlapping islands will be moved into. If an island is already in a maximum tile and needs to me moved further, it will be moved one tile up in the Y direction and X tile coord will be reset to 0. If the value is set 0, the functionality is disabled'

    SPLIT_OVERLAP_DONT_SPLIT_PRIORITIES_NAME="Don't Split Priorities"
    SPLIT_OVERLAP_DONT_SPLIT_PRIORITIES_DESC="When enabled, the packer doesn't split islands sharing the same Align Priority value. WARNING: option supported only when the Align Priority panel is enabled"

    _ORIENT_PRIM_DESC_HEADER = 'When orienting UVs to the 3D space, the packer first tries to match the primary 3D axis to the primary UV axis'

    ORIENT_PRIM_3D_AXIS_NAME = 'Primary 3D Axis'
    ORIENT_PRIM_3D_AXIS_DESC = '{}. This parameter defines the primary 3D axis'.format(_ORIENT_PRIM_DESC_HEADER)

    ORIENT_PRIM_UV_AXIS_NAME = 'Primary UV Axis'
    ORIENT_PRIM_UV_AXIS_DESC = '{}. This parameter defines the primary UV axis'.format(_ORIENT_PRIM_DESC_HEADER)

    _ORIENT_SEC_DESC_HEADER = 'When orienting UVs to the 3D space, if primary axes matching fails for a given UV island, the packer will try to match the secondary 3D axis to the secondary UV axis for that island'

    ORIENT_SEC_3D_AXIS_NAME = 'Secondary 3D Axis'
    ORIENT_SEC_3D_AXIS_DESC = "{}. This parameter defines the secondary 3D axis. Note that the addon prevents setting '{}' and '{}' to the same value".format(_ORIENT_SEC_DESC_HEADER, ORIENT_PRIM_3D_AXIS_NAME, ORIENT_SEC_3D_AXIS_NAME)

    ORIENT_SEC_UV_AXIS_NAME = 'Secondary UV Axis'
    ORIENT_SEC_UV_AXIS_DESC = '{}. This parameter defines the secondary UV axis'.format(_ORIENT_SEC_DESC_HEADER)

    ORIENT_TO_3D_AXES_SPACE_NAME = '3D Axes Space'
    ORIENT_TO_3D_AXES_SPACE_DESC = "The 3D space to consider when orienting UV islands to the 3D space"

    ORIENT_PRIM_SEC_BIAS_NAME = 'Primary/Secondary Bias (deg)'
    ORIENT_PRIM_SEC_BIAS_DESC = "Angle (from 0 to 90 degrees) defining to what extent the packer favors orienting using the primary axes over the secondary axes. The greater value of this parameter, the more likely the packer will use the primary axes for orienting. The default value (80 degrees) should be optimal for most scenarios. Do not change the value of this parameter unless really needed. Technical explanation: the packer will orient UVs using secondary axes, only if the primary 3D axis is more perpendicular to the 3D geometry than the secondary 3D axis by the value of this parameter"

    FULLY_INSIDE_NAME='Only Islands Fully Inside'
    FULLY_INSIDE_DESC="Process only islands which are fully inside the UV target box"

    MOVE_ISLANDS_NAME='Move Box With Islands'
    MOVE_ISLANDS_DESC="Move the UV target box together with selected islands inside"

    TILE_X_NAME='Tile (X)'
    TILE_X_DESC='X coordinate of a tile to be set'

    TILE_Y_NAME='Tile (Y)'
    TILE_Y_DESC='Y coordinate of a tile to be set'

    TILE_COUNT_X_NAME='Tile Count (X)'
    TILE_COUNT_X_DESC='Number of tiles to use in the X direction'

    TILE_COUNT_Y_NAME='Tile Count (Y)'
    TILE_COUNT_Y_DESC='Number of tiles to use in the Y direction'

    CUSTOM_TARGET_BOX_ENABLE_NAME='Enable Custom Target Box'
    CUSTOM_TARGET_BOX_ENABLE_DESC='Pack to a custom box in the UV space'

    OVERRIDE_GLOBAL_OPTIONS_NAME='Override Global Options'
    OVERRIDE_GLOBAL_OPTIONS_DESC='Enable overriding of the global options for the given group'
    OVERRIDE_GLOBAL_OPTION_DESC='Override the given option for the given group'

    LAST_GROUP_COMPLEMENTARY_SUPPORTED_MSG="Supported only if '{}' is set to '{}' or '{}' and the grouping scheme has at least 2 groups".format(TEXEL_DENSITY_GROUP_POLICY_NAME, TEXEL_DENSITY_GROUP_POLICY_UNIFORM_NAME, TEXEL_DENSITY_GROUP_POLICY_AUTOMATIC_NAME)
    LAST_GROUP_COMPLEMENTARY_NAME='Last Group As Complementary'
    LAST_GROUP_COMPLEMENTARY_DESC="Automatically pack the last group on the top of all other groups. {}".format(LAST_GROUP_COMPLEMENTARY_SUPPORTED_MSG)

    GROUPS_TOGETHER_CONFIRM_MSG = 'WARNING: packing groups together requires the heuristic search to produce an optimal result - it is strongy recommended to enable it before continuing. Press OK to continue, click outside the pop-up to cancel the operation'

    SEED_NAME='Seed'
    TEST_PARAM_NAME='Test Parameter'
    WRITE_TO_FILE_NAME='Write UV Data To File'
    SIMPLIFY_DISABLE_NAME='Simplify Disable'
    WAIT_FOR_DEBUGGER_NAME='Wait For Debugger'

    ORIENT_AWARE_UV_ISLANDS_NAME = 'Orientation-Aware UV Islands'
    ORIENT_AWARE_UV_ISLANDS_DESC = 'This option defines the approach the packer uses to determine whether two UV faces belong to a single UV island.\n\nWhen the option is unchecked (the default state) - two UV faces will be considered as forming the same UV island, if they share at least one common UV vertex. When the option is checked, two faces will be considered as belonging to the same island, if they share a single edge and the edge orientation is opposite in both faces.\n\nThe default approach (the option unchecked) is equivalent to the way how Blender divides faces to islands but it can be problematic in some cases - for example when two islands of similar shape are stacked on top of each other, the default approach may merge both islands together (start considering both islands as a single island).\n\nIn such a situation enabling this option will solve the problem (prevent the islands from being merged)'

    ALLOW_INCONSISTENT_ISLANDS_NAME = 'Allow Inconsistent Islands'
    ALLOW_INCONSISTENT_ISLANDS_DESC = 'When the option is enabled, the packer will not raise an error when it finds an island with inconsistent per-island parameter assignment. Instead, it will take the parameter value assigned to the island face with the lowest face id as the value for the entire island. Press the help button for more info'

    HORI_MULTI_PANEL_TOGGLES_NAME='Horizontal Multi Panel Toggles'
    HORI_MULTI_PANEL_TOGGLES_DESC='Draw multi panel toggles horizontally in the UI'

    APPEND_MODE_NAME_TO_OP_LABEL_NAME="Append Mode To Operator Name"
    APPEND_MODE_NAME_TO_OP_LABEL_DESC="This option should only be enabled temporarily, only for the time when you want to add an UVPackmaster operator to Quick Favorites. If you add an operator with this option enabled, the selected mode name will be permanently appended to the operator name in the Quick Favorites list. After the operator was added, you can disable this option immediately"

    DONT_TRANSFORM_PINNED_UVS_NAME="Don't Transform Pinned UVs"
    DONT_TRANSFORM_PINNED_UVS_DESC='Do not transform pinned UVs during packing. WARNING: this option only applies to packing operations. Pinned UVs may still be transformed by other operations e.g. Align Similar'

    PINNED_UVS_AS_OTHERS_NAME="Pinned UVs As Others"
    PINNED_UVS_AS_OTHERS_DESC="Treat pinned UVs as 'others'. If the option is enabled when running the 'Pack To Others' operation, selected UVs will be packed so that they do not overlap pinned UVs"

    #UI options
    DISABLE_TIPS_NAME='Disable Tips'
    DISABLE_TIPS_DESC='Do not display usage tips in operation output'

    FONT_SIZE_TEXT_OUTPUT_NAME='Font Size (Text Output)'
    FONT_SIZE_TEXT_OUTPUT_DESC='Sets the font size for the operation text output'

    FONT_SIZE_UV_OVERLAY_NAME='Font Size (UV Overlay)'
    FONT_SIZE_UV_OVERLAY_DESC='Sets the font size for text rendered over UV islands (e.g. per-island parameter values)'

    BOX_RENDER_LINE_WIDTH_NAME="Box Border Width"
    BOX_RENDER_LINE_WIDTH_DESC="Determines the width of box borders rendered in the UV editor during the operation. WARNING: setting width to a low value is not recommended"

    SHORT_ISLAND_OPERATOR_NAMES_NAME='Short Island Operator Names'
    SHORT_ISLAND_OPERATOR_NAMES_DESC="Make island parameter operator names in the UI shorter. For example: change the name 'Set Rotation Step' to 'Set', the name 'Reset Rotation Step' to 'Reset' etc"

    # Expert options
    SHOW_EXPERT_OPTIONS_NAME = 'Show Expert Options'
    SHOW_EXPERT_OPTIONS_DESC = ''

    DISABLE_IMMEDIATE_UV_UPDATE_NAME = 'Disable Immediate UV Update'
    DISABLE_IMMEDIATE_UV_UPDATE_DESC = 'By default, when performing a heuristic search, the packer updates the UV map in Blender immediately as soon as it finds a better result. When this option is enabled, the packer will not do such immediate updates - it will only report the area, when a better result is found, but the UV map will stay intact in Blender during the entire search. The UV map will be updated with the best result only once, after the search is done.\n\nThe purpose of this option is to optimize the packer operation, when packing a UV map containing a huge number of UV faces (a few millions and more) - it should NOT be used during the standard packer usage'

    OTHER_ISLANDS_DESC = "'Other' islands are: 1. unselected islands 2. pinned islands if the '{}' option is enabled (in the Addon Preferences multi panel)".format(PINNED_UVS_AS_OTHERS_NAME)

    PACK_OP_TYPE_PACK_DESC = "Pack selected UV islands into the target UV area. 'Other' islands will be ignored.\n\n{}".format(OTHER_ISLANDS_DESC)
    PACK_OP_TYPE_PACK_TO_OTHERS_DESC = "Pack selected UV islands into the target UV area so that they do not overlap with 'Other' islands.\n\n{}".format(OTHER_ISLANDS_DESC)
    PACK_OP_TYPE_REPACK_WITH_OTHERS_DESC = "Repack selected UV islands into the target UV area together will all unselected islands which are already placed in the target area (or overlap the area by some part). Unselected islands which do not overlap the target area will be ignored.\n\nIf the '{}' option is enabled (in the Addon Preferences multi panel), islands will be packed so they do not overlap with pinned islands".format(PINNED_UVS_AS_OTHERS_NAME)
