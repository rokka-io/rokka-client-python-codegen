# coding: utf-8

"""
    rokka.io

    digital image processing done right. [Documentation](https://rokka.io/documentation). [Changelog](https://api.rokka.io/changelog.md).  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StackOperationDescriptionProperties(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'default': 'str',
        'description': 'str',
        'pattern': 'str',
        'minimum': 'int',
        'maximum': 'int',
        'values': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'default': 'default',
        'description': 'description',
        'pattern': 'pattern',
        'minimum': 'minimum',
        'maximum': 'maximum',
        'values': 'values'
    }

    def __init__(self, type=None, default=None, description=None, pattern=None, minimum=None, maximum=None, values=None):  # noqa: E501
        """StackOperationDescriptionProperties - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._default = None
        self._description = None
        self._pattern = None
        self._minimum = None
        self._maximum = None
        self._values = None
        self.discriminator = None

        self.type = type
        if default is not None:
            self.default = default
        self.description = description
        if pattern is not None:
            self.pattern = pattern
        if minimum is not None:
            self.minimum = minimum
        if maximum is not None:
            self.maximum = maximum
        if values is not None:
            self.values = values

    @property
    def type(self):
        """Gets the type of this StackOperationDescriptionProperties.  # noqa: E501


        :return: The type of this StackOperationDescriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StackOperationDescriptionProperties.


        :param type: The type of this StackOperationDescriptionProperties.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def default(self):
        """Gets the default of this StackOperationDescriptionProperties.  # noqa: E501


        :return: The default of this StackOperationDescriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this StackOperationDescriptionProperties.


        :param default: The default of this StackOperationDescriptionProperties.  # noqa: E501
        :type: str
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this StackOperationDescriptionProperties.  # noqa: E501


        :return: The description of this StackOperationDescriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StackOperationDescriptionProperties.


        :param description: The description of this StackOperationDescriptionProperties.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def pattern(self):
        """Gets the pattern of this StackOperationDescriptionProperties.  # noqa: E501


        :return: The pattern of this StackOperationDescriptionProperties.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this StackOperationDescriptionProperties.


        :param pattern: The pattern of this StackOperationDescriptionProperties.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def minimum(self):
        """Gets the minimum of this StackOperationDescriptionProperties.  # noqa: E501


        :return: The minimum of this StackOperationDescriptionProperties.  # noqa: E501
        :rtype: int
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this StackOperationDescriptionProperties.


        :param minimum: The minimum of this StackOperationDescriptionProperties.  # noqa: E501
        :type: int
        """

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this StackOperationDescriptionProperties.  # noqa: E501


        :return: The maximum of this StackOperationDescriptionProperties.  # noqa: E501
        :rtype: int
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this StackOperationDescriptionProperties.


        :param maximum: The maximum of this StackOperationDescriptionProperties.  # noqa: E501
        :type: int
        """

        self._maximum = maximum

    @property
    def values(self):
        """Gets the values of this StackOperationDescriptionProperties.  # noqa: E501


        :return: The values of this StackOperationDescriptionProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this StackOperationDescriptionProperties.


        :param values: The values of this StackOperationDescriptionProperties.  # noqa: E501
        :type: list[str]
        """

        self._values = values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StackOperationDescriptionProperties, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StackOperationDescriptionProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other