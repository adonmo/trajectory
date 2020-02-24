from .codec import TrajectoryCodec


def decode(expression, precision=5):
    """
    Decode a polyline string into a set of coordinates.

    :param expression: Polyline string, e.g. '_p~iF~ps|U_ynpijgz~G_ulLnnqC_c`|@_mqNvxq`@__t`B'.
    :param precision: Precision of the encoded coordinates. Google Maps uses 5, OpenStreetMap uses 6.
        The default value is 5.
    :return: List of coordinate tuples in (lat, lon, unix time in seconds) order.
    """
    return TrajectoryCodec().decode(expression, precision)


def encode(trajectory, precision=5):
    """
    Encode a set of trajectory in a polyline string.

    :param trajectory: List of spatiotemporal tuples, e.g. [(0, 0, 1582482601), (1, 0, 1582482611)]. The order
        is expected to be (lat, lon, unix time in seconds).
    :param precision: Precision of the trajectory to encode. Google Maps uses 5, OpenStreetMap uses 6.
        The default value is 5.
    :return: The encoded polyline string.
    """
    return TrajectoryCodec().encode(trajectory, precision)


__all__ = ["decode", "encode"]
