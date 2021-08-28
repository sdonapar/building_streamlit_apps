from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, GridUpdateMode
import pandas as pd

def interactive_datatable(df):
    '''    
    Use st_aggrid to show well table in GUI with interactive sorting and filtering options.
    
    df: input dataframe
    
    Returns: dataframe of AgGrid output (including filtering via GUI)
    '''
    #set up aggrid display/interactivity options
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=False)
    #gb.configure_selection("single", use_checkbox=False, groupSelectsChildren=False, groupSelectsFiltered=False)
    #gb.configure_grid_options(domLayout='normal')
    gb.configure_pagination(paginationAutoPageSize=True)
    gridOptions = gb.build()
    
    #set up data return/update modes
    return_mode_value = list(DataReturnMode.__members__)[1]
    update_mode_value = list(GridUpdateMode.__members__)[6]
    
    data_return_mode = return_mode_value
                       
    grid_data = AgGrid(df, 
                        gridOptions=gridOptions,
                        width='100%',
                        data_return_mode=return_mode_value,
                        update_mode=update_mode_value,
                        fit_columns_on_grid_load=False)
    
    grid_data_df = pd.DataFrame(grid_data['data'])
    
    return grid_data,grid_data_df