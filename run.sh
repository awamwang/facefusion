# python run.py --execution-providers cuda --face-swapper-model inswapper_128 \
#   --output-video-resolution 1080x1920 --face-mask-padding 5 --execution-thread-count 8 --video-memory-strategy moderate --face-selector-mode one \
#   & ssh -R 80:localhost:7860 remote.moe

# python run.py --execution-providers cuda --face-swapper-model inswapper_128 & ssh -R 80:localhost:7860 remote.moe


# nohup python run.py --face-swapper-model inswapper_128 >core.log 2>&1 &

# ssh -R 80:localhost:7860 remote.moe '' >web.log 2>&1 &

# nohup ssh -R 80:localhost:7860 remote.moe '' >web.log 2>&1 &

# source .venv/bin/activate
rm /tmp/gradio/ -rf && rm /tmp/facefusion/ -rf
echo "" > core.log
killall -9 python
echo "清理环境完成"
nohup python run.py >core.log 2>&1 &
echo "启动完成"