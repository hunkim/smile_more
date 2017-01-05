import camera_reader as cr
import google_vision as gv
import settings
import json

# Global values to track numbers
count, joy_score, anger_score, distance = 0,0,0,0


def main_job():
    global count, joy_score, anger_score, distance

    # take a picture
    dist = cr.make_picture()
    if dist == -1:
        print ("Check camera setting and/or camera index")
        return
    elif dist == 0:
        print ("Cannot find your face!")
        return

    if settings.USE_GOOGLE_VISION:
        response = gv.g_vision(settings.IMG_NAME, 'FACE_DETECTION')
        j_s, a_s = gv.get_scores(response)
        if j_s == -1 or a_s== -1:
            print("Cannot find your face!")
            return

    count += 1
    distance += dist

    if settings.USE_GOOGLE_VISION:
        joy_score += j_s
        anger_score += a_s

        print("Distance: ", dist, "Joy: ", j_s, "Anger: ", a_s);
        print("Distance avg: ", distance/count, "Joy avg: ", joy_score/count,
          "Anger avg: ", anger_score/count), "count: ", count;
    else:
        print("Distance: ", dist, "Distance avg: ", distance / count, "count: ", count);

    # Adjust the distance for you
    # Modify values in settings
    if dist < settings.MIN_DISTANCE:
        print '\a'
        print ("Too close!")

if __name__ == '__main__':
    main_job()
