import gym
from gym import spaces
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import yaml
from easydict import EasyDict


def load_parameters_from_yaml(file_path):
    with open(file_path, "r") as file:
        params = yaml.safe_load(file)
    return EasyDict(params)


class EnvironmentalEconomicSystemEnv(gym.Env):
    """
    Custom Environment that follows gym interface.
    This is a simple version of an environmental-economic system environment.
    """

    metadata = {"render.modes": ["console"]}

    def __init__(
        self,
        params_file="A Multi-phase Integrated Assessment Model for Mitigation and Adaptation\parameters.yaml",
    ):
        super(EnvironmentalEconomicSystemEnv, self).__init__()

        # Define a 5-dimensional action space corresponding to the control vector U
        # Example: actions can be the rates or levels of various policy measures
        self.action_space = spaces.Box(
            low=np.array([0, 0, 0, 0, 0, 0, 0]),  # 7 zeros for lower bound
            high=np.array([1, 1, 1, 1, 1, 1, 1]),  # 7 ones for upper bound
            dtype=np.float32,
        )

        # Define a 5-dimensional observation space corresponding to the state variables X
        self.observation_space = spaces.Box(
            low=np.array([0, 0, 0, 0, 0]),
            high=np.array([np.inf, np.inf, np.inf, np.inf, np.inf]),
            dtype=np.float32,
        )

        # Initial conditions
        self.state = np.array(
            [1000, 500, 400, 300, 200], dtype=np.float32
        )  # Example values
        self.state_history = []
        self.params = load_parameters_from_yaml(params_file)
        self.current_time = 0

    def step(self, action):
        # Execute one time step within the environment

        # Here you need to implement how your action affects the environment
        # For now, let's just pass the action as parameters to our differential equations
        new_state = odeint(self.model, self.state, [0, 1], args=(action,))[1]
        self.state = new_state

        # Define your reward and done (whether the episode is over)
        reward = self.calculate_reward(new_state, action)
        done = False  # You can define your own condition
        self.state_history.append(self.state.copy())
        self.current_time += 1

        return new_state, reward, done, {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.state = np.array([1000, 500, 400, 300, 200], dtype=np.float32)
        return self.state

    def render(self, mode="console"):
        # Plot the state history
        if mode == "console":
            print(f"State: {self.state}")
        elif mode == "human":
            # Assuming state has 5 components
            plt.figure(figsize=(10, 6))
            for i in range(5):
                plt.plot([state[i] for state in self.state_history], label=f"State {i}")
            plt.title("State Variables Over Time")
            plt.xlabel("Time Step")
            plt.ylabel("State Value")
            plt.legend()
            plt.show()
        else:
            raise NotImplementedError(
                "Only console and human render modes are implemented"
            )

    def model(self, X, t, U):
        # Your differential equations go here
        # X is the state vector, U is the action vector
        K, R, M, b, g = X
        (
            C,
            eP,
            u,
            nu_1,
            nu_2,
            nu_3,
            varsigma_k,
        ) = U  # Control variables: C, eP, u, nu_1, nu_2, nu_3, varsigma_k

        Y = self.params["Y"]
        tau_k = self.params["tau_k"]
        delta_K = self.params["delta_K"]
        n = self.params["n"]
        psi = self.params["psi"]
        zeta = self.params["zeta"]
        gamma = self.params["gamma"]
        mu = self.params["mu"]
        kappa = self.params["kappa"]
        theta = self.params["theta"]
        phi = self.params["phi"]
        alpha_4 = self.params["alpha_4"]
        beta = self.params["beta"]
        r_t = self.params["r_t"]
        delta_g = self.params["delta_g"]
        alpha_1 = self.params["alpha_1"]
        M_tilde = self.params["M_tilde"]

        dKdt = (
            Y * (nu_1 * g) ** beta * (1 - tau_k)
            - C
            - eP
            - (delta_K + n) * K
            - u * psi * R ** (-zeta)
        )
        dRdt = -u
        dMdt = gamma * u - mu * (M - kappa * M_tilde) - theta * (nu_3 * g) ** phi
        dbdt = (
            (r_t - n) * b
            - alpha_4 * eP
            - Y * (nu_1 * g) ** beta * tau_k
            + varsigma_k * g
        )
        dgdt = alpha_1 * eP - (delta_g + n) * g + varsigma_k * g
        return [dKdt, dRdt, dMdt, dbdt, dgdt]

    def calculate_reward(self, state, action):
        # Unpacking the state and action variables
        K, R, M, b, g = state
        C, eP, u, nu_1, nu_2, nu_3, varsigma_k = action

        # Parameters for the reward function
        rho = self.params["rho"]
        n = self.params["n"]
        alpha_2 = self.params["alpha_2"]
        eta = self.params["eta"]
        M_tilde = self.params["M_tilde"]
        epsilon = self.params["epsilon"]
        omega = self.params["omega"]
        sigma = self.params["sigma"]

        # Calculating the reward for the current step
        try:
            welfare_component = (
                C
                * (alpha_2 * eP) ** eta
                * (M - M_tilde) ** (-epsilon)
                * (nu_2 * g) ** omega
            ) ** (1 - sigma)
            reward = np.exp(-(rho - n) * self.current_time) * (
                (welfare_component - 1) / (1 - sigma)
            )
        except Exception as e:
            # Handling potential numerical issues (like division by zero or invalid operations)
            print(f"An error occurred in reward calculation: {e}")
            reward = 0

        return reward


env = EnvironmentalEconomicSystemEnv()

# Example of interaction with the environment
state = env.reset()
for _ in range(1000):
    action = env.action_space.sample()  # Replace this with your policy action
    state, reward, done, info = env.step(action)
    if done:
        break

# Render the environment (plotting the states)
env.render(mode="human")
env.close()
