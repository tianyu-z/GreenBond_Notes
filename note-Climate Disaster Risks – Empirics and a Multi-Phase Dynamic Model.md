[Climate Disaster Risks – Empirics and a Multi-Phase Dynamic Model (imf.org)](https://www.imf.org/en/Publications/WP/Issues/2019/07/11/Climate-Disaster-Risks-Empirics-and-a-Multi-Phase-Dynamic-Model-47013)

### Objective Function:
$$ W(T, X, U) = \int_0^T e^{-(\rho - n)t} [C(α_2 e^P)^\eta M^{-M} - (ν_2 g)^\omega] \frac{1}{1 - σ} dt $$
- $W$ : Welfare function over time $T$.
- $C$ : Consumption.
- $α_2$, $ν_2$, $η$, $ω$, $σ$ : Parameters affecting consumption, public capital, and the welfare function.
- $e^P$ : Reflects the price level.
- $M$ : Atmospheric concentration of CO2.
- $ρ$, $n$ : Discount rate and population growth rate, respectively.

### Dynamic Equations:
1. Capital Dynamics:
   $$ \dot{K} = Y \cdot (\nu_1 g)^\beta - C - e_P - (\delta_{dis} K + n)K - u \psi R^{-\zeta} $$
   - $\dot{K}$ : Rate of change of private (green) capital.
   - $Y$ : Economic output.
   - $\nu_1$, $\beta$ : Parameters related to the productivity of public capital $g$.
   - $\delta_{dis}$ : Depreciation rate of private capital during disasters.
   - $u$, $\psi$, $\zeta$ : Parameters related to resource usage.

2. Resource Depletion:
   $$ \dot{R} = -u $$
   - $\dot{R}$ : Rate of change of the stock of the non-renewable resource.
   - $u$ : Resource usage rate.

3. Atmospheric CO2 Concentration:
   $$ \dot{M} = \gamma u - \mu(M - \kappa \widetilde{M}) - \theta (\nu_3 \cdot g)^\phi $$
   - $\dot{M}$ : Rate of change of atmospheric CO2.
   - $\gamma$, $\mu$, $\kappa$ : Emission and CO2 removal parameters.
   - $\theta$, $\phi$ : Effectiveness of public capital in reducing CO2.

4. Government Debt Dynamics:
   $$ \dot{b} = (\overline{rr} - n)b - (1 - \alpha_1 - \alpha_2 - \alpha_3) \cdot e_P + \varsigma_k g $$
   - $\dot{b}$ : Rate of change of government debt.
   - $\overline{rr}$ : Real interest rate on government debt.
   - $\alpha_1$, $\alpha_2$, $\alpha_3$, $\varsigma_k$ : Budgetary parameters and bond financing coefficients.

5. Public Capital Dynamics:
   $$ \dot{g} = \alpha_1 e_P + i_F - (\delta_{dis} g + n)g + \varsigma_k g $$
   - $\dot{g}$ : Rate of change of public capital.
   - $i_F$ : External investments into public capital.
   - $\delta_{dis}$ : Depreciation rate of public capital during disasters.

### Inclusion of Green Bonds:
The term $\varsigma_k g$ in the equations for government debt and public capital dynamics represents the influence of green bond financing. This term reflects the use of bond financing (including green bonds) for funding public capital and its impact on government debt. Green bonds, as part of this financing mechanism, are used to support public sector investments in environmental and climate-related projects, as well as to manage the financial implications of such investments on government debt