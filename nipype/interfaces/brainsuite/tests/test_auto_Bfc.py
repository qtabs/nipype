# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brainsuite import Bfc


def test_Bfc_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        biasEstimateConvergenceThreshold=dict(argstr='--beps %f', ),
        biasEstimateSpacing=dict(argstr='-s %d', ),
        biasFieldEstimatesOutputPrefix=dict(argstr='--biasprefix %s', ),
        biasRange=dict(argstr='%s', ),
        controlPointSpacing=dict(argstr='-c %d', ),
        convergenceThreshold=dict(argstr='--eps %f', ),
        correctWholeVolume=dict(argstr='--extrapolate', ),
        correctedImagesOutputPrefix=dict(argstr='--prefix %s', ),
        correctionScheduleFile=dict(argstr='--schedule %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        histogramRadius=dict(argstr='-r %d', ),
        histogramType=dict(argstr='%s', ),
        inputMRIFile=dict(
            argstr='-i %s',
            mandatory=True,
        ),
        inputMaskFile=dict(
            argstr='-m %s',
            hash_files=False,
        ),
        intermediate_file_type=dict(argstr='%s', ),
        iterativeMode=dict(argstr='--iterate', ),
        maxBias=dict(
            argstr='-U %f',
            usedefault=True,
        ),
        minBias=dict(
            argstr='-L %f',
            usedefault=True,
        ),
        outputBiasField=dict(
            argstr='--bias %s',
            hash_files=False,
        ),
        outputMRIVolume=dict(
            argstr='-o %s',
            genfile=True,
            hash_files=False,
        ),
        outputMaskedBiasField=dict(
            argstr='--maskedbias %s',
            hash_files=False,
        ),
        splineLambda=dict(argstr='-w %f', ),
        timer=dict(argstr='--timer', ),
        verbosityLevel=dict(argstr='-v %d', ),
    )
    inputs = Bfc.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Bfc_outputs():
    output_map = dict(
        correctionScheduleFile=dict(),
        outputBiasField=dict(),
        outputMRIVolume=dict(),
        outputMaskedBiasField=dict(),
    )
    outputs = Bfc.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
