[Financing Climate Change Policies A Multi-phase Integrated Assessment Model for Mitigation and Adaptation - Springer-2020_1010079783030545765_6](https://link.springer.com/chapter/10.1007/978-3-030-54576-5_6)

1. **State Variables $X = (K, R, M, b, g)$**:
   - $K$ : Stock of private capital.
   - $R$ : Stock of non-renewable resources.
   - $M$ : Atmospheric concentration of CO2.
   - $b$ : Public debt level.
   - $g$ : Stock of public capital, which funds climate policy actions.

2. **Differential Equations**:
   - $\dot{K}$ : Change in private capital, influenced by factors like output $Y$, tax rate $\tau_k$, private consumption $C$, pollution expenditure $eP$, population growth rate $n$, and resource extraction rate $u$.
   - $\dot{R}$ : Change in non-renewable resources, determined by the extraction rate $u$.
   - $\dot{M}$ : Change in atmospheric CO2, affected by emissions from resource extraction and mitigation efforts through public infrastructure $g$.
   - $\dot{b}$ : Change in public debt, influenced by interest rate $r_t$, green bonds issuance ($\sigma_k g$), and other financial factors.
   - $\dot{g}$ : Change in public capital, considering factors like pollution expenditure, depreciation, and green bonds issuance ($\sigma_k g$).

3. **Involvement of Green Bonds**:
   - The model extends to incorporate multiple regimes through parameters $\tau_k$ and $\sigma_k$, defining three phases:
     - No Green Bonds Phase: $\tau_k = \sigma_k = 0$.
     - Green Bonds Issuance Phase: $\sigma_k > 0$, indicating the issuance of green bonds and allocation of funds to public capital $g$.
     - Green Bonds Repayment Phase: $\tau_k > 0$, involving repayment of green bonds through a special income tax.

4. **Welfare Optimization Objective**:
   - The goal is to maximize per capita social welfare $W$, a CES function of state variables $X$ and control variables $U$.
   - $W$ is influenced by private consumption $C$, tax revenue used for welfare enhancement ($\alpha_2 eP$), atmospheric CO2 concentration ($M$), and public infrastructure allocation for climate change adaptation ($\nu_2 g$).
   - The welfare function includes parameters for social expenditures, adaptation benefits, carbon emissions disutility, and a discount rate adjusted for population growth.

$$\begin{aligned}W(T,X,U)&=\int_0^Te^{-(\rho-n)t}\frac{\left(C\cdot(\alpha_2e_P)^\eta\left(M-\widetilde{M}\right)^{-\epsilon}\left(\nu_2g\right)^\omega\right)^{1-\sigma}-1}{1-\sigma}dt.\end{aligned}$$
5. **Control Vector $U = (C, eP, u, \nu_1, \nu_2, \nu_3)$**:
   - Represents the decision variables for the policymaker, including private consumption, pollution expenditure, resource extraction rate, and allocation of public capital for various climate change responses.

Green bonds are mathematically incorporated into the model through the regime-specific parameters $\tau_k$ and $\sigma_k$ in the differential equations governing public debt ($\dot{b}$) and public capital ($\dot{g}$).

1. **Public Debt ($\dot{b}$)**:
   - The differential equation for public debt is:
     $$ \dot{b} = (r_t - n)b - \alpha_4 eP - Y \cdot (\nu_1 g)^\beta \tau_k + \sigma_k g $$
   - The term $\sigma_k g$ is key to the green bonds' involvement. It represents funds raised from issuing green bonds that are allocated to the stock of public capital $g$, used for climate change action.
   - The term $\tau_k$ represents a special income tax levied to pay down the public debt, which includes green bonds when $\tau_k > 0$.

2. **Public Capital ($\dot{g}$)**:
   - The differential equation for public capital is:
     $$ \dot{g} = \alpha_1 eP - (\delta_g + n)g + \sigma_k g $$
   - $\sigma_k g$ indicates the investment in public capital funded through green bonds. When $\sigma_k > 0$, it shows that green bonds are being issued and the proceeds are being used to enhance public capital.

3. **Regime-Specific Phases**:
   - The model operates under different regimes (phases) defined by the values of $\tau_k$ and $\sigma_k$ :
     - **No Green Bonds Phase**: $\tau_k = \sigma_k = 0$, indicating the absence of green bonds.
     - **Green Bonds Issuance Phase**: $\sigma_k > 0$, indicating the issuance of green bonds and allocation of funds to public capital.
     - **Green Bonds Repayment Phase**: $\tau_k > 0$, indicating the repayment of green bonds through a special income tax.

Green bonds are mathematically represented in the model by the terms $\sigma_k g$ in the equations for public debt and public capital, affecting how funds are raised and allocated within the economy, especially for climate change actions.