# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
  """Choose the fruits you want in your smoothie!
  """
)


name_on_order = st.text_input('Name on smoothie:')
st.write("The name on your Smoothie will be:", name_on_order)


cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'))


ingredients_list = st.multiselect(
    'choose up to 5 ingredients:',
    my_dataframe,
    max_selections=5
    )

if ingredients_list:
    ingredients_string = ''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen+' '
        
    #st.write(ingredients_string);
   
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values('"""+ingredients_string+"""','"""+name_on_order+"""')"""
    
    time_to_insert = st.button('Submit Order')
    
    #st.write(my_insert_stmt)
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered '+name_on_order+'!', icon="✅")
# new section to display smoothiefroot nutrition information
import request
smoothiefroot_response = requests.get("http://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response.json())
