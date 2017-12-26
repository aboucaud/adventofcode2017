"""
http://adventofcode.com/2017/day/20
"""
from typing import List


class Particle:
    def __init__(self,
                 id: int,
                 position: List[int],
                 velocity: List[int],
                 acceleration: List[int]) -> None:
        self.id = id
        self.p = position
        self.v = velocity
        self.a = acceleration

    def update(self):
        self.v = [v + a for v, a in zip(self.v, self.a)]
        self.p = [p + v for p, v in zip(self.p, self.v)]

    @property
    def distance(self) -> int:
        return sum(abs(p) for p in self.p)

    def __repr__(self) -> str:
        return f"Particle_{self.id}(p={self.p}, v={self.v}, a={self.a})"

    def __eq__(self, p2) -> bool:
        return self.p == p2.p


def parse_input(lines: List[str]) -> List[Particle]:
    plist = []
    for idx, line in enumerate(lines):
        entries = line.replace('<', '[').replace('>', ']').split(', ')
        plist.append(Particle(idx, *[eval(e.split('=')[1]) for e in entries]))
    return plist


def simulation(particles: List[Particle], min_streak: int) -> int:
    min_id = -1
    streak = 0
    while streak < min_streak:
        for p in particles:
            p.update()
        d = [p.distance for p in particles]
        new_min = d.index(min(d))
        if new_min != min_id:
            min_id = new_min
            streak = 0
        streak += 1

    return min_id


def resolve_collisions(particles: List[Particle], min_streak: int) -> int:
    streak = 0
    while streak < min_streak:
        d = [p.distance for p in particles]
        if len(d) != len(set(d)):
            to_remove = set()
            for i in range(len(d) - 1):
                for j in range(i + 1, len(d)):
                    if particles[i] == particles[j]:
                        to_remove.add(i)
                        to_remove.add(j)
            for i in reversed(list(to_remove)):
                particles.pop(i)
            streak = 0
        streak += 1
        for p in particles:
            p.update()

    return len(particles)


TEST = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>""".splitlines()
TEST_PARTICLES = parse_input(TEST)
assert simulation(TEST_PARTICLES, 100) == 0


TEST2 = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""".splitlines()
TEST2_PARTICLES = parse_input(TEST2)
assert resolve_collisions(TEST2_PARTICLES, 100) == 1


if __name__ == '__main__':
    with open('day20_input.txt', 'r') as f:
        INPUT = parse_input(f.read().splitlines())
    print("Particle ID:", simulation(INPUT[:], 10000))
    print("Particles left:", resolve_collisions(INPUT[:], 10000))
