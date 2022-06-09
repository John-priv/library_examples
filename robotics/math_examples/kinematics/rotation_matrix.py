import numpy as np


def get_rotation_matrix(angle, axis='x', angle_type='degrees'):
    if angle_type == 'degrees':
        angle = np.radians(angle)
    if axis == 'x':
        return np.mat([[1, 0, 0], [0, np.cos(angle), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]])
    if axis == 'y':
        return np.mat([[np.cos(angle), 0, np.sin(angle)], [0, 1, 0], [-np.sin(angle), 0, np.cos(angle)]])
    if axis == 'z':
        return np.mat([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    else:
        print('NO TYPE SPECIFIED: Returning z transformation')
        return np.mat([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])


def main():
    # angle = 45
    rot_x = get_rotation_matrix(angle=45, axis='x', angle_type='degrees')
    rot_y = get_rotation_matrix(angle=45, axis='y', angle_type='degrees')
    rot_z = get_rotation_matrix(angle=45, axis='z', angle_type='degrees')
    print('rot_x =\n{}'.format(rot_x))
    print('rot_y =\n{}'.format(rot_y))
    print('rot_z =\n{}'.format(rot_z))


if __name__ == '__main__':
    main()
