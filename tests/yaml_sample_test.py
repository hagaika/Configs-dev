from configs.yaml_sample import Structure


class TestStructure:
    def test_no_structure(self):
        struct = Structure()
        assert struct.show_structure() == "Structure yet to be defined."

    def test_structured(self):
        import os

        from os.path import join

        struct = Structure()
        struct.structure_from_file(join(os.getcwd(), "layers.yaml"))

    def test_show_structure(self):
        import os

        from os.path import join

        struct = Structure()
        struct.structure_from_file(join(os.getcwd(), "layers.yaml"))
        print(struct.show_structure())
