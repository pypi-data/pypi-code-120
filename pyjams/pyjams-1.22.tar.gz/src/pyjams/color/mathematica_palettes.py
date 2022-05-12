#!/usr/bin/env python
"""
Color palettes from Mathematica

.. moduleauthor:: Juliane Mai and Matthias Cuntz

History
    * Written Sep 2014, Juliane Mai
    * Made dictionaries with color palettes,
      Mar 2015, Matthias Cuntz
    * Ported to pyjams, Nov 2021, Matthias Cuntz
    * flake8 compatible, Nov 2021, Matthias Cuntz
    * Prepend mathematica to all palette names, Nov 2021, Matthias Cuntz

"""

__all__ = ['mathematica_rainbow']


# Mathematica color maps
mathematica_rainbow = {
    'mathematica_dark_rainbow_8': [
        (0.237736, 0.340215, 0.575113),
        (0.256345, 0.364426, 0.514838),
        (0.277947, 0.450097, 0.328156),
        (0.385163, 0.535801, 0.249218),
        (0.624866, 0.673302, 0.264296),
        (0.829244, 0.75748, 0.309318),
        (0.845341, 0.62487, 0.315178),
        (0.750604, 0.309223, 0.249086) ],
    'mathematica_dark_rainbow_16': [
        (0.237736, 0.340215, 0.575113),
        (0.247683, 0.343139, 0.564512),
        (0.256345, 0.364426, 0.514838),
        (0.263078, 0.413258, 0.406556),
        (0.277947, 0.450097, 0.328156),
        (0.307085, 0.486942, 0.267712),
        (0.385163, 0.535801, 0.249218),
        (0.494571, 0.599579, 0.250249),
        (0.624866, 0.673302, 0.264296),
        (0.74247, 0.731421, 0.288772),
        (0.829244, 0.75748, 0.309318),
        (0.86977, 0.735451, 0.323966),
        (0.845341, 0.62487, 0.315178),
        (0.80244, 0.483782, 0.294397),
        (0.750604, 0.309223, 0.249086),
        (0.72987, 0.239399, 0.230961) ],
    'mathematica_dark_rainbow_256': [
        (0.237736, 0.340215, 0.575113),
        (0.238358, 0.340398, 0.57445),
        (0.238979, 0.34058, 0.573788),
        (0.239601, 0.340763, 0.573125),
        (0.240223, 0.340946, 0.572463),
        (0.240844, 0.341129, 0.5718),
        (0.241466, 0.341311, 0.571138),
        (0.242088, 0.341494, 0.570475),
        (0.242709, 0.341677, 0.569812),
        (0.243331, 0.34186, 0.56915),
        (0.243953, 0.342042, 0.568487),
        (0.244574, 0.342225, 0.567825),
        (0.245196, 0.342408, 0.567162),
        (0.245818, 0.342591, 0.566499),
        (0.24644, 0.342773, 0.565837),
        (0.247061, 0.342956, 0.565174),
        (0.247683, 0.343139, 0.564512),
        (0.248305, 0.343321, 0.563849),
        (0.248926, 0.343504, 0.563187),
        (0.249548, 0.343687, 0.562524),
        (0.25017, 0.34387, 0.561861),
        (0.250791, 0.344052, 0.561199),
        (0.251413, 0.344235, 0.560536),
        (0.252035, 0.344418, 0.559874),
        (0.252656, 0.344601, 0.559211),
        (0.253278, 0.344783, 0.558549),
        (0.253819, 0.346114, 0.555444),
        (0.25424, 0.349166, 0.548676),
        (0.254661, 0.352218, 0.541909),
        (0.255082, 0.35527, 0.535141),
        (0.255503, 0.358322, 0.528373),
        (0.255924, 0.361374, 0.521606),
        (0.256345, 0.364426, 0.514838),
        (0.256765, 0.367478, 0.508071),
        (0.257186, 0.37053, 0.501303),
        (0.257607, 0.373582, 0.494535),
        (0.258028, 0.376634, 0.487768),
        (0.258449, 0.379686, 0.481),
        (0.25887, 0.382738, 0.474233),
        (0.259291, 0.38579, 0.467465),
        (0.259711, 0.388842, 0.460697),
        (0.260132, 0.391894, 0.45393),
        (0.260553, 0.394946, 0.447162),
        (0.260974, 0.397998, 0.440394),
        (0.261395, 0.40105, 0.433627),
        (0.261816, 0.404102, 0.426859),
        (0.262237, 0.407154, 0.420092),
        (0.262657, 0.410206, 0.413324),
        (0.263078, 0.413258, 0.406556),
        (0.263499, 0.41631, 0.399789),
        (0.26392, 0.419362, 0.393021),
        (0.264341, 0.422414, 0.386254),
        (0.26527, 0.424716, 0.381353),
        (0.266327, 0.426831, 0.37692),
        (0.267383, 0.428946, 0.372487),
        (0.268439, 0.431061, 0.368054),
        (0.269496, 0.433176, 0.363621),
        (0.270552, 0.435291, 0.359188),
        (0.271609, 0.437407, 0.354754),
        (0.272665, 0.439522, 0.350321),
        (0.273721, 0.441637, 0.345888),
        (0.274778, 0.443752, 0.341455),
        (0.275834, 0.445867, 0.337022),
        (0.276891, 0.447982, 0.332589),
        (0.277947, 0.450097, 0.328156),
        (0.279003, 0.452212, 0.323722),
        (0.28006, 0.454327, 0.319289),
        (0.281116, 0.456442, 0.314856),
        (0.282173, 0.458557, 0.310423),
        (0.283229, 0.460672, 0.30599),
        (0.284285, 0.462787, 0.301557),
        (0.285342, 0.464903, 0.297123),
        (0.286398, 0.467018, 0.29269),
        (0.287455, 0.469133, 0.288257),
        (0.288511, 0.471248, 0.283824),
        (0.289567, 0.473363, 0.279391),
        (0.290624, 0.475478, 0.274958),
        (0.292445, 0.477781, 0.27118),
        (0.297325, 0.480834, 0.270024),
        (0.302205, 0.483888, 0.268868),
        (0.307085, 0.486942, 0.267712),
        (0.311965, 0.489996, 0.266556),
        (0.316844, 0.493049, 0.2654),
        (0.321724, 0.496103, 0.264244),
        (0.326604, 0.499157, 0.263089),
        (0.331484, 0.50221, 0.261933),
        (0.336364, 0.505264, 0.260777),
        (0.341244, 0.508318, 0.259621),
        (0.346124, 0.511372, 0.258465),
        (0.351004, 0.514425, 0.257309),
        (0.355883, 0.517479, 0.256153),
        (0.360763, 0.520533, 0.254997),
        (0.365643, 0.523586, 0.253841),
        (0.370523, 0.52664, 0.252685),
        (0.375403, 0.529694, 0.25153),
        (0.380283, 0.532748, 0.250374),
        (0.385163, 0.535801, 0.249218),
        (0.390043, 0.538855, 0.248062),
        (0.394923, 0.541909, 0.246906),
        (0.399802, 0.544962, 0.24575),
        (0.404682, 0.548016, 0.244594),
        (0.409562, 0.55107, 0.243438),
        (0.414442, 0.554124, 0.242282),
        (0.42128, 0.55811, 0.242347),
        (0.429424, 0.562717, 0.243225),
        (0.437567, 0.567325, 0.244103),
        (0.44571, 0.571933, 0.244981),
        (0.453854, 0.57654, 0.245859),
        (0.461997, 0.581148, 0.246737),
        (0.470141, 0.585756, 0.247615),
        (0.478284, 0.590363, 0.248493),
        (0.486428, 0.594971, 0.249371),
        (0.494571, 0.599579, 0.250249),
        (0.502714, 0.604187, 0.251126),
        (0.510858, 0.608794, 0.252004),
        (0.519001, 0.613402, 0.252882),
        (0.527145, 0.61801, 0.25376),
        (0.535288, 0.622617, 0.254638),
        (0.543432, 0.627225, 0.255516),
        (0.551575, 0.631833, 0.256394),
        (0.559719, 0.63644, 0.257272),
        (0.567862, 0.641048, 0.25815),
        (0.576005, 0.645656, 0.259028),
        (0.584149, 0.650264, 0.259906),
        (0.592292, 0.654871, 0.260784),
        (0.600436, 0.659479, 0.261662),
        (0.608579, 0.664087, 0.26254),
        (0.616723, 0.668694, 0.263418),
        (0.624866, 0.673302, 0.264296),
        (0.632216, 0.676934, 0.265826),
        (0.639567, 0.680567, 0.267356),
        (0.646917, 0.684199, 0.268885),
        (0.654267, 0.687832, 0.270415),
        (0.661617, 0.691464, 0.271945),
        (0.668968, 0.695097, 0.273475),
        (0.676318, 0.698729, 0.275004),
        (0.683668, 0.702361, 0.276534),
        (0.691018, 0.705994, 0.278064),
        (0.698369, 0.709626, 0.279594),
        (0.705719, 0.713259, 0.281123),
        (0.713069, 0.716891, 0.282653),
        (0.72042, 0.720523, 0.284183),
        (0.72777, 0.724156, 0.285713),
        (0.73512, 0.727788, 0.287242),
        (0.74247, 0.731421, 0.288772),
        (0.749821, 0.735053, 0.290302),
        (0.757171, 0.738686, 0.291832),
        (0.764521, 0.742318, 0.293362),
        (0.771871, 0.74595, 0.294891),
        (0.779222, 0.749583, 0.296421),
        (0.786572, 0.753215, 0.297951),
        (0.793922, 0.756848, 0.299481),
        (0.801273, 0.76048, 0.30101),
        (0.808623, 0.764113, 0.30254),
        (0.814046, 0.765741, 0.303824),
        (0.816579, 0.764364, 0.30474),
        (0.819112, 0.762988, 0.305655),
        (0.821645, 0.761611, 0.306571),
        (0.824178, 0.760234, 0.307486),
        (0.826711, 0.758857, 0.308402),
        (0.829244, 0.75748, 0.309318),
        (0.831776, 0.756103, 0.310233),
        (0.834309, 0.754727, 0.311149),
        (0.836842, 0.75335, 0.312064),
        (0.839375, 0.751973, 0.31298),
        (0.841908, 0.750596, 0.313895),
        (0.844441, 0.749219, 0.314811),
        (0.846974, 0.747842, 0.315726),
        (0.849507, 0.746466, 0.316642),
        (0.85204, 0.745089, 0.317557),
        (0.854572, 0.743712, 0.318473),
        (0.857105, 0.742335, 0.319389),
        (0.859638, 0.740958, 0.320304),
        (0.862171, 0.739581, 0.32122),
        (0.864704, 0.738205, 0.322135),
        (0.867237, 0.736828, 0.323051),
        (0.86977, 0.735451, 0.323966),
        (0.872303, 0.734074, 0.324882),
        (0.874836, 0.732697, 0.325797),
        (0.877368, 0.73132, 0.326713),
        (0.875842, 0.724409, 0.326164),
        (0.8733, 0.716114, 0.325248),
        (0.870758, 0.707819, 0.324333),
        (0.868216, 0.699524, 0.323417),
        (0.865675, 0.691229, 0.322502),
        (0.863133, 0.682934, 0.321586),
        (0.860591, 0.674639, 0.320671),
        (0.85805, 0.666344, 0.319755),
        (0.855508, 0.658049, 0.31884),
        (0.852966, 0.649754, 0.317924),
        (0.850424, 0.641459, 0.317009),
        (0.847883, 0.633164, 0.316093),
        (0.845341, 0.62487, 0.315178),
        (0.842799, 0.616575, 0.314262),
        (0.840258, 0.60828, 0.313346),
        (0.837716, 0.599985, 0.312431),
        (0.835174, 0.59169, 0.311515),
        (0.832632, 0.583395, 0.3106),
        (0.830091, 0.5751, 0.309684),
        (0.827549, 0.566805, 0.308769),
        (0.825007, 0.55851, 0.307853),
        (0.822466, 0.550215, 0.306938),
        (0.819924, 0.54192, 0.306022),
        (0.817382, 0.533625, 0.305107),
        (0.81484, 0.52533, 0.304191),
        (0.812159, 0.516512, 0.302893),
        (0.808919, 0.505602, 0.300061),
        (0.80568, 0.494692, 0.297229),
        (0.80244, 0.483782, 0.294397),
        (0.7992, 0.472872, 0.291565),
        (0.79596, 0.461962, 0.288733),
        (0.792721, 0.451052, 0.285901),
        (0.789481, 0.440142, 0.283069),
        (0.786241, 0.429232, 0.280237),
        (0.783002, 0.418322, 0.277405),
        (0.779762, 0.407412, 0.274573),
        (0.776522, 0.396502, 0.271741),
        (0.773282, 0.385592, 0.268909),
        (0.770043, 0.374683, 0.266077),
        (0.766803, 0.363773, 0.263245),
        (0.763563, 0.352863, 0.260413),
        (0.760323, 0.341953, 0.257581),
        (0.757084, 0.331043, 0.254749),
        (0.753844, 0.320133, 0.251917),
        (0.750604, 0.309223, 0.249086),
        (0.747365, 0.298313, 0.246254),
        (0.744125, 0.287403, 0.243422),
        (0.740885, 0.276493, 0.24059),
        (0.737645, 0.265583, 0.237758),
        (0.734406, 0.254673, 0.234926),
        (0.731166, 0.243763, 0.232094),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961),
        (0.72987, 0.239399, 0.230961) ],
}


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
