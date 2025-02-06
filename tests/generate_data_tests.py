import os
import json
import numpy as np
from utils.generate_data import (
    generate_allocation_data,
    generate_heatmap_data,
    generate_time_series_data
)

def test_allocation_data():
    """Test allocation data generation and save results."""
    costs, capacity, requirements = generate_allocation_data(seed=42)
    
    # Basic validation
    assert costs.shape == (5, 10), "Costs matrix has incorrect shape"
    assert capacity.shape == (5,), "Resource capacity has incorrect shape"
    assert requirements.shape == (10,), "Task requirements has incorrect shape"
    
    # Save test data
    allocation_test = {
        'costs': costs.tolist(),
        'resource_capacity': capacity.tolist(),
        'task_requirements': requirements.tolist()
    }
    return allocation_test

def test_heatmap_data():
    """Test heatmap data generation and save results."""
    X, Y, Z = generate_heatmap_data(num_points=20, seed=42)
    
    # Basic validation
    assert X.shape == (20, 20), "X grid has incorrect shape"
    assert Y.shape == (20, 20), "Y grid has incorrect shape"
    assert Z.shape == (20, 20), "Z values have incorrect shape"
    
    # Save test data
    heatmap_test = {
        'X': X.tolist(),
        'Y': Y.tolist(),
        'Z': Z.tolist()
    }
    return heatmap_test

def test_time_series_data():
    """Test time series data generation and save results."""
    time_series = generate_time_series_data(num_days=10, seed=42)
    
    # Basic validation
    assert len(time_series['dates']) == 10, "Incorrect number of dates"
    assert len(time_series['series_0']) == 10, "Incorrect number of values"
    assert 'series_2' in time_series, "Missing expected series"
    
    return time_series

def run_all_tests():
    """Run all tests and save results to JSON files."""
    # Create test-data directory if it doesn't exist
    os.makedirs('test-data', exist_ok=True)
    
    # Run tests and save results
    test_results = {
        'allocation_test.json': test_allocation_data(),
        'heatmap_test.json': test_heatmap_data(),
        'time_series_test.json': test_time_series_data()
    }
    
    # Save all test results
    for filename, data in test_results.items():
        filepath = os.path.join('test-data', filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Test results saved to {filepath}")

if __name__ == "__main__":
    run_all_tests() 