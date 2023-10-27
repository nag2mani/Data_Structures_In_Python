        def _validate(self, p):
            """Return associated node if the position is valid."""
            if not isinstance(p, self.Position):
                raise TypeError("p must be a proper Position type")
            if p._container is not self:
                raise ValueError("p does not belong to this container")
            if p._node._parent is p._node:  # convention for deprecated nodes
                raise ValueError("p is no longer valid")
            return p._node

        def _make_position(self, node):
            """Return Position instance for a given node (or None if no node)."""
            return self.Position(self, node) if node is not None else None