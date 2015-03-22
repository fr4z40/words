# -*- coding: utf-8 -*-
'''
Developed by: Eduardo Frazão (fr4z40)
https://github.com/fr4z40

On jan,18,2015

A Class: Combinations generator
and a function: file_filter
'''

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
        cntd = filein.readlines()
    filein.close()
    cntd_out = []
    for x in cntd:
        cntd_out.append(((x.replace('\r', '')).replace('\t', '')).strip('\n'))
    cntd_out = list(set(cntd_out))
    cntd_out.sort()

    with open(f_out, 'w', encoding='utf8') as fileout:
        for x in cntd_out:
            fileout.write('%s\n' % x)
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


    def wordlist_dates_dma(ano):
        '''{
              Generate a list of date-lists...
              something like: [[d, m, y], [m, d, y], [y, m, d] ... ]
              example:
                  wordlist_dates_dma('2000')
                  >>>[[2000, m, d], [d, m, 2000] ... ]
           }
        '''
        dias = []
        meses = []
        back = []
        for x in range(1,13):
            if len(str(x)) == 1:
                meses.append('0%s' % str(x))
                meses.append(str(x))
            else:
                meses.append(str(x))
        for x in range(1, 32):
            if len(str(x)) == 1:
                dias.append('0%s' % str(x))
                dias.append(str(x))
            else:
                dias.append(str(x))
        for d in dias:
            for m in meses:
                var = (list((d, m, ano)))
                if var not in back:
                    back.append(var)
                var = (list((d, ano, m)))
                if var not in back:
                    back.append(var)
                var = (list((m, d, ano)))
                if var not in back:
                    back.append(var)
                var = (list((m, ano, d)))
                if var not in back:
                    back.append(var)
                var = (list((ano, d, m)))
                if var not in back:
                    back.append(var)
                var = (list((ano, m, d)))
                if var not in back:
                    back.append(var)
        del meses
        del dias
        return back
