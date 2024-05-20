import gradio as gr
import pywhatkit
import datetime

def send_message(phone, message,time_hour,time_min):
    try:
        phone = f"+91{phone}"
        current_time = datetime.datetime.now()
        if time_hour < current_time.hour or (time_hour == current_time.hour and time_min <= current_time.minute):
            time_hour += 1
            if time_hour == 24:
                time_hour = 0
        pywhatkit.sendwhatmsg(phone, message, time_hour, time_min,20,True,20)
        return "Message sent successfully!"
   
   
   
    except Exception as e:
        return f"Error: {e}"


iface = gr.Interface(
    fn=send_message,
    inputs=[gr.Number(label="Phone Number"), gr.Textbox(label="Message"),gr.Number(label="Time Hour"),gr.Number(label="Time Minutes")],
    outputs="text",
    title="Send WhatsApp Message",
    description="Enter the phone number and message and click submit to send the message."
)
iface.launch()