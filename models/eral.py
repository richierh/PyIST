from eralchemy import render_er
## Draw from database
table_name = ["data_kandidat",
            
            ]

render_er("sqlite:///ist", "ouput.png",include_tables=table_name)
# def render_er(input, output, mode='auto', include_tables=None, include_columns=None,
