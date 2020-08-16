import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
  id='Baoding-v0',
  entry_point='robotgym.envs:BaodingEnv',
  max_episode_steps=1000,
)

register(
  id='Dclaw-v0',
  entry_point='robotgym.envs:DclawEnv',
  max_episode_steps=1000,
)

register(
  id='Cube-v0',
  entry_point='robotgym.envs:CubeEnv',
  max_episode_steps=1000,
)
