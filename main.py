from Doc2Query import Doc2Query
from Query2Doc import Query2Doc
data_path = './dataset/clean/data.json'


get_query = Doc2Query(query_len = 10)
get_doc = Query2Doc(data_path)


if __name__ == '__main__':
    query = get_query('./dataset/raw/AI/A First-Order Model to Assess Computer Architecture Sustainability.pdf')
    result = get_doc(query)
    print(f'Query : {query}')
    print(result)