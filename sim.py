import json
import math
import pathlib

ROOT = pathlib.Path("c:/Users/Kui Ching/.gemini/test")
questions_txt = (ROOT / 'questions.js').read_text('utf-8').replace('const SOCIUS_QUESTIONS = ', '').rstrip(';\n')
scholars_txt = (ROOT / 'scholars.js').read_text('utf-8').replace('const SOCIUS_SCHOLARS = ', '').rstrip(';\n')

questions = json.loads(questions_txt)
scholars = json.loads(scholars_txt)

axes = ['scale', 'force', 'order', 'stance']
max_scores = {ax: 0 for ax in axes}
for q in questions:
    for ax in axes:
        max_possible = max(abs(opt['effects'].get(ax, 0)) for opt in q['options'])
        max_scores[ax] += max_possible

def find_best_path(target_vector):
    # Greedy approach is usually fine since questions are independent 
    # but we want to minimize distance after normalization.
    # Actually, we can just pick the option in each question that has the highest dot product with the target vector?
    # Or try greedy search: pick the option that minimizes the distance to target * max_scores.
    
    target_raw = {ax: target_vector[i] * max_scores[ax] for i, ax in enumerate(axes)}
    
    path = []
    current_raw = {ax: 0 for ax in axes}
    
    for q in questions:
        best_opt = None
        best_dist = float('inf')
        for i, opt in enumerate(q['options']):
            effects = opt['effects']
            dist = sum((current_raw[ax] + effects.get(ax, 0) - target_raw[ax])**2 for ax in axes)
            if dist < best_dist:
                best_dist = dist
                best_opt = (i, opt['label'])
        
        path.append(best_opt[1])
        # Add to current raw
        for ax in axes:
            current_raw[ax] += q['options'][best_opt[0]]['effects'].get(ax, 0)
            
    # Calculate final normalized vector
    final_vec = [current_raw[ax] / max_scores[ax] for ax in axes]
    dist = math.sqrt(sum((final_vec[i] - target_vector[i])**2 for i in range(4)))
    
    return path, final_vec, dist

print("--- Lan (蓝佩嘉) ---")
lan = next(s for s in scholars if s['id'] == 'lan')
p, v, d = find_best_path(lan['vector'])
print(f"Target: {lan['vector']}")
print(f"Result: {[round(x, 2) for x in v]}")
print(f"Distance: {d:.4f}")
print(f"Path: {','.join(p)}")

print("\n--- Mears (阿什利·米尔斯) ---")
mears = next(s for s in scholars if s['id'] == 'mears')
p, v, d = find_best_path(mears['vector'])
print(f"Target: {mears['vector']}")
print(f"Result: {[round(x, 2) for x in v]}")
print(f"Distance: {d:.4f}")
print(f"Path: {','.join(p)}")
