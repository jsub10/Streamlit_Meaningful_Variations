from math import factorial
import os

def count_permutations_for_distribution(distribution, n):
    """Calculate number of permutations for a given distribution using multinomial coefficient"""
    numerator = factorial(n)
    denominator = 1
    for count in distribution:
        denominator *= factorial(count)
    return numerator // denominator

def find_distributions_with_average(n_respondents, target_average, scores=[1,2,3,4,5]):
    """Find all score distributions that achieve target average"""
    
    # Check if average is achievable
    target_sum = target_average * n_respondents
    if target_sum != int(target_sum):
        return None, f"Average {target_average} is not possible with {n_respondents} respondents (sum must be integer)"
    
    target_sum = int(target_sum)
    
    # Check if sum is within valid range
    min_possible_sum = n_respondents * min(scores)
    max_possible_sum = n_respondents * max(scores)
    
    if target_sum < min_possible_sum or target_sum > max_possible_sum:
        return None, f"Average {target_average} is not possible (sum {target_sum} out of range [{min_possible_sum}, {max_possible_sum}])"
    
    valid_distributions = []
    
    # This is hard coded for a list of possible scores, in this case
    ## [1, 2, 3, 4, 5]
    for n1 in range(n_respondents + 1):
        for n2 in range(n_respondents - n1 + 1):
            for n3 in range(n_respondents - n1 - n2 + 1):
                for n4 in range(n_respondents - n1 - n2 - n3 + 1):
                    n5 = n_respondents - n1 - n2 - n3 - n4
                    if n1*1 + n2*2 + n3*3 + n4*4 + n5*5 == target_sum:
                        valid_distributions.append((n1, n2, n3, n4, n5))
    
    return valid_distributions, None

def calculate_average_distribution(n_respondents, target_average):
    """Calculate the average counts of 1s, 2s, 3s, 4s, and 5s across all distributions"""
    
    result = find_distributions_with_average(n_respondents, target_average)
    
    if result[1] is not None:  # Error message exists
        return None, result[1]
    
    distributions = result[0]
    
    # Calculate weighted average of each score count
    # Weight by the number of permutations each distribution generates
    total_weight = 0
    weighted_sums = [0, 0, 0, 0, 0]  # for scores 1, 2, 3, 4, 5
    
    for dist in distributions:
        weight = count_permutations_for_distribution(dist, n_respondents)
        total_weight += weight
        
        for i in range(5):
            weighted_sums[i] += dist[i] * weight
    
    # Calculate weighted averages
    avg_counts = [ws / total_weight for ws in weighted_sums]
    
    return avg_counts, None

def compare_two_averages(n_respondents, avg1, avg2):
    """Compare the average distributions for two different average scores"""
    
    def find_closest_valid_averages(n, target_avg):
        """Find the closest valid averages below and above target"""
        min_sum = n  # all 1s
        max_sum = 5 * n  # all 5s
        
        # Generate all possible averages for this number of respondents
        possible_averages = []
        for total_sum in range(min_sum, max_sum + 1):
            avg = total_sum / n
            possible_averages.append(avg)
        
        # Find closest below and above target
        lower = None
        higher = None
        
        for avg in possible_averages:
            if avg < target_avg:
                if lower is None or avg > lower:
                    lower = avg
            elif avg > target_avg:
                if higher is None or avg < higher:
                    higher = avg
        
        return lower, higher
    
    print(f"Comparing average {avg1} vs {avg2} with {n_respondents} respondents")
    print("=" * 70)
    
    # Get average distribution for first average
    result1 = calculate_average_distribution(n_respondents, avg1)
    if result1[1] is not None:
        print(f"\nAverage {avg1} is not possible: {result1[1]}")
        lower, higher = find_closest_valid_averages(n_respondents, avg1)
        if lower is not None:
            print(f"  → Closest lower average: {lower:.6g}")
        if higher is not None:
            print(f"  → Closest higher average: {higher:.6g}")
        avg_dist1 = None
    else:
        avg_dist1 = result1[0]
    
    # Get average distribution for second average
    result2 = calculate_average_distribution(n_respondents, avg2)
    if result2[1] is not None:
        print(f"\nAverage {avg2} is not possible: {result2[1]}")
        lower, higher = find_closest_valid_averages(n_respondents, avg2)
        if lower is not None:
            print(f"  → Closest lower average: {lower:.6g}")
        if higher is not None:
            print(f"  → Closest higher average: {higher:.6g}")
        avg_dist2 = None
    else:
        avg_dist2 = result2[0]
    
    # Only continue with comparison if both averages are valid
    if avg_dist1 is None or avg_dist2 is None:
        print("\nCannot complete comparison - one or both averages are not possible.")
        return
    
    # Display results
    print(f"\nAverage counts across all distributions:\n")
    print(f"{'Score':<8} {'Avg ' + str(avg1):<12} {'%':<8} {'Avg ' + str(avg2):<12} {'%':<8} {'Diff':<12} {'Diff %':<10}")
    print("-" * 80)
    
    for score in range(1, 6):
        count1 = avg_dist1[score-1]
        count2 = avg_dist2[score-1]
        pct1 = (count1 / n_respondents) * 100
        pct2 = (count2 / n_respondents) * 100
        diff = count2 - count1
        diff_pct = (diff / n_respondents) * 100
        print(f"{score:<8} {count1:<12.4f} {pct1:<8.2f} {count2:<12.4f} {pct2:<8.2f} {diff:+12.4f} {diff_pct:+10.2f}")
    
    print(f"\nTotal:   {sum(avg_dist1):<12.4f} {100.0:<8.2f} {sum(avg_dist2):<12.4f} {100.0:<8.2f}")
    
    # Summary
    print("\n" + "=" * 80)
    print("Interpretation:")
    print(f"Moving from average {avg1} to {avg2}:")
    for score in range(1, 6):
        diff = avg_dist2[score-1] - avg_dist1[score-1]
        if abs(diff) > 0.01:  # Only show meaningful differences
            direction = "more" if diff > 0 else "fewer"
            diff_pct = (diff / n_respondents) * 100
            print(f"  • {direction} {score}s (difference: {diff:+.4f}, {diff_pct:+.2f}%)")
