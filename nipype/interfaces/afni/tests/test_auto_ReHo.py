# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import ReHo


def test_ReHo_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        chi_sq=dict(argstr='-chi_sq', ),
        ellipsoid=dict(
            argstr='-neigh_X %s -neigh_Y %s -neigh_Z %s',
            xor=['sphere', 'neighborhood'],
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-inset %s',
            mandatory=True,
            position=1,
        ),
        label_set=dict(argstr='-in_rois %s', ),
        mask=dict(argstr='-mask %s', ),
        neighborhood=dict(
            argstr='-nneigh %s',
            xor=['sphere', 'ellipsoid'],
        ),
        out_file=dict(
            argstr='-prefix %s',
            keep_extension=True,
            name_source='in_file',
            name_template='%s_localstat',
            position=0,
        ),
        overwrite=dict(argstr='-overwrite', ),
        sphere=dict(
            argstr='-neigh_RAD %s',
            xor=['neighborhood', 'ellipsoid'],
        ),
    )
    inputs = ReHo.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ReHo_outputs():
    output_map = dict(
        out_file=dict(),
        out_vals=dict(),
    )
    outputs = ReHo.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
