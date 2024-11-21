from interface.gradio_ui import build_interface

if __name__ == "__main__":
    interface = build_interface()
    interface.launch(share=True)
