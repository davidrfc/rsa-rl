

from rsarl.networks.topology import Topology

class GERMAN(Topology): 
	""" German Network from Deutsche Telekom (GERMAN) """

	def __init__(self):
		super().__init__('GERMAN')

	def weighted_edges(self):
		return [\
                  (0, 6, 306),
                  (0, 7, 298),
                  (0, 10, 174),
                  (1, 6, 114),
                  (1, 7, 120),
                  (1, 13, 144),
                  (2, 4, 37),
                  (2, 7, 208),
                  (2, 9, 88),
                  (2, 13, 278),
                  (3, 4, 36),
                  (3, 9, 41),
                  (5, 7, 316),
                  (5, 9, 182),
                  (5, 10, 353),
                  (5, 11, 85),
                  (5, 14, 224),
                  (6, 7, 157),
                  (7, 10, 258),
                  (8, 11, 64),
                  (8, 15, 74),
                  (10, 14, 275),
                  (12, 14, 179),
                  (12, 16, 143),
                  (14, 15, 187),
                  (15, 16, 86)
		]


	def edges(self):
		return [\
                  (0, 6),
                  (0, 7),
                  (0, 10),
                  (1, 6),
                  (1, 7),
                  (1, 13),
                  (2, 4),
                  (2, 7),
                  (2, 9),
                  (2, 13),
                  (3, 4),
                  (3, 9),
                  (5, 7),
                  (5, 9),
                  (5, 10),
                  (5, 11),
                  (5, 14),
                  (6, 7),
                  (7, 10),
                  (8, 11),
                  (8, 15),
                  (10, 14),
                  (12, 14),
                  (12, 16),
                  (14, 15),
                  (15, 16)
            ]


	def nodes_2D_pos(self):
		return dict([\
                  [0,  (127, 121)],
                  [1,  (58, 262)],
                  [2,  (170, 160)],
                  [3,  (191, 128)],
                  [4,  (12, 183)],
                  [5,  (56, 261)],
                  [6,  (260, 135)],
                  [7,  (175, 179)],
                  [8,  (76, 178)],
                  [9,  (126, 285)],
                  [10,  (115, 118)],
                  [11,  (195, 143)],
                  [12,  (100, 12)],
                  [13,  (277, 249)],
                  [14,  (297, 78)],
                  [15,  (136, 54)],
                  [16,  (217, 118)]
		])

