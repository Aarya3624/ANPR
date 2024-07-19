# # import string
# # import easyocr

# # reader = easyocr.Reader(['en'], gpu=True)

# # dict_char_to_int = {
# #     "O": '0',
# #     "I": '1',
# #     'J': '3',
# #     'A': '4',
# #     "G": '6',
# #     "S": '5'
# # }

# # dict_int_to_char = {
# #     '0': 'O',
# #     '1': 'I',
# #     '3': 'J',
# #     '4': 'A',
# #     '6': 'G',
# #     '5': 'S'
# # }

# # def get_car(license_plate, vehicle_track_ids):
# #     x1, y1, x2, y2, score, class_id = license_plate

# #     foundIt = False
# #     for j in range(len(vehicle_track_ids)):
# #         xcar1, ycar1, xcar2, ycar2, car_id = vehicle_track_ids[j]

# #         if x1 > xcar1 and y1 > ycar1 and x2 < xcar2 and y2 < ycar2:
# #             car_indx = j
# #             foundIt = True
# #             break

# #     if foundIt:
# #         return vehicle_track_ids[car_indx]

# #     return -1, -1, -1, -1, -1

# # def license_complies_format(text):
# #     if len(text) == 7:
# #         if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
# #            (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
# #            (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
# #            (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
# #            (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
# #            (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
# #            (text[6] in string.ascii_uppercase or text[6] in dict_int_to_char.keys()):
# #             return True, 1

# #     elif len(text) == 10:
# #         if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
# #            (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
# #            (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
# #            (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
# #            (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
# #            (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
# #            (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[6] in dict_char_to_int.keys()) and \
# #            (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[7] in dict_char_to_int.keys()) and \
# #            (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[8] in dict_char_to_int.keys()) and \
# #            (text[9] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[9] in dict_char_to_int.keys()):
# #             return True, 2
    
# #     elif len(text) == 9:
# #         if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
# #            (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
# #            (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
# #            (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
# #            (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
# #            (text[5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[5] in dict_char_to_int.keys()) and \
# #            (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[6] in dict_char_to_int.keys()) and \
# #            (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[7] in dict_char_to_int.keys()) and \
# #            (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[8] in dict_char_to_int.keys()):
# #             return True, 3

# #     else: return False, 0

# # def format_license(text, type):
# #     license_plate_ = ''
# #     if type == 1:
# #         mapping = {
# #             0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char, 6: dict_int_to_char,
# #             2: dict_char_to_int, 3: dict_char_to_int
# #         }
# #         for j in range(7):
# #             if text[j] in mapping[j].keys():
# #                 license_plate_ += mapping[j][text[j]]
# #             else:
# #                 license_plate_ += text[j]


# #     elif type == 2:
# #         mapping = {
# #             0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char,
# #             2: dict_char_to_int, 3: dict_char_to_int, 6: dict_char_to_int, 7: dict_char_to_int, 8: dict_char_to_int, 9: dict_char_to_int
# #         }
# #         for j in range(7):
# #             if text[j] in mapping[j].keys():
# #                 license_plate_ += mapping[j][text[j]]
# #             else:
# #                 license_plate_ += text[j]

# #     elif type == 3:
# #         mapping = {
# #             0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char,
# #             2: dict_char_to_int, 3: dict_char_to_int, 5: dict_char_to_int, 6: dict_char_to_int, 7: dict_char_to_int, 8: dict_char_to_int
# #         }
# #         for j in range(9):
# #             if text[j] in mapping[j].keys():
# #                 license_plate_ += mapping[j][text[j]]
# #             else:
# #                 license_plate_ += text[j]

# #     return license_plate_

# # def read_license_plate(license_plate_crop):
# #     detections = reader.readtext(license_plate_crop)

# #     for detection in detections:
# #         bbox, text, score = detection

# #         text = text.upper().replace(' ', '')

# #         complies, type = license_complies_format(text)
# #         if complies:
# #             return format_license(text, type), score

# #     return None, None

