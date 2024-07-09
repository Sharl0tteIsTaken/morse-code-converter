class BuiltinsInput:
    def __init__(self):
        self.log:list[str] = []
        self.counts = 0
        self.chained_log:list[str] = []
        self.chained_counts = 0
        
    def enter(self):
        self.log.append(input('enter something: '))
        self.counts = self.counts + 1
        
    def chained_enter(self):
        print('this is a set of chained questions.')
        for n in range(3):
            self.chained_log.append(input(f'Question {n}. enter something: '))
            
    def tree_enter(self):
        usitr = input('a or b: ')
        print(f'first input: {usitr}')
        if usitr == 'a':
            usitr_2 = input('z or x: ')
            print(f'secnd input: {usitr_2}')
            if usitr_2 == 'z':
                self.tree = 'az'
            elif usitr_2 == 'x':
                self.tree = 'ax'
            else:
                self.tree = 'a_'
        elif usitr == 'b':
            usitr_2 = input('q or w: ')
            print(f'secnd input: {usitr_2}')
            if usitr_2 == 'q':
                self.tree = 'bq'
            elif usitr_2 == 'w':
                self.tree = 'bw'
            else:
                self.tree = 'b_'
        else:
            self.tree = '_0'
        print(self.tree)