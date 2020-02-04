from eralchemy import render_er
# # Draw from database
table_name = ["NormaISTSMA,D3,S1", "NormaSarjana",
                "NormaSLTA/STM", "NORMA IST IQ", "jumlah"
            ]

render_er("sqlite:///istcore", "diagrameral.png")# exclude_tables=None)# table_name)
# def render_er(input, output, mode='auto', include_tables=None, include_columns=None,

