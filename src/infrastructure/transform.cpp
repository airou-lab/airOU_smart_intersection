#include <pcl/common/transforms.h>

int main() {
    
// Create an identity transformation
Eigen::Affine3f transform = Eigen::Affine3f::Identity();

// Set translation (optional)
transform.translation() << 0.0, 0.0, 0.0;

// Rotate around the X-axis (rotx degrees)
float rotx = 45.0; // Example rotation angle
transform.rotate(Eigen::AngleAxisf((rotx * M_PI) / 180, Eigen::Vector3f::UnitX()));

// Apply the transformation to your point cloud
pcl::transformPointCloud(*input_cloud, *output_cloud, transform);

}