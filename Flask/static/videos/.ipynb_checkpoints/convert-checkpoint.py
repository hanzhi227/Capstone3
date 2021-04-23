import ffmpy
ff = ffmpy.FFmpeg(
    inputs={'results.avi': None},
    outputs={'results.mp4': None}
)
ff.run()