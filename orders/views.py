from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .rules.registry import RULE_REGISTRY


class RuleCheckView(APIView):
    def post(self, request):
        order_id = request.data.get("order_id")
        rule_keys = request.data.get("rules", [])

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )

        results = {}
        passed = True

        for key in rule_keys:
            rule_class = RULE_REGISTRY.get(key)
            if not rule_class:
                results[key] = False
                passed = False
                continue

            rule = rule_class(order)
            result = rule.check()
            results[key] = result
            if not result:
                passed = False

        return Response({"passed": passed, "details": results})
