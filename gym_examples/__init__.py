from gymnasium.envs.registration import register

register(
    id="gym_examples/Blackjack-v1",
    entry_point="gym_examples.envs:blackjack_env:BlackjackEnv",
)
