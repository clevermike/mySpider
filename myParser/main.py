#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# -*- author:dongchen -*-

#from myParser.saver.orm import mysql_db, Deal, dealTable
#from sqlalchemy.orm import mapper, sessionmaker

from settings import SITE_LIST


if __name__ == '__main__':
    # Session = sessionmaker(bind=mysql_db)
    # session = Session()
    # mapper(Deal, dealTable)
    #
    # for site in SITE_LIST:
    #     exec "from parser.%sParser import %sParser" % (site, site)
    #     exec "parser = %sParser()" % site
    #     for deal in parser.parse():
    #         session.flush()
    #         session.add(Deal(identity=deal['identity'],
    #                          site=deal['site'],
    #                          title=deal['title'],
    #                          description=deal['description'],
    #                          bread=deal['bread'],
    #                          quantity=deal['quantity']))
    #         session.commit()
    #         print deal

    import sys
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    for site in SITE_LIST:
        # print (os.path.abspath('.'))
        exec "from parser.%sParser import %sParser" % (site, site)
        exec "parser = %sParser()" % site
        exec "f = open('data/%s.txt', 'w')" % site

        f.write('deals = [\n')
        for deal in parser.parse():
            f.write("\t{'%s','%s','%s','%s','%s'}\n" % (deal['identity'], deal['title'], deal['description'], deal['bread'], deal['quantity']))
        f.write(']\n')
