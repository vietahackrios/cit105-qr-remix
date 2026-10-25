"""CIT 105 QR remix with custom colors."""
import io
import qrcode
import streamlit as st
from qrcode.exceptions import DataOverflowError


def luminance(color):
    """Convert hex color to relative luminance."""
    rgb = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def make_png(text, foreground, background):
    """Encode text into PNG bytes with a four-module quiet zone."""
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,
                       box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    image = qr.make_image(fill_color=foreground, back_color=background).convert('RGB')
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    return buffer.getvalue()


def main():
    st.set_page_config(page_title='Cream & Blue QR Studio', layout='centered')
    st.caption('CIT 105 | QR CODE REMIX')
    st.title('Cream & Blue QR Studio')
    st.write('Turn a link or message into a QR code with your own colors.')
    with st.sidebar:
        st.header('Your colors')
        foreground = st.color_picker('QR color', '#173B63')
        background = st.color_picker('Background color', '#FFF5E4')
        st.caption('Deep blue ink on warm cream.')
    text = st.text_area('Link or text', placeholder='https://example.com', height=100)
    st.caption('For a website, include https://. Your exact text is encoded.')
    if not text.strip():
        st.info('Enter a link or text to create your QR code.')
        return
    dark, light = luminance(foreground), luminance(background)
    contrast = (max(dark, light) + 0.05) / (min(dark, light) + 0.05)
    if dark >= light or contrast < 4.5:
        st.warning('Choose a darker QR color and a lighter background with stronger contrast.')
        st.caption('This design check does not replace scanning with your phone.')
        return
    try:
        png = make_png(text, foreground, background)
    except DataOverflowError:
        st.error('Too much text for one QR code. Try a shorter message or link.')
        return
    st.subheader('Your QR code')
    st.image(png, width=320, caption='Scan with your phone to check the result.')
    st.download_button('Download QR as PNG', data=png,
                       file_name='cream-blue-qr.png', mime='image/png')
    st.caption('Your preview and download use the same image.')


if __name__ == '__main__':
    main()
