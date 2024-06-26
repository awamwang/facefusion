import multiprocessing
import gradio
import os

from facefusion.uis.components import about, frame_processors, frame_processors_options, execution, execution_thread_count, execution_queue_count, memory, temp_frame, output_options, common_options, source, target, output, preview, trim_frame, face_analyser, face_selector, face_masker


def pre_check() -> bool:
	return True


def pre_render() -> bool:
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 2):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					frame_processors.render()
				with gradio.Blocks():
					frame_processors_options.render()
				with gradio.Blocks():
					execution.render()
					execution_thread_count.render()
					execution_queue_count.render()
				with gradio.Blocks():
					memory.render()
				with gradio.Blocks():
					temp_frame.render()
				with gradio.Blocks():
					output_options.render()
			with gradio.Column(scale = 2):
				with gradio.Blocks():
					source.render()
				with gradio.Blocks():
					target.render()
				with gradio.Blocks():
					output.render()
			with gradio.Column(scale = 3):
				with gradio.Blocks():
					preview.render()
				with gradio.Blocks():
					trim_frame.render()
				with gradio.Blocks():
					face_selector.render()
				with gradio.Blocks():
					face_masker.render()
				with gradio.Blocks():
					face_analyser.render()
				with gradio.Blocks():
					common_options.render()
	return layout


def listen() -> None:
	frame_processors.listen()
	frame_processors_options.listen()
	execution.listen()
	execution_thread_count.listen()
	execution_queue_count.listen()
	memory.listen()
	temp_frame.listen()
	output_options.listen()
	source.listen()
	target.listen()
	output.listen()
	preview.listen()
	trim_frame.listen()
	face_selector.listen()
	face_masker.listen()
	face_analyser.listen()
	common_options.listen()


def run(ui : gradio.Blocks) -> None:
    address = os.getenv('GRADIO_SERVER_ADDRESS', '127.0.0.1')
    port = int(os.getenv('GRADIO_SERVER_PORT', 7860))
    if os.name == 'nt' and address == '0.0.0.0':
        address = '127.0.0.1'

    print(f'Listening on http://{address}:{port}')
    ui.launch(show_api = False, server_name = address, server_port = port)
    # ui.launch(show_api = False, server_name = address, server_port = port, quiet=True, share=True)
    # ui.launch(show_api=False, quiet=True)
    concurrency_count = min(8, multiprocessing.cpu_count())
    ui.queue(concurrency_count = concurrency_count).launch(show_api = False, server_name = address, server_port = port, quiet = True)
