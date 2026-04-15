from dataclasses import dataclass
from typing import List
@dataclass
class Factory:
    pos: int
    capacity: int
    used: int = 0
    first_bot_idx: int = -1 
    shift_penalty: int = 0 


class Solution:
    def minimumTotalDistance(self, robots: List[int], factory: List[List[int]]) -> int:
        robots.sort()
        
        factories_data = [[-int(1e15), 1]] + sorted(f for f in factory if f[1] > 0) + [[int(1e15), 1]]
        
        factories = [
            Factory(pos=f[0], capacity=f[1]) for f in factories_data
        ]

        def update_shift_penalty(f_idx: int):
            curr_f = factories[f_idx]
            prev_f = factories[f_idx - 1]
            bot_pos = robots[curr_f.first_bot_idx]
            
            curr_f.shift_penalty = abs(bot_pos - prev_f.pos) - abs(bot_pos - curr_f.pos)

        def assign_and_shift(bot_idx: int, f_idx: int):
            target_f = factories[f_idx]
            
            while target_f.used == target_f.capacity:
                displaced_bot_idx = target_f.first_bot_idx
                target_f.first_bot_idx += 1
                update_shift_penalty(f_idx)
                
                bot_idx = displaced_bot_idx
                f_idx -= 1
                target_f = factories[f_idx]
                
            if target_f.used == 0:
                target_f.first_bot_idx = bot_idx
                
            target_f.used += 1
            if target_f.used > 0:
                update_shift_penalty(f_idx)

        total_ans = 0
        factory_ptr = 1

        for bot_idx, bot_pos in enumerate(robots):
            if factories[factory_ptr].pos < bot_pos:
                while factories[factory_ptr + 1].pos < bot_pos:
                    factory_ptr += 1
            
            right_cost = factories[factory_ptr + 1].pos - bot_pos
            
            left_cost = abs(factories[factory_ptr].pos - bot_pos)
            
            temp_idx = factory_ptr
            while factories[temp_idx].used == factories[temp_idx].capacity:
                left_cost += factories[temp_idx].shift_penalty
                temp_idx -= 1
                
            if left_cost <= right_cost:
                total_ans += left_cost
                assign_and_shift(bot_idx, factory_ptr)
            else:
                factory_ptr += 1
                total_ans += right_cost
                assign_and_shift(bot_idx, factory_ptr)

        return total_ans                
            