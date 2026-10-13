![Procedural Reconstruction Shell](Ekran%20Resmi%202026-10-13%2012.02.17.png)
# Algorithmic Heritage & Digital Restitution
### Automated Procedural Reconstruction of Destroyed Cultural Assets

> An autonomous, code-driven execution pipeline bridging archival NLP with procedural 3D modeling to resurrect endangered and destroyed monuments from physical erasure.

---

## 🏛️ Case Study: The Malatya Yeni Camii (Hacı Yusuf Mosque)
Catastrophically destroyed during the earthquakes of February 6, 2023, the Malatya Yeni Camii serves as the primary proving ground for this computational restitution framework.

### 📐 Procedural Reconstruction Core
The model dynamically instantiates classical Ottoman architectural elements via Python-driven procedural algorithms:
- **Parametric Dome Instantiation:** Mathematical calculation of dome radius relative to nave wall bounds:  
  $$R_d = \alpha \times W_n$$
- **Transition Mechanics:** Programmatic generation of octagonal drums and load-bearing pillars without manual modeling bias.
- **Historical Veracity Index (HVI):** A metric scoring algorithmically generated geometry layers based on archival source fidelity.

---

## 💻 Python / Blender API Implementation
Below is the core script generating the parametric hemisphere and octagonal base structure:

```python
# Core algorithmic generator executed in Blender Python API (bpy)
wall_width = 10.0
alpha = 0.52
dome_radius = alpha * wall_width
wall_height = 7.0
# [Procedural mesh generation logic...]
