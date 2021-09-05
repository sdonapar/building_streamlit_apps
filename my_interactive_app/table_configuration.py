from st_aggrid import GridOptionsBuilder

def get_table_configuration(df):
    table_editable = False
    enable_selection = True
    selection_mode = "single" # ['single','multiple']
    use_checkbox = True
    rowMultiSelectWithClick = False
    suppressRowDeselection = False
    enable_pagination = True
    paginationAutoSize = True
    paginationPageSize = 25
    groupSelectsChildren = False
    groupSelectsFiltered = False

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(groupable=False, value=True, enableRowGroup=False, aggFunc='sum', editable=table_editable)
    gb.configure_selection(selection_mode,use_checkbox=use_checkbox)

    if ((selection_mode == 'multiple') & (not use_checkbox)):
        if not rowMultiSelectWithClick:
            suppressRowDeselection = False
        else:
            suppressRowDeselection=False

    if not paginationAutoSize:
        paginationPageSize = 25
    if enable_selection:
        gb.configure_selection(selection_mode)
        if use_checkbox:
            gb.configure_selection(selection_mode, use_checkbox=True, groupSelectsChildren=groupSelectsChildren, groupSelectsFiltered=groupSelectsFiltered)
            #gb.configure_selection(selection_mode, use_checkbox=True)
        if ((selection_mode == 'multiple') & (not use_checkbox)):
            gb.configure_selection(selection_mode, use_checkbox=False, rowMultiSelectWithClick=rowMultiSelectWithClick, suppressRowDeselection=suppressRowDeselection)

    if enable_pagination:
        if paginationAutoSize:
            gb.configure_pagination(paginationAutoPageSize=True)
        else:
            gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=paginationPageSize)

    gb.configure_grid_options(domLayout='normal')
    gridOptions = gb.build()
    return gridOptions