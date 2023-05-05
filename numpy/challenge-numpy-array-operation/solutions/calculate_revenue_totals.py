from typing import Tuple
import numpy as np


def calculate_revenue_totals(
    total_purchases_by_customer: np.ndarray,
    total_purchases_by_product: np.ndarray,
    prices: int,
) -> Tuple[np.ndarray, np.ndarray]:
    """
     Calculate the total revenue generated by each customer and product.

     Parameters
     ----------
     total_purchases_by_customer : np.ndarray
         A 1D NumPy array of shape (num_customers,) containing the total number of purchases for each customer.
     total_purchases_by_product : np.ndarray
         A 1D NumPy array of shape (num_product,) containing the total number of purchases for each product.
     prices : int
         A int, representing the price of each product.

     Returns
    -------
     Tuple[np.ndarray, np.ndarray]
         A tuple containing the following two NumPy arrays:
             - total_revenue_by_customer : np.ndarray
                 A 1D NumPy array of shape (num_customers,) containing the total revenue generated by each customer.
             - total_revenue_by_product : np.ndarray
                 A 1D NumPy array of shape (num_products,) containing the total revenue generated by each product.
    """
    total_revenue_by_customer = np.multiply(total_purchases_by_customer, prices)
    total_revenue_by_product = np.multiply(total_purchases_by_product, prices)
    return total_revenue_by_customer, total_revenue_by_product
