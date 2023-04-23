import pygame

class Collision:

    def checkCollisionRotate(blocks, block, width, height) -> bool:
        if blocks == []:
            return False
        i = block
        for j in blocks:
            if j != i:
                for k in j.rects:
                    for l in i.rects:
                        if k.colliderect(l):
                            return True
        for m in i.rects:
            if m.x < 0 or m.x > width or m.y > height or m.y < 40:
                return True
        return False

    def checkCollisionsDown(blocks, count, width, height) -> bool:
        if blocks == []:
            return False
        i = blocks[count]
        for j in blocks:
            if j != i:
                for k in j.rects:
                    for l in i.rects:
                        l.y = l.y + 40
                        if k.colliderect(l):
                            l.y = l.y - 40
                            return True
                        l.y = l.y - 40
        for m in i.rects:
            if m.x < 0 or m.x + 39 > width or m.y + 40 > height:
                return True
        return False
    
    def checkCollisionsLeft(blocks, count) -> bool:
        if blocks == []:
            return False
        i = blocks[count]
        for j in blocks:
            if j != i:
                for k in j.rects:
                    for l in i.rects:
                        l.x = l.x - 40
                        if k.colliderect(l) or l.x < 0:
                            l.x = l.x + 40
                            return True
                        l.x = l.x + 40
        if count == 0:
            for k in j.rects:
                k.x = k.x - 40
                if k.x < 0:
                    k.x = k.x + 40
                    return True
                k.x = k.x + 40
        return False
    
    def checkCollisionsRight(blocks, count) -> bool:
        if blocks == []:
            return False
        i = blocks[count]
        for j in blocks:
            if j != i:
                for k in j.rects:
                    for l in i.rects:
                        l.x = l.x + 40
                        if k.colliderect(l) or l.x > 600:
                            l.x = l.x - 40
                            return True
                        l.x = l.x - 40
        return False