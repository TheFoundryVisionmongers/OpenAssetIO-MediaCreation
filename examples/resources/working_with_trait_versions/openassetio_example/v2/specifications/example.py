
"""
Specification definitions in the 'example' namespace.

Test specifications.
"""

# WARNING: This file is auto-generated by openassetio-traitgen, do not edit.

from openassetio.trait import TraitsData


from .. import traits



class ExampleSpecification:
    """
    An example specification.
    Usage: entity
    """
    kTraitSet = {
        # 'openassetio-example:example.Unchanged'
        traits.example.UnchangedTrait.kId,
        # 'openassetio-example:example.Updated'
        traits.example.UpdatedTrait.kId,
        
    }

    def __init__(self, traitsData):
        """
        Constructs the specification as a view on the supplied
        shared @fqref{TraitsData} "TraitsData" instance.

        @param traitsData @fqref{TraitsData} "TraitsData"

        @warning Specifications are always a view on the supplied data,
        which is held by reference. Any changes made to the data will be
        visible to any other specifications or @ref trait "traits" that
        wrap the same TraitsData instance.
        """
        if not isinstance(traitsData, TraitsData):
            raise TypeError("Specifications must be constructed with a TraitsData instance")
        self.__data = traitsData

    def traitsData(self):
        """
        Returns the underlying (shared) @fqref{TraitsData} "TraitsData"
        instance held by this specification.
        """
        return self.__data

    @classmethod
    def create(cls):
        """
        Returns a new instance of the Specification, holding a new
        @fqref{TraitsData} "TraitsData" instance, pre-populated with all
        of the specifications traits.
        """
        data = TraitsData(cls.kTraitSet)
        return cls(data)


    def unchangedTrait(self):
        """
        Returns the view for the 'openassetio-example:example.Unchanged' trait wrapped around
        the data held in this instance.
        """
        return traits.example.UnchangedTrait(self.traitsData())
        
    def updatedTrait(self):
        """
        Returns the view for the 'openassetio-example:example.Updated' trait wrapped around
        the data held in this instance.
        """
        return traits.example.UpdatedTrait(self.traitsData())
        