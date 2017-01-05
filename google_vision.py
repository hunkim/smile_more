import base64
import requests
import settings
import json
import pprint as pp

'''
https://cloud.google.com/vision/reference/rest/v1/images/annotate#Likelihood

UNKNOWN	Unknown likelihood.
VERY_UNLIKELY	The image very unlikely belongs to the vertical specified.
UNLIKELY	The image unlikely belongs to the vertical specified.
POSSIBLE	The image possibly belongs to the vertical specified.
LIKELY	The image likely belongs to the vertical specified.
VERY_LIKELY	The image very likely belongs to the vertical specifie
'''
likelihood_score = {'UNKNOWN':0, 'VERY_UNLIKELY':0, 'UNLIKELY':25,
                    'POSSIBLE': 50, 'LIKELY': 75, 'VERY_LIKELY': 100}

def get_scores (r):
    count, joy_score, anger_score = 0,0,0
    result = json.loads(r.text)
    for res in result['responses']:
        if not 'faceAnnotations' in res:
            return -1,-1
        try:
            for ann in res['faceAnnotations']:
                joy_score += likelihood_score[ann['joyLikelihood']]
                anger_score += likelihood_score[ann['angerLikelihood']]
                count += 1
        except IndexError, KeyError:
                pass

    return joy_score/count, anger_score/count

'''
https://cloud.google.com/vision/reference/rest/v1/images/annotate

TYPE_UNSPECIFIED	Unspecified feature type.
FACE_DETECTION	Run face detection.
LANDMARK_DETECTION	Run landmark detection.
LOGO_DETECTION	Run logo detection.
LABEL_DETECTION	Run label detection.
TEXT_DETECTION	Run OCR.
SAFE_SEARCH_DETECTION	Run various computer vision models to compute image safe-search properties.
IMAGE_PROPERTIES	Compute a set of properties about the image (such as the image's dominant colors).
'''
def g_vision(photo_file, type="FACE_DETECTION"):
    with open(photo_file, 'rb') as image:
        url = settings.GOOGLE_VISION_END_POINT + settings.GOOGLE_VISION_KEY
        image_content = base64.b64encode(image.read())

        payload = {
            'requests': {
                'image': {'content': image_content},
                'features': {"type": type, "maxResults":999}
                }
            }
        return requests.post(url, data=json.dumps(payload))


if __name__ == '__main__':
    r = g_vision(settings.IMG_NAME, 'FACE_DETECTION')
    print(get_scores(r))


