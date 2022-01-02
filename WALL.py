from init import cell_number, wall_group_id, pygame, cell_size, screen
from ELEMENT import ELEMENT

class WALL(ELEMENT):

    def __init__(self, randomly = False, length = cell_number-1):
        super().__init__()
        self.length = length
        self.group_id = wall_group_id
        self.randomly = randomly

        self.wall = pygame.image.load('graphisms/wall.png').convert_alpha()

    def draw(self):
        for block in self.body:
            # On crée les rect pour les positions
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size,cell_size)
            #pygame.draw.rect(screen, (0,0,0), block_rect)

            screen.blit(self.wall,block_rect)