# # def write_csv(results, output_path):
# #     with open(output_path, 'w') as f:
# #         f.write('{},{},{},{},{},{},{}\n'.format('frame_nmr', 'car_id', 'car_bbox',
# #                                                 'license_plate_bbox', 'license_plate_bbox_score', 'license_number',
# #                                                 'license_number_score'))

# #         for frame_nmr in results.keys():
# #             for car_id in results[frame_nmr].keys():
# #                 if 'car' in results[frame_nmr][car_id].keys() and \
# #                    'license_plate' in results[frame_nmr][car_id].keys() and \
# #                    'text' in results[frame_nmr][car_id]['license_plate'].keys():
# #                     f.write('{},{},{},{},{},{},{}\n'.format(frame_nmr,
# #                                                             car_id,
# #                                                             '[{} {} {} {}]'.format(
# #                                                                 results[frame_nmr][car_id]['car']['bbox'][0],
# #                                                                 results[frame_nmr][car_id]['car']['bbox'][1],
# #                                                                 results[frame_nmr][car_id]['car']['bbox'][2],
# #                                                                 results[frame_nmr][car_id]['car']['bbox'][3]),
# #                                                             '[{} {} {} {}]'.format(
# #                                                                 results[frame_nmr][car_id]['license_plate']['bbox'][0],
# #                                                                 results[frame_nmr][car_id]['license_plate']['bbox'][1],
# #                                                                 results[frame_nmr][car_id]['license_plate']['bbox'][2],
# #                                                                 results[frame_nmr][car_id]['license_plate']['bbox'][3]),
# #                                                             results[frame_nmr][car_id]['license_plate']['bbox_score'],
# #                                                             results[frame_nmr][car_id]['license_plate']['text'],
# #                                                             results[frame_nmr][car_id]['license_plate']['text_score'])
# #                             )
# #         f.close()


# import string
# import easyocr

# reader = easyocr.Reader(['en'], gpu=True)

# dict_char_to_int = {
#     "O": '0',
#     "I": '1',
#     'J': '3',
#     'A': '4',
#     "G": '6',
#     "S": '5'
# }

# dict_int_to_char = {
#     '0': 'O',
#     '1': 'I',
#     '3': 'J',
#     '4': 'A',
#     '6': 'G',
#     '5': 'S'
# }

# def get_car(license_plate, vehicle_track_ids):
#     x1, y1, x2, y2, score, class_id = license_plate

#     foundIt = False
#     for j in range(len(vehicle_track_ids)):
#         xcar1, ycar1, xcar2, ycar2, car_id = vehicle_track_ids[j]

#         if x1 > xcar1 and y1 > ycar1 and x2 < xcar2 and y2 < ycar2:
#             car_indx = j
#             foundIt = True
#             break

#     if foundIt:
#         return vehicle_track_ids[car_indx]

#     return -1, -1, -1, -1, -1

# def license_complies_format(text):
#     if len(text) == 7:
#         if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
#            (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
#            (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
#            (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
#            (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
#            (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
#            (text[6] in string.ascii_uppercase or text[6] in dict_int_to_char.keys()):
#             return True, 1

#     elif len(text) == 10:
#         if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
#            (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
#            (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
#            (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
#            (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
#            (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
#            (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[6] in dict_char_to_int.keys()) and \
#            (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[7] in dict_char_to_int.keys()) and \
#            (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[8] in dict_char_to_int.keys()) and \
#            (text[9] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[9] in dict_char_to_int.keys()):
#             return True, 2
    
#     elif len(text) == 9:
#         if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
#            (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
#            (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
#            (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
#            (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
#            (text[5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[5] in dict_char_to_int.keys()) and \
#            (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[6] in dict_char_to_int.keys()) and \
#            (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[7] in dict_char_to_int.keys()) and \
#            (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[8] in dict_char_to_int.keys()):
#             return True, 3

#     return False, 0

# def format_license(text, type):
#     license_plate_ = ''
#     if type == 1:
#         mapping = {
#             0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char, 6: dict_int_to_char,
#             2: dict_char_to_int, 3: dict_char_to_int
#         }
#         for j in range(7):
#             if text[j] in mapping[j].keys():
#                 license_plate_ += mapping[j][text[j]]
#             else:
#                 license_plate_ += text[j]

