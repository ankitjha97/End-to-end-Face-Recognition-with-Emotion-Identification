from utils import *
class Face_detection:
    def __init__(self):
        self.length = 224
        self.width  = 224
        self.height = 3
        #self.image = np.fliplr([[[0] * self.length] * self.width] * self.height)
        self.upscaling_factor = 1
        #self.image = image
    def read_image(self, filename):
        im = PIL.Image.open("Ankit.jpg")
        im = im.convert('RGB')
        #self.image = np.array(im)
   
    def show_face(self, face_locations):
        im = PIL.Image.open("Ankit.jpg")
        im = im.convert('RGB')
        image = np.array(im)
        for face_location in face_locations:
            top, right, bottom, left = max(face_location.rect.top(), 0), min(face_location.rect.right(), image.shape[1]), 		    min(face_location.rect.bottom(), image.shape[0]), max(face_location.rect.left(), 0)
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        face_image = image[top:bottom, left:right]
        pil_image = PIL.Image.fromarray(face_image)
        pil_image.show()
  
    def detect_face(self, image):
        cnn_face_detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
        face_locations = cnn_face_detector(image, self.upscaling_factor)
        return face_locations
