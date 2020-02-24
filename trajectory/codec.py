import itertools
import six
import math


class TrajectoryCodec(object):
    def _pcitr(self, iterable):
        return six.moves.zip(iterable, itertools.islice(iterable, 1, None))

    def _py2_round(self, x):
        # The polyline algorithm uses Python 2's way of rounding
        return int(math.copysign(math.floor(math.fabs(x) + 0.5), x))

    def _write(self, output, curr_value, prev_value, factor):
        curr_value = self._py2_round(curr_value * factor)
        prev_value = self._py2_round(prev_value * factor)
        coord = curr_value - prev_value
        coord <<= 1
        coord = coord if coord >= 0 else ~coord

        while coord >= 0x20:
            output.write(six.unichr((0x20 | (coord & 0x1F)) + 63))
            coord >>= 5

        output.write(six.unichr(coord + 63))

    def _trans(self, value, index):
        byte, result, shift = None, 0, 0

        while byte is None or byte >= 0x20:
            byte = ord(value[index]) - 63
            index += 1
            result |= (byte & 0x1F) << shift
            shift += 5

        return ~(result >> 1) if result & 1 else (result >> 1), index

    def decode(self, expression, precision=5):
        traj, index, lat, lng, time, length, factor = (
            [],
            0,
            0,
            0,
            0,
            len(expression),
            float(10 ** precision),
        )

        while index < length:
            lat_change, index = self._trans(expression, index)
            lng_change, index = self._trans(expression, index)
            time_change, index = self._trans(expression, index)
            lat += lat_change
            lng += lng_change
            time += time_change
            traj.append((lat / factor, lng / factor, time / factor))

        return traj

    def encode(self, traj, precision=5):
        output, factor = six.StringIO(), int(10 ** precision)

        self._write(output, traj[0][0], 0, factor)
        self._write(output, traj[0][1], 0, factor)
        self._write(output, traj[0][2], 0, factor)

        for prev, curr in self._pcitr(traj):
            self._write(output, curr[0], prev[0], factor)
            self._write(output, curr[1], prev[1], factor)
            self._write(output, curr[2], prev[2], factor)

        return output.getvalue()
