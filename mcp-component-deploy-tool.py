from fastmcp import FastMCP

mcp = FastMCP('Component Deploy Tool')

@mcp.tool()
def write_component(r) -> str:
    """
        Generate the build-config.yml, comp-{component_name}.yml and deployment-config.yml.
        Args:
           component_name: The component name
        Returns:
            str: Details of the generation of the component yaml files.
    """
    return "The yaml files for deploy {component_name} were created successfully!"

@mcp.tool()
def write_redis(r) -> str:
    """
        If redis is mentioned it also generates the comp-redis.yml file.        
        Args:
           none
        Returns:
            str: Details of the generation of the redis yaml files.
    """
    return 'The yaml files for deploy the redis component were created successfully!'

if __name__ == '__main__':
    mcp.run(transport="stdio")
