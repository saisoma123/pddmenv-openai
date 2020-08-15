import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
  id='Baoding-v0',
  entry_point='robotgym.envs:BaodingEnv',
  timestep_limit=1000,
  reward_threshold=1.0,
  nondeterministic = True,
)

register(
  id='Dclaw-v0',
  entry_point='robotgym.envs:DclawEnv',
  timestep_limit=1000,
  reward_threshold=1.0,
  nondeterministic = True,
)

register(
  id='Dhand-v0',
  entry_point='robotgym.envs:DhandEnv',  
  timestep_limit=1000,
  reward_threshold=1.0,
  nondeterministic = True,
)

register(
  id='Cube-v0',
  entry_point='robotgym.envs:CubeEnv',
  timestep_limit=1000,
  reward_threshold=1.0,
  nondeterministic = True,
)

register(
  id='Pencil-v0',
  entry_point='robotgym.envs:PencilEnv',  
  timestep_limit=1000,
  reward_threshold=1.0,
  nondeterministic = True,
)
