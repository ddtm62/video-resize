#PY  <- Needed to identify #
#--automatically built--

adm = Avidemux()
adm.setPostProc(3, 3, 0)
adm.videoCodec("x264", "useAdvancedConfiguration=True", "general.params=AQ=28", "general.threads=0", "general.preset=ultrafast", "general.tuning=none", "general.profile=baseline", "general.fast_decode=False", "general.zero_latency=False"
, "general.fast_first_pass=True", "general.blueray_compatibility=False", "general.fake_interlaced=False", "level=-1", "vui.sar_height=1", "vui.sar_width=1", "MaxRefFrames=3", "MinIdr=25", "MaxIdr=250"
, "i_scenecut_threshold=40", "intra_refresh=False", "MaxBFrame=3", "i_bframe_adaptive=1", "i_bframe_bias=0", "i_bframe_pyramid=2", "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0", "i_deblocking_filter_beta=0"
, "cabac=True", "interlaced=False", "constrained_intra=False", "tff=True", "fake_interlaced=False", "analyze.b_8x8=True", "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=True", "analyze.b_p16x16=False"
, "analyze.b_b16x16=False", "analyze.weighted_pred=2", "analyze.weighted_bipred=True", "analyze.direct_mv_pred=1", "analyze.chroma_offset=0", "analyze.me_method=1", "analyze.me_range=16", "analyze.mv_range=-1"
, "analyze.mv_range_thread=-1", "analyze.subpel_refine=7", "analyze.chroma_me=True", "analyze.mixed_references=True", "analyze.trellis=1", "analyze.psy_rd=1.000000", "analyze.psy_trellis=0.000000", "analyze.fast_pskip=True"
, "analyze.dct_decimate=True", "analyze.noise_reduction=0", "analyze.psy=True", "analyze.intra_luma=11", "analyze.inter_luma=21", "ratecontrol.rc_method=0", "ratecontrol.qp_constant=0", "ratecontrol.qp_min=10"
, "ratecontrol.qp_max=51", "ratecontrol.qp_step=4", "ratecontrol.bitrate=0", "ratecontrol.rate_tolerance=1.000000", "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0", "ratecontrol.vbv_buffer_init=1"
, "ratecontrol.ip_factor=1.400000", "ratecontrol.pb_factor=1.300000", "ratecontrol.aq_mode=1", "ratecontrol.aq_strength=1.000000", "ratecontrol.mb_tree=True", "ratecontrol.lookahead=40")
w = adm.getWidth()
h = adm.getHeight()
top="top=0"
bottom="bottom=0"
left="left=0"
right="right=0"
crop = False
if w/h > 720/480:
  nh = 480
  nw = int(round(30*w/h))*16 # 480/16 = 30
  if nw > 720:
    crop = True
    l = int((nw-720)/2)
    left="left="+str(l)
    right="right="+str(nw-720-l)
else:
  nw = 720
  nh = int(round(45*h/w))*16 # 720/16 = 45
  if nh > 480:
    crop = True
    t = int((nh-480)/2)
    top="top="+str(t)
    bottom="bottom="+str(nh-480-t)
sw = "width="+str(nw)
sh = "height="+str(nh)
adm.clearVideoFilters()
adm.addVideoFilter("swscale", sw, sh, "algo=0", "sourceAR=0", "targetAR=0", "lockAR=FALSE", "roundup=False")
if crop:
  adm.addVideoFilter("crop", top, bottom, left, right, "rubber_is_hidden=False")
adm.audioClearTracks()
adm.setSourceTrackLanguage(0,"und")
adm.audioAddTrack(0)
adm.audioCodec(0, "LavAAC", "bitrate=56");
adm.audioSetMixer(0, "MONO");
adm.audioSetDrc(0, 0)
adm.audioSetShift(0, 0, 0)
adm.setContainer("MP4", "muxerType=0", "optimize=1", "forceAspectRatio=False", "aspectRatio=1", "rotation=0")
