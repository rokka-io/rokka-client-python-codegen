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


class OrganizationOptions(object):
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
        'remote_basepath': 'str',
        'remote_fullurl_allow': 'bool',
        'remote_fullurl_whitelist': 'list[str]'
    }

    attribute_map = {
        'remote_basepath': 'remote_basepath',
        'remote_fullurl_allow': 'remote_fullurl_allow',
        'remote_fullurl_whitelist': 'remote_fullurl_whitelist'
    }

    def __init__(self, remote_basepath=None, remote_fullurl_allow=None, remote_fullurl_whitelist=None):  # noqa: E501
        """OrganizationOptions - a model defined in Swagger"""  # noqa: E501

        self._remote_basepath = None
        self._remote_fullurl_allow = None
        self._remote_fullurl_whitelist = None
        self.discriminator = None

        if remote_basepath is not None:
            self.remote_basepath = remote_basepath
        if remote_fullurl_allow is not None:
            self.remote_fullurl_allow = remote_fullurl_allow
        if remote_fullurl_whitelist is not None:
            self.remote_fullurl_whitelist = remote_fullurl_whitelist

    @property
    def remote_basepath(self):
        """Gets the remote_basepath of this OrganizationOptions.  # noqa: E501


        :return: The remote_basepath of this OrganizationOptions.  # noqa: E501
        :rtype: str
        """
        return self._remote_basepath

    @remote_basepath.setter
    def remote_basepath(self, remote_basepath):
        """Sets the remote_basepath of this OrganizationOptions.


        :param remote_basepath: The remote_basepath of this OrganizationOptions.  # noqa: E501
        :type: str
        """

        self._remote_basepath = remote_basepath

    @property
    def remote_fullurl_allow(self):
        """Gets the remote_fullurl_allow of this OrganizationOptions.  # noqa: E501


        :return: The remote_fullurl_allow of this OrganizationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._remote_fullurl_allow

    @remote_fullurl_allow.setter
    def remote_fullurl_allow(self, remote_fullurl_allow):
        """Sets the remote_fullurl_allow of this OrganizationOptions.


        :param remote_fullurl_allow: The remote_fullurl_allow of this OrganizationOptions.  # noqa: E501
        :type: bool
        """

        self._remote_fullurl_allow = remote_fullurl_allow

    @property
    def remote_fullurl_whitelist(self):
        """Gets the remote_fullurl_whitelist of this OrganizationOptions.  # noqa: E501


        :return: The remote_fullurl_whitelist of this OrganizationOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._remote_fullurl_whitelist

    @remote_fullurl_whitelist.setter
    def remote_fullurl_whitelist(self, remote_fullurl_whitelist):
        """Sets the remote_fullurl_whitelist of this OrganizationOptions.


        :param remote_fullurl_whitelist: The remote_fullurl_whitelist of this OrganizationOptions.  # noqa: E501
        :type: list[str]
        """

        self._remote_fullurl_whitelist = remote_fullurl_whitelist

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
        if issubclass(OrganizationOptions, dict):
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
        if not isinstance(other, OrganizationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
