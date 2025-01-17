from istacpy.resources import resources


def get_structuralresources_categorisations(limit=25, offset=0, query=None, orderby=None):
    """Get categorisations

    This function returns the content from /v1.0/categorisations

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_categorisations()
        >>> get_structuralresources_categorisations(query = "ID EQ 2090", orderby = "ID ASC")
    """
    # Parse query
    query = resources.resources.get_content(query)

    # Parse orderby
    orderby = resources.resources.get_content(orderby)
    
    # Build URL
    api = "structural-resources"
    path = "categorisations"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&orderby=" + orderby + "&query=" + query
    path = path + params
    url = resources.get_url(api, path)
    
    # Get content
    content = resources.get_content(url)
    
    return content


def get_structuralresources_categorisations_agency(agencyid, limit=25, offset=0, query=None, orderby=None):
    """Get categorisations agency

    This function returns the content from /v1.0/categorisations/{agencyID}

    Args:
        agencyid (string): Identifier of the agency that publishes.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_categorisations_agency("ISTAC")
    """
    # Parse query
    query = resources.resources.get_content(query)
    
    # Parse orderby
    orderby = resources.resources.get_content(orderby)
    
    # Build URL
    api = "structural-resources"
    path = "categorisations"
    resource = agencyid
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&orderby=" + orderby + "&query=" + query
    resource = resource + params
    url = resources.get_url(api, path, resource)
    
    # Get content
    content = resources.get_content(url)
    
    return content


def get_structuralresources_categorisations_agency_resource(agencyid, resourceid, limit=25, offset=0, query=None,
                                                            orderby=None):
    """Get categorisations agency resource

    This function returns the content from /v1.0/categorisations/{agencyID}/{resourceID}

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_categorisations_agency_resource("ISTAC", "cat2")
    """
    # Parse query
    query = resources.resources.get_content(query)

    # Parse orderby
    orderby = resources.resources.get_content(orderby)

    # Build URL
    api = "structural-resources"
    path = "categorisations"
    resource = agencyid + "/" + resourceid
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&orderby=" + orderby + "&query=" + query
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_categorisations_agency_resource_version(agencyid, resourceid, version):
    """Get categorisations agency resource version
    
    This function returns the content from /v1.0/categorisations/{agencyID}/{resourceID}/{version}
    
    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.
        
    Examples:
        >>> get_structuralresources_categorisations_agency_resource_version("ISTAC", "cat2", "01.000") 
    """
    # Build URL
    api = "structural-resources"
    path = "categorisations"
    resource = agencyid + "/" + resourceid + "/" + version
    url = resources.get_url(api, path, resource)
    
    # Get content
    content = resources.get_content(url)
    
    return content


def get_structuralresources_category_schemes(limit=25, offset=0, query=None, orderby=None):
    """Get category schemes

    This function returns the content from /v1.0/categoryschemes

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_category_schemes()
        >>> get_structuralresources_category_schemes(query = "ID EQ 2090", orderby = "ID ASC")
    """
    # Parse query
    query = resources.resources.get_content(query)

    # Parse orderby
    orderby = resources.resources.get_content(orderby)

    # Build URL
    api = "structural-resources"
    path = "categoryschemes"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&orderby=" + orderby + "&query=" + query
    path = path + params
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_category_schemes_agency(agencyid, limit=25, offset=0, query=None, orderby=None):
    """Get category schemes agency

    This function returns the content from /v1.0/categoryschemes/{agencyID}

    Args:
        agencyid (string): Identifier of the agency that publishes.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_category_schemes_agency("ISTAC", query = "ID EQ 2090", orderby = "ID ASC")
    """
    # Parse query
    query = resources.resources.get_content(query)

    # Parse orderby
    orderby = resources.resources.get_content(orderby)

    # Build URL
    api = "structural-resources"
    path = "categoryschemes"
    resource = agencyid
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&orderby=" + orderby + "&query=" + query
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_category_schemes_agency_resource(agencyid, resourceid, limit=25, offset=0, query=None,
                                                             orderby=None):
    """ Get category schemes agency resource

    This function returns the content from /v1.0/categoryschemes/{agencyID}/{resourceID}

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_category_schemes_agency_resource("ISTAC", "TEMAS_CANARIAS")
    """
    # Parse query
    query = resources.resources.get_content(query)

    # Parse orderby
    orderby = resources.resources.get_content(orderby)

    # Build URL
    api = "structural-resources"
    path = "categoryschemes"
    resource = agencyid + "/" + resourceid
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&orderby=" + orderby + "&query=" + query
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_category_schemes_agency_resource_version(agencyid, resourceid, version):
    """Get category schemes agency resource version

    This function returns the content from /v1.0/categoryschemes/{agencyID}/{resourceID}/{version}

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.

    Examples:
        >>> get_structuralresources_category_schemes_agency_resource_version("ISTAC", "TEMAS_CANARIAS", "01.000")
    """
    # Build URL
    api = "structural-resources"
    path = "categoryschemes"
    resource = agencyid + "/" + resourceid + "/" + version
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_category_schemes_agency_resource_version_categories(agencyid, resourceid, version,
                                                                                limit=25, offset=0, query=None,
                                                                                orderby=None):
    """Get category schemes agency resource version categories

    This function returns the content from /v1.0/categoryschemes/{agencyID}/{resourceID}/{version}/categories

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_category_schemes_agency_resource_version_categories("ISTAC", "TEMAS_CANARIAS",
            "01.000")
    """
    # Parse query
    query = resources.resources.get_content(query)

    # Parse orderby
    orderby = resources.resources.get_content(orderby)

    # Build URL
    api = "structural-resources"
    path = "categoryschemes"
    resource = agencyid + "/" + resourceid + "/" + version + "/categories"
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_category_schemes_agency_resource_version_categories_id(agencyid, resourceid, version,
                                                                                   categoryid):
    """Get category schemes agency resource version categories (id)

    This function returns the content from /v1.0/categoryschemes/{agencyID}/{resourceID}/{version}/categories/
    {categoryID}

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.
        categoryid (string): category identifier

    Examples:
        >>> get_structuralresources_category_schemes_agency_resource_version_categories_id("ISTAC", "TEMAS_CANARIAS",
            "01.000", "060")
        >>> get_structuralresources_category_schemes_agency_resource_version_categories_id("ISTAC", "TEMAS_CANARIAS",
            "01.000", "060.060_010.060_010_010")
    """
    # Build URL
    api = "structural-resources"
    path = "categoryschemes"
    resource = agencyid + "/" + resourceid + "/" + version + "/categories/" + categoryid
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content
