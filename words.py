# -*- coding: utf-8 -*-
'''
Developed by: Eduardo Frazão (fr4z40)
https://github.com/fr4z40

On jan,18,2015

A Class: Combinations generator
and a function: file_filter
'''


days = list(map((lambda x: ('0%s' % str(x))), range(1,10)))
days = days + list(map((lambda x: str(x)), range(1,32)))
months = list(map((lambda x: ('0%s' % str(x))), range(1,10)))
months = months + list(map((lambda x: str(x)), range(1,13)))


def file_filter(f_in, f_out):
    '''
    Removes repetitions.
      >> this "word" isn't the same as "word " or " word".
      >> be careful with large files.
         -----------------------------
      >> Char-Encoders:
          {
              latin: iso-8859-1
              UTF-8: utf8, utf-8
          }
    '''

    with open(f_in, 'r', encoding='utf8') as filein:
        cntd = list(set((((filein.read()).replace('\r','')).replace('\t','')).split('\n')))
    filein.close()
    cntd.sort()

    with open(f_out, 'w', encoding='utf8') as fileout:
        for x in cntd:
            fileout.write('%s\n' % x.strip())
    fileout.close()



class gen:
    '''
    Combinations generator, based on dates and tel. numbers
    '''

    def pos(pre, sep):
        '''
           {
              Generate a list of tel. numbers, with a prefix inputed by user.
              example:
                  pos('2668', '-')
                  >>2668-0001...
                  >>2668-0002...
           }
        '''
        posfixo = []
        pos = '9999'
        for x in range(10000):
            if len(pos) == 4:
                posfixo.append(pre + sep + pos)
                pos = str(int(pos) - 1)
            else:
                pos =  (('0' * (4 - len(pos))) + pos)
                posfixo.append(pre + sep + pos)
                pos = str(int(pos) - 1)
        posfixo = list(set(posfixo))
        posfixo.sort()
        return(posfixo)


    def wdlist_yearbase(year):
        '''{
              Generate a list of "date-lists", based on year "X"...
              something like: [[d, m, y], [m, d, y], [y, m, d] ... ]
              example:
                  wordlist_dates_dma('2000')
                  >>>[[2000, m, d], [d, m, 2000] ... ]
           }
        '''
        back = []
        days = list(map((lambda x: ('0%s' % str(x))), range(1,10)))
        days = days + list(map((lambda x: str(x)), range(1,32)))
        months = list(map((lambda x: ('0%s' % str(x))), range(1,10)))
        months = months + list(map((lambda x: str(x)), range(1,13)))
        for d in days:
            temp = []
            for m in months:
                temp.append(list((d,m,str(year))))
                temp.append(list((d,str(year),m)))
                temp.append(list((m,d,str(year))))
                temp.append(list((m,str(year),d)))
                temp.append(list((str(year),d,m)))
                temp.append(list((str(year),m,d)))
            for t in temp:
                if t not in back:
                    back.append(t)
        return back


    def wdlist_mounth(mounth, year):
        '''{
              Generate a list of "date-lists", based on mounth and year
              something like: [[d, m, y], [m, d, y], [y, m, d] ... ]
              example:
                  wordlist_dates_dma('03','2000')
                  >>>[[2000, 03, d], [d, 03, 2000] ... ]
           }
        '''
        back = []
        temp = []
        days = list(map((lambda x: ('0%s' % str(x))), range(1,10)))
        days = days + list(map((lambda x: str(x)), range(1,32)))
        months = list(map((lambda x: ('0%s' % str(x))), range(1,10)))
        months = months + list(map((lambda x: str(x)), range(1,13)))
        for d in days:
            temp.append(list((d, str(mounth), str(year))))
            temp.append(list((d, str(year), str(mounth))))
            temp.append(list((str(mounth), d, str(year))))
            temp.append(list((str(mounth), str(year), d)))
            temp.append(list((str(year), d, str(mounth))))
            temp.append(list((str(year), str(mounth), d)))
        for t in temp:
            if t not in back:
                back.append(t)
        back.sort()
        return back
