import streamlit as st
import pandas as pd

st.title('Hello, World!')

st.header('This is a header')
st.subheader('This is a subheader')
st.caption('This is a caption')

st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.markdown(
    """
    Ini adalah contoh **bold text**.
    """
)

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.dataframe(data=df, width=500, height=150)
st.table(data=df)
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")