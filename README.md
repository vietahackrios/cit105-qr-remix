# Cream and Blue QR Studio

CIT 105 QR remix. New feature: foreground and background color pickers, default blue #173B63 and cream #FFF5E4. The interface uses the same palette.

Run from this project folder:

    python -m pip install -r requirements.txt
    python -m streamlit run app.py

In a PyCharm Python run configuration use module name streamlit, parameters run app.py, and this folder as working directory. Do not run app.py as an ordinary script.

The QR is generated in memory and the preview and download use identical PNG bytes. A four-module quiet zone is preserved. A conservative contrast check rejects dark backgrounds or weak contrast; it does not guarantee scanning. Long payloads show a readable error.

Verification: the student reported that the app opens, the on-screen QR scans and opens the entered link, and the color controls work. Scanning the downloaded PNG and additional edge cases remain to be checked. Syntax, theme configuration, and default color contrast were checked during preparation.

Before submission: download and scan the image, try equal colors, clear the input, and verify decoded text. Record the five-minute walkthrough and send the repository and video links to the professor.

References:
https://docs.streamlit.io/develop/api-reference/widgets/st.color_picker
https://docs.streamlit.io/develop/api-reference/widgets/st.download_button
