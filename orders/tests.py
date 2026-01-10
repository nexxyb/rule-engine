from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Order
from .rules.registry import RULE_REGISTRY


class RuleEngineTests(APITestCase):

    def setUp(self):
        """
        Seed test data
        """
        self.order1 = Order.objects.create(total=50, items_count=1)
        self.order2 = Order.objects.create(total=120, items_count=3)
        self.order3 = Order.objects.create(total=200, items_count=2)

    def test_rules_are_registered(self):
        """
        Ensure all rules are auto-registered
        """
        self.assertIn("min_total_100", RULE_REGISTRY)
        self.assertIn("min_items_2", RULE_REGISTRY)
        self.assertIn("total_divisible_by_5", RULE_REGISTRY)

    def test_min_total_100_rule(self):
        rule = RULE_REGISTRY["min_total_100"](self.order2)
        self.assertTrue(rule.check())

        rule = RULE_REGISTRY["min_total_100"](self.order1)
        self.assertFalse(rule.check())

    def test_min_items_2_rule(self):
        rule = RULE_REGISTRY["min_items_2"](self.order3)
        self.assertTrue(rule.check())

        rule = RULE_REGISTRY["min_items_2"](self.order1)
        self.assertFalse(rule.check())

    def test_total_divisible_by_5_rule(self):
        rule = RULE_REGISTRY["total_divisible_by_5"](self.order3)
        self.assertTrue(rule.check())

    def test_rule_check_api_success(self):
        url = "/rules/check/"
        payload = {
            "order_id": self.order2.id,
            "rules": ["min_total_100", "min_items_2"],
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["passed"])
        self.assertEqual(response.data["details"]["min_total_100"], True)
        self.assertEqual(response.data["details"]["min_items_2"], True)

    def test_rule_check_api_partial_failure(self):
        url = "/rules/check/"
        payload = {
            "order_id": self.order1.id,
            "rules": ["min_total_100", "min_items_2"],
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data["passed"])
        self.assertEqual(response.data["details"]["min_total_100"], False)
        self.assertEqual(response.data["details"]["min_items_2"], False)

    def test_rule_check_api_invalid_order(self):
        url = "/rules/check/"
        payload = {"order_id": 999, "rules": ["min_total_100"]}

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
