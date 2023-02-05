from urllib.robotparser import RobotFileParser


def exclusion_standard(robots_url: str) -> RobotFileParser:
    """
    Robots Exclusion Standard.
    https://en.wikipedia.org/wiki/Robots_exclusion_standard
    """

    parser = RobotFileParser()
    parser.set_url(robots_url)
    parser.read()
    return parser


def validate(
    robots_url: str,
    init_url: str,
    useragent: str = "*",
) -> bool:
    """
    Validate URL by robots.txt.
    """

    parser = exclusion_standard(robots_url)
    if not parser.can_fetch(useragent=useragent, url=init_url):
        raise PermissionError("Cannot fetch")

    return True
