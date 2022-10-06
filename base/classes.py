class MixedSerializer:
    def get_serializer(self, *args, **kwargs):
        try:
            serializer_class = self.serializer_class_by_action[self.action]
        except KeyError:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)