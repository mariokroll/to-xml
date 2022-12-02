import pandas as pd
import lxml.etree as ET


def extract():
    """
    Extract the data from the CSV file
    """
    df = pd.read_csv('2017_prediction.csv', encoding='unicode_escape')
    df.set_index('Unnamed: 0', inplace=True)
    df_dict = df.to_dict('index')
    order_details = pd.read_csv('order_details.csv', sep=';')
    orders = pd.read_csv('orders.csv', sep=';')
    pizzas = pd.read_csv('pizzas.csv')
    pizzas_types = pd.read_csv('pizza_types.csv', encoding='unicode_escape')
    return df_dict, order_details, orders, pizzas, pizzas_types


def data_info(order_details: pd.DataFrame, orders: pd.DataFrame, pizzas: pd.DataFrame, pizzas_types: pd.DataFrame) -> pd.DataFrame:
    """
    Before start making predictions, let's have some information about the data, like the shape of the dataframes,
    the number of NaN or null values, the number of unique values or the type of the columns, represented in dictionaries
    """
    # Create a DataFrame that will contain the information
    info = {'order_details': {}, 'orders': {}, 'pizzas': {}, 'pizzas_types': {}}

    for csv in info.keys(): 
        # Get the shape of the dataframes
        info[csv]['shape'] = eval(csv).shape

        # Get the number of Na values per column
        info[csv]['na'] = eval(csv).isna().sum().to_dict()

        # Get the number of unique values per column
        info[csv]['unique'] = eval(csv).nunique().to_dict()

        # Get the type of each column
        info[csv]['type'] = eval(csv).dtypes.to_dict()

    return info


def convert_to_xml(pred: dict, info_from_data: dict):

    root = ET.Element('XML_information')
    iters = 0
    subel1 = ET.SubElement(root, 'Subelement', information='Prediction_per_weeks')
    for k in pred.keys():
        # Create the first subelement of subel1, that contains the number of week
        iters += 1
        if iters < 10:
            m1 = ET.SubElement(subel1, 'week', number=k[-1])
        else:
            m1 = ET.SubElement(subel1, 'week', number=k[-2:])
        for ing in pred[k].keys():
            # Subelement m2 is the ingredient prediction
            m2 = ET.SubElement(m1, 'attribute')
            m2.set('ingredient', ing)
            m2.text = str(int(pred[k][ing]))

    subel2 = ET.SubElement(root, 'Subelement', information='Data_information')
    for key in info_from_data.keys():

        # Create the first subelement, that is the file name
        m1 = ET.SubElement(subel2, 'file', name=key)
        for k in info_from_data[key]:

            # Create a new subelement, that is the info attribute
            m2 = ET.SubElement(m1, 'info', attribute=k)

            # If the new subelement is another dictionary, we create a new subelement adding the information that
            # the dictionary contains. If not, we write directly the info of the subelement
            if type(info_from_data[key][k]) == dict:
                for col in info_from_data[key][k]:
                    m3 = ET.SubElement(m2, 'column', name=col)
                    m3.text = str(info_from_data[key][k][col])
            else:
                m2.text = str(info_from_data[key][k])
    tree = ET.ElementTree(root)
    tree.write('2017_predictions.xml')


if __name__ == '__main__':
    df, order_details, orders, pizzas, pizzas_types = extract()
    info_from_data = data_info(order_details, orders, pizzas, pizzas_types)
    convert_to_xml(df, info_from_data)