import unittest
from pathlib import Path

from dissect.definitions import TRAIT_PATH
from dissect.traits.merge_trait_results import merge_results
from dissect.utils.json_handler import save_into_json, load_from_json

merge_inputs = [
    {
        "x962_sim_128_seed_diff_3640081": {
            "{'l': 2}": {
                "factorization": [
                    [
                        "x^3 + 340282366762482138434845932244680310780*x + 69858533633187904213879055222589606230",
                        1,
                    ]
                ],
                "degs_list": [3],
                "len": 1,
            },
            "{'l': 3}": {
                "factorization": [
                    ["x + 57684394103371434835061991181330480188", 1],
                    [
                        "x^3 + 282597972659110703599783941063349830595*x^2 + 131361467314673257169224863338731807923*x + 235236902321734479651538900332443239374",
                        1,
                    ],
                ],
                "degs_list": [1, 3],
                "len": 2,
            },
        }
    },
    {
        "x962_sim_128_seed_diff_3640081": {
            "{'l': 2}": {"degs_list": [3], "len": 1},
            "{'l': 5}": {
                "factorization": [
                    [
                        "x^4 + 177980960030996657236569222432725655388*x^3 + 179015355494025119327482085732000807424*x^2 + 216744513767469203344656553134460169377*x + 59873075032689953147204208915541107074",
                        1,
                    ],
                    [
                        "x^4 + 215301915362031801597625930420423931372*x^3 + 22866495619330969609719939869590653745*x^2 + 138217323356300110336638435026096196018*x + 300868354871567179274729464879481506102",
                        1,
                    ],
                    [
                        "x^4 + 287281858131935818035496711636211034806*x^3 + 23410975633657774686744387410174523121*x^2 + 270327788618048874734423025783234213456*x + 70315420425780573490221884732686552257",
                        1,
                    ],
                ],
                "degs_list": [4, 4, 4],
                "len": 3,
            },
        }
    },
    {
        "x962_sim_128_seed_diff_2012754": {
            "{'l': 2}": {
                "factorization": [
                    ["x + 107153254081081322654423031912408718212", 1],
                    [
                        "x^2 + 233129112681400815780422900332271592571*x + 325820627126239880063822572368425406855",
                        1,
                    ],
                ],
                "degs_list": [1, 2],
                "len": 2,
            }
        }
    },
]

merge_output = {
    "x962_sim_128_seed_diff_3640081": {
        "{'l': 2}": {
            "factorization": [
                [
                    "x^3 + 340282366762482138434845932244680310780*x + 69858533633187904213879055222589606230",
                    1,
                ]
            ],
            "degs_list": [3],
            "len": 1,
        },
        "{'l': 3}": {
            "factorization": [
                ["x + 57684394103371434835061991181330480188", 1],
                [
                    "x^3 + 282597972659110703599783941063349830595*x^2 + 131361467314673257169224863338731807923*x + 235236902321734479651538900332443239374",
                    1,
                ],
            ],
            "degs_list": [1, 3],
            "len": 2,
        },
        "{'l': 5}": {
            "factorization": [
                [
                    "x^4 + 177980960030996657236569222432725655388*x^3 + 179015355494025119327482085732000807424*x^2 + 216744513767469203344656553134460169377*x + 59873075032689953147204208915541107074",
                    1,
                ],
                [
                    "x^4 + 215301915362031801597625930420423931372*x^3 + 22866495619330969609719939869590653745*x^2 + 138217323356300110336638435026096196018*x + 300868354871567179274729464879481506102",
                    1,
                ],
                [
                    "x^4 + 287281858131935818035496711636211034806*x^3 + 23410975633657774686744387410174523121*x^2 + 270327788618048874734423025783234213456*x + 70315420425780573490221884732686552257",
                    1,
                ],
            ],
            "degs_list": [4, 4, 4],
            "len": 3,
        },
    },
    "x962_sim_128_seed_diff_2012754": {
        "{'l': 2}": {
            "factorization": [
                ["x + 107153254081081322654423031912408718212", 1],
                [
                    "x^2 + 233129112681400815780422900332271592571*x + 325820627126239880063822572368425406855",
                    1,
                ],
            ],
            "degs_list": [1, 2],
            "len": 2,
        }
    },
}


class TestMergeTestResults(unittest.TestCase):
    def test_merging_and_file_manipulation(self):
        tmp_test = Path(TRAIT_PATH, "a00")
        tmp_test.mkdir()

        for _ in range(2):
            # check functionality without and with already existing result file
            for (i, merge_input) in enumerate(merge_inputs):
                save_into_json(
                    merge_input,
                    Path(
                        tmp_test,
                        "a00_part"
                        + str(i + 1).zfill(4)
                        + "_of_"
                        + str(len(merge_inputs)).zfill(4)
                        + ".json",
                    ),
                    "w+",
                )
            merge_results("a00")
            results = load_from_json(Path(tmp_test, "a00.json"))
            self.assertEqual(results, merge_output)

        Path(tmp_test, "a00.json").unlink()
        tmp_test.rmdir()


if __name__ == "__main__":
    unittest.main()
