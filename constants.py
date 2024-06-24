# constants.py

# 窗口设置
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
WORLD_WIDTH = 3200  # 世界宽度
WORLD_HEIGHT = 1800  # 世界高度

# 控制栏和游戏空间宽度
CONTROL_PANEL_WIDTH = 400

# 按钮属性
BUTTON_COLOR = (0, 255, 0)
BUTTON_HOVER_COLOR = (255, 0, 0)
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20

# 字体设置
FONT_SIZE = 36
BUTTON_TEXTS = ["Start Game", "Button 2", "Button 3", "Slow Down"]

# 游戏状态
MAIN_MENU = 0
IN_GAME = 1

# 游戏空间中间50%的区域
CENTER_AREA_WIDTH = int(WORLD_WIDTH // 1.5)
CENTER_AREA_HEIGHT = int(WORLD_HEIGHT // 1.5)
CENTER_AREA_X_START = int((WORLD_WIDTH - CENTER_AREA_WIDTH) // 1)
CENTER_AREA_Y_START = int((WORLD_HEIGHT - CENTER_AREA_HEIGHT) //1)

# 小方块属性
NUM_PREDATORS = 50  # 捕食者初始数量
NUM_PREY = 50  # 猎物初始数量
BLOCK_SIZE = 30

# 捕食者和猎物的生命值和生命值衰减
PREDATOR_INITIAL_HEALTH = 50
PREY_INITIAL_HEALTH = 100
PREDATOR_HEALTH_DECAY = 0.03  # 增加捕食者的生命值衰减速度
PREY_HEALTH_DECAY = 0

# 捕食者和猎物的生命值上限
PREDATOR_MAX_HEALTH = 30
PREY_MAX_HEALTH = 30

# 食物属性
NUM_FOOD = 300  # 增加食物数量
FOOD_SIZE = 20
FOOD_COLOR = (0, 0, 255)
FOOD_HEALTH_GAIN = 10

# 捕食相关
PREDATOR_HEALTH_GAIN_FACTOR = 0.5

# 游戏速度
DEFAULT_FPS = 30
SLOW_FPS = 10

# 遗传算法相关
MUTATION_CHANCE = 0.01  # 增加突变几率
PREY_REPRODUCTION_CHANCE = 0.05  # 增加猎物繁殖几率
PREDATOR_REPRODUCTION_CHANCE = 0.030  # 增加捕食者繁殖几率
PREDATOR_SPEED = 5

# 速度和加速度
PREY_MAX_SPEED = 22
PREY_MAX_ACCELERATION = 1.4
PREY_MAX_TURNING_ANGLE = 0.4

PREDATOR_MAX_SPEED = 10
PREDATOR_MAX_ACCELERATION = 1.2
PREDATOR_MAX_TURNING_ANGLE = 0.3

# 听觉范围
PREDATOR_HEARING_RANGE = 600
PREY_HEARING_RANGE = 500

# 健康值减少相关常量
PREDATOR_ACCELERATION_HEALTH_DECAY_FACTOR = 0.1
PREY_ACCELERATION_HEALTH_DECAY_FACTOR = 0.03

# 新增的常量
PREDATOR_MIN_DISTANCE = 10  # 捕食者最小接近距离
PREDATOR_ROTATION_CHANCE = 0.1  # 停下来旋转的几率
PREDATOR_ROTATION_SPEED = 1  # 旋转的速度
PREDATOR_ACCELERATION_FACTOR = 1.5  # 捕食者加速因子

PREY_EVASION_FACTOR = 1.5  # 远离捕食者的因子
PREY_RANDOM_MOVE_CHANCE = 0.1  # 随机移动的几率
PREY_RANDOM_MOVE_SPEED = 1  # 随机移动的速度
PREY_TURN_INTERVAL = 30  # 定期回头观察的间隔（帧数）

# 视觉范围
PREDATOR_SIGHT_RANGE = 400  # 捕食者的视觉范围
PREY_SIGHT_RANGE = 400  # 猎物的视觉范围