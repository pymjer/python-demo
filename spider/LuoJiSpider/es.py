import elasticsearch
import datetime


class ES(object):
    @classmethod
    def connect_host(cls):
        hosts = [{"host": "192.168.8.152"},
                 {"host": "192.168.8.154"},
                 {"host": "192.168.8.155"}, ]
        es = elasticsearch.Elasticsearch(
            hosts,
            sniff_on_start=True,
            sniff_on_connection_fail=True,
            sniffer_timeout=600
        )
        return es


def es_query(about="", start=None, end=None, reverse=False, limit_cnt=20):
    es = ES.connect_host()
    q_body = {
        "size": limit_cnt,
        "query": {
            "match": {
                "about": about
            }
        }
    }
    res = es.search(index='megacorp', body=q_body)
    print(res)
    return res


def es_index(id, title, author, content):
    es = ES.connect_host()
    q_body = {
        "title": title,
        "content": content,
        "author": author,
        "created": datetime.datetime.now()
    }
    es.index(index="logic-thinking", doc_type="morning-call", id=id, body=q_body)


if __name__ == '__main__':
    es_index(2, "22", "很2", "就是一个二货")
