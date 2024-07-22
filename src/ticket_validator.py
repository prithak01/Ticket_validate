from datetime import datetime
from mapping_dict import train_type_mapping, class_mapping, concession_type_mapping

    # Defining a dictionary for common OCR misinterpretations
char_equivalences = {
    '0': ['0', 'O'],
    'O': ['0', 'O'],
    '1': ['1', 'I', 'l'],
    'I': ['1', 'I', 'l'],
    'l': ['1', 'I', 'l'],
    '5': ['5', 'S'],
    'S': ['5', 'S'],
    '8': ['8', 'B'],
    'B': ['8', 'B'],
    '6': ['6', 'G'],
    'G': ['6', 'G'],
    '2': ['2', 'Z'],
    'Z': ['2', 'Z'],
    '7': ['7', 'T'],
    'T': ['7', 'T']
    }

def preprocess_ocr_output(ocr_text):
    possible_variants = ['']
    for char in ocr_text:
        if char in char_equivalences:
            new_variants = []
            for variant in possible_variants:
                for equivalent in char_equivalences[char]:
                    new_variants.append(variant + equivalent)
            possible_variants = new_variants
        else:
            possible_variants = [variant + char for variant in possible_variants]
    return possible_variants

def validate_ticket(ticket_data):
    is_valid = True
    reasons = []


    # Check if the UTS number is present
    if 'uts_no' not in ticket_data:
        is_valid = False
        reasons.append("UTS No. is missing")
    else:
        # Preprocess the UTS number to handle OCR misinterpretations
        uts_no_variants = preprocess_ocr_output(ticket_data['uts_no'])
        # Perform validation using the variants
        if not any(variant in demo_database for variant in uts_no_variants):
            is_valid = False
            reasons.append("UTS No. is invalid")

    return {
        'is_valid': is_valid,
        'reasons': reasons
    }





# def validate_ticket(ticket_info, db_info):
#     validation_results = {}
#     if not db_info:
#         validation_results['exists'] = False
#         validation_results['errors'] = ['Ticket number does not exist']
#         return validation_results

#     validation_results['exists'] = True
#     validation_results['errors'] = []

#     # Check for date, time, and station conflicts
#     if ticket_info['date'] != db_info['date']:
#         validation_results['errors'].append('Wrong date')
#     if ticket_info['time'] != db_info['time']:
#         validation_results['errors'].append('Wrong time')
#     if ticket_info['station'] != db_info['station']:
#         validation_results['errors'].append('Wrong station')

#     return validation_results

