import gradio as gr
from utils.camera_utils import capture_image
from utils.azure_api import classify_image
from utils.parqueadero import Parqueadero
import cv2

# Instancia global del parqueadero
parqueadero = None  # Inicialmente vacío


def configurar_parqueadero(cupos_carros, cupos_motos,entrada_salida):
    """
    Configura los cupos iniciales del parqueadero.
    """
    global parqueadero
    parqueadero = Parqueadero(cupos_carros, cupos_motos)
    return f"Esta es la {entrada_salida} de un parqueadero configurado con {cupos_carros} cupos para carros y {cupos_motos} cupos para motos."


def process_image(entrada_salida):
    """
    Captura una imagen y gestiona la entrada al parqueadero.
    """
    try:
        if parqueadero is None:
            return "El parqueadero no ha sido configurado."

        # Capturar imagen usando la cámara
        image = capture_image()

        # Convierte la imagen en bytes para enviarla a Azure
        _, encoded_image = cv2.imencode('.jpg', image)  # Aquí se usa cv2
        image_bytes = encoded_image.tobytes()

        # Clasifica la imagen con Azure
        result = classify_image(image_bytes)

        # Procesa la entrada al parqueadero
        return parqueadero.ingresar_vehiculo(result,entrada_salida)

    except Exception as e:
        return f"Error al procesar la imagen: {str(e)}"


def liberar_cupo(tipo_vehiculo):
    """
    Libera un cupo del parqueadero.
    """
    if parqueadero is None:
        return "El parqueadero no ha sido configurado."

    return parqueadero.liberar_cupo(tipo_vehiculo)


def build_interface():
    """
    Construye la interfaz de usuario con Gradio.
    """
    with gr.Blocks() as demo:
        gr.Markdown("# Sistema de Clasificación y Parqueo")
        gr.Markdown("### Configuración del parqueadero")

        # Configuración de cupos
        with gr.Row():
            cupos_carros_input = gr.Number(value=10, label="Cupos para carros", precision=0)
            cupos_motos_input = gr.Number(value=10, label="Cupos para motos", precision=0)
            entrada_salida_input=gr.Dropdown(label="Selecciona si es la entrada o la salida del parqueadero",choices=["Entrada","Salida"])
            configurar_button = gr.Button("Configurar parqueadero")
            

        configurar_output = gr.Textbox(label="Resultado de Configuración", interactive=False)
        configurar_button.click(
            configurar_parqueadero,
            inputs=[cupos_carros_input, cupos_motos_input,entrada_salida_input],
            outputs=configurar_output,
        )

        # Clasificación de vehículos
        gr.Markdown("### Clasificación de vehículos")
        classify_button = gr.Button("Detectar Vehículo")
        classify_output = gr.Textbox(label="Resultado de Clasificación", interactive=False)
        classify_button.click(process_image, inputs=[entrada_salida_input], outputs=classify_output)

        # Liberación de cupos
        gr.Markdown("### Liberación de cupos")
        tipo_vehiculo_input = gr.Radio(choices=["carro", "moto"], label="Tipo de Vehículo")
        liberar_button = gr.Button("Liberar Cupo")
        liberar_output = gr.Textbox(label="Resultado de Liberación", interactive=False)
        liberar_button.click(liberar_cupo, inputs=tipo_vehiculo_input, outputs=liberar_output)
 

    return demo