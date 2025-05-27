from pdfrw import PdfReader, PdfWriter, PageMerge

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = PdfReader(input_pdf_path)
    
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        if annotations:
            for annotation in annotations:
                if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY and annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]  # remove parentheses
                    if key in data_dict:
                        annotation.update(
                            {
                                ANNOT_VAL_KEY: f'({data_dict[key]})'
                            }
                        )
    PdfWriter().write(output_pdf_path, template_pdf)

# Örnek kullanım
form_data = {
    "Name": "Ahmet Yılmaz",
    "Age": "25",
    "City": "İstanbul"
}

fill_pdf("form.pdf", "filled_form.pdf", form_data)
