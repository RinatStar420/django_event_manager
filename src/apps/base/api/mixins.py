class SerializerPerActionMixin:
    action_serializers = None
    action = None

    def get_serializer_class(self):
        assert self.action_serializers is not None, (
            f"{self.__class__.__name__} needs to define an " "`action_serializers`"
        )
        assert self.action_serializers.get("default"), (
            f"{self.__class__.__name__} needs to define a "
            "`default` in `action_serializers` attribute"
        )
        assert (
                self.action is not None
        ), f"{self.__class__.__name__} needs to define an `action`"

        self.serializer_class = self.action_serializers.get(
            self.action, self.action_serializers["default"]
        )

        return super().get_serializer_class()
        # return self.serializer_class