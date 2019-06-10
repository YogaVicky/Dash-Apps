Row([
    Col([
        html.H3('Facebook Overview'),
        html.P('Spend (Last 30 Days): $%.2f' % fb_total_spend),
        html.P('Spend (Yesterday): $%.2f' % fb_yesterday_spend),
    ]),
    Col([
        html.H3('Adwords Overview'),
        html.P('Spend (Last 30 Days): $%.2f' % google_total_spend),
        html.P('Spend (Yesterday): $%.2f' % google_yesterday_spend),
    ]),
    Col([
        html.H3('All Accounts Overview'),
        html.P('Spend (Last 30 Days): $%.2f' % total_30day_spend),
        html.P('Spend (Yesterday): $%.2f' % total_yesterday_spend),
    ]),
])
