import os
import json
from tracemalloc import start
from unittest import case
import tqdm
import numpy as np
import matplotlib.pyplot as plt
import cv2

MAP_H = 500
MAP_W = 500

def load_trajectory(traj_folder, start_index=0):
    trajectories = os.listdir(traj_folder)
    trajectories.sort(key=lambda x: int(x.split('.')[0]))
    
    traj_len = len(trajectories)
    
    trajectory_list = []
    
    if start_index >= traj_len:
        raise ValueError('start index larger then whole trajectory length')
    
    for i in range(start_index, traj_len):
        with open(os.path.join(traj_folder, trajectories[i]), 'r') as f:
            trajectory = json.load(f)
        ego_pos = trajectory['ego']
        x,y,heading = ego_pos
        trajectory_list.append([x,y,heading])
        
    return np.stack(trajectory_list)

def visualize_traj(trajectory, img_path):
    img = plt.imread(img_path)
    fig, ax = plt.subplots()
    ax.imshow(img)
    x = trajectory[:,0]
    y = trajectory[:,1]
    # plt.xlim(MAP_W)
    # plt.ylim(MAP_H)
    plt.plot(x,y)
    plt.show()
    # plt.close()
    
if __name__ == '__main__':
    case_folder = '../data_export/case_0005/475e51d7d902469abe1cbafcc121c867'
    trajectory_folder = os.path.join(case_folder, 'status')
    map_folder = os.path.join(case_folder, 'maps')
    traj = load_trajectory(trajectory_folder, start_index=0)
    map_image = cv2.imread(os.path.join(map_folder, str(1).zfill(4)+'.jpg'))
    visualize_traj(traj, os.path.join(map_folder, str(1).zfill(4)+'.jpg'))
            
    
    