#     elif type == 2:
#         mapping = {
#             0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char,
#             2: dict_char_to_int, 3: dict_char_to_int, 6: dict_char_to_int, 7: dict_char_to_int, 8: dict_char_to_int, 9: dict_char_to_int
#         }
#         for j in range(10):
#             if text[j] in mapping[j].keys():
#                 license_plate_ += mapping[j][text[j]]
#             else:
#                 license_plate_ += text[j]

#     elif type == 3:
#         mapping = {
#             0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char,
#             2: dict_char_to_int, 3: dict_char_to_int, 5: dict_char_to_int, 6: dict_char_to_int, 7: dict_char_to_int, 8: dict_char_to_int
#         }
#         for j in range(9):
#             if text[j] in mapping[j].keys():
#                 license_plate_ += mapping[j][text[j]]
#             else:
#                 license_plate_ += text[j]

#     return license_plate_

# def read_license_plate(license_plate_crop):
#     detections = reader.readtext(license_plate_crop)

#     for detection in detections:
#         bbox, text, score = detection

#         text = text.upper().replace(' ', '')

#         complies, type = license_complies_format(text)
#         if complies:
#             return format_license(text, type), score

#     return None, None

# def write_csv(results, output_path):
#     with open(output_path, 'w') as f:
#         f.write('{},{},{},{},{},{},{}\n'.format('frame_nmr', 'car_id', 'car_bbox',
#                                                 'license_plate_bbox', 'license_plate_bbox_score', 'license_number',
#                                                 'license_number_score'))

#         for frame_nmr in results.keys():
#             for car_id in results[frame_nmr].keys():
#                 if 'car' in results[frame_nmr][car_id].keys() and \
#                    'license_plate' in results[frame_nmr][car_id].keys() and \
#                    'text' in results[frame_nmr][car_id]['license_plate'].keys():
#                     f.write('{},{},{},{},{},{},{}\n'.format(frame_nmr,
#                                                             car_id,
#                                                             '[{} {} {} {}]'.format(
#                                                                 results[frame_nmr][car_id]['car']['bbox'][0],
#                                                                 results[frame_nmr][car_id]['car']['bbox'][1],
#                                                                 results[frame_nmr][car_id]['car']['bbox'][2],
#                                                                 results[frame_nmr][car_id]['car']['bbox'][3]),
#                                                             '[{} {} {} {}]'.format(
#                                                                 results[frame_nmr][car_id]['license_plate']['bbox'][0],
#                                                                 results[frame_nmr][car_id]['license_plate']['bbox'][1],
#                                                                 results[frame_nmr][car_id]['license_plate']['bbox'][2],
#                                                                 results[frame_nmr][car_id]['license_plate']['bbox'][3]),
#                                                             results[frame_nmr][car_id]['license_plate']['bbox_score'],
#                                                             results[frame_nmr][car_id]['license_plate']['text'],
#                                                             results[frame_nmr][car_id]['license_plate']['text_score'])
#                             )
#         f.close()

# # Example usage:
# # frame_number = 1
# # car_id = 1
# # car_bbox = (10, 10, 100, 100)
# # license_plate_bbox = (20, 20, 80, 80)
# # license_plate_score = 0.9
# # license_plate_crop = ...  # Your license plate image crop
# # license_text, text_score = read_license_plate(license_plate_crop)

# # results = {frame_number: {car_id: {'car': car_bbox, 'license_plate': {'bbox': license_plate_bbox, 'score': license_plate_score, 'text': license_text, 'text_score': text_score}}}}
# # write_csv(results, 'output.csv')


import string
import easyocr

reader = easyocr.Reader(['en'], gpu=True)

dict_char_to_int = {
    "O": '0',
    "I": '1',
    'J': '3',
    'A': '4',
    "G": '6',
    "S": '5'
}

dict_int_to_char = {
    '0': 'O',
    '1': 'I',
    '3': 'J',
    '4': 'A',
    '6': 'G',
    '5': 'S'
}

