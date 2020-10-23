# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_query_starships 1'] = {
    'data': {
        'starships': {
            'edges': [
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6MQ==',
                        'length': 11.0,
                        'name': 'Starship One'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mg==',
                        'length': 12.0,
                        'name': 'Starship Two'
                    }
                },
                {
                    'node': {
                        'id': 'U3RhcnNoaXA6Mw==',
                        'length': 13.0,
                        'name': 'Starship Three'
                    }
                }
            ]
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
                        'length': 11.0,
                        'name': 'Starship One'
                    }
                }
            ]
        }
    }
}
