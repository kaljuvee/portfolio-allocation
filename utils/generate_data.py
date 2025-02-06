import numpy as np
import json
import os
from typing import Dict, List, Tuple, Union
from datetime import datetime, timedelta

def generate_allocation_data(num_resources: int = 5, 
                           num_tasks: int = 10, 
                           seed: int = None) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate random data for resource allocation demonstration.
    
    Args:
        num_resources: Number of resources
        num_tasks: Number of tasks
        seed: Random seed for reproducibility
    
    Returns:
        Tuple of (costs, resource_capacity, task_requirements)
    """
    if seed is not None:
        np.random.seed(seed)
        
    # Generate cost matrix
    costs = np.random.randint(10, 100, size=(num_resources, num_tasks))
    
    # Generate resource capacity (available hours)
    resource_capacity = np.random.randint(20, 50, size=num_resources)
    
    # Generate task requirements (hours needed)
    task_requirements = np.random.randint(5, 15, size=num_tasks)
    
    return costs, resource_capacity, task_requirements

def generate_heatmap_data(num_points: int = 100,
                         x_range: Tuple[float, float] = (-5, 5),
                         y_range: Tuple[float, float] = (-5, 5),
                         seed: int = None) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate random data for heatmap demonstration.
    
    Args:
        num_points: Number of points in each dimension
        x_range: Range for x values
        y_range: Range for y values
        seed: Random seed for reproducibility
    
    Returns:
        Tuple of (X, Y, Z) where Z is the heatmap values
    """
    if seed is not None:
        np.random.seed(seed)
        
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = np.linspace(y_range[0], y_range[1], num_points)
    X, Y = np.meshgrid(x, y)
    
    # Generate some interesting patterns
    Z = (np.sin(X) * np.cos(Y) + 
         np.random.normal(0, 0.1, (num_points, num_points)))
    
    return X, Y, Z

def generate_time_series_data(num_days: int = 30,
                            num_series: int = 3,
                            seed: int = None) -> Dict[str, List]:
    """
    Generate random time series data.
    
    Args:
        num_days: Number of days to generate data for
        num_series: Number of different time series
        seed: Random seed for reproducibility
    
    Returns:
        Dictionary with dates and values for each series
    """
    if seed is not None:
        np.random.seed(seed)
        
    end_date = datetime.now()
    dates = [(end_date - timedelta(days=i)).strftime('%Y-%m-%d') 
            for i in range(num_days)]
    dates.reverse()
    
    series_data = {}
    series_data['dates'] = dates
    
    for i in range(num_series):
        # Generate random walk
        values = np.random.normal(0, 1, num_days).cumsum()
        # Scale to reasonable values
        values = (values - values.min()) * 100
        series_data[f'series_{i}'] = values.tolist()
    
    return series_data
