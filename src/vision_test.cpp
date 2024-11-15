#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

Mat mycontours(Mat image){
  Mat img_gray;
  cvtColor(image,img_gray, COLOR_BGR2GRAY);
  Mat thresh;
  threshold(img_gray, thresh, 150, 255, THRESH_BINARY);
  // detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
  vector<vector<Point>> contours;
  vector<Vec4i> hierarchy;
  findContours(thresh, contours, hierarchy, RETR_TREE, CHAIN_APPROX_NONE);
  // draw contours on the original image
  Mat image_copy = thresh.clone();
  drawContours(image_copy, contours, -1, Scalar(0, 255, 0), 2);
  return image_copy;

}

int main(){

Mat image ;
namedWindow("Webcam");

VideoCapture cap(0);

if (!cap.isOpened())

{
cout << "Cannot Open Cam";
}

while (true)

{

cap >> image;
image = mycontours(image);
imshow("Webcam", image);
waitKey(25);
}

return 0;

}
