import os
os.environ['OMNIGIBSON_HEADLESS'] = '1'
os.environ["OMNIGIBSON_RENDERING_MODE"] = "offscreen"
import omnigibson as og
import json
from omnigibson.macros import gm
import numpy as np
from PIL import Image
import sys
sys.path.append("/mnt/home/ssa2206/Robot/SteerKep/COMS6998-ReKep/")
from utils import get_config
from environment import ReKepOGEnv

import faulthandler
faulthandler.enable()

RUN_QUICKSTART = True

config_dir = "/mnt/home/ssa2206/Robot/SteerKep/COMS6998-ReKep/configs/"
global_config = get_config(config_path=os.path.join(config_dir, 'config.yaml'))
scene_file = os.path.join(config_dir, 'og_scene_file_pen.json')

output_dir = "/mnt/home/ssa2206/Robot/SteerKep/data/camera_output"
pathify = lambda x: os.path.join(output_dir, x)
os.makedirs(output_dir, exist_ok=True)

if RUN_QUICKSTART:
    cfg = dict()

    # Define scene
    cfg["scene"] = {
        "type": "Scene",
        "floor_plane_visible": True,
    }

    # Define objects
    cfg["objects"] = [
        {
            "type": "USDObject",
            "name": "ghost_stain",
            "usd_path": f"{gm.ASSET_PATH}/models/stain/stain.usd",
            "category": "stain",
            "visual_only": True,
            "scale": [1.0, 1.0, 1.0],
            "position": [1.0, 2.0, 0.001],
            "orientation": [0, 0, 0, 1.0],
        },
        {
            "type": "DatasetObject",
            "name": "delicious_apple",
            "category": "apple",
            "model": "agveuv",
            "position": [0, 0, 1.0],
        },
        {
            "type": "PrimitiveObject",
            "name": "incredible_box",
            "primitive_type": "Cube",
            "rgba": [0, 1.0, 1.0, 1.0],
            "scale": [0.5, 0.5, 0.1],
            "fixed_base": True,
            "position": [-1.0, 0, 1.0],
            "orientation": [0, 0, 0.707, 0.707],
        },
        {
            "type": "LightObject",
            "name": "brilliant_light",
            "light_type": "Sphere",
            "intensity": 50000,
            "radius": 0.1,
            "position": [3.0, 3.0, 4.0],
        },
    ]

    # Define robots
    cfg["robots"] = [
        {
            "type": "Fetch",
            "name": "skynet_robot",
            "obs_modalities": ["scan", "rgb", "depth"],
        },
    ]

    # Define task
    cfg["task"] = {
        "type": "DummyTask",
        "termination_config": dict(),
        "reward_config": dict(),
    }
    env = og.Environment(cfg)
    env.reset()
    obs, rew, terminated, truncated, info = env.step(env.action_space.sample())
    sys.exit(0)

else:
        
    # Create the environment
    env = ReKepOGEnv(global_config['env'], scene_file, verbose=True)
    print(f"Environment created with {env.cams=}")
    for cam_id in env.cams:
        cam_obs = env.cams[cam_id].get_obs()
        print(f"Camera {cam_id} has {cam_obs.keys()}")
        for key, value in cam_obs.items():
            print(f"{key}: {value.shape}, {value.dtype}")

    env.step()
    # Allow camera teleoperation
    #env = og.Environment(cfg)
    #og.sim.enable_viewer_camera_teleoperation()

