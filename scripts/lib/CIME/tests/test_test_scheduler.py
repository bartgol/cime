#!/usr/bin/env python3

import os
import unittest
from unittest import mock

from CIME.test_scheduler import TestScheduler

class TestTestScheduler(unittest.TestCase):

    @mock.patch.dict(os.environ, {"CIME_MODEL": "cesm"})
    @mock.patch("time.strftime", return_value="00:00:00")
    def test_chksum(self, strftime): # pylint: disable=unused-argument
        ts = TestScheduler(
            ["SEQ_Ln9.f19_g16_rx1.A.cori-haswell_gnu"],
            machine_name="cori-haswell",
            chksum=True,
            test_root="/tests",
        )

        with mock.patch.object(ts, "_shell_cmd_for_phase") as _shell_cmd_for_phase:
            ts._run_phase("SEQ_Ln9.f19_g16_rx1.A.cori-haswell_gnu") # pylint: disable=protected-access

            _shell_cmd_for_phase.assert_called_with(
                "SEQ_Ln9.f19_g16_rx1.A.cori-haswell_gnu",
                "./case.submit --skip-preview-namelist --chksum",
                "RUN",
                from_dir="/tests/SEQ_Ln9.f19_g16_rx1.A.cori-haswell_gnu.00:00:00",
            )

if __name__ == '__main__':
    unittest.main()
