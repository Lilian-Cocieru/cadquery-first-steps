import cadquery as cq
result = cq.Workplane("XY" ).box(3, 3, 0.5).edges("|Z").fillet(0.125)
show_object(result)
import cadquery as cq

# Параметры ступени — МЕНЯЙ ЦИФРЫ под свои проекты!
width = 900   # ширина ступени
depth = 300   # глубина проступи
height = 180  # высота подступенка

# Создаём ступень
step = (
    cq.Workplane("XY")
    .box(width, depth, height)        # основной объём
    .edges("|Z").fillet(10)           # скругляем вертикальные рёбра — как в реальной лестнице
)

show_object(step, name="Моя первая ступень")