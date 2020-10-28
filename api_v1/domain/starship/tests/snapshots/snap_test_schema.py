# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_mutation_create_starship[data0] 1'] = {
    'data': {
        'createStarship': {
            'id': 'U3RhcnNoaXA6MQ==',
            'length': 12.0,
            'name': 'Starship 1'
        }
    }
}

snapshots['test_mutation_create_starship[data1] 1'] = {
    'data': {
        'createStarship': {
            'id': 'U3RhcnNoaXA6MQ==',
            'length': 12.56,
            'name': 'Starship 2'
        }
    }
}

snapshots['test_mutation_delete_starship 1'] = {
    'data': {
        'deleteStarship': {
            'id': 'U3RhcnNoaXA6Tm9uZQ==',
            'length': 9.0,
            'name': 'Starship One'
        }
    }
}

snapshots['test_mutation_update_starship[data0] 1'] = {
    'data': {
        'updateStarship': {
            'id': 'U3RhcnNoaXA6MQ==',
            'length': 9.0,
            'name': 'Starhip Updated'
        }
    }
}

snapshots['test_mutation_update_starship[data1] 1'] = {
    'data': {
        'updateStarship': {
            'id': 'U3RhcnNoaXA6MQ==',
            'length': 12.0,
            'name': 'Starship One'
        }
    }
}

snapshots['test_mutation_update_starship[data2] 1'] = {
    'data': {
        'updateStarship': {
            'id': 'U3RhcnNoaXA6MQ==',
            'length': 12.0,
            'name': 'Starship One'
        }
    }
}

snapshots['test_mutation_update_starship[data3] 1'] = {
    'data': {
        'updateStarship': {
            'id': 'U3RhcnNoaXA6MQ==',
            'length': 12.0,
            'name': 'Starship Updated'
        }
    }
}

snapshots['test_mutation_update_starship[data4] 1'] = {
    'data': {
        'updateStarship': {
            'id': 'U3RhcnNoaXA6MQ==',
            'length': 12.0,
            'name': 'Starship Updated'
        }
    }
}

snapshots['test_query_starship 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where0] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where10] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where11] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where12] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where13] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where14] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where15] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where16] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where17] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where18] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where1] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where2] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where3] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where4] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where5] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where6] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where7] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where8] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 10.0,
                        'name': 'Starship Two'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 11.0,
                        'name': 'Starship Three'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_starships_with_filters[where9] 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 9.0,
                        'name': 'Starship One'
                    }
                }
            ]
        }
    }
}
