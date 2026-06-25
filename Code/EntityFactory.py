
from Code.Background import Background
from Code.Const import WIN_WIDTH


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
















