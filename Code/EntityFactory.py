from Code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'stageBg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'stageBg{i}',(0,0)))
                return list_bg