def get_car(license_plate, vehicle_track_ids):
    x1, y1, x2, y2, score, class_id = license_plate

    for j in range(len(vehicle_track_ids)):
        xcar1, ycar1, xcar2, ycar2, car_id = vehicle_track_ids[j]

        if x1 > xcar1 and y1 > ycar1 and x2 < xcar2 and y2 < ycar2:
            return vehicle_track_ids[j]

    return -1, -1, -1, -1, -1

def license_complies_format(text):
    if len(text) == 7:
        if all((text[i] in string.ascii_uppercase or text[i] in dict_int_to_char.keys()) for i in [0, 1, 4, 5, 6]) and \
           all((text[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[i] in dict_char_to_int.keys()) for i in [2, 3]):
            return True, 1

    elif len(text) == 10:
        if all((text[i] in string.ascii_uppercase or text[i] in dict_int_to_char.keys()) for i in [0, 1, 4, 5]) and \
           all((text[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[i] in dict_char_to_int.keys()) for i in [2, 3, 6, 7, 8, 9]):
            return True, 2

    elif len(text) == 9:
        if all((text[i] in string.ascii_uppercase or text[i] in dict_int_to_char.keys()) for i in [0, 1, 4]) and \
           all((text[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[i] in dict_char_to_int.keys()) for i in [2, 3, 5, 6, 7, 8]):
            return True, 3

    return False, 0

def format_license(text, type):
    license_plate_ = ''
    if type == 1:
        mapping = {
            0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char, 6: dict_int_to_char,
            2: dict_char_to_int, 3: dict_char_to_int
        }
        for j in range(7):
            license_plate_ += mapping.get(j, {}).get(text[j], text[j])

    elif type == 2:
        mapping = {
            0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char,
            2: dict_char_to_int, 3: dict_char_to_int, 6: dict_char_to_int, 7: dict_char_to_int, 8: dict_char_to_int, 9: dict_char_to_int
        }
        for j in range(10):
            license_plate_ += mapping.get(j, {}).get(text[j], text[j])

    elif type == 3:
        mapping = {
            0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char,
            2: dict_char_to_int, 3: dict_char_to_int, 5: dict_char_to_int, 6: dict_char_to_int, 7: dict_char_to_int, 8: dict_char_to_int
        }
        for j in range(9):
            license_plate_ += mapping.get(j, {}).get(text[j], text[j])

    return license_plate_

def read_license_plate(license_plate_crop):
    detections = reader.readtext(license_plate_crop)

    for detection in detections:
        bbox, text, score = detection

        text = text.upper().replace(' ', '')

        complies, type = license_complies_format(text)
        if complies:
            return format_license(text, type), score

    return None, None

def write_csv(results, output_path):
    with open(output_path, 'w') as f:
        f.write('{},{},{},{},{},{},{}\n'.format('frame_nmr', 'car_id', 'car_bbox',
                                                'license_plate_bbox', 'license_plate_bbox_score', 'license_number',
                                                'license_number_score'))

        for frame_nmr in results.keys():
            for car_id in results[frame_nmr].keys():
                if 'car' in results[frame_nmr][car_id].keys() and \
                   'license_plate' in results[frame_nmr][car_id].keys() and \
                   'text' in results[frame_nmr][car_id]['license_plate'].keys():
                    f.write('{},{},{},{},{},{},{}\n'.format(frame_nmr,
                                                            car_id,
                                                            '[{} {} {} {}]'.format(
                                                                results[frame_nmr][car_id]['car']['bbox'][0],
                                                                results[frame_nmr][car_id]['car']['bbox'][1],
                                                                results[frame_nmr][car_id]['car']['bbox'][2],
                                                                results[frame_nmr][car_id]['car']['bbox'][3]),
                                                            '[{} {} {} {}]'.format(
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][0],
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][1],
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][2],
                                                                results[frame_nmr][car_id]['license_plate']['bbox'][3]),
                                                            results[frame_nmr][car_id]['license_plate']['bbox_score'],
                                                            results[frame_nmr][car_id]['license_plate']['text'],
                                                            results[frame_nmr][car_id]['license_plate']['text_score'])
                            )
