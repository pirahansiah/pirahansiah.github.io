#pip install opencv-contrib-python
path_to_file = r'/Users/farshid/Downloads/im' #sys.argv[1]
f = 1.1 #float(sys.argv[2])
cx = 55.55 #float(sys.argv[3])
cy = 77.77 #float(sys.argv[4])


import cv2
import numpy as np
import os
import sys

def help():
    print("""
------------------------------------------------------------------------------------
This program shows the multiview reconstruction capabilities in the 
OpenCV Structure From Motion (SFM) module.
It reconstructs a scene from a set of 2D images 
Usage:
example_sfm_scene_reconstruction <path_to_file> <f> <cx> <cy>
where: path_to_file is the file absolute path into your system which contains
the list of images to use for reconstruction.
f is the focal length in pixels.
cx is the image principal point x coordinates in pixels.
cy is the image principal point y coordinates in pixels.
------------------------------------------------------------------------------------
""")

def get_images(directory):
    """Read file paths from a directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def main(argv):
    # if len(argv) != 5:
    #     help()
    #     sys.exit(0)
    
    # path_to_file, f, cx, cy = argv[1], float(argv[2]), float(argv[3]), float(argv[4])
    images_paths = get_images(path_to_file)
    
    # Camera intrinsics
    K = np.array([[f, 0, cx],
                  [0, f, cy],
                  [0, 0, 1]], dtype=float)
    
    # Assuming you have the SFM module in your OpenCV-Python package
    is_projective = True
    _, Rs_est, ts_est, points3d_estimated = cv2.sfm.reconstruct(images_paths, K, is_projective)
    
    print("\n----------------------------")
    print("Reconstruction: ")
    print("============================")
    print("Estimated 3D points:", len(points3d_estimated))
    print("Estimated cameras:", len(Rs_est))
    print("Refined intrinsics:\n", K)
    print("3D Visualization: ")
    print("============================")
    
    # Visualization (requires Viz module)
    try:
        from cv2 import viz
        window = viz.Viz3d('Coordinate Frame')
        window.setWindowSize((500, 500))
        window.setWindowPosition((150, 150))
        window.setBackgroundColor() # black by default
        
        # Create the point cloud widget
        point_cloud_est = np.array(points3d_estimated, dtype=np.float32)
        cloud_widget = viz.WCloud(point_cloud_est, viz.Color.green())
        window.showWidget("point_cloud", cloud_widget)
        
        # Create the camera trajectory widget
        path = [viz.makeCameraPose(R, t) for R, t in zip(Rs_est, ts_est)]
        window.showWidget("cameras_frames_and_lines", viz.WTrajectory(path, viz.WTrajectory.BOTH, 0.1, viz.Color.green()))
        window.showWidget("cameras_frustums", viz.WTrajectoryFrustums(path, K, 0.1, viz.Color.yellow()))
        window.setViewerPose(path[0])
        
        print("\nPress 'q' to close each windows ... ")
        window.spin()
    except ImportError as e:
        print("Viz module is not installed: ", e)

if __name__ == "__main__":
    main(sys.argv)
