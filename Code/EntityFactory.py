from Code.Enemy import Enemy
from Code.Background import Background
from Code.Const import WIN_WIDTH
from Code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'stageBg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'stageBg{i}',(0,0)))
                    list_bg.append(Background(f'stageBg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'ninjaMove1':
                return Player('ninjaMove1', (10, 390))
            case 'Enemy1':
                return Enemy('Enemy1',(WIN_WIDTH ,380 ))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH, 380))

















