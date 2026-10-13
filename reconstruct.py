import bpy
import math

# 1. Sahnedeki eski nesneleri temizle
if bpy.ops.object.select_all.poll():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

# 2. Parametrik Değişkenler (Makaledeki mimari oranlar)
wall_width = 10.0
alpha = 0.52
dome_radius = alpha * wall_width
wall_height = 7.0
pillar_thickness = 1.2

# 3. Dört Ana Taşıyıcı Sütun/Ayak
pillar_offset = (wall_width / 2) - (pillar_thickness / 2)
coords = [(-pillar_offset, -pillar_offset), (pillar_offset, -pillar_offset),
          (pillar_offset, pillar_offset), (-pillar_offset, pillar_offset)]

for i, (px, py) in enumerate(coords):
    bpy.ops.mesh.primitive_cube_add(
        size=1.0, 
        location=(px, py, wall_height / 2)
    )
    col = bpy.context.active_object
    col.name = f"Pillar_{i+1}"
    col.scale = (pillar_thickness, pillar_thickness, wall_height)

# 4. Sekizgen Kasnak (Octagonal Drum - Geçiş Elemanı)
bpy.ops.mesh.primitive_cylinder_add(
    vertices=8,
    radius=dome_radius * 1.05,
    depth=1.8,
    location=(0, 0, wall_height + 0.9)
)
drum = bpy.context.active_object
drum.name = "Octagonal_Drum"

# 5. Ana Kubbe (Yarım Küre - Procedural Hemisphere)
segments = 64
rings = 16
verts = []
faces = []

# Tepe noktası
verts.append((0.0, 0.0, dome_radius))

# Halka noktaları (Sadece üst yarım küre)
for r in range(1, rings):
    phi = (math.pi / 2) * (r / rings)
    z = dome_radius * math.cos(phi)
    xy_rad = dome_radius * math.sin(phi)
    for s in range(segments):
        theta = 2 * math.pi * (s / segments)
        x = xy_rad * math.cos(theta)
        y = xy_rad * math.sin(theta)
        verts.append((x, y, z))

# Etek dairesi (Taban kotu)
for s in range(segments):
    theta = 2 * math.pi * (s / segments)
    verts.append((dome_radius * math.cos(theta), dome_radius * math.sin(theta), 0.0))

# Tepe üçgen yüzeyleri
for s in range(segments):
    next_s = (s + 1) % segments
    faces.append((0, 1 + s, 1 + next_s))

# Gövde dörtgen yüzeyleri
for r in range(rings - 1):
    r_start = 1 + r * segments
    next_r_start = 1 + (r + 1) * segments
    for s in range(segments):
        next_s = (s + 1) % segments
        faces.append((
            r_start + s,
            next_r_start + s,
            next_r_start + next_s,
            r_start + next_s
        ))

# Taban kapağı
bottom_center_idx = len(verts)
verts.append((0.0, 0.0, 0.0))
base_start = 1 + (rings - 1) * segments
for s in range(segments):
    next_s = (s + 1) % segments
    faces.append((bottom_center_idx, base_start + next_s, base_start + s))

# Mesh ve Obje Oluşturma
dome_mesh = bpy.data.meshes.new("Dome_Mesh")
dome_mesh.from_pydata(verts, [], faces)
dome_mesh.update()

dome_obj = bpy.data.objects.new("Main_Dome_Malatya", dome_mesh)
bpy.context.collection.objects.link(dome_obj)
dome_obj.location = (0, 0, wall_height + 1.8)

# 6. Kamera ve Işıklandırma
bpy.ops.object.camera_add(location=(22, -22, 18), rotation=(math.radians(60), 0, math.radians(45)))
bpy.context.scene.camera = bpy.context.active_object

bpy.ops.object.light_add(type='SUN', location=(10, -10, 20))
sun = bpy.context.active_object
sun.data.energy = 3.5

print(">> Başarılı: Malatya Yeni Camii kubbe ve taşıyıcı elemanları modellendi.")
