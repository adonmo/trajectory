import unittest
from random import uniform, randint
import time

import trajectory


class TrajectoryCodecOfficialExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.decoded = [
            (38.500, -120.200, 1582482601),
            (40.700, -120.950, 1582482611),
            (43.252, -126.453, 1582482627),
        ]
        self.encoded = "_p~iF~ps|U_ynpijgz~G_ulLnnqC_c`|@_mqNvxq`@__t`B"
        self.encoded_with_precision_6 = (
            "_izlhA~rlgdF_c}mhpro}xA_{geC~ywl@_gjaR_kwzCn`{nI__qo]"
        )

    def test_decode(self):
        d = trajectory.decode(self.encoded)
        self.assertEqual(d, self.decoded)

    def test_encode(self):
        e = trajectory.encode(self.decoded)
        self.assertEqual(e, self.encoded)

    def test_encode_and_decode(self):
        data = self.decoded
        e = trajectory.encode(data)
        d = trajectory.decode(e)
        self.assertEqual(d, data)

    def test_decode_with_precision_6(self):
        d = trajectory.decode(self.encoded_with_precision_6, 6)
        self.assertEqual(d, self.decoded)

    def test_encode_with_precision_6(self):
        e = trajectory.encode(self.decoded, 6)
        self.assertEqual(e, self.encoded_with_precision_6)

    def test_encode_and_decode_with_precision_6(self):
        data = self.decoded
        e = trajectory.encode(data, 6)
        d = trajectory.decode(e, 6)
        self.assertEqual(d, data)


class TrajectoryCodecMultiplePointsTestCase(unittest.TestCase):
    def setUp(self):
        self.decoded = [
            (40.641, -8.654, 1582482601),
            (40.641, -8.654, 1582482602),
            (40.641, -8.656, 1582482603),
            (40.642, -8.656, 1582482604),
            (40.642, -8.655, 1582482605),
            (40.642, -8.655, 1582482606),
            (40.642, -8.655, 1582482607),
            (40.642, -8.653, 1582482608),
            (40.642, -8.653, 1582482609),
            (40.642, -8.653, 1582482610),
            (40.641, -8.653, 1582482611),
            (40.641, -8.654, 1582482612),
        ]
        self.encoded = "gu`wFnfys@_ynpijgz~G??_ibE?nK_ibEgE?_ibE?gE_ibE??_ibE??_ibE?oK_ibE??_ibE??_ibEfE?_ibE?fE_ibE"
        self.encoded_precision_6 = "o}oolA~ieoO_c}mhpro}xA??_c`|@?~{B_c`|@o}@?_c`|@?o}@_c`|@??_c`|@??_c`|@?_|B_c`|@??_c`|@??_c`|@n}@?_c`|@?n}@_c`|@"

    def test_decode(self):
        d = trajectory.decode(self.encoded)
        self.assertEqual(d, self.decoded)

    def test_encode(self):
        e = trajectory.encode(self.decoded)
        self.assertEqual(e, self.encoded)

    def test_encode_and_decode(self):
        data = self.decoded
        e = trajectory.encode(data)
        d = trajectory.decode(e)
        self.assertEqual(d, data)

    def test_decode_with_precision_6(self):
        d = trajectory.decode(self.encoded_precision_6, 6)
        self.assertEqual(d, self.decoded)

    def test_encode_with_precision_6(self):
        e = trajectory.encode(self.decoded, 6)
        self.assertEqual(e, self.encoded_precision_6)

    def test_encode_and_decode_with_precision_6(self):
        data = self.decoded
        e = trajectory.encode(data, 6)
        d = trajectory.decode(e, 6)
        self.assertEqual(d, data)


class TrajectoryCodecSinglePointTestCase(unittest.TestCase):
    def setUp(self):
        self.decoded = [(40.641, -8.653, 1582482601)]
        self.encoded = "gu`wFf`ys@_ynpijgz~G"
        self.encoded_precision_6 = "o}oolAnkcoO_c}mhpro}xA"

    def test_decode(self):
        d = trajectory.decode(self.encoded)
        self.assertEqual(d, self.decoded)

    def test_encode(self):
        e = trajectory.encode(self.decoded)
        self.assertEqual(e, self.encoded)

    def test_encode_and_decode(self):
        data = self.decoded
        e = trajectory.encode(data)
        d = trajectory.decode(e)
        self.assertEqual(d, data)

    def test_decode_with_precision_6(self):
        d = trajectory.decode(self.encoded_precision_6, 6)
        self.assertEqual(d, self.decoded)

    def test_encode_with_precision_6(self):
        e = trajectory.encode(self.decoded, 6)
        self.assertEqual(e, self.encoded_precision_6)

    def test_encode_and_decode_with_precision_6(self):
        data = self.decoded
        e = trajectory.encode(data, 6)
        d = trajectory.decode(e, 6)
        self.assertEqual(d, data)

    def test_encode_rounding(self):
        e = trajectory.encode([(0, 0.000006, 1582482601), (0, 0.000002, 1582482601)])
        self.assertEqual(e, "?A_ynpijgz~G?@?")


class TrajectoryCodecGeneratedDataTestCase(unittest.TestCase):
    def test_a_variety_of_precisions(self):
        """uses a generator to create a variety of lat-lon's across the global
            and tests a range of precision settings from 4 to 8"""

        def generator():
            while True:
                trajectory = []
                curr_t = 1582482600
                for i in range(2, randint(4, 10)):
                    lat, lon, curr_t = (
                        uniform(-180.0, 180.0),
                        uniform(-180.0, 180.0),
                        curr_t + uniform(2, 60),
                    )
                    trajectory.append((lat, lon, curr_t))
                yield trajectory

        patience = 3  # seconds.
        waypoints, okays = 0, 0

        g = generator()
        start = time.time()
        while time.time() < start + patience:
            precision = randint(4, 7)
            wp = next(g)
            waypoints += len(wp)
            traj = trajectory.encode(wp, precision)
            wp2 = trajectory.decode(traj, precision)
            if wp == wp2:
                okays += len(wp2)
            else:
                for idx, _ in enumerate(wp):
                    dx, dy, dt = (
                        abs(wp[idx][0] - wp2[idx][0]),
                        abs(wp[idx][1] - wp2[idx][1]),
                        abs(wp[idx][2] - wp2[idx][2]),
                    )
                    if (
                        dx > 10 ** -(precision - 1)
                        or dy > 10 ** -(precision - 1)
                        or dt > 10 ** -(precision - 1)
                    ):
                        print("idx={}, dx={}, dy={}, dt={}".format(idx, dx, dy, dt))
                    else:
                        okays += 1

        self.assertEqual(okays, waypoints)
        print(
            "encoded and decoded {0:.2f}% correctly for {1} waypoints @ {2} wp/sec".format(
                100 * okays / float(waypoints),
                waypoints,
                round(waypoints / patience, 0),
            )
        